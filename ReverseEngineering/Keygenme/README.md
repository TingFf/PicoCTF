## Comment  
1. Had some technical libraries issue.  

## Challenge Overview  
**Difficulty:** Hard    
**Description:** Look into the memory that the input is being compare with.  
## Tools Used  
**GDB**  

## Writeup  
![ScreenShot](https://imgur.com/8AGWHTP.png)  
1. It seems like the flag checker is in the function FUN_555555555209.  
 
![ScreenShot](https://imgur.com/2PzThu6.png)  
![ScreenShot](https://imgur.com/fJ2YN7V.png)  
2. Part of the flag is revealed in the binary code.  
3. Looking at the code, it hashes picoCTF{brlng_y0ur_0wn_k3y_, manipulate it and use the output as the last part of the flag.  
4. After the flag is complete, it moved on to compared with pre-stored flag.  
5. The entire flag should be 36 in length.  
6. Hence the idea I had was to debug and break at the point when its being compare.  

![ScreenShot](https://imgur.com/O1yo2XN.png)  
![ScreenShot](https://imgur.com/pFJ71wZ.png)  
7. Setting a break point.  

![ScreenShot](https://imgur.com/C2fhrd3.png)  
8. Any input should works fine as long as its length 36.  

![ScreenShot](https://imgur.com/A6QU1L7.png)  
9. The flag is stored at $rbp-0x30.  

![ScreenShot](https://imgur.com/JXJvVmu.png)  
10. Look into $rbp-0x30 after enter a input of length 36 will get me the flag.  

## Stuff Learned  
1.  BYTE PTR [rbp+rax*1-0x30] => stored at $rbp-0x30.  


