## Comment  
1. Didnt document babystep 1 & 2 as its pretty straighforward.

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Get the flag at register rbp
## Tools Used  
**gdb**  

## Writeup  
![Screenshot](https://imgur.com/Qpt9lHR.png)  
1. Looking at the disassembles of main, the local variable is stored at rbp-4 before storing at eax.
![Screenshot](https://imgur.com/OdMpfYP.png)  
3. Set a break point right before rbp is pop.  
4. View the data stored in rbp-4 using "x/4xb $rbp-4".  
5. The flag will be the little endian of the local variable.  
## Stuff Learned
1. Local variable is stored in rbp and it will be in little-endian.
2. $rbp-4 represents offset of 4 from rbp.
3. **Command Breakdown:**
   x: The x command stands for "examine memory".
   /4x: The /4 part specifies the number of units to examine (4 units in this case), and the x specifies the format (hexadecimal).
   b: The b specifies the unit size as a byte (1 byte).
   **Full Command: x/4xb**
   4: This tells GDB to examine 4 consecutive memory locations.
   x: This specifies that the values should be displayed in hexadecimal format.
   b: This specifies that each memory unit is a byte (8 bits).
