## Comment  
1. This challenges need to know the zip file signature.

## Challenge Overview  
**Difficulty:** Hard  
**Description:**   
Do you recognize this cyberpunk baddie? We don't either. AI art generators are all the rage nowadays, which makes it hard to get a reliable known cover image. But we know you'll figure it out. The suspect is believed to be trafficking in classics. That probably won't help crack the stego, but we hope it will give motivation to bring this criminal to justice!
Download the image here

## Tools Used  
**hexeditor, python**

## Writeup  
1. This challenges starts off with a bmp file.  

![image](https://github.com/user-attachments/assets/4f1a69b7-a84e-4fca-809b-829725e8310c)

2. Usually for corrupted file, there is something wrong with the bytes level.  
3. Look at the bytes using hex editor.  

![image](https://github.com/user-attachments/assets/0dcb0c54-8479-483d-8b8d-44ce61104d48)

4. Looking at the header, its seems like a normal bmp file.  
5. Take a look at bmp header file.  
https://www.file-recovery.com/bmp-signature-format.htm

6. Then looking further down, there is a zip signature.
```
00000000  42 4D 8A A4  1F 00 00 00   00 00 8A 00  00 00 7C 00                                                                                                                                                              BM............|.
00000010  00 00 C0 03  00 00 1C 02   00 00 01 00  20 00 03 00                                                                                                                                                              ............ ...
00000020  00 00 00 A4  1F 00 23 2E   00 00 23 2E  00 00 00 00                                                                                                                                                              ......#...#.....
00000030  00 00 00 00  00 00 00 7C   00 00 E0 03  00 00 1F 00                                                                                                                                                              .......|........
00000040  00 00 00 00  00 00 42 47   52 73 00 00  00 00 00 00                                                                                                                                                              ......BGRs......
00000050  00 00 00 00  00 00 00 00   00 00 00 00  00 00 00 00                                                                                                                                                              ................
00000060  00 00 00 00  00 00 00 00   00 00 00 00  00 00 00 00                                                                                                                                                              ................
00000070  00 00 00 00  00 00 00 00   00 00 02 00  00 00 00 00                                                                                                                                                              ................
00000080  00 00 00 00  00 00 00 00   00 00 38 67  50 4B 95 52                                                                                                                                                              ..........8gPK.R
00000090  03 04 C6 18  14 00 CE 3D   00 00 10 4A  08 00 6F 56                                                                                                                                                              .......=...J..oV
000000A0  6F 13 10 16  70 56 72 3E   22 9B 0E 3A  64 E7 D5 5A                                                                                                                                                              o...pVr>"..:d..Z
000000B0  B0 95 AB 39  02 00 2D 4E   82 D8 69 3D  06 00 EF 41                                                                                                                                                              ...9..-N..i=...A
000000C0  1C 00 4E 49  1C 00 31 4A   5A 6E AF 1D  4A 68 B4 52                                                                                                                                                              ..NI..1JZn..Jh.R
000000D0  62 6D 11 46  74 6C 09 09   62 6E B4 4A  4E 30 AC 35
```
7. The header of a zip file is:  
![image](https://github.com/user-attachments/assets/e9344bfd-2fbb-4b12-bac5-4a59c45665df)

```
00000080  00 00 00 00  00 00 00 00   00 00 38 67  50 4B 95 52                                                                                                                                                              ..........8gPK.R
00000090  03 04 C6 18  14 00 CE 3D   00 00 10 4A  08 00 6F 56                                                                                                                                                              .......=...J..oV
```
8. But its seems the bytes are in the interval of every two bytes.  
9. `50 4B` then two bytes in between then `03 04`.  
10. After getting just the bytes that we wanted.  
11. The header should consist of these bytes.  

![image](https://github.com/user-attachments/assets/154f46b7-8f58-46eb-ba39-a7d4939bbe75)

12. The end looks like this.  

![image](https://github.com/user-attachments/assets/1529d657-d1be-47fd-849e-22d565d0b2dd)

13. After getting this, we need to clip off the bmp header and the rubbish bytes at the end.  
14. I wrote a script to edit the bytes.  
15. After that, output the bytes data to a zip file and unzip it.
    
![image](https://github.com/user-attachments/assets/cb12abaf-cedc-4fe4-9565-a0bdf58c013f)

16. A text file appears and then just search for the flag.  

![image](https://github.com/user-attachments/assets/a33f4fc3-4403-4931-94fe-ac4f571f4b3d)

17. picoCTF{w0rd_d4wg_y0u_f0und_5h3113ys_m4573rp13c3_539ea4a8}  

## Stuff Learned  
1. Zip and bmp file signature and header  
Zip file signature: https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html  
Bmp file header: https://stackoverflow.com/questions/33483708/understanding-bmp-file  

