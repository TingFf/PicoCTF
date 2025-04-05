## Comment  
1. Similar to previous challenges, need to change the binary header to a valid one.  
2. Not sure what I could do to remove the red backgrouund so went to look at writeup.  
**Link:** https://medium.com/@matus.vaclav1/picoctf-advanced-potion-making-eff6b4ebbdcf


## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it! 
## Tools Used  
**bvi, eog, online tool**

## Writeup  
1. As usual, download the challenge file.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ wget https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making
--2025-04-04 22:17:18--  https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.165.102.27, 3.165.102.104, 3.165.102.60, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.165.102.27|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30372 (30K) [binary/octet-stream]
Saving to: ‘advanced-potion-making’

advanced-potion-making                                     100%[========================================================================================================================================>]  29.66K  --.-KB/s    in 0.006s  

2025-04-04 22:17:20 (4.66 MB/s) - ‘advanced-potion-making’ saved [30372/30372]

                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ ls
advanced-potion-making
```
2. First, I start with some triage on the file.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ file advanced-potion-making 
advanced-potion-making: data
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ strings advanced-potion-making           
IHDR
sRGB
gAMA
        pHYs
v9IDATx^
(>Zv
e2>|
28\%]
y22\+
,a`
<P~^
 8)!
O``
$_Bn
r2/9
'w|F
...

┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ binwalk advanced-potion-making                                                               

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
91            0x5B            Zlib compressed data, compressed

                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ exiftool advanced-potion-making.png
Error: File not found - advanced-potion-making.png
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ exiftool advanced-potion-making    
ExifTool Version Number         : 13.10
File Name                       : advanced-potion-making
Directory                       : .
File Size                       : 30 kB
File Modification Date/Time     : 2021:05:03 21:38:44-04:00
File Access Date/Time           : 2025:04:04 22:18:17-04:00
File Inode Change Date/Time     : 2025:04:04 22:17:20-04:00
File Permissions                : -rw-rw-r--
Error                           : Unknown file type
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ 
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ zsteg advanced-potion-making    
[!] #<ZPNG::NotSupported: Unsupported header "\x89PB\x11\r\n\x1A\n" in #<File:advanced-potion-making>>
```

3. Looking at the error the tool zteg gave.  
4. It seems there is something wrong with the header.  
5. Open using ```bvi```.  
![ScreenShot](https://imgur.com/mBcU94j.png)  
6. I copied the header and search whether its similar to any header.  
7. Apparently, its very similar to png header.  
![ScreenShot](https://imgur.com/i2n8UaU.png)  
8. Using bvi, I replace some of the bytes.  
![ScreenShot](https://imgur.com/j0u6UXT.png)  
9. After that, I use ```file``` again to check the file type.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ file advanced-potion-making 
advanced-potion-making: PNG image data, 2448 x 1240, 8-bit/color RGB, non-interlaced
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ mv advanced-potion-making advanced-potion-making.png 
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/advanced-potion-making]
└─$ ls
advanced-potion-making.png
```
10. Indeed it was a png file.  
11. Open using ```eog```.   
![ScreenShot](https://imgur.com/Rq4DxjZ.png)
12. The image is just a red background.  
13. Wonder is it just covering the flag.  
14. Using online tools, I found this image editor.
![ScreenShot](https://imgur.com/mqT3yYg.png)
15. Follow the steps.
    - Color change
    - B&W
16. Flag:
```
picoCTF{w1z4rdry}
```

## Stuff Learned  
1. PNG Header:
```
89 50 4E 47 0D 0A 1A 0A    --> PNG signature
00 00 00 0D                --> Length of the IHDR chunk (13 bytes)
49 48 44 52                --> 'IHDR' (Image Header Chunk)
```


