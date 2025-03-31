## Comment  
1. New tool to use.

## Challenge Overview  
**Difficulty:** Medium  
**Description:**  
Now you DON’T see me. This report has some critical data in it, some of which have been redacted correctly, while some were not.  
Can you find an important key that was not redacted properly?
## Tools Used  
**PDFtoText**

## Writeup  
![ScreenShot](https://imgur.com/PHRpHMu.png)  
1. A redacted PDF was given after downloading.  
2. A indicator: "Just painted over in ...".  
3. The words is just painted over.  
4. Using a ```pdftotext```tool to get just the text.  
```
┌──(kali㉿kali)-[~/HTBTryout/RedactionGoneWrong]
└─$ pdftotext Financial_Report_for_ABC_Labs.pdf output.txt 


                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/HTBTryout/RedactionGoneWrong]
└─$ ls
Financial_Report_for_ABC_Labs.pdf  output.txt
                                                                                                                                                                                                                                           
┌──(kali㉿kali)-[~/HTBTryout/RedactionGoneWrong]
└─$ cat output.txt       
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.

Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```

## Stuff Learned  
1. "Redacted" means that information has been intentionally removed, censored, or obscured. This is often done for security, privacy, or confidentiality reasons.  
   For example, in classified documents, sensitive information may be [REDACTED] to prevent unauthorized access.  
   In CTF challenges, "redacted" might indicate missing or hidden data that you need to uncover.  
2. PDFtoText: extracts all text. This works because it was only visually hidden (not properly reacted).  

