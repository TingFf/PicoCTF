## Comment  
1. Kind of new type of challenge.  
2. Bytes pattern into binary  
3. Link: https://medium.com/@sobatistacyber/picoctf-writeup-whitepages-4d13300b3566  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!  
## Tools Used  
**bvi**

## Writeup  
1. A txt download contain what seems to be empty.  
2. But actually it contain spaces.  
```
00000000  E2 80 83 E2 80 83 E2 80 83 E2 80 83 20 E2 80 83 20 E2 80 83 E2 80 83 E2 ............ ... .......
00000018  80 83 E2 80 83 E2 80 83 20 E2 80 83 E2 80 83 20 E2 80 83 E2 80 83 E2 80 ........ ...... ........
00000030  83 E2 80 83 20 E2 80 83 E2 80 83 20 E2 80 83 20 20 20 E2 80 83 E2 80 83 .... ...... ...   ......
00000048  E2 80 83 E2 80 83 E2 80 83 20 20 E2 80 83 20 E2 80 83 E2 80 83 20 E2 80 .........  ... ...... ..
00000060  83 20 20 E2 80 83 E2 80 83 E2 80 83 20 20 E2 80 83 20 20 E2 80 83 20 20 .  .........  ...  ...
00000078  20 20 E2 80 83 20 E2 80 83 E2 80 83 E2 80 83 E2 80 83 20 20 E2 80 83 20   ... ............  ...
00000090  E2 80 83 20 E2 80 83 20 E2 80 83 E2 80 83 E2 80 83 20 E2 80 83 E2 80 83 ... ... ......... ......
000000A8  E2 80 83 20 20 E2 80 83 E2 80 83 E2 80 83 E2 80 83 E2 80 83 20 E2 80 83 ...  ............... ...
```
3. bytes `e2 80 83` is actually a unicode character call "EM SPACE" which is just a white space but I think the width is bit larger than normal spaces.   
4. bytes `20` is ascii value for white spaces.  
5. If you look closey, the whole file just contain these two sets of bytes.  
6. There maybe a pattern to it.  
7. At this point, I was stuck and had to research on writeup to get some clues to continue.  
8. Actually, we can represent the pattern into binary and convert them into ascii value.  
9. Basically, the "EM SPACE" represent '0' and the white space represent '1'.  
```
def convertSpacesToBinary():
    """ Convert the bytes pattern to binary """
    with open('whitepages.txt', 'rb') as f:
        result = f.read()
    result = result.replace(b'\xe2\x80\x83', b'0')  # Unicode EM SPACE -> 0
    result = result.replace(b'\x20', b'1')  # ASCII Space -> 1
    result = result.decode()
    return result

def convertFromBinaryToASCII(binaryValues):
    # Convert binary string to integer
    binary_int = int(binaryValues, 2)  # 'binaryValues' should be a string like '01001000'
    
    # Calculate number of bytes needed to represent the binary integer
    byte_number = (binary_int.bit_length() + 7) // 8
    
    # Convert integer to byte array (big-endian)
    binary_array = binary_int.to_bytes(byte_number, "big")
    
    # Decode byte array to ASCII text
    ascii_text = binary_array.decode('ascii')

convertFromBinaryToASCII(convertSpacesToBinary())
```
10. Flag:  
```
picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
```


## Stuff Learned  
1. `e2 80 83` -> EM SPACE.  
2. Some malware may use byte patterns to obfuscate the payload.  


