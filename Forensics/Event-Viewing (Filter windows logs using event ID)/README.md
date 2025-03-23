## Comment  
1. A story-based challenge.  
2. Base on the story line, find out how the company got infected with malware.  
3. Very educational.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Filter based on event ID and get parts of the flag.   
## Tools Used  
**evtx_dump.py**

## Writeup  
1. Here is the story:  
One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. The story given by the employee is as follows:

    1. They installed software using an installer they downloaded online
    2. They ran the installed software but it seemed to do nothing
    3. Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.  

See if you can find evidence for the each of these events and retrieve the flag (split into 3 pieces) from the correct logs!  
2. Downloaded the log file:
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Event_Viewing]
└─$ ls
Windows_Logs.evtx
```
3. First time encounter a .evtx file so went to do some research.
4. Find out have to use ```evxt_dump.py``` to output 
```
┌──(kali㉿kali)-[~/CTF_PlayGround/Event_Viewing]
└─$ evtx_dump.py Windows_Logs.evtx > output.xml
```
5. Look like this.  
![ScreenShot](https://imgur.com/4ftMKFJ.png)

6. Based on the hints, I have to filter based on the windows event ID.  
7. Did some more research and each event ID represent different meaning.  
8. First, keywords: ```installer software```,```download online```.  
9. Event ID 11707: Windows Installer started  
10. Event ID 1033: Windows Installer outcome  
11. Filter based on these two ID and found the first part of the flag.  
![ScreenShot](https://imgur.com/7XI4DtD.png)
![ScreenShot](https://imgur.com/aMDNhCe.png)
12. Next, looking at the name of the software which obviously seems suspicious.  
13. Filter based on that and found the second part of the flag.  
![ScreenShot](https://imgur.com/rd64xXi.png)
14. Event ID 4657: A registry value was modified.  
15. Looking at the registry, this malware seems to modify the run registry which relates to some persistence regarding malware.  
16. It says immediate shutdown hence maybe that what it does.  
17. When the user on the desktop it will shutdown immediately.  
18. Lastly, keywords ```bootup```,```shutdown```.
19. Event ID 1074: System Shutdown or Restart Initiated
![ScreenShot](https://imgur.com/1HwkGoY.png)
20. shutdown.exe is not a windows exe file hence its probably installed by the malware.
21. Piecing the flags together:
```
picoCTF{Ev3nt_vi3wv3r_1s_a_pr3tty_us3ful_t00l_81ba3fe9}
```


## Stuff Learned  
Here's should be how the whole story goes.  
1. Employees may have download some malware due to phishing from emails.  
2. After downloading the malware, the user run the malware and it installed a custom shutdown.exe.  
3. It then modifies the run registry which will cause the the shutdown.exe to run whenever the system bootsup.  
4. For a malware to does its things, it must be run.  


