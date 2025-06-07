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
13. In the gallery directory, there are four .bmp images file.
14. To view, I use ```eog 1.bmp``` to view.  

![image](https://github.com/user-attachments/assets/fb8a551f-e0ad-442f-ae74-23dbf7eceec6)

15. Usually, when I find any image. I would assume there is hidden data.
16. For image steganography, tools I use ```steghide extract -sf 1.bmp```.
    
```
# The -sf option stands for "stegofile", which specifies the file that contains the hidden data
                                                                                                                 
┌──(kali㉿kali)-[/mnt/myimage/home/yone/gallery]
└─$ steghide extract -sf 3.bmp
Enter passphrase: 

```
17. The image is password protected.
18. But remember there is a password stated by yone.
19. Entering the password for all images.
20. Does not work for 7.bmp.
21. For the rest, a text file is extracted.
```
┌──(kali㉿kali)-[/mnt/myimage/home/yone/gallery]
└─$ ls                   
1.bmp  3.bmp 
2.bmp  7.bmp  dracula.txt.enc  frankenstein.txt.enc  les-mis.txt.enc
```
22. Its seems the txt file is encoded.
23. There was also a hint about crytographyn key and iv was provided.
24. I research and found that with the information I have, I can decrypt the file using the command below.  

```openssl enc -d -aes-256-cbc -K 58593a7522257f2a95cce9a68886ff78546784ad7db4473dbd91aecd9eefd508 -iv 7a12fd4dc1898efcd997a1b9496e7591 -in les-mis.txt.enc -out les-mis.txt```  
25. ```-iv```: initialize vector. It's require for aes cbc mode before encrypting.  
26. (Remember learning AES during school but...anyways!!)  
27. After looking through the text file, there wasn't much clues to continue so I was kinda stuck here.  
28. Remember the the password used before was the combination of four LOL champions.  

![image](https://github.com/user-attachments/assets/84c8adda-03af-4c91-956f-875b91a2064b)
29. Looking at these conversation, it safe to assume the password is also the combination of games characters.

![image](https://github.com/user-attachments/assets/226fce93-cf03-48a3-98b3-c45b1d7585f2)  
30. There is another hint here.  
31. The password should be LOL champions as well with these two as the start.  
32. Now we have to crack the other two.  
33. I create a dictionary of all the possible combination using python.  
34. I have attached the script.  
35. It just brute force the password.  
36. Now, another new file was found.  

![image](https://github.com/user-attachments/assets/8b9b9c2a-75dd-4203-b4c4-901405c2964e)

37. There was another file that might leads to something.

![image](https://github.com/user-attachments/assets/3509a70e-50a1-46ed-85aa-16ac99b01a8d)

38. After doing some research, this is apparently golden base ratio encoded text.
39. Had no idea what is golden base ration even after I read online so had to look at writeup.
40. Link is below:  
https://medium.com/@12gnathic.xsgb9/picoctf-2023-unforgottenbits-writeup-3f758528bcdc
41. In this write, they provides the decoder for this so I just utilize it.

```
C:\Users\User\PycharmProjects\PythonProject\.venv\Scripts\python.exe C:\Users\User\PycharmProjects\PythonProject\phi_decoder.py 
salt=2350e88cbeaf16c9
key=a9f86b874bd927057a05408d274ee3a88a83ad972217b81fdc2bb8e8ca8736da
iv=908458e48fc8db1c5a46f18f0feb119f
```
42. The output of the encoded text was another set of salt, key and IV.
43. I suppose this is use for the last enc txt file so lets decrypt it.
```
┌──(kali㉿kali)-[/mnt/myimage/home/yone/gallery]
└─$ openssl enc -d -aes-256-cbc -K a9f86b874bd927057a05408d274ee3a88a83ad972217b81fdc2bb8e8ca8736da -iv 908458e48fc8db1c5a46f18f0feb119f -in ledger.1.txt.enc -out ledger.1.txt

┌──(kali㉿kali)-[/mnt/myimage/home/yone/gallery]
└─$ ls
1.bmp  3.bmp  brute_force.py  dracula.txt.enc   frankenstein.txt.enc  ledger.1.txt.enc  les-mis.txt.enc
2.bmp  7.bmp  dracula.txt     frankenstein.txt  ledger.1.txt          les-mis.txt
                                                                                                                    
┌──(kali㉿kali)-[/mnt/myimage/home/yone/gallery]
└─$ cat ledger.1.txt
avidreader13                                                 PAID
    Les Mis, Dracula, Frankenstein, Swiss Family 
    Robinson, Don Quixote, A Tale of Two Cities

513u7h                                                       PAID
    Don Quixote

masterOfSp1n                                                 PAID
    Swiss Family Robinson, A Tale of Two Cities

AwolCoyote                                                   PAID
    Les Mis, Dracula

picoCTF                                                    UNPAID
    picoCTF{f473_53413d_8a5065d1}

```
44. It worked.  
45. Here is the flag:  
`picoCTF{f473_53413d_8a5065d1}`  



## Stuff Learned  
1. Golden base ratio encode
