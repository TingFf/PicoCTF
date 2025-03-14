## Overview ##
# This script is attempting to find an input string that,
# when processed through a specific encryption algorithm,
# produces a given output string. It uses Z3, a powerful
# constraint solver, to work backwards from the encrypted
# output to find the original input.

# Imports Z3 solver library
# Defines the target encrypted output string (50 characters)
# Creates 50 8-bit BitVec variables to represent each character of the input we're trying to find

from z3 import *

output = "qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze"
userinput = [BitVec(f"userInput_{i}", 8) for i in range(50)]


# This function extracts the index number from the BitVec variable names
def getIndex(g):
    return int(FuncDeclRef.name(g).replace("userInput_", ""))


# Creates a new Z3 solver instance
# Adds constraints ensuring all input characters are printable ASCII (between 33 and 126)
s = Solver()
for v in userinput:
    s.add(v > 32)
    s.add(v < 127)

# Same loop in Ghidra
for i in range(3):
    for j in range(len(output)):
        uVar1 = (((j % 255) >> 1) & 0x55) + ((j % 255) & 0x55)
        uVar1 = ((uVar1 >> 2) & 0x33) + (uVar1 & 0x33)
        iVar2 = ((uVar1 >> 4) & 0xF) + (userinput[j] - 97) + (0xF & uVar1)
        userinput[j] = 97 + iVar2 + (iVar2 / 26) * (-26)

# Make sure the encrypted value equals the memcmp value which is based in the decomplied code
# Compares each character position with the corresponding character in the output string
for j in range(50):
    s.add(userinput[j] == ord(output[j]))

# Checks if a solution exists
# Gets the solution model from Z3
# Sorts the solution variables by their index to maintain correct order
# Converts the solution numbers to characters
# Prints the final decrypted string

print(s.check())
model = s.model()
result = ""
for d in sorted(model.decls(), key=getIndex):
    result = result + chr(model[d].as_long())
print(result)


## Summary ##
# This script is likely solving a CTF (Capture The Flag) or reverse engineering challenge where:
# The original program encrypted some input
# The challenge provides the encrypted output
# This script uses Z3 to work backwards and find what input would produce that output
# The found input is likely the flag or solution to the challenge
# The strength of using Z3 here is that it can solve these complex constraints without
# having to manually reverse the encryption algorithm.
