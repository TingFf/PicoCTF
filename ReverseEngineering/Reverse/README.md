## Comment  
1. Used similar technique that I learned in previous challenges.  
2. Two ways to get the flag.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Either just copy and paste the flag or get the password.  
## Tools Used  
**Ghidra,GDB**  

## Writeup  
![ScreenShot](https://imgur.com/Z5F8FqI.png)  
**First way:**  
1. Very straight forward the flag is right there when open in ghidra.  

![ScreenShot](https://imgur.com/iyxgQdk.png)  
**Second way:**  
1. We can see the string of 48 char password is stored in RBP.  
2. Looking at the address after the line when the password is stored in memory (0x0010123b).  
![ScreenShot](https://imgur.com/1TlaZBs.png)  
3. Setting a break point at the address in gdb.  
4. Display what is stored at rbp using x/s rbp-48.  
![ScreenShot](https://imgur.com/bdnwDU4.png)
5. Change the file permission to executable and execute it.  
6. Enter the password to get the flag.  

## Stuff Learned  
NA



