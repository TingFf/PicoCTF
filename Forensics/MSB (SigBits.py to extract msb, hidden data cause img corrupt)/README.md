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
┌──(kali㉿kali)-[~/CTF_PlayGround/MSB]
└─$ python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```
11. It will output a txt file.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/MSB]
└─$ ls
Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png  outputSB.txt  sigBits.py
```
12. Open and look at the content.
```
──(kali㉿kali)-[~/CTF_PlayGround/MSB]
└─$ cat outputSB.txt
The Project Gutenberg eBook of The History of Don Quixote, by Miguel de CervantesThis eBook is for the use of anyone anywhere in the United States andmost other parts of the world at no cost and with almost no restrictionswhatsoever. You may copy it, give it away or re-use it under the termsof the Project Gutenberg License included with this eBook or online atwww.gutenberg.org. If you are not located in the United States, youwill have to check the laws of the country where you are located beforeusing this eBook.Title: The History of Don QuixoteAuthor: Miguel de Cervantes SaavedraTranslator: John OrmsbyRelease Date: July, 1997 [eBook #996][Most recently updated: February 28, 2022]Language: EnglishProduced by: David Widger*** START OF THE PROJECT GUTENBERG EBOOK DON QUIXOTE ***bookcover.jpg (230K)Full Sizespine.jpg (152K)Full SizeDon Quixoteby Miguel de Cervantes Translated by John OrmsbyEbook Editor's NoteThe book cover and spine above and the images which follow were notpart of the original Ormsby translation--they are taken from the 1880edition of J. W. Clark, illustrated by Gustave Dore. Clark in hisedition states that, "The English text of 'Don Quixote' adopted in thisedition is that of Jarvis, with occasional corrections from Motteaux."See in the introduction below John Ormsby's critique of both the Jarvisand Motteaux translations. It has been elected in the present ProjectGutenberg edition to attach the famous engravings of Gustave Dore tothe Ormsby translation instead of the Jarvis/Motteaux. The detail ofmany of the Dore engravings can be fully appreciated only by utilizingthe "Full Size" button to expand them to their original dimensions.Ormsby in his Preface has criticized the fanciful nature of Dor...
```
13. Looks like extract the msb of each RGB pixel forms a text.
14. Seach the flag using subl and ctrl+f.
15. Flag:
```
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_24d55bee}
```
    
## Stuff Learned  
1. Most images (such as BMP, PNG, or JPEG) store pixel data using RGB values (Red, Green, Blue). Each color component is usually represented by 8 bits (1 byte).
      For example, a pixel with the RGB value (101, 202, 154) is stored as:
      ```
      Red:   101  =  01100101
      Green: 202  =  11001010
      Blue:  154  =  10011010
      ```
      Each color component contributes to the overall color of a pixel.
2. LSB statistical analysis
    - Least Significant Bit (LSB) statistical analysis is commonly used in steganalysis, watermarking, and cryptography to detect hidden information or assess data integrity. It involves analyzing the              statistical properties of the LSBs in digital data, such as images, audio, or network traffic.
3. Similar to MSB hidden data is in the msb of the pixel of the image.
4. Since each pixel has three color channels (Red, Green, and Blue), we can hide data in different ways. The most common sequences are:
![ScreenShot](https://imgur.com/fdWROwZ.png)
5. Alternative LSB Encoding Patterns
    - Other encoding sequences may include:
        - RGB → RGB → RGB (use LSB of Red first, then Green, then Blue)
        - Only One Channel (hide data in just the Blue channel for minimal distortion)
        - Randomized Embedding (use a key to shuffle pixel selection for security)
6. Difference between changing in LSB and MSB
    - Least Significant Bit (LSB) Modification  
        - Definition: Changing the rightmost (least significant) bit in a byte.  
        - Effect on Image: Minimal, often imperceptible to the human eye.  
        - Use Case: Steganography (hiding messages in images).  
        - Example:  
            - Original Byte: 10101101 (173 in decimal)
            - Modified Byte: 10101100 (172 in decimal)
            - Visual Impact: Almost no noticeable change.
    -Most Significant Bit (MSB) Modification  
        - Definition: Changing the leftmost (most significant) bit in a byte.  
        - Effect on Image: Major change, significantly alters pixel brightness/color.  
        - Use Case: Watermarking, encryption, or error detection.  
        - Example:  
            - Original Byte: 10101101 (173 in decimal)  
            - Modified Byte: 00101101 (45 in decimal)  
            - Visual Impact: Huge color difference.  
