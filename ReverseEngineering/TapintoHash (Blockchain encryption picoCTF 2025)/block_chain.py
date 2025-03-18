import time
import base64
import hashlib
import sys
import secrets


class Block:
    def __init__(self, index, previous_hash, timestamp, encoded_transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.encoded_transactions = encoded_transactions
        self.nonce = nonce

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.encoded_transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def proof_of_work(previous_block, encoded_transactions):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0

    block = Block(index, previous_block.calculate_hash(),
                  timestamp, encoded_transactions, nonce)

    while not is_valid_proof(block):
        nonce += 1
        block.nonce = nonce

    return block


def is_valid_proof(block):
    guess_hash = block.calculate_hash()
    return guess_hash[:2] == "00"


def decode_transactions(encoded_transactions):
    return base64.b64decode(encoded_transactions).decode('utf-8')


def get_all_blocks(blockchain):
    return blockchain


def blockchain_to_string(blockchain):
    block_strings = [f"{block.calculate_hash()}" for block in blockchain]
    return '-'.join(block_strings)


def encrypt(plaintext, inner_txt, key):
    midpoint = len(plaintext) // 2

    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part
    block_size = 16
    plaintext = pad(modified_plaintext, block_size)
    key_hash = hashlib.sha256(key).digest()

    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        ciphertext += cipher_block

    return ciphertext


def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding

def unpad(data):
    padding_length = data[-1]  # Last byte indicates padding length
    return data[:-padding_length]  # Remove the padding


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def generate_random_string(length):
    return secrets.token_hex(length // 2)


random_string = generate_random_string(64)


def decrypt(ciphertext,key):
    block_size = 16
    key_hash = hashlib.sha256(key).digest()
    decrypted_plaintext = b''

    # XOR each block again to reverse encryption
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted_plaintext += xor_bytes(block, key_hash)

    # Remove padding
    decrypted_plaintext = unpad(decrypted_plaintext)

    # Convert bytes to string
    decrypted_plaintext = decrypted_plaintext.decode('utf-8')

    # Remove inserted `inner_txt`
    ## decrypted_plaintext = decrypted_plaintext.replace(inner_txt, "", 1)

    return decrypted_plaintext


def main(token):
    key = bytes.fromhex(random_string)

    print("Key:", key)

    genesis_block = Block(0, "0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]

    for i in range(1, 5):
        encoded_transactions = base64.b64encode(
            f"Transaction_{i}".encode()).decode('utf-8')
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        blockchain.append(new_block)

    all_blocks = get_all_blocks(blockchain)

    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)

    print("Encrypted Blockchain:", encrypted_blockchain)



if __name__ == "__main__":
    #text = sys.argv[1]
    #main(text)
    decrypted_plaintext=decrypt(b'o\xd3\xefR\xf9@\x01(\xebg\xf0\xed\xc5K\xcc\x87>\x83\xe8\x05\xaeB\x02)\xbe2\xa7\xe2\xc6\x19\x97\xd2h\xd9\xeaW\xfcF\x05+\xb20\xf4\xb7\x97N\x9f\xd5e\xd2\xeb\x02\xf9FVx\xeb`\xa2\xe4\xc7M\x9c\x85p\xd1\xe8P\xffOR.\xee5\xa6\xb6\x94\x18\x9e\x84i\xd6\xbaQ\xf9\x14\x00.\xee3\xa2\xe4\x93\x1c\x9a\x83h\x87\xea\x01\xf8FV"\xbbe\xa2\xb6\x93N\x9b\xd5l\xd4\xbaU\xa8\x17Z.\xbdb\xa6\xe5\xc7H\xcc\x8fk\xcc\xe8P\xa9C\x07(\xbd<\xf4\xe7\xc6\x18\x99\xd0;\x82\xe0\x01\xa8GQz\xeb6\xaf\xe5\xc7H\xca\x829\xd2\xa8\t\xa9\x19 O\xcc\x7f\xf4\xb9\x99\x1e\xc5\xe9n\xb2\x8a\x08\x9c\x1f1y\xde5\xe7\xb6\xae"\xf6\xe37\xac\xe8\x12\xfeO\x00S\xd5u\xd5\xaf\x9b7\xf4\xcc\x1f\xaa\x87T\xff\x15\x07)\xeb1\xa4\xa8\x92D\x9b\xd5k\x87\xebQ\xac\x17U,\xb93\xf2\xe4\x92I\x96\xd3l\x87\xbcQ\xa8DV*\xb3f\xf4\xb6\xdbM\x9e\x82e\xd6\xbcY\xfdNQ"\xbc4\xf3\xe4\xc4I\x97\x858\xd8\xbcQ\xabDZ+\xe83\xa7\xb7\xc2I\x9f\xd7d\x80\xee\x01\xafG\x07,\xbf7\xa3\xe6\x95\x1c\x99\xd7m\xd0\xb9Y\xacCU}\xece\xaf\xb3\x90P\x9e\x86n\x82\xbaQ\xae\x14W/\xec`\xf0\xe7\xc0N\x9a\x81m\xd6\xe8Y\xa8BU(\xbd6\xa1\xe1\xc1J\x97\x81j\x87\xbbV\xfeBW~\xbf3\xa6\xb6\xc2\x18\x97\xd0>\xd4\xeaU\xf8\x13\x01-\xeb2\xf2\xe5\xc5\x19\xac\xb4',b'Z\xa3\xf6\xd4\xdb\x8a\x9c\x10\x84\xf8\xb6\xb0:\x1c\xce\xca\xbfX\x96\x9d\x87\tm\xd6\xbe4a\xc5\xd5\x91^\x98')
    print(decrypted_plaintext)


