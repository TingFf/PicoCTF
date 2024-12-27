## Comment  
1. Had to look at writeup for this wan.  
(https://www.youtube.com/watch?v=_ehvUhWoNYM)  
2. First RE that requires python script

## Challenge Overview  
**Difficulty:** Medium  
**Description:** The purpose of the challenge is the find the specific input that the code will encrypt and match with the secret value.  
## Tools Used  
**Ghidra, z3**  

## Writeup  
![Screenshot](https://imgur.com/7dcTyzr.png)  
1. Did some script analysis by changing the variables name to make sense of the code.  
2. Basically the secret value is a large string.  
### **TIP**  
![Screenshot](https://imgur.com/sL6gEtv.png)  
![Screenshot](https://imgur.com/DKcJvid.png)  
1. Retype the secretValue to let the compiler to interpret and display in another way for easy understanding.  
2. Change the type to char[51] as the "secret password" takes in 50 char from user input.  
### **Explaination**  
1. When the string is too large to fit into a single variable (based on the data type and architecture), the compiler interprets, splits, and stores the data across multiple variables or memory locations for efficient representation and access.  
2. The original value, 0x7570626770636871, is a 64-bit (8-byte) integer constant.  
3. Additional values (uStack_60, uStack_58, etc.) also hold 64-bit constants.  
4. When ValueToCompare is changed to char[51], the compiler treats it as an array of 51 bytes (characters).  
5. Each of the hexadecimal constants (0x7570626770636871, etc.) is interpreted as sequential memory content, unpacked byte by byte, and stored into the array.  
6. Memory layout for the original int version:  
[0x75706267] [0x70636871] (for _ValueToCompare)  
[0x75706567] [0x67616277] (for uStack_60)  
7. Memory layout for the char[51] version:  
['q', 'h', 'c', 'p', 'g', 'b', 'p', 'u'] (first 8 bytes from _ValueToCompare)  
['w', 'b', 'a', 'g', 'g', 'e', 'p', 'u'] (next 8 bytes from uStack_60)  
8. If the total string size (51 characters in this case) exceeds what can be efficiently managed in a single memory location (due to hardware constraints or compiler optimization), the compiler needs to distribute it across multiple storage units (e.g., stack slots, memory blocks).  
9. The compiler optimizes storage by treating parts of the char[51] array as chunks and mapping them to pre-existing stack variables (uStack_60, uStack_58, etc.). This reuses memory space already allocated for those variables, ensuring no extra memory is wasted.  
![Screenshot](https://imgur.com/7dcTyzr.png)  
3. Create a python script thats replicates the decompiled code.  
4. Used z3 to find a input that will match the output.  
5. Comments are in the script.py for understanding.  
![Screenshot](https://imgur.com/e5c7INR.png)  
![Screenshot](https://imgur.com/S2r2uhR.png)  
5. After getting the solution from the script, paste it into the program and the flag will be displayed.    
## Stuff Learned  
1. z3 library is used in RE to find a solution of specific input from given output.  
2. How compiler interprets the data and displays in ghidra based on data size and type.  



