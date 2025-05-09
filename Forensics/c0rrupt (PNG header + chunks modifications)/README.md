## Comment  
1. Very educational.
 

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
We found this file. Recover the flag.
## Tools Used  
**Pngchecker, xxd, bvi**

## Writeup  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ ls
mystery
```
1. Based on the hints, the headers and bytes in the file is wrong hence corrupted.  
2. Using bvi to view the bytes.  
```
00000000  89 65 4E 34 0D 0A B0 AA 00 00 00 0D .eN4........
0000000C  43 22 44 52 00 00 06 6A 00 00 04 47 C"DR...j...G
00000018  08 02 00 00 00 7C 8B AB 78 00 00 00 .....|..x...
00000024  01 73 52 47 42 00 AE CE 1C E9 00 00 .sRGB.......
00000030  00 04 67 41 4D 41 00 00 B1 8F 0B FC ..gAMA......
0000003C  61 05 00 00 00 09 70 48 59 73 AA 00 a.....pHYs..
00000048  16 25 00 00 16 25 01 49 52 24 F0 AA .%...%.IR$..
00000054  AA FF A5 AB 44 45 54 78 5E EC BD 3F ....DETx^..?
00000060  8E 64 CD 71 BD 2D 8B 20 20 80 90 41 .d.q.-.  ..A
0000006C  83 02 08 D0 F9 ED 40 A0 F3 6E 40 7B ......@..n@{
...
...
```
3. Looks like png header but some bytes are wrong.  
4. Png header: `89 50 4E 47 0D 0A 1A 0A`  
5. In png, the data is stored in chuncks.  
6. Each chunk has the following 4 parts:  

**Field	Size (bytes)	Description(All chunk follows this structure**  
*Length*	4	Length of the Data field (not including header or CRC)  
*Type*	4	Chunk type (ASCII letters, e.g. IHDR, IDAT)  
*Data*	Variable	The actual chunk data  
*CRC*	4	CRC-32 checksum of the Type and Data fields  

**Chunk Type	Description**  
*IHDR*	Image header (must be first)  
*PLTE*	Palette (for indexed-color images)  
*IDAT*	Image data (can be multiple)  
*IEND*	Marks end of PNG file (must be last)  
*tEXt*	Textual metadata (optional)  
*zTXt*	Compressed text  
*iTXt*	International text  
*tIME*	Timestamp (last modified)  
*gAMA*	Gamma correction  
*bKGD*	Background color  

7. After the png header, the next chunck must be IHDR but its missing.  
```
00000000  89 50 4E 47 0D 0A 1A 0A 00 00 00 0D .PNG........
0000000C  49 48 44 52 00 00 06 6A 00 00 04 47 IHDR...j...G
00000018  08 02 00 00 00 7C 8B AB 78 00 00 00 .....|..x...
00000024  01 73 52 47 42 00 AE CE 1C E9 00 00 .sRGB.......
00000030  00 04 67 41 4D 41 00 00 B1 8F 0B FC ..gAMA......
0000003C  61 05 00 00 00 09 70 48 59 73 AA 00 a.....pHYs..
00000048  16 25 00 00 16 25 01 49 52 24 F0 AA .%...%.IR$..
00000054  AA FF A5 AB 44 45 54 78 5E EC BD 3F ....DETx^..?
00000060  8E 64 CD 71 BD 2D 8B 20 20 80 90 41 .d.q.-.  ..A
0000006C  83 02 08 D0 F9 ED 40 A0 F3 6E 40 7B ......@..n@{
00000078  90 23 8F 1E D7 20 8B 3E B7 C1 0D 70 .#... .>...p
00000084  03 74 B5 03 AE 41 6B F8 BE A8 FB DC .t...Ak.....
00000090  3E 7D 2A 22 33 6F DE 5B 55 DD 3D 3D >}*"3o.[U.==
0000009C  F9 20 91 88 38 71 22 32 EB 4F 57 CF . ..8q"2.OW.
000000A8  14 E6 25 FF E5 FF 5B 2C 16 8B C5 62 ..%...[,...b
000000B4  B1 58 2C 16 8B C5 62 B1 58 2C 16 1D .X,...b.X,..
000000C0  D6 D7 67 8B C5 62 B1 58 2C 16 8B C5 ..g..b.X,...
...
...
```
8. Change the extension to .png and check using png checker to see for any errors.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ pngcheck -v mystery.png
zlib warning:  different version (expected 1.2.13, using 1.3.1)

File: mystery.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in mystery.png
```
9. There is a `CRC` errror in the `pHYs` chunck so lets fixed that.  
10. Looking at the info, pHYs is at offset 0x00042.  
11. This refers to the type section of the chunk, not the length before it so the offset should look like this.  
```
              length    type     data   crc
size            4        4        9      4  
offset       0x0003e  0x00042    ...    ...
```
12. pHYs data chunk size:  
![ScreenShot](https://imgur.com/KmUyykr.png)  
```
00000040  00 09 70 48 59 73 AA AA 16 25 00 00 16 25 01 49 52 24 F0 AA AA FF A5 AB 44 45 54 78 5E EC BD 3F ..pHYs...%...%.IR$......DETx^..?
70 48 59 73 (hex bytes) -> pHYs (Ascii)
```
13. It usually the same for the pixel per unit (x & y) in the data chunk to be the same.  
14. Hence:  
```
00000040  00 09 70 48 59 73 00 00 16 25 00 00 16 25 01 49 52 24 F0 AA AA FF A5 AB 44 45 54 78 5E EC BD 3F ..pHYs...%...%.IR$......DETx^..?
```
15. This should fixed the error.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ pngcheck -v mystery.png
zlib warning:  different version (expected 1.2.13, using 1.3.1)

File: mystery.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery.png
```
16. Now another error is shown.  
17. Continue to fix starting from the end of the pHYs chunk.  
```
0x3e+0x4+0x9(length of the data)+0x4(CRC) = 0x53
```
18. The end of pHYs chunk should be at offset 0x53.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ xxd -g 1 -s 0x53 -l 10  mystery.png 
00000053: aa aa ff a5 ab 44 45 54 78 5e                    .....DETx^
```
19. Look like the next chunk might be IDAT but the ascii of it is wrong.  
20. Multiple IDAT must be in consective.  
21. First change to IDAT:  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ xxd -g 1 -s 0x53 -l 10  mystery.png 
00000053: aa aa ff a5 49 44 41 54 78 5e                    ....IDATx^
```
22. Next, lets check if there are more IDAT chunk.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ binwalk -R "IDAT" mystery.png  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
87            0x57            Raw signature (IDAT)
65544         0x10008         Raw signature (IDAT)
131080        0x20008         Raw signature (IDAT)
196616        0x30008         Raw signature (IDAT)
```
23. There next IDAT should be at offset 0x10008.  
24. Drawn a diagram for easy understanding.  
![ScreenShot](https://imgur.com/IcQBy9Y.png)  
26. Hence it should be `FFA5`.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ xxd -g 1 -s 0x53 -l 10  mystery.png
00000053: 00 00 ff a5 49 44 41 54 78 5e                    ....IDATx^
```
27. Now check again.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/c0rrupt]
└─$ pngcheck -v mystery.png             
zlib warning:  different version (expected 1.2.13, using 1.3.1)

File: mystery.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
No errors detected in mystery.png (9 chunks, 96.3% compression).
```
28. Use `eog` to view the image.  
![ScreenShot](https://imgur.com/whcM6fo.png)  
29. Flag:  
`picoCTF{c0rrupt10n_1847995}`
## Stuff Learned  
1. That image uses headers + chunk + end trailer.  
2. Every chunk uses the same structure.   
3. View the specific offset.  
`xxd -g 1 -s 0x53 -l 10  mystery.png`  
`-g` : Column bytes  
`-s` : offset  
`-l` : Bytes length displayed  
5. View the offset of each chunk in the entire file.  
`binwalk -R "IDAT" mystery.png`
6. `IHDR` must be the first chunk after the 8-byte PNG signature/header.  
7. `IDAT` must appear after IHDR and contains the compressed image data. You can have multiple IDATs (they’re concatenated).  
8. `IEND` must be the last chunk, and it's always empty (zero-length data).  
  
