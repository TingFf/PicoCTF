## Comment  
1. Packet Analysis.  
2. Still not experience enough to get the full picture.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
How about some hide and seek heh?
## Tools Used  
**WireShark**

## Writeup  
1. Download the pcap file.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/PcapPoisoning]
└─$ ls
trace.pcap
```
2. Use wireshark to analyse it.  
![ScreenShot](https://imgur.com/4JcbVgm.png)
3. Packet 1: Malformed packet.  
4. Following based on the IP address.  
5. Packet 2: Sends a TCP SYN packet to create a link to 10.253.0.6.  
6. Packet 3: But based on the ICMP packet, destination cant be reach.  
7. Packet 4: Tries to request for username and password.  
8. Packet 507: Sends another TCP SYN packet to recreate the session.
9. Which is where the flag is hidden.
![ScreenShot](https://imgur.com/w6CYO5d.png)
10. Flag:
```
picoCTF{P64P_4N4L7S1S_SU55355FUL_4624a8b6}
```

## Stuff Learned  
1. Look at one suspicious packet then follow base on the IP address.  


