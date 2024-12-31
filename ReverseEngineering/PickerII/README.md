## Comment  
NIL

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Exploiting the vulnerability of eval function to get the flag.
## Tools Used  
**CyberChef**  

## Writeup  
![Screenshot](https://imgur.com/w3l8hd6.png)  
1. Exploiting the eval function to the win function and get the flag.

## Stuff Learned
1. Even though eval(print(open('flag.txt','r').read())()) returns error as there is another bracket after the print function but it still evaluates the line and execute the print(open('flag.txt','r').read()) which open the flag.txt, read it and prints the flag out.

