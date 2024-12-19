<img width="369" alt="image" src="https://github.com/user-attachments/assets/8ebd65df-d321-4a4f-970c-15081bd6f1d3" />## Comment
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
6. Continued to triage.  

![ScreenShot of PEiD](https://imgur.com/PRgPRBL.png)  
7. Seems like the flag has been found but is encrypted.  
8. Looks like Hex.  

![ScreenShot of PEiD](https://imgur.com/wFZj61O.png)  
9. Flag found  

## Stuff Learned  
1. Always make sure to change file packed.
2. Static analysis is useful.


