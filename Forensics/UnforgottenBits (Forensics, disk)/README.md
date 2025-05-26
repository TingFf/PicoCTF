## Comment  
1. It's been some time since I note down a CTF.
2. Hard forensic challenge

## Challenge Overview  
**Difficulty:** Hard  
**Description:**   
Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.


## Tools Used  
**Autospy**

## Writeup  
![image](https://github.com/user-attachments/assets/f6cb32da-1207-42f8-b64c-3f36695ad965)
1. Since its a disk image, using the gui autopsy to analysis the content.  
2. There is four partitions.  
3. As usual, focusing on vol4.  
4. Usually I will look into the root folder if there is any interesting findings.

<img width="719" alt="image" src="https://github.com/user-attachments/assets/e82fc205-25c5-4e2c-b2cd-c0320fa0a687" />  

6. Seems nothing interesting.  
7. Moving on to home.

<img width="701" alt="image" src="https://github.com/user-attachments/assets/dd72b6cc-34af-4031-af2d-2bdba35042f2" />
8. There is a user call yone. 
9. Assume is reference from lol.  
10. After some, traversing through the files. There is a conversation between the yone and avidreader.  

![image](https://github.com/user-attachments/assets/a52065bc-257d-4a23-9986-373de2ba9f39)  

11. There is some hints/clues that caught my attention such as the ```password(akalibardzyratrundle)``` and ```salt=0f3fa17eeacd53a9 key=58593a7522257f2a95cce9a68886ff78546784ad7db4473dbd91aecd9eefd508 iv=7a12fd4dc1898efcd997a1b9496e7591```
12. Noting down these two clues first and move on for now.  
13. In the gallery directory, 
```openssl enc -d -aes-256-cbc -K 58593a7522257f2a95cce9a68886ff78546784ad7db4473dbd91aecd9eefd508 -iv 7a12fd4dc1898efcd997a1b9496e7591 -in les-mis.txt.enc -out les-mis.txt```





## Stuff Learned  
