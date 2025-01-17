## Comment  
1. Related to cryptography.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** 
1. Modify the python code to get the flag. 
2. Decrypt the payload using cyberchef.  
## Tools Used  
CyberChef  

## Writeup  
![ScreenShot](https://imgur.com/dg0mFru.png)  
**First way:**  
1. Change the exec line to print.  
2. The payload will be display which shows the password and the flag.  
![ScreenShot](https://imgur.com/rS1SEAE.png)  
**Second way:**  
1. Follow the logic of the python code.  
2. First encode the key to base64.  
![ScreenShot](https://imgur.com/HjdbDIZ.png)  
3. Use the encoded key as the key for the decyption of fernet cryptography.  
![ScreenShot](https://imgur.com/BaC9ZH7.png)  
5. Either enter the password or just copy the flag.  
## Stuff Learned  
1. Fernet is a type of symmetric cryptography.    


