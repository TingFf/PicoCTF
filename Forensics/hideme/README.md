## Comment  
NA

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. 
They decided to investigate and found out that there was more than what meets the eye here.
## Tools Used  
**eog, binwalk**

## Writeup  
1. Download the image.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/hideme]
└─$ wget https://artifacts.picoctf.net/c/258/flag.png                                               
--2025-03-26 06:48:54--  https://artifacts.picoctf.net/c/258/flag.png
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.165.102.33, 3.165.102.104, 3.165.102.27, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.165.102.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 42937 (42K) [application/octet-stream]
Saving to: ‘flag.png’

flag.png                        100%[=======================================================>]  41.93K  --.-KB/s    in 0.005s  

2025-03-26 06:48:55 (7.67 MB/s) - ‘flag.png’ saved [42937/42937]

                                                                                                                                
┌──(kali㉿kali)-[~/CTF_PlayGround/hideme]
└─$ ls
flag.png
```
2. It opens up to be nothing of interest, just the logo of picoCTF.
3. Triage using binwalk.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/hideme]
└─$ binwalk flag.png                                                  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2876, uncompressed size: 3029, name: secret/flag.png
42915         0xA7A3          End of Zip archive, footer length: 22
```
4. Extract using ``` binwalk -e flag.png```
5. Extracted files:
```
┌──(kali㉿kali)-[~/CTF_PlayGround/hideme/_flag.png.extracted]
└─$ ls
29  29.zlib  9B3B.zip  secret
```
6. Folder secret seems suspicious.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/hideme/_flag.png.extracted/secret]
└─$ ls
flag.png
```
7. Its another flag.  
8. Open using ```eog flag.png```.    
![ScreenShot](https://imgur.com/qG70tID.png)
9. Flag:
```
picoCTF{Hiddinng_An_imag3_within_@nima9e_d55982e8}
```

## Stuff Learned  
NA


