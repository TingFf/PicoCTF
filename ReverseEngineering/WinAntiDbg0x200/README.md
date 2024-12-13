## Comment
For this challenge, it is similar to WinAntiDbg0x100, so I chose not to document it separately.

## Challenge Overview
**Difficulty:** Medium  
**Description:** As it is a reverse engineering challenge, it supplies an exe file and requests that a debugger be used to locate the flag.
## Tools Used
**Ghidra,x32Dbg**  
## WriteUp
Once I downloaded the exe file, the first thing I assessed was whether to use x32 or x64 debugger, and I can determine that by examining the register display in Ghidra.
![ScreenShot of Ghidra](https://imgur.com/a/t5pUg5s)


