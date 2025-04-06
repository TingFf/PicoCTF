## Comment  
1. Somehow my file is different from writeup so solution is a bit different.
2. Link: https://ctftime.org/writeup/26976


## Challenge Overview  
**Difficulty:** Medium  
**Description:**  NA
## Tools Used  
**zsteg, ffmpeg**

## Writeup  
1. First click on the milk icon, it direct us to a web page.
![ScreenShot](https://imgur.com/DVi3QrR.png)
2. Inspect the web.
```
<!doctype html>

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=400" />
  <title>🥛</title>
  <link rel="stylesheet" href="style.css" />

</head>
<body>
  <div id="image" class="center"></div>
  <div id="foot" class="center">
    <h1>MilkSlap!</h1>
    Inspired by <a href="http://eelslap.com">http://eelslap.com</a> <br>
    Credit to: <a href="https://github.com/boxmein">boxmein</a> for code inspiration.
  </div>
  <script src="script.js">


</script>
</body>
</html>
```
3. Nothing of interest.
4. Looking at the css.
```
/* source: milkslap-milkslap.scss */
body {
  margin: 0;
  padding: 0;
  overflow: hidden; }

a {
  color: inherit; }

.center {
  width: 1080px;
  height: 720px;
  margin: 0 auto; }

#image {
  height: 720px;
  margin-top: 5%;
  margin-bottom: 20px;
  background-image: url(concat_v.png);
  background-position: 0 0; }

#foot {
  margin-bottom: 5px;
  color: #999999; }
  #foot h1 {
    font-family: serif;
    font-weight: normal;
    font-size: 1rem;
    text-align: center; }
```
5. There is a image for us.  
6. Download the image.
```
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/milkslap]
└─$ ls 
concat_v.png
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/CTF_PlayGround/milkslap]
└─$ file concat_v.png                         
concat_v.png: PNG image data, 1280 x 47520, 8-bit/color RGB, non-interlaced
```
7. For this challenge, we can use zsteg to get the metadata of the lsb and rgb.
8. However, for some reason there is some error message unlike others when I tried to solve the error.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/milkslap]
└─$ zsteg -s first concat_v.png
/home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:303:in `upto': stack level too deep (SystemStackError)
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:303:in `decoded_bytes'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line/mixins.rb:17:in `prev_scanline_byte'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:377:in `prev_scanline_byte'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:319:in `block in decoded_bytes'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:318:in `upto'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:318:in `decoded_bytes'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line/mixins.rb:17:in `prev_scanline_byte'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zpng-0.4.5/lib/zpng/scan_line.rb:377:in `prev_scanline_byte'
         ... 9483 levels...
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg.rb:26:in `run'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/bin/zsteg:8:in `<top (required)>'
        from /usr/local/bin/zsteg:25:in `load'
        from /usr/local/bin/zsteg:25:in `<main>'
```
9. Apparently, the ```zsteg``` crash (SystemStackError) happened because the PNG file is likely corrupted or crafted to confuse the tool with deep recursion.
10. I used ```ffmeg``` to clean the image and then use zsteg.
```
┌──(kali㉿kali)-[~/CTF_PlayGround/milkslap]
└─$ ffmpeg -i concat_v.png -f image2 clean.png

┌──(kali㉿kali)-[~/CTF_PlayGround/milkslap]
└─$ ls
clean.png  concat_v.png

┌──(kali㉿kali)-[~/CTF_PlayGround/milkslap]
└─$ zsteg clean.png 
imagedata           .. text: "ztupjojdvql"
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
b1,bgr,lsb,xy       .. /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s': stack level too deep (SystemStackError)
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/iostruct-0.5.0/lib/iostruct.rb:180:in `inspect'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
         ... 10066 levels...
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/lib/zsteg.rb:26:in `run'
        from /home/kali/.local/share/gem/ruby/3.1.0/gems/zsteg-0.2.13/bin/zsteg:8:in `<top (required)>'
        from /usr/local/bin/zsteg:25:in `load'
        from /usr/local/bin/zsteg:25:in `<main>'

```
11. It still not able to display all the metadata but just until the flag.
12. Flag:
```
picoCTF{imag3_m4n1pul4t10n_sl4p5}
```
## Stuff Learned  
1. ```ffmeg:``` Atakes the possibly broken or weird concat_v.png and re-encodes it into a fresh, clean clean.png using FFmpeg.This can help fix corrupted PNGs or strip hidden data.
(✅ Good for cleaning up images before running tools like zsteg.)


