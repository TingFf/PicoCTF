## Comment  
1. Another image stegnography challenge.  

## Challenge Overview  
**Difficulty:** Easy  
**Description:** Use the right tool to find the flag.  
## Tools Used  
**Exiftool**  

## Writeup  
1. Challenge start with a zip file.
2. Unzip it and its a jpg file.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/CanYouSee]
└─$ ls
ukn_reality.jpg  unknown.zip
```
3. First I tried to use binwalk.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/CanYouSee]
└─$ binwalk -e ukn_reality.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented
```
5. But it failed.
6. So went to find out any other tool.
```
Tools for JPEG Steganography:
Steghide – Hides data in JPEGs but primarily works with BMP and WAV.
StegSolve – Can analyze hidden messages in images.
Stegdetect – Detects steganography in JPEG files.
OutGuess – A steganographic tool designed for JPEGs.
Exiftool – Reads and modifies metadata.
```
7. Tried zsteg.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/CanYouSee]
└─$ zsteg ukn_reality.jpg
[!] #<ZPNG::NotSupported: Unsupported header "\xFF\xD8\xFF\xE0\x00\x10JF" in #<File:ukn_reality.jpg>>
```
8. Tried exiftool.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/CanYouSee]
└─$ exiftool ukn_reality.jpg  
ExifTool Version Number         : 13.10
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:03:11 20:05:51-04:00
File Access Date/Time           : 2025:03:21 03:00:03-04:00
File Inode Change Date/Time     : 2025:03:21 02:59:56-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```
9. Saw a base64 encoded metadata and I know that is the flag.
10. Decode in cyberchef.
11. Flag:
```
picoCTF{ME74D47A_HIDD3N_3b9209a2}
```
 
## Stuff Learned  
1. ExifTool is a powerful command-line utility used to read, write, and modify metadata in various file formats, including JPEG, PNG, PDF, MP4, and many others. It is commonly used in digital forensics, steganography, and CTF challenges to extract or manipulate hidden data.
2. It shows the metadata of the jpg file.  


