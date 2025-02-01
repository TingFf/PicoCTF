## Comment  
NA

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Reverse back from base64 then url encoding.  
## Tools Used  
**CyberChef**  

## Writeup  
![ScreenShot](https://imgur.com/btTQQNJ.png)  
![ScreenShot](https://imgur.com/UDnQcqb.png)  
1. Copy and paste the entire base64 encoding string into cyberchef.  
2. From base64 encoded string -> base64 decode -> url encoded string -> url decode string.  

## Stuff Learned  
**What is URL Encoding?**  
URL encoding (also called percent-encoding) is used to convert characters in a URL into a format that can be safely transmitted over the internet.  
**Why is URL Encoding Needed?**  
Prevent reserved(e.g., ?, &, =) and unsafe(like spaces or non-ASCII characters) char from being misinterpreted.  
**Example**
%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%38%34%66%64%35%30%39%35  

