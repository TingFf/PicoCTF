## Comment  
1. Been using quite a lot of exiftool for the challenges.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**   
The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?
Set the timestamps on this picture to ```1970:01:01 00:00:00.001+00:00``` with as much precision as possible for each timestamp. 
In this example, ```+00:00``` is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. 
As an example, this timestamp is acceptable as well: ```1969:12:31 19:00:00.001-05:00```. 
For timestamps without a timezone adjustment, put them in GMT time ```(+00:00)```.   
The checker program provides the timestamp needed for each.  
Use this picture.  
## Tools Used  
**Exiftool, Bvi**

## Writeup  
1. Image metadata:  
![ScreenShot](https://imgur.com/dk31Lvs.png)  
2. To modify the image metadata.  
3. Using exiftool cmd line:  
![ScreenShot](https://imgur.com/qeKaFFF.png)
4. To view more information:
```
exiftool -v3 original.png
```
6. Only the samsung trailer timestamp needs a bit more than using cmdline.
![ScreenShot](https://imgur.com/tiaiMco.png)
7. As exiftool does not support as it a third party thing.  
8. Hence have to modify the data using different method.  
9. View the binary of the png file using bvi.
![ScreenShot](https://imgur.com/E96Q5k3.png)
10. Bvi cmd:
```
Shift G -> To the bottom
:set memmov -> To enable editing
i -> Insert
x -> Delete
esc -> Go the command mode
r -> replace
```
11. Replace all the metadata to 0.
12. Then send the modified png to the server and the flag will be displayed.  
13. Flag:
```
picoCTF{71m3_7r4v311ng_p1c7ur3_a25174ab}
```

## Stuff Learned  
1970:01:01 00:00:00.001+00:00 
1. January 1, 1970, is known as the Unix Epoch. It is the reference point from which Unix time (also called POSIX time or Epoch time) is calculated.

