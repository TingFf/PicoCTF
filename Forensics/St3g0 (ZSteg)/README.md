## Comment  
1. For image stegnography challenge, I just use all the tools I used before first.  
2. If non of them works, then need do some research.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Using Zsteg
## Tools Used  
**Zsteg**

## Writeup  
![ScreenShot](https://imgur.com/dQAptDT.png)    
1. Receive this image.  
2. Tried solving by using tools lile strings,file, stepic, exiftools and binwalk.  
3. Also checked whether is it packed.  
4. All did not gave me the flag.  
5. Then I tried zteg.
```
┌──(kali㉿kali)-[~/HTBTryout/St3g0]
└─$ zsteg pico.flag.png 
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_a1062667}$t3g0"
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
b2,b,lsb,xy         .. text: "AAPAAQTAAA"
b2,b,msb,xy         .. text: "HWUUUUUU"
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b4,r,lsb,xy         .. file: Targa image data (16-273) 65536 x 4097 x 1 +4352 +4369 - 1-bit alpha - right "\021\020\001\001\021\021\001\001\021\021\001"
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map 272 x 17 x 16 +257 +272 - 1-bit alpha "\020\001\021\001\021\020\020\001\020\001\020\001"
b4,bgr,lsb,xy       .. file: Targa image data - Map 273 x 272 x 16 +1 +4113 - 1-bit alpha "\020\001\001\001"
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
```
6. Which is a tool used to detect hidden data in png (focus on LSB Steganography).  
7. LSB Steganography is a method where hidden data are split and hide at each of the LSB in each pixel (RGB).  
8. The image does not shows any corruption because changing LSB in the RGB of each pixel does not create much changes that is visble to human eyes.  
9. Flag:
```
picoCTF{7h3r3_15_n0_5p00n_a1062667}
```

## Stuff Learned  
NA


