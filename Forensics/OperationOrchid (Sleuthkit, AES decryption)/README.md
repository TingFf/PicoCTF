## Comment  
1. Used Sleuthkit again.  
2. Need decrypt using AES.   

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Download this disk image and find the flag.
## Tools Used  
**Sleuthkit**

## Writeup  
1. After downloading and unzip the disk image file, I used what I learn from previous challenge and use sleuthkit commands to look into the disk image.  
2. Used ```mmls``` to see the partitions of the disk.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ mmls disk.flag.img                                                           
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
```
3. To view the file directoy, use ```fls```.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ fls -o 411648 disk.flag.img 
d/d 460:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 81: proc
d/d 82: dev
d/d 83: tmp
d/d 84: lib
d/d 87: var
d/d 96: usr
d/d 106:        bin
d/d 120:        sbin
d/d 466:        media
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles
```
4. Then based on experience, I look whether there is flag.txt file.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ fls -o 411648 -r disk.flag.img | grep flag.txt
+ r/r * 1876(realloc):  flag.txt
+ r/r 1782:     flag.txt.enc
```
5. The * means that the file is deleted from the system.  
6. I extract the enc file using ```icat```.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ icat -o 411648 disk.flag.img 1782 > flag.txt

┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ ls
disk.flag.img  flag.txt
```
7. Did some triage on the file.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ file flag.txt                                 
flag.txt: openssl enc'd data with salted password
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ strings flag.txt 
Salted__S
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ cat flag.txt     
Salted__S�+%���+�O��k�ђ(A����c��
                                @]ԣ
L�ޢȤ7� ���؎$�'%
```
8. Seems like its encrypted but not sure the algorithm.  
9. According to chatgpt, AES is commonly used with openssl and a password.  
10. So now I need to look for the password.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ strings disk.flag.img | grep "password" | grep "aes" 
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
```
11. It seems like the command to encrypt the file.txt and output flag.txt.enc.  
12. To decrypt, use the same command but add a option ```-d``` to decrypt.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ openssl aes256 -d -salt -in flag.txt -out real_flag.txt -k unbreakablepassword1234567

*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
401747D6957F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ ls
disk.flag.img  flag.txt  real_flag.txt
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOrchid]
└─$ cat real_flag.txt 
picoCTF{h4un71ng_p457_1d02081e}
```
13. Flag:
```
picoCTF{h4un71ng_p457_1d02081e}
```
     
## Stuff Learned  
1. salted with openssl may means AES is being use as the encrypted algoritm.  
2. * : file is deleted from the file system.  


