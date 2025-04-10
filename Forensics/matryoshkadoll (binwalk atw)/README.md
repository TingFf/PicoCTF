## Comment  
1. Binwalk all the way.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?
## Tools Used  
**Binwalk**

## Writeup  
1. Binwalk is a tool that extract any hidden files or data within another file.  
```
┌──(kali㉿kali)-[~/matryoshkadoll]
└─$ wget https://mercury.picoctf.net/static/1b70cffdd2f05427fff97d13c496963f/dolls.jpg              
--2025-04-09 17:57:00--  https://mercury.picoctf.net/static/1b70cffdd2f05427fff97d13c496963f/dolls.jpg
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 651634 (636K) [application/octet-stream]
Saving to: ‘dolls.jpg’

dolls.jpg                                                  100%[=======================================================================================================================================>] 636.36K   598KB/s    in 1.1s    

2025-04-09 17:57:03 (598 KB/s) - ‘dolls.jpg’ saved [651634/651634]

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll]
└─$ binwalk dolls.jpg  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378954, uncompressed size: 383938, name: base_images/2_c.jpg
651612        0x9F15C         End of Zip archive, footer length: 22

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll]
└─$ binwalk -e dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378954, uncompressed size: 383938, name: base_images/2_c.jpg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll]
└─$ ls
dolls.jpg  _dolls.jpg.extracted
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll]
└─$ cd _dolls.jpg.extracted   
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted]
└─$ ls
4286C.zip  base_images
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted]
└─$ cd base_images             
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images]
└─$ ls
2_c.jpg
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images]
└─$ eog 2_c.jpg          
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images]
└─$ binwalk 2_c.jpg      

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 526 x 1106, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg
383805        0x5DB3D         End of Zip archive, footer length: 22
383916        0x5DBAC         End of Zip archive, footer length: 22

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images]
└─$ binwalk -e 2_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
187707        0x2DD3B         Zip archive data, at least v2.0 to extract, compressed size: 196043, uncompressed size: 201445, name: base_images/3_c.jpg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images]
└─$ ls
2_c.jpg  _2_c.jpg.extracted
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images]
└─$ cd _2_c.jpg.extracted  
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted]
└─$ ls
2DD3B.zip  base_images
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/matryoshkadoll/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted]
└─$ cd base_images       
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls
3_c.jpg
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ binwalk -e 3_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
123606        0x1E2D6         Zip archive data, at least v2.0 to extract, compressed size: 77651, uncompressed size: 79807, name: base_images/4_c.jpg

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ ls
3_c.jpg  _3_c.jpg.extracted
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images]
└─$ cd _3_c.jpg.extracted 
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted]
└─$ ;s
s: command not found
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted]
└─$ ls
1E2D6.zip  base_images
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted]
└─$ cd base_images       
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ ls
4_c.jpg
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ binwalk -e 4_c.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
79578         0x136DA         Zip archive data, at least v2.0 to extract, compressed size: 63, uncompressed size: 81, name: flag.txt

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ ls
4_c.jpg  _4_c.jpg.extracted
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images]
└─$ cd _4_c.jpg.extracted 
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ ls
136DA.zip  flag.txt
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/…/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted]
└─$ cat flag.txt         
picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}
```

## Stuff Learned  
NA


