## Comment  
1. Think is a series of challenge teaching people about Sleuthkit.
2. First tools use is ```mmls```

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Download the disk image and use mmls on it to find the size of the Linux partition. 
Connect to the remote checker service to check your answer and get the flag. 
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory. 

## Tools Used  
**mmls**

## Writeup  
1. Pretty straight forward challenge.  
2. Just follow the instructions.  
```
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitIntro]
└─$ ls
disk.img.gz
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitIntro]
└─$ gunzip disk.img.gz     
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitIntro]
└─$ ls
disk.img
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitIntro]
└─$ mmls disk.img       
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
3. The length is 202752.  
```
┌──(kali㉿kali)-[~/HTBTryout/SleuthkitIntro]
└─$ nc saturn.picoctf.net 58673
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```

## Stuff Learned  
1. Sleuth Kit (TSK) is an open-source digital forensics toolkit used for analyzing disk images and investigating file systems.
   It provides command-line tools for examining file structures, recovering deleted files, and analyzing metadata.
2. Key Features of Sleuth Kit (TSK):
    -  File System Analysis: Supports FAT, NTFS, EXT, HFS+, and more.
    -  Deleted File Recovery: Recovers lost or deleted files from disk images.
    -  Metadata Inspection: Examines timestamps, permissions, and other attributes.
    -  Volume & Partition Analysis: Identifies and examines partitions within a disk.
    -  Integration with Autopsy: Works with Autopsy, a GUI-based forensic platform for easier analysis.
3. Common Tools in Sleuth Kit:
    -  ```fls```: Lists files in a file system.
    - ```icat```: Extracts file contents.
    - ```istat```: Displays metadata of a file.
    - ```mmls``` : Lists partition layout of a disk.
    - ```blkls```: Recovers deleted data from unallocated space.

