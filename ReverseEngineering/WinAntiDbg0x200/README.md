## Comment
For this challenge, it is similar to WinAntiDbg0x100, so I chose not to document it separately.

## Challenge Overview
**Difficulty:** Medium  
**Description:** As it is a reverse engineering challenge, it supplies an exe file and requests that a debugger be used to locate the flag.
## Tools Used
**Ghidra,x32Dbg**  
## WriteUp
Once I downloaded the exe file, the first thing I assessed was whether to use x32 or x64 debugger, and I can determine that by examining the register display in Ghidra.  
![ScreenShot of Ghidra](https://imgur.com/pA0uWMR.png)  
Since its EAX,...,etc, the exe uses 32 bit hence I use x32dbg.  

![ScreenShot of Ghidra](https://imgur.com/q5YqPxQ.png)  
I begin by reviewing the file while examining the logs.

![ScreenShot of x32dbg](https://imgur.com/KgNm3a7.png)  
Considering the hints provided, I assumed it might be connected to the fork() function.

![ScreenShot of Ghidra](https://imgur.com/w7ZKpHk.png)  
Line 60-62: The output string of the hint
Line 64-79: Seems like to get the flag, must past some conditions(Line 65 & 67)
