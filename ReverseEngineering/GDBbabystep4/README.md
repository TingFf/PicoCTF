## Comment  
NIL

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Find the constant  
## Tools Used  
**gdb**  

## Writeup  
![Screenshot](https://imgur.com/5jUN7xK.png)  
1. Looking at the disassembles of main, there is another function.  
2. Command: disas function_name to look into that function.  
3. Based on the description of the challenge, the constant is 0x3269 and the flag is in decimal of that.  

## Stuff Learned  
1. How to disas into other function.  
2. imul instruction represent signed multiplication.
**Example of signed multiplication with two operands:**
mov eax, 5      ; Load 5 into eax
mov ebx, -3     ; Load -3 into ebx
imul eax, ebx   ; eax = eax * ebx, so eax = 5 * -3 = -15
