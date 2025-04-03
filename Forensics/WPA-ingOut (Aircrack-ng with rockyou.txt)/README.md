## Comment  
1. Used chatgpt to search for aircrack-ng.


## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, 
especially if I used the same wireless network password as one in the rockyou.txt credential dump. 
Use this 'pcap file' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.

## Tools Used  
**aircrack-ng, wireshark**

## Writeup  
1. Open up the pcap file using wireshark.
![ScreenShot](https://imgur.com/vKgHtUt.png)
2. Its my first time ever encountering these type pcap.
3. Didnt analyse much and just went to see the hints.
4. The work aircrack-ng appears a few times so I went to chatGPT for it.
5. It turns out Aircrack-ng is a suite of tools used for assessing Wi-Fi network security.
6. It primarily focuses on WEP and WPA/WPA2-PSK key cracking by capturing packets and performing cryptographic attacks to recover the network key.
7. Below are the steps:
```
┌──(kali㉿kali)-[~/CTF_PlayGround/WPA-ingOut]
└─$ aircrack-ng wpa-ing_out.pcap                                                
Reading packets, please wait...
Opening wpa-ing_out.pcap
Resetting EAPOL Handshake decoder state.
Resetting EAPOL Handshake decoder state.
Read 23523 packets.

   #  BSSID              ESSID                     Encryption

   1  00:5F:67:4F:6A:1A  Gone_Surfing              WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening wpa-ing_out.pcap
Resetting EAPOL Handshake decoder state.
Resetting EAPOL Handshake decoder state.
Read 23523 packets.

1 potential targets

Please specify a dictionary (option -w).
```
8. These says that the PCAP file contains a WPA handshake for the network ```Gone_Surfing``` and need a wordlist to attempt cracking the password.
9. Then I remember the description says something on rockyou.txt so I went to research.
10. Apparantly, rockyou.txt is a famous password wordlist commonly used for password cracking.
11. It contains over 14 million real-world passwords that were leaked from the RockYou.com data breach in 2009.
12. Since these are actual passwords used by real people, it's highly effective for brute-force and dictionary attacks on WPA handshakes, hashes, and login credentials.
13. The rockyou.txt is already ownloaded in kali linux.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/WPA-ingOut]
└─$ ls /usr/share/wordlists/

amass  dirbuster   fasttrack.txt  john.lst  metasploit  rockyou.txt.gz  wfuzz
dirb   dnsmap.txt  fern-wifi      legion    nmap.lst    sqlmap.txt      wifite.txt
                                                                                                                    
┌──(kali㉿kali)-[~/CTF_PlayGround/WPA-ingOut]
└─$ gunzip /usr/share/wordlists/rockyou.txt.gz


gzip: /usr/share/wordlists/rockyou.txt: Permission denied
                                                                                                                    
┌──(kali㉿kali)-[~/CTF_PlayGround/WPA-ingOut]
└─$ sudo gunzip /usr/share/wordlists/rockyou.txt.gz

[sudo] password for kali: 
                                                                                                                    
┌──(kali㉿kali)-[~/CTF_PlayGround/WPA-ingOut]
└─$ ls                      
wpa-ing_out.pcap
                                                                                                                    
┌──(kali㉿kali)-[~/CTF_PlayGround/WPA-ingOut]
└─$ aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 00:5F:67:4F:6A:1A wpa-ing_out.pcap

Reading packets, please wait...
Opening wpa-ing_out.pcap
Resetting EAPOL Handshake decoder state.
Resetting EAPOL Handshake decoder state.
Read 23523 packets.

1 potential targets


                               Aircrack-ng 1.7 

      [00:00:01] 1195/10303727 keys tested (1088.54 k/s) 

      Time left: 2 hours, 37 minutes, 44 seconds                 0.01%

                          KEY FOUND! [ mickeymouse ]


      Master Key     : 61 64 B9 5E FC 6F 41 70 70 81 F6 40 80 9F AF B1 
                       4A 9E C5 C4 E1 67 B8 AB 58 E3 E8 8E E6 66 EB 11 

      Transient Key  : 62 37 2F 54 3B 7B B4 43 9B 37 F4 57 40 FD D1 91 
                       86 7F FE 26 85 7B AC DD 2C 44 E6 06 18 03 B0 0F 
                       F2 75 A2 32 63 F7 35 74 2D 18 10 1C 25 F9 14 BC 
                       41 DA 58 52 48 86 B0 D6 14 89 F6 77 00 7B AB 00 

      EAPOL HMAC     : 65 2F 6C 0E 75 F0 49 27 6A AA 6A 06 A7 24 B9 A9 


```
14. Flag:
```
picoCTF{mickeymouse}
```



## Stuff Learned  
1. ```aircrack-ng -w <wordlist.txt> -b 00:5F:67:4F:6A:1A wpa-ing_out.pcap```
      - Replace <wordlist.txt> with an actual wordlist file (e.g., rockyou.txt).
      - ```-b 00:5F:67:4F:6A:1A``` → The target BSSID (Access Point MAC) which is from the previous aircrack-ng result.
      - ```wpa-ing_out.pcap``` → Your packet capture file.
2. The whole story:
    - Summary:
        - You're trying to crack a WPA/WPA2 Wi-Fi password from a captured PCAP file.
        - ✅ You captured a WPA handshake from ```Gone_Surfing```.
        - ✅ Aircrack-ng detected the handshake but needs a wordlist to crack it.
        - ✅ Use rockyou.txt to attempt brute-force guessing.
        - ✅ If Aircrack-ng is slow, convert it for Hashcat and use GPU-based cracking.
    - You captured Wi-Fi traffic (possibly with airodump-ng).
    - The PCAP file contains packets from a Wi-Fi network named ```Gone_Surfing```.
    - It includes a WPA handshake (the key exchange between a client and the router).
    - Now you need to crack the password using a wordlist.
    - Aircrack-ng read the PCAP file and analyzed the captured packets.
    - It found one Wi-Fi network:
        - BSSID → 00:5F:67:4F:6A:1A
        - ESSID (Wi-Fi Name) → Gone_Surfing
        - Encryption → WPA (with 1 handshake detected).
        - Aircrack-ng asked for a dictionary (-w) because WPA/WPA2 can't be cracked without a wordlist.
        - WPA/WPA2 passwords are not stored in the handshake itself.
        - Instead:
            - The handshake encrypts the password using a cryptographic hash.
            - To break it, we must try possible passwords (dictionary attack).
            - Aircrack-ng compares hashes from the wordlist to the handshake hash.




