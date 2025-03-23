<img width="492" alt="image" src="https://github.com/user-attachments/assets/d6289e6a-47be-41e6-a7c3-acd8d5e2ecad" />## Comment  
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
![ScreenShot](https://imgur.com/D1Ia2RO.png)


## Stuff Learned  
1. Argument is stored in w0.  


