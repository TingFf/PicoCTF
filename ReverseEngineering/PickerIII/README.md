:---
## Comment  
1. Had fun doing this challenge.    
2. Wanted to give up and look at writeup but didnt so i am proud.
3. Python debugger is pretty useful.

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Modifying the table to get the function to read a different name a call the win function to print the flag.  
## Tools Used  
**CyberChef, Pdb**  

## Writeup  

![Screenshot](https://imgur.com/Kbo4Gyc.png)  
1. The main objective to let the get_func to return the string "win" so that the eval("win"+"()") will call the win function which will print the flag.  
![Screenshot](https://imgur.com/HquRYwx.png)  
![Screenshot](https://imgur.com/bW8ji46.png)  
2. I used PDB to debug the code to understand the data and variables.  
3. Basically the the get_func will loop through the func_table and depending on the starting index, it will read until a space and return the string.  
4. Hence, what is require is to change the table to win and plus a space.  
![Screenshot](https://imgur.com/utoIEpM.png)  
5. To change the table, we have to utilize one of the write_variable function to change the global variable func_table.  
6. But take note there is a condition camparing the length of the table which means the length of the original string must be equal to the modified string.  
7. After modifying the table to the new string, call the get_func again and this time it will return the string win and the call_func will call the win function.  
![Screenshot](https://imgur.com/81B0biq.png)  
8. Here are the steps.  

## Stuff Learned  
1. Sometimes just give a bit more time to solve the challenge before looking at the writeup.  
2. How to use python debugger.
3. eval() and exec() has vulnerabilities.
