## Comment
For this challenge, it is similar to WinAntiDbg0x100, so I chose not to document it separately.

## Challenge Overview
**Difficulty:** Medium  
**Description:** As it is a reverse engineering challenge, it supplies an exe file and requests that a debugger be used to locate the flag.
## Tools Used
**Ghidra,x32Dbg**  
## WriteUp
1. Once I downloaded the exe file, the first thing I assessed was whether to use x32 or x64 debugger, and I can determine that by examining the register display in Ghidra.  
![ScreenShot of Ghidra](https://imgur.com/pA0uWMR.png)  
2. Since its EAX,...,etc, the exe uses 32 bit hence I use x32dbg.  

![ScreenShot of x32dbg](https://imgur.com/q5YqPxQ.png)  
3. I begin by reviewing the file while examining the logs.

![ScreenShot of x32dbg](https://imgur.com/KgNm3a7.png)  
4. Considering the hints provided, I assumed it might be connected to the fork() function.

![ScreenShot of Ghidra](https://imgur.com/w7ZKpHk.png)  
5. Line 60-62: The output string of the hint  
6. Line 64-79: Seems like to get the flag, must past some conditions(Line 65 & 67)  
7. Looking at the memory address respectively to the code in the left panel (Notice the memory address is slightly different in x32dbg, just look at the last 4 numbers and digits)  

![ScreenShot of Ghidra](https://imgur.com/LPVZvg9.png)  
8. At memory address ...1824 & ...182E, make sure the EDX and EAX equals 0.

![ScreenShot of x32dbg](https://imgur.com/wmCPIXR.png)  
9. After passing the checks, go back to logs and the flag should be displayed.

## Stuff Learned  
1. In this challenge, know which line to set a break point.
2. Value in the registers must be modify to past the checks and get the flag.
3. Ensure x32dbg is run as admin.
4. Focus on the last 4 values of the memory addresses.
5. By using function call tree (under windows tab), to have a better understand of the code hierachy


