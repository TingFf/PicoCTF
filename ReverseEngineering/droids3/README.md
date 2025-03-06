## Comment  
1. Challenge itself is simple but the process of modifying the apk took the longest time.  


## Challenge Overview  
**Difficulty:** Hard  
**Description:** Decompiled the apk, modify it and build to get the flag.  
## Tools Used  
**Android Studio, jadx, apktool, keytool ,jarsigner**   

## Writeup  
FlagstaffHill:
```
package com.hellocmu.picoctf;

import android.content.Context;

/* loaded from: classes.dex */
public class FlagstaffHill {
    public static native String cilantro(String str);

    public static String nope(String input) {
        return "don't wanna";
    }

    public static String yep(String input) {
        return cilantro(input);
    }

    public static String getFlag(String input, Context ctx) {
        String flag = nope(input);
        return flag;
    }
}
```
1. Looking the at code, is pretty obvious that we have to change the function call in ```getFlag``` from ```nope``` to ```yep``` but how to change I had to look it up.
2. Firstly, decompile the apk file.
```
apktool d three.apk --no-res
```
3. Then modify.
```
.class public Lcom/hellocmu/picoctf/FlagstaffHill;
.super Ljava/lang/Object;
.source "FlagstaffHill.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static native cilantro(Ljava/lang/String;)Ljava/lang/String;
.end method

.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 19
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->nope(Ljava/lang/String;)Ljava/lang/String;
                                                                |
                                                          change to yep
    move-result-object v0

    .line 20
    .local v0, "flag":Ljava/lang/String;
    return-object v0
.end method

.method public static nope(Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;

    .line 11
    const-string v0, "don\'t wanna"

    return-object v0
.end method

.method public static yep(Ljava/lang/String;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;

    .line 15
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cilantro(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    return-object v0
.end method
```
4. After modifying, build it back to a apk.
```
apktool b three -o recompiled/recompiled_apkname.apk
```
5. Modifying a apk remove the sign certificate hence need to sign it again.
6. To sign, use the following cmd below.  
```
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000  
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore my_application.apk alias_name  
```
7. Then remember to uninstall the previous app before dragging in the modified as it will give error.
8. Just enter anything in the text box and the flag will be displayed.
![ScreenShot](https://imgur.com/RQTrCKq.png)  
Flag:
```
picoCTF{tis.but.a.scratch}
```
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
