## Comment  
1. First medium forensic challenge.
2. Have multiple parts to the challenge so it was pretty fun.  


## Challenge Overview  
**Difficulty:** Medium  
**Description:** Inspect the non-existence flag and download a png to get the flag 
## Tools Used  
**Steptic**  

## Writeup  
1. First the challenge brings us to a website.  
![ScreenShot](https://imgur.com/DKl7yHo.png)  
2. Just a bunch of flags.  
3. Looking at the hints."In the country that doesn't exist, the flag persists"  
4. I guess I have to find a country that doesn't exist.  
5. I copied and pasted the whole page into chatGPT.  
![ScreenShot](https://imgur.com/S2K7ZYZ.png)  
6. The country was "Upanzi, Republic"  
![ScreenShot](https://imgur.com/Ukcqmtz.png)  
7. Inspecting the image and find out the img src.
![ScreenShot](https://imgur.com/Gx4bzEB.png)
8. Copied the link and download the image.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/CanYouSee]
└─$ wget http://standard-pizzas.picoctf.net:56405/flags/upz.png     
--2025-03-21 03:41:03--  http://standard-pizzas.picoctf.net:56405/flags/upz.png
Resolving standard-pizzas.picoctf.net (standard-pizzas.picoctf.net)... 3.22.195.189
Connecting to standard-pizzas.picoctf.net (standard-pizzas.picoctf.net)|3.22.195.189|:56405... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1788400 (1.7M) [image/png]
Saving to: ‘upz.png’

upz.png                         100%[=======================================================>]   1.71M  1.16MB/s    in 1.5s    

2025-03-21 03:41:05 (1.16 MB/s) - ‘upz.png’ saved [1788400/1788400]
┌──(kali㉿kali)-[~/CTF_PlayGround/flagsarestepic]
└─$ ls
upz.png
```
9. Another image stegnography challenge.
10. Tried binwalk,zsteg and exiftool.
11. These tools are the tools I learn based on past challenges.
12. Not the correct one.
13. Looking at the challenge title.
```
Flag are stepic
```
14. Went to search what stepic is and found out its another tools for image stegnography.
15. It a python library based hence had to create a script.
16. script.py:
```
┌──(kali㉿kali)-[~/CTF_PlayGround/flagsarestepic]
└─$ cat script.py 
import stepic
from PIL import Image

# Open the stego image
img = Image.open("upz.png")

# Decode the message
message = stepic.decode(img)

print("Hidden message:", message)

┌──(kali㉿kali)-[~/CTF_PlayGround/flagsarestepic]
└─$ python3 script.py
/usr/lib/python3/dist-packages/PIL/Image.py:3402: DecompressionBombWarning: Image size (150658990 pixels) exceeds limit of 89478485 pixels, could be decompression bomb DOS attack.
  warnings.warn(
Hidden message: picoCTF{fl4g_h45_fl4g3e22f365}
```
17. Flag:  
```
picoCTF{fl4g_h45_fl4g3e22f365}
```

## Stuff Learned  
1. Stepic is a Python-based steganography tool that allows you to embed and extract hidden messages in PNG images.  
2. Most forensic are image steganography challenges.  


