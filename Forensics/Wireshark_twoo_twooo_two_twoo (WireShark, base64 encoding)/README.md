## Comment  
1. WireShark challenge.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Can you find the flag?
## Tools Used  
**wireshark**

## Writeup  
1. For this challenge, a pcap file is provided.  
![ScreenShot](https://imgur.com/iDWmb1p.png)
2. First, I look through the packet to find any obvious clues or hints about the flag.  
3. Below, there is multiple http get request on a flag.html. However, it seems like fake flag.  
![ScreenShot](https://imgur.com/yOJxe9R.png)
4. Moving on, there are a lot of dns request to reddshrimpandherring.com which seems like to start with small part of a base64 encoding string.  
5. But there are some request that is not base64 encoding.  
6. So we have to somehow find filters hints to get those that are base64 encoding instead of searching line by line.  
7. At the end, there is a request that is obvious that its a base64 due to the equal sign.  
![ScreenShot](https://imgur.com/GUtvDn7.png)
8. Search, base on these filters.  
`dns && ip.src == 192.168.38.104`
![ScreenShot](https://imgur.com/UM5qGNn.png)  
9. Gather the strings and combine then in squence.  
```
1633	9.334169	192.168.38.104	18.217.1.57	DNS	93	Standard query 0xdf26 A cGljb0NU.reddshrimpandherring.com
2042	11.870534	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x3a30 A RntkbnNf.reddshrimpandherring.com
2444	14.503146	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x531d A M3hmMWxf.reddshrimpandherring.com
3140	16.404809	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x99dd A ZnR3X2Rl.reddshrimpandherring.com
3429	18.239530	192.168.38.104	18.217.1.57	DNS	93	Standard query 0x16f6 A YWRiZWVm.reddshrimpandherring.com
3969	20.266171	192.168.38.104	18.217.1.57	DNS	89	Standard query 0xbe68 A fQ==.reddshrimpandherring.com
```
10. Decode this cyberchef to get the flag.  
![ScreenShot](https://imgur.com/0Oopkum.png)  
11. Flag.
`picoCTF{p4ck37_5h4rk_ceccaa7f}`

## Stuff Learned  
1. Look for obvious hints on the flag.  
2. Utilizing the filters.  


