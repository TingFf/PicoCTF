## Comment  
1. New tool to use on image disk.
2. Straight forward  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image.
## Tools Used  
**srch_strings**

## Writeup  
1. For this challenge, unlike previous ones, just use one command to search the entire image disk file.
2. For other sleuthkit challenges, have to use `mmls`,`icat` and `fls`.  
```
srch_strings -a -n 15 dds1-alpine.flag.img > extracted_strings.txt`
```
4. option `-a` scans the entire file, not just data sections.
5. option `-n` filter by string length.
6. After strings extracted, use grep to get the flag.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Disk,disk,sleuth!]
└─$ cat extracted_strings.txt | grep "picoCTF{"
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}
```
7. Flag:
```
picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}
```

## Stuff Learned  
1. `srch_strings` is like the the enhanced version of `strings`.
2. `terminal-fu:` It’s a term that basically refers to being highly skilled at using the terminal (aka shell kung-fu).
