## Comment  
1. New knowledge on slack space.  
2. For this challenge have to use the new autopsy instead of the old one.  


## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
'Suspicious' is written all over this disk image.
## Tools Used  
**Autopsy**

## Writeup  
1. Downloading a dd.sda1 file.  
2. This file instead of the image disk file, its one of the partition image file.  
3. To analyse image disk files, you can use the sleuthkit command line such as mmls, fls and icat.  
4. But for this challenge, u have to use the new autopsy.  
![ScreenShot](https://imgur.com/yJno3XR.png)  
5. It seems the flag is not in the suspicious-txt file.  
6. Looking at the hints on slack space.  
7. We have to enable viewing of slack space to find the hidden file.  
![ScreenShot](https://imgur.com/RDdD4H0.png)  
![ScreenShot](https://imgur.com/H0WLNhn.png)  
8. It seems the flag is in reverse so I created a simple script to reverse it.  
```
def reverse():
    string = "}1937befc_3<_|Lm_111t5_3b{FTCocip"
    for i in string[::-1]:
        print(i, end = "")

def main():
    reverse()

if __name__ == "__main__":
    main()
```
9.Flag:
```
picoCTF{b3_5t111_mL|_<3_cfeb7391}
```

# Stuff Learned  

Slack space is the leftover empty space inside a disk cluster when a file doesn’t use the entire cluster.
Imagine this:
Your disk is divided into fixed-size blocks called clusters.
Let’s say each cluster is 4096 bytes.
Now imagine you save a small file:
The file is only 3000 bytes.
The filesystem still gives it a whole 4096-byte cluster.
The extra space (4096 - 3000 = 1096 bytes) is not erased —
it's called:
👉 Slack Space
That leftover space might still contain old deleted data from other files, random junk, or sensitive information.

-------------------------------------------------------------------------------------------------------------------

Can hide fragments of deleted files.
May contain old sensitive info that wasn’t fully overwritten.
Can sometimes even store malware or steganography tricks.

-------------------------------------------------------------------------------------------------------------------
Let’s say a deleted .txt file used to live there,
and a new small file got written over it.
The new file might not fill the whole cluster,
so the tail end could still contain part of the old text!



