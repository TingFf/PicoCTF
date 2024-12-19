## Comment
1. Pretty straight forward challenge.
2. Title provides some hints

## Challenge Overview
**Difficulty:** Medium  
**Description:** Static analysis on the file to get the flag

## Tools Used
Upx, CyberChef
## WriteUp
![ScreenShot of PEiD](https://imgur.com/YYjX49H.png)  
1. I change the permission to executable since the challenge states its a binary executable.  

![ScreenShot of PEiD](https://imgur.com/d6aWVhw.png)  
![ScreenShot of PEiD](https://imgur.com/BZRngG8.png)  
2. Using strings to do a quick triage.  
3. Notice it may be packed by UPX.  

![ScreenShot of PEiD](https://imgur.com/JfvQ0ii.png)  
4. Unpacked using UPX.  

![ScreenShot of PEiD](https://imgur.com/xfVwo34.png)  
5. Apparently, password is required.   

![ScreenShot of PEiD](https://imgur.com/PRgPRBL.png)  
6. Seems like the flag has been found but is encrypted.  

![ScreenShot of PEiD](https://imgur.com/wFZj61O.png)  

## Stuff Learned  
1. Always make sure to change file packed.
2. Static analysis is useful.


