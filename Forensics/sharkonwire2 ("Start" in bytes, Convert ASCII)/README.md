## Comment  
NA

## Challenge Overview  
**Difficulty:** Medium  
**Description:** 
We found this packet capture. Recover the flag that was pilfered from the network.
## Tools Used  
**Wireshark** 

## Writeup  
1. First look at the pcap file.  
2. There are some malformed packet but its just distraction.  
![ScreenShot](https://imgur.com/vM9eVng.png)  
3. There is another filter bar(ctrl+f).  
4. Search "start" by packet bytes, strings.  
![ScreenShot](https://imgur.com/ed5Uxlx.png)  
5. Search based on the src ip.address.  
![ScreenShot](https://imgur.com/K8mqp4a.png)  
6. Enable name resolution on transport address.  
7. Convert the port numbers to names respectively.
8. Convert the last three digits to ascii value of each packet based on the time.
9. Flag:
```
picoCTF{p1LLf3r3d_data_v1a_st3g0}
```

## Stuff Learned  
1. You can filter and search in the bytes and string using ctrl+f.  
2. Enable 'Resolve Transport Address'.  
