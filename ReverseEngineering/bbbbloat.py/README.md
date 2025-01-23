## Comment  
1. Trying to use IDA more to look at assembly code.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Get the secret number in decimal.  
## Tools Used  
**IDA Free,gdb**  

## Writeup  
![ScreenShot](https://imgur.com/rrFB6PM.png)  
1. Looks like the program will ask for a number from user input.  

![ScreenShot](https://imgur.com/2JVGmzB.png)  
2. Just before the branch, there is a cmp instruction.   
3. Seems like the secret number is 86187h.  

![ScreenShot](https://imgur.com/01NWzxj.png)  
4. Using gdb to debug the code.  
5. Convert the hex number to decimal as the number.  
6. Flag will be then display.  

## Stuff Learned  
1. Try to use more tools to expand my skillset.   
