## Comment  
1. Still can't analyse PCAP file, will always get overwhelm.  
 

## Challenge Overview  
**Difficulty:** Easy  
**Description:** Extract the base64 data from each fragment in each packet and get the flag.  
## Tools Used  
**WireShark**  

## Writeup  
1. Lets take a look at the pcap file.
![ScreenShot](https://imgur.com/2DPxhmj.png)
2. After clicking around, I notice that some packets data fragment is base64 encoded at the end.
![ScreenShot](https://imgur.com/qOdNEEv.png)
3. There are 7 of them.
```
NjZkMGJmYg==  -> 66d0bfb
bnRfdGg0dA==  -> nt_th4t
ezF0X3c0cw==  -> {1t_w4s
XzM0c3lfdA==  -> _34sy_t
cGljb0NURg==  -> picoCTF
YmhfNHJfOQ==  -> bh_4r_9
fQ==          -> }
```
4. Each decoded as fragment part of the flag.
5. At first I thought is was according to the time when the packet came in but is not.
6. Not sure whats the hint is for but after rearranging.
7. Flag:
```
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}
```

## Stuff Learned  
1. Base64 indicators is the ==, = is not.  


