## Comment  
1. Stuck at the password part.
2. Link: https://medium.com/@quackquackquack/picoctf-trivial-flag-transfer-protocol-writeup-20c5d2d0dfdf

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Figure out how they moved the flag.
## Tools Used  
**wireshark, steghide, online decrypter**

## Writeup  
1. First download the pcap file.  
2. At first glance, the whole pcap seems to be mostly tftp protocol packet.  
3. In wireshark, u can extract the tftp object during the point of time the packet was transferred.  
![ScreenShot](https://imgur.com/wASVdsE.png)  
4. Extract it.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ ls
instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb  tftp.pcapng
```
5. Usually, I will focus on the images.  
6. I used the tools that I used on steganography challenges.  
7. `binwalk`, `exiftool`, `zsteg`, `strings`.  
8. But all did not give any hints or clues of the flag.  
9. So I move on to other files.  
10. I download the program.deb.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ sudo dpkg -i program.deb                         
[sudo] password for kali: 
(Reading database ... 483273 files and directories currently installed.)
Preparing to unpack program.deb ...
Unpacking steghide (0.5.1-9.1+b1) over (0.5.1-9.1+b1) ...
Setting up steghide (0.5.1-9.1+b1) ...
Processing triggers for man-db (2.13.0-1) ...
Processing triggers for kali-menu (2025.1.1) ...
```
11. Here is the first hints.  
12. steghide is another tool for steganography.  
13. I tried to use steghide on the images.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ steghide extract -sf picture1.bmp                
Enter passphrase: 
```
14. But need a passphrase.  
15. So now we need a passphrase for the image file.  
16. There are more file that we did not look into.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ cat instructions.txt
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ cat plan            
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```
17. Seems suspicious and look like some encryption.  
18. There is a popular tools that decrypts a lot of cipher text.  
![ScreenShot](https://imgur.com/d8Fuq6X.png)  
19. According to this tool, it look like its encrypted with ROT13.  
20. Basically, it shift each char 13 times in the alphabetic order.  
21. You can use the website to decrypt or cyber chef.  
```
I USED THE PROGRAM AND HID IT WITH-DUEDILIGENCE. CHECK OUT THE PHOTOS

TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER .FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
```
22. These two strings are the plain text.  
23. `I USED THE PROGRAM AND HID IT WITH-DUEDILIGENCE.`This sentence seems like the clue as the dash shoulden be there.  
24. It says it hide it with `DUEDILIDENCE` so maybe that is the password.  
25. Entering the password on three of the .bmp file.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ steghide extract -sf picture1.bmp 
Enter passphrase: 
zsh: suspended  steghide extract -sf picture1.bmp
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ steghide extract -sf picture1.bmp 
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ steghide extract -sf picture2.bmp 
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ steghide extract -sf picture3.bmp 
Enter passphrase: 
wrote extracted data to "flag.txt".

┌──(kali㉿kali)-[~/CTF_PlayGround/TrivialFlagTransferProtocol]
└─$ cat flag.txt 
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```
26. Flag:  
`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`


## Stuff Learned  
1. A .BMP file stands for Bitmap Image File — it's a raster graphics image format used to store pixel data.  
2. For any encrypted strings, try to use the online tools use here (link: https://www.dcode.fr/cipher-identifier)  
3. Tools to use for steganography. (zteg, steghide, binwalk, exiftool, strings)  


