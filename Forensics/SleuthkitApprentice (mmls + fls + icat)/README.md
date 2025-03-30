## Comment  
1. Another Sleuthkit challenge but with no hints.  
2. Had to research and use the cmds I learn from previous challenge.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Download this disk image and find the flag.
## Tools Used  
**mmls, fls, icat** 

## Writeup  
1. Since this challenges is regards to using tools under the sleuthkit.
2. The cmds to use should be clear.  
3. First use mmls to check whether there is partitions.  

```
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```
4. As we can see, there is 3 partitions of interest.  
5. With the offset, we can view the file system in the partitions.
```
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ fls -o 2048  disk.flag.img              

d/d 11: lost+found
r/r 12: ldlinux.sys
r/r 13: ldlinux.c32
r/r 15: config-virt
r/r 16: vmlinuz-virt
r/r 17: initramfs-virt
l/l 18: boot
r/r 20: libutil.c32
r/r 19: extlinux.conf
r/r 21: libcom32.c32
r/r 22: mboot.c32
r/r 23: menu.c32
r/r 14: System.map-virt
r/r 24: vesamenu.c32
V/V 25585:      $OrphanFiles

┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ fls -o 206848  disk.flag.img

Cannot determine file system type

┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ fls -o 360448  disk.flag.img 

d/d 451:        home
d/d 11: lost+found
d/d 12: boot
d/d 1985:       etc
d/d 1986:       proc
d/d 1987:       dev
d/d 1988:       tmp
d/d 1989:       lib
d/d 1990:       var
d/d 3969:       usr
d/d 3970:       bin
d/d 1991:       sbin
d/d 1992:       media
d/d 1993:       mnt
d/d 1994:       opt
d/d 1995:       root
d/d 1996:       run
d/d 1997:       srv
d/d 1998:       sys
d/d 2358:       swap
V/V 31745:      $OrphanFiles
```
6. Maybe due to the OS the partition 206848 file system cannot be determine.
7. I choose to analyse offet 360448 as it looks more familier.
8. To list what are the files in the directory.
```
fls -o 360448 -r  disk.flag.img
```
9. Use grep to filter.
```
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ fls -o 360448 -r  disk.flag.img | grep "flag"
++ r/r * 2082(realloc): flag.txt
++ r/r 2371:    flag.uni.txt
```
10. To extract use icat.
11. I extracted both to see the content.
```
──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ fls -o 360448 -r  disk.flag.img | grep "flag"
++ r/r * 2082(realloc): flag.txt
++ r/r 2371:    flag.uni.txt
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ icat -o 360448 disk.flag.img 2371 > flag.uni.txt

                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ icat -o 360448 disk.flag.img 2082 > flag.txt 

                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ ls
disk.flag.img  flag.txt  flag.uni.txt
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ cat flag.txt    
            3.449677            13.056403
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitApprentice]
└─$ cat flag.uni.txt                             
picoCTF{by73_5urf3r_3497ae6b}
```
12. Flag:
```
picoCTF{by73_5urf3r_3497ae6b}

```

## Stuff Learned  
1. mmls
    - **Purpose:** Displays the partition layout of a disk image.
    - **What it shows:** Partition types, start/end sectors, and lengths.
    - **Use:** To understand the structure of the disk and locate partitions.
2. icat
    - **Purpose:** Extracts the content of a file from a disk image using its inode number.
    - **What it shows:** The file data.
    - **Use:** To recover or view files from a disk image (even deleted ones).
3. fls
    - **Purpose:** Lists files and directories in a disk image.
    - **What it shows:** File and directory names, inode numbers, and whether they’re deleted.
    - **Use:** To explore and identify files in the disk image.


