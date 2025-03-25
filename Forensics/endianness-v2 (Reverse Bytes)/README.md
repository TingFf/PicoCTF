## Comment  
1. New type of forensic challenge.
2. Reversing the bytes.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. 
We're not even sure what type of file it is.

## Tools Used  
**bvi, eog**

## Writeup  
1. After downloading challenge file, I did some triage.  
```
                                                                                                                                
┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ file challengefile.1 
challengefile.1: data
                                                                                                                                
┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ exiftool challengefile.1 
ExifTool Version Number         : 13.10
File Name                       : challengefile.1
Directory                       : .
File Size                       : 3.4 kB
File Modification Date/Time     : 2024:03:11 20:36:50-04:00
File Access Date/Time           : 2025:03:24 22:01:26-04:00
File Inode Change Date/Time     : 2025:03:24 22:00:57-04:00
File Permissions                : -rw-rw-r--
Warning                         : Processing JPEG-like data after unknown 1-byte header
                                                                                                                                
┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ binwalk challengefile.1 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ strings challengefile.1 
 '.$
#,")7(
410,'
4428=943.<
!2222222222222222222222222222222222222222222222222
)('&654*:987FEDCJIHGVUTSZYXWfedcjihgvutszyxw
5*)(9876EDC:IHGFUTSJYXWVedcZihgfutsjyxwv
Tx+(
(<yA
G2PF
Y'@2
o/IB
*klv
77T4
F8Yx$
1O3F
,UQk
hM|A
kV.l
X^5q
24.h
0Rg~
sodmn@
#iRy
yskg
[H%'
0>0U
3Gb}
XdW6
JGr ^
4)|/
OdX|
''      YP4w
Xk}N
H13O
-2yD
=ouY
+oh[
hcY 
~/EQ

```
2. Doesn't seem very useful.
3. Since the challenge relates to bytes organized, I use bvi to view the binary.  
![ScreenShot](https://imgur.com/ZubdOiK.png)
4. Notice the first 4 bytes (header signature) is actually the reverse of a jpg header.
5. JPG header:
```
FF D8 FF E0 (JPG header) → E0 FF D8 FF
```
6. So maybe I have to reverse every 4 bytes to get a proper file.  
7. Created a python script to auto it.
```
with open('challengefile','rb') as f:
	data = f.read()
	data_hex = data.hex()
data = str(data_hex)

array_data = [data[i:i+8] for i in range(0,len(data),8)]
reversed_values = ["".join(reversed([h[i:i+2] for i in range(0, len(h), 2)])) for h in array_data]
reversed_values = "".join(reversed_values)

with open('reversedbytes.txt','w') as f:
	f.write(reversed_values)
```
8. After reversing the bytes, I check the file type again and it changed to a jpeg image.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ file reversedbytes.txt 
reversedbytes.txt: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 300x150, components 3
```
9. Renaming the filename.
```                                                                                                                             
┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ mv reversedbytes.txt reversedbytes.jpg
```
10. View the image using eog.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/endianness-v2]
└─$ eog reversedbytes.jpg
```
![ScreenShot](https://imgur.com/q0gW8B2.png)  
11. Flag:
```
picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_94cc03f3}
```

## Stuff Learned  
1. Looking at the header might be useful sometimes.
2. JPG header and trailer
```
JPG Header : FF D8 FF E0
JPG Tailer: FF D9
```


