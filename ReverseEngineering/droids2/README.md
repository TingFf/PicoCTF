## Comment  
1. Simple Challenge.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Just replicate the code in python and print the password or just eyeball it.  
## Tools Used  
**Android Studio, Jadx**

## Writeup  
1. After completing the previous two challenge, straight went to the main function thats related to getting the password.  
FlagstaffHill:
```
package com.hellocmu.picoctf;

import android.content.Context;

/* loaded from: classes.dex */
public class FlagstaffHill {
    public static native String sesame(String str);

    public static String getFlag(String input, Context ctx) {
        String[] witches = {"weatherwax", "ogg", "garlick", "nitt", "aching", "dismass"};
        int second = 3 - 3;
        int third = (3 / 3) + second;
        int fourth = (third + third) - second;
        int fifth = 3 + fourth;
        int sixth = (fifth + second) - third;
        String password = "".concat(witches[fifth]).concat(".").concat(witches[third]).concat(".").concat(witches[second]).concat(".").concat(witches[sixth]).concat(".").concat(witches[3]).concat(".").concat(witches[fourth]);
        return input.equals(password) ? sesame(input) : "NOPE";
    }
}
```
2. After analyse the code, the password seems to be the concatenation of each word in the list and join them with a dot.
3. Instead of manually eyeballing, I replicate the code in python.
Python code:
```
witches = ["weatherwax", "ogg", "garlick", "nitt", "aching", "dismass"]
second = 3 - 3
third = (3 // 3) + second
fourth = (third + third) - second
fifth = 3 + fourth
sixth = (fifth + second) - third
print(witches[fifth] + "."+ witches[third]+"."+ witches[second]+"."+ witches[sixth]+"."+ witches[3]+"."+ witches[fourth])
```
Password:
```
dismass.ogg.weatherwax.aching.nitt.garlick
```
Flag:  
![ScreenShot](https://imgur.com/NF0kISC.png)  

## Stuff Learned  
NA


