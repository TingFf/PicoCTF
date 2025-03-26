## Comment  
1. Very educational challenge.  
2. Hiding data in the msb of the image.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
This image passes LSB statistical analysis, 
but we can't help but think there must be something to the visual artifacts present in this image...
## Tools Used  
**Sigbits.py**

## Writeup  
1. Download the png.
```
wget https://artifacts.picoctf.net/c/303/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```
2. Open using ```eog```.
![ScreenShot](https://imgur.com/fFPvTPm.png)
3. Looks like the image is corrupted.  
4. Based on the description, went to research at what is LSB statistical analysis.  
5. Then the title indicates that there may be hidden data in the msb.
6. Did some more research.
7. Sigbits.py 
8. Link to the tools
```
https://github.com/Pulho/sigBits
```
9. It a steganography significant bits image decoder.
10. Run the tool on the img.
```
Steganography significant bits image decoder


## Stuff Learned  
1. Argument is stored in w0.  
