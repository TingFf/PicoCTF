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
![ScreenShot]()
6. Click New Case.  
7. Enter all the info and use default settings.  

## Stuff Learned  
1. Argument is stored in w0.  







picoCTF{1_533_n4m35_80d24b30}
