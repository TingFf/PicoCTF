## Comment  
1. Tried to use the stuff I learn from the android series challenges.  
2. In the end, just need to search for the flag among all the files.

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Can you handle APKs?
Download the android apk here.

## Tools Used  
**unzip**

## Writeup  
1. Hint 1: unzip apk  
![ScreenShot](https://imgur.com/O6Ji8Yg.png)  
2. These are all the files.  
3. Hint 2: Assume we need to search for the flag among all the files.  
4. /res:  
![ScreenShot](https://imgur.com/IlT7KR9.png)  
5. Using grep to search for keywords like ```picoCTF``` or ```flag```.  
![ScreenShot](https://imgur.com/pDP6CLw.png)  
6. There is a file name flag.txt in this directory.  
7. Using cat to see the content.  
![ScreenShot](https://imgur.com/yQcyGoA.png)  
8. Seems like hex string.  
9. Put into cyberchef.  
10. Flag:  
```
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_a3eb5ac2}
```
 
## Stuff Learned  
1. unzip works on apk file.
2. To search for file name in all files and sub directory:
```
find . | grep "name"
```

