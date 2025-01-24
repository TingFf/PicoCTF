## Comment  
NA

## Challenge Overview  
**Difficulty:** Medium  
**Description:** RE the python code.  
## Tools Used  
NIL  

## Writeup  
![ScreenShot](https://imgur.com/JEGpgwe.png)  
1. After looking through the code, it seems like we need to figure our the last 8 digits of the flag store in the "dynamic" variable.

![ScreenShot](https://imgur.com/Bcub0KS.png)  
3. The check key function is matching the secret key char to the SHA256 hash of the string "PRITCHARD".  

![ScreenShot](https://imgur.com/pGLdKgF.png)  
4. I created a simple python script to get the flag.  

    
## Stuff Learned  
1. *hashlib.sha256(b"PRITCHARD").hexdigest()*.  
   **sha256**: hash function sha256.  
   **b"PRITCHARD"**: byte string.  
   **hexdigest**: return in hexdecimal.  


