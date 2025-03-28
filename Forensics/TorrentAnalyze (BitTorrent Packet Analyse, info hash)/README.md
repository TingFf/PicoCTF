## Comment  
1. Just gotten humbled by HTBCTF easy difficulty challenges.
2. PicoCTF really is for begineers only.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
SOS, someone is torrenting on our network. One of your colleagues has been using torrent to download some files on the company’s network. 
Can you identify the file(s) that were downloaded? 
The file name will be the flag, like picoCTF{filename}. Captured traffic.
## Tools Used  
**WireShark**

## Writeup  
1. PCAP file:
![ScreenShot](https://imgur.com/Ylh8Qwm.png)
2. This challenges requires use to find the file name.  
3. One idea is to use the hash to get the respective file.
4. This is possible because bittorrent packets contain info hash as one the data.
![ScreenShot](https://imgur.com/0sq0rzh.png)
5. According to these packets, ip 192.168.73.132 might be a seeder.
6. Then we filter based on the ip address and protocol.  
![ScreenShot](https://imgur.com/Sb7Yckl.png)
7. There are multiples info hash, so just copy and paste and search on the net.
![ScreenShot](https://imgur.com/O7jmQCe.png)
![ScreenShot](https://imgur.com/X3S9Yln.png)
8. Flag:
```
picoCTF{ubuntu-19.10-desktop-amd64.iso}
```

## Stuff Learned  
1. Seeders (Seeds) 🌱  
    - People who have the full file and are sharing it.  
    - If someone has finished downloading the file and keeps uploading it for others, they are a seeder.  
    - The more seeders, the faster the download because there are more sources.  
    - Example: Imagine you have the whole puzzle and you help others by giving them pieces.  
2. Leechers (Downloaders) 🧲  
    - People who are still downloading the file.  
    - A leecher takes pieces from seeders and other leechers.  
    - If there are too many leechers and not enough seeders, downloads can be slow.  
    - Example: You are collecting puzzle pieces from different people, but you don’t have the full puzzle yet.  
3. Peers (General Term) 🤝  
    - Anyone sharing parts of the file (both seeders and leechers).  
    - A peer can be downloading, uploading, or both.  
    - Example: If 10 people are working on the same puzzle together, they are peers.  
4. How BitTorrent Works in Simple Steps  
    - You download a torrent file (or use a magnet link).  
    - Your BitTorrent software (like uTorrent, qBittorrent) connects you to peers.  
    - Your computer downloads pieces of the file from seeders and leechers.  
    - At the same time, your computer uploads pieces to others.  
    - Once you have all pieces, your torrent is complete.  
    - If you stay connected, you become a seeder and help others download.  
