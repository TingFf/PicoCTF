## Comment  
NA

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Someone might have hidden the password in the trace file. 
Find the key to unlock this file. 
This tracefile might be good to analyze.
## Tools Used  
**Wireshark**

## Writeup  
1. Received one pcap file and a zip file that requires password.
```
                                                                                                                                
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ wget https://artifacts.picoctf.net/c/493/flag.zip
--2025-03-26 09:46:28--  https://artifacts.picoctf.net/c/493/flag.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.165.102.104, 3.165.102.60, 3.165.102.27, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.165.102.104|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 231 [application/octet-stream]
Saving to: ‘flag.zip’

flag.zip                        100%[=======================================================>]     231  --.-KB/s    in 0s      

2025-03-26 09:46:29 (232 MB/s) - ‘flag.zip’ saved [231/231]

                                                                                                                                
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ wget https://artifacts.picoctf.net/c/493/dump.pcap
--2025-03-26 09:46:38--  https://artifacts.picoctf.net/c/493/dump.pcap
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.165.102.60, 3.165.102.33, 3.165.102.104, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.165.102.60|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7413 (7.2K) [application/octet-stream]
Saving to: ‘dump.pcap’

dump.pcap                       100%[=======================================================>]   7.24K  --.-KB/s    in 0.001s  

2025-03-26 09:46:39 (9.19 MB/s) - ‘dump.pcap’ saved [7413/7413]
```
2. Using wireshark to view the pcap.
3. There are some packets contain the hints.
4. "Is this the flag"
![ScreenShot](https://imgur.com/88qi3Lz.png)
5. "Could the flag have been splitted"
![ScreenShot](https://imgur.com/FPks7vR.png)  
6. There is a base64 encoded data.(The = sign)  
![ScreenShot](https://imgur.com/iOoMHj1.png)
7. Paste the string in cyber chef.  
![ScreenShot](https://imgur.com/ErlFgNe.png)
```
picoCTF{R34DING_LOKd_
```
8. This is the password to the zip file.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ ls
dump.pcap  flag.zip
                                                     
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ unzip flag.zip
Archive:  flag.zip
[flag.zip] flag password: 
 extracting: flag                    
                                                     
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ ls
dump.pcap  flag  flag.zip
                                                     
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ cat flag.txt                        
cat: flag.txt: No such file or directory
                                                     
┌──(kali㉿kali)-[~/CTF_PlayGround/FindAndOpen]
└─$ cat flag    
picoCTF{R34DING_LOKd_fil56_succ3ss_419835ef}
```
9. Flag:
```
picoCTF{R34DING_LOKd_fil56_succ3ss_419835ef}
```

## Stuff Learned  
NA



