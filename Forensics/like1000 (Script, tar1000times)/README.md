## Comment  
1. Now after first two weeks of the red alpha training on python.  
2. I have a easier time when doing scripting.  


## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
This .tar file got tarred a lot.  
## Tools Used  
**Python** 

## Writeup  
1. Download a tar file from the link.  
2. Using cmd  
```tar -xvf 1000.tar```  
3. Will give 999.tar and so on.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/like1000]
└─$ tar -xvf 1000.tar                                                                       
999.tar
filler.txt

┌──(kali㉿kali)-[~/CTF_PlayGround/like1000]
└─$ tar -xvf 999.tar 
998.tar
filler.txt

```
4. Instead of repeating a 1000 times.  
5. I wrote a python script to automate.  
```
import os 
import subprocess

counter = 1000
while counter>0:
	subprocess.run(["tar","-xvf",f"{counter}.tar"])
	subprocess.run(["rm",f"{counter}.tar"]) # Remove the previous file to reduce the space used.  
	counter-=1
```
6. After the script it done, the final file is a png file.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/like1000]
└─$ ls
filler.txt  flag.png  script.py
```
7. Using `eog` to view the image.  
8. Flag:  
`picoCTF{l0t5_0f_TAR5}`


## Stuff Learned  
1. How to script in command line using `os` and `subprocess` modules.  
