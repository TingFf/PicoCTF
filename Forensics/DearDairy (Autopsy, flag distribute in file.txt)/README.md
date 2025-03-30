## Comment  
1. First time knowing and using autopsy. 

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
If you can find the flag on this disk image, we can close the case for good!
## Tools Used  
**Autopsy, gunzip**  

## Writeup  
1. File downloaded.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/DearDiary]
└─$ ls
disk.flag.img.gz
```
2. To open a .gz file using ```gunzip```.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/DearDiary]
└─$ gunzip disk.flag.img.gz
                                                                                                                                 
┌──(kali㉿kali)-[~/CTF_PlayGround/DearDiary]
└─$ ls
disk.flag.img
```
3. Autopsy is a kali linux tool that is commonly use to analyse disk image file.
4. Open using ```sudo autopsy```
5. Then open browser ```http://localhost:9999/autopsy```.
6. Click New Case.
![ScreenShot](https://imgur.com/GdTVZXe.png)
![ScreenShot](https://imgur.com/FelNAIp.png)
7. Enter all the info and use default settings.  
![ScreenShot](https://imgur.com/9AiQMzt.png)
8. Analyse the disk image and it seems on the 7th unit onwards is part of the flag.  
![ScreenShot](https://imgur.com/TbeSfAP.png)
![ScreenShot](https://imgur.com/oukCX9q.png)
![ScreenShot](https://imgur.com/EIifAbd.png)
9. Gather all the flag and piece them together.
10. Flag:
```
picoCTF{1_533_n4m35_80d24b30}
```

## Stuff Learned  
1. Use Autopsy to analyse image disk.  
2. .gz file can be unzip suing gunzip.  







