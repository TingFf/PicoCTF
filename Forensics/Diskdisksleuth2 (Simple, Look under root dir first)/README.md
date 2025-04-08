## Comment  
1. Simple SleuthKit Challenge.

## Challenge Overview  
**Difficulty:** Medium  
**Description:** 
All we know is the file with the flag is named ```down-at-the-bottom.txt```...  
## Tools Used  
**SleuthKit, gunzip**

## Writeup  
1. First I download and unzip the file using gunzip.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ wget https://mercury.picoctf.net/static/aed64c508175df5fe23207c10e0e47e5/dds2-alpine.flag.img.gz
--2025-04-07 18:06:02--  https://mercury.picoctf.net/static/aed64c508175df5fe23207c10e0e47e5/dds2-alpine.flag.img.gz
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 29770550 (28M) [application/octet-stream]
Saving to: ‘dds2-alpine.flag.img.gz’

dds2-alpine.flag.img.gz                                    100%[========================================================================================================================================>]  28.39M  8.19MB/s    in 3.5s    

2025-04-07 18:06:06 (8.19 MB/s) - ‘dds2-alpine.flag.img.gz’ saved [29770550/29770550]

                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ ls
dds2-alpine.flag.img.gz
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ gunzip dds2-alpine.flag.img.gz                
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ ls
dds2-alpine.flag.img
```
2. Then utilizing sleuthkit, first I check the partition.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ mmls dds2-alpine.flag.img 
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```
3. Continue to dive deep into the Linux partition.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ fls -o 2048 dds2-alpine.flag.img              
d/d 26417:      home
d/d 11: lost+found
r/r 12: .dockerenv
d/d 20321:      bin
d/d 4065:       boot
d/d 6097:       dev
d/d 2033:       etc
d/d 8129:       lib
d/d 14225:      media
d/d 16257:      mnt
d/d 18289:      opt
d/d 16258:      proc
d/d 18290:      root
d/d 16259:      run
d/d 18292:      sbin
d/d 12222:      srv
d/d 16260:      sys
d/d 18369:      tmp
d/d 12223:      usr
d/d 14229:      var
V/V 32513:      $OrphanFiles
```
4. Based on the hints, we need to find a file call ```down-at-the-bottom.txt```.
5. U can list all the files using this cmd:
```
fls -o 2048 -r dds2-alpine.flag.img | grep "down-at-the-bottom.txt"
```
6. And just grep the specific text file.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ fls -o 2048 -r dds2-alpine.flag.img | grep "down-at-the-bottom.txt"
+ r/r 18291:    down-at-the-bottom.txt
```
7. To extract that file, use the inode to specify which file u want to extract.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ icat -o 2048  dds2-alpine.flag.img 18291 > here.txt 
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ ls
dds2-alpine.flag.img  here.txt
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth2]
└─$ cat here.txt        
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( 3 ) ( _ ) ( f ) ( 5 ) ( 5 ) ( 6 ) ( 5 ) ( e ) ( 7 ) ( b ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
```
8. Flag:
```
picoCTF{f0r3ns1c4t0r_n0v1c3_f5565e7b}
```


## Stuff Learned  
1. Look under root directory first.  


