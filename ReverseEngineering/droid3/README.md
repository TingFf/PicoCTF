## Comment  
1. Still not familier enough to read assembly code.  
2. For this challenge, no write up but noted and commented beside the assembly code instead.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Understand assembly code.  
## Tools Used  
NIL  

## Writeup  
NA  
## Stuff Learned  
1. To decompile and rebuild the modified apk:
```
apktool d apkname.apk --no-res
apktool b three -o recompiled/recompiled_apkname.apk
```
2. Modified apk must be signed
cmd line to sign:
``` 
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000  
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore my_application.apk alias_name  
```
3. Modifed apk cannot be drag and drop while previous app is still in the emulator, will give error hence must uninstall the original one first.  
