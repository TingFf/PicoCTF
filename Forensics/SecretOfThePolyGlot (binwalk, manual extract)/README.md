## Comment  
1. Quite fun, did it on my own.
2. Binwalk is a good tool.  

## Challenge Overview  
**Difficulty:** Easy  
**Description:** Use binwalk to get the other part of the flag.   
## Tools Used  
**Binwalk, eog**

## Writeup  
1. The challenge starts by opening a pdf file.
2. The pdf shows half of the flag.
```
1n_pn9_&_pdf_2a6a1ea8}
```
3. For some reason I thought of using binwalk to extract the file due to previous challenges.
4. Should use it more often.  
5. Extract using cmd line:
```
binwalk flag2of2-final.pdf

```
6. Extracted files:  
![ScreenShot](https://imgur.com/JjzVJ3L.png)
7. There is the a png.  
8. But there wasnt any images in the pdf.
9. Type cmd line:
```
binwalk -e flag2of2-final.pdf
```
10. Extracting using binwalk doesn't extract the png.
11. Hence manually extract.  
```
dd if=flag2of2-final.pdf bs=1 skip=0 of=extracted.png
```
12. After that open the png using eog.
```
eog extracted.png
```
![ScreenShot](https://imgur.com/5ra1VOg.png)  
13.Flag:
```
picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}
```

## Stuff Learned  
1. eog is used to open images.  
2. Try to use binwalk more.  
3. Why use dd:  
   - If a file contains multiple embedded formats (like a PDF with a hidden PNG), dd allows us to extract specific sections.  
   - Since binwalk identified a PNG at offset 0x0, running dd should ideally extract a valid PNG file.
   - skip = 0 because offset at 0x0 based on binwalk.  
