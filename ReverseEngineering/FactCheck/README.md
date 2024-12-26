## Comment  
1.  Type of challenge that relates to getting the flag before its gets erase.  
2.  Since the challenge is quite straightforward, I have only document the part when I debug using gdb. In addition, analysing the decompiled code documented as I find it useful.

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Retrieve the flag before the deconstructor erase it  
## Tools Used  
**Ghidra, gdb**  

## Writeup 
![ScreenShot](https://imgur.com/TE898FO.png) 
![ScreenShot](https://imgur.com/gLPZn5f.png) 
1. Based on ghidra, the flag is stored in RAX at memory 0x0101860 before its deconstructed.

![ScreenShot](https://imgur.com/i6jjVjD.png)  
2. Add a break point at that memory in gdb. (Remember to change its permission using chmod +x file)

![ScreenShot](https://imgur.com/w6Nxa9V.png)  
3. Examined the stack memory address in RAX, and looks like it contains a pointer. (address starting with 0x5555..)  
4. Examined the content the pointer pointing too.  
5. Flag obtained.  

## Stuff Learned  
1. Examples of deconstructor in a decompiled code.
2. Adding breakpoints in gdb
3. The memory in ghidra and gdb is a bit different hence need to pad with the same number while following the last three digits.
4. std::string = Constructor
5. Due to memory safety, C++ automatically manages memory for std::string objects, so explicit destructor calls from the decompiled code are unnecessary.
