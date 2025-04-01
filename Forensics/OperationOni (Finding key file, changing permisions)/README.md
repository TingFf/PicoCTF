## Comment  
1. Had to look at writeup.  
2. Not sure what I was looking for.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Download this disk image, find the key and log into the remote machine.  

## Tools Used  
**Sleuthkit**  

## Writeup  
1. Check the partitions.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```
2. Look at file directory.
```                                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ fls -o 206848 disk.img              
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles
```
3. Look under root.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ fls -o 206848 disk.img 470 
r/r 2344:       .ash_history
d/d 3916:       .ssh

┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ fls -o 206848 disk.img 3916 
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
```
4. Check the contents of the files.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ icat -o 206848 disk.img 2345      
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ icat -o 206848 disk.img 2346
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGCtd7hso2E7OQItY6aTjMMyKZb1FVmeBfnVjyHcGYos root@localhost
```
5. Extract the files.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ icat -o 206848 disk.img 2345 > key               
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ ls   
disk.img  key
```
6. Due to some control, the permissions on the key file must be modified before sending to the server.
```                                                                                                                                                                                                                                        
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ ssh -i key -p 51683 ctf-player@saturn.picoctf.net 
The authenticity of host '[saturn.picoctf.net]:51683 ([13.59.203.175]:51683)' can't be established.
ED25519 key fingerprint is SHA256:XBSvB1lk28EctsAVdKJtsl0A7C5bonqPrvHCYH8aEy4.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '[saturn.picoctf.net]:51683' (ED25519) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'key' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "key": bad permissions
ctf-player@saturn.picoctf.net's password: 

┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ ls -l
total 235524
-rw-rw-r-- 1 kali kali 241172480 Aug  4  2023 disk.img
-rw------- 1 kali kali       411 Apr  1 02:39 key
```
7. Then follow based on the steps from the description.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/OperationOni]
└─$ ssh -i key -p 62088 ctf-player@saturn.picoctf.net 
aaWelcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt 
picoCTF{k3y_5l3u7h_339601ed}
ctf-player@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```
8. Flag:
```
picoCTF{k3y_5l3u7h_339601ed}
```

## Stuff Learned  
1. Look at root directory first.


