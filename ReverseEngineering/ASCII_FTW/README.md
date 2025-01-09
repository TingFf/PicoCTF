## Comment  
1. Feel there is a simpler way to do this.    

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Print the 32 bytes from the base pointer.  
## Tools Used  
NIL  

## Writeup  
![ScreenShot](https://imgur.com/RDDezzb.png)  
1. In the assembly code, the flag is stored as individual bytes, sequentially from the base pointer up to 32 bytes.  
![ScreenShot](https://imgur.com/6BbroMk.png)  
2. "x/s $rbp-0x30" to print the string out from the offset of the base pointer.  

## Stuff Learned  
1. x/s to print the entire string.   


