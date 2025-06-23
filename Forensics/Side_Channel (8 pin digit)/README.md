## Comment  
1. Took me forever to code the script.

## Challenge Overview  
**Difficulty:** Hard  
**Description:** There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?
## Tools Used  
**Python**  

## Writeup  
1. This challenge ask user to enter a 8 digit pin.  
2. Based on the hint, we do not need to decompile and look at the source code.  
3. We can utilizing the time it takes for each digit to know the correct pin.  
4. The longer the time it took to process the digit, the digit is the correct pin.  
```
┌──(kali㉿kali)-[~/CTF_PlayGround/SideChannel]
└─$ ./pin_checker                     
Please enter your 8-digit PIN code:
00000000
8
Checking PIN...
Access denied.
```
5. Obviously, we have to write a script for this.  
6. The correct code is `48390513`  
7. Flag:  
`picoCTF{t1m1ng_4tt4ck_914c5ec3}`  
 
## Stuff Learned  
1. Side channel attack utilize time to interpret get the secret.  
