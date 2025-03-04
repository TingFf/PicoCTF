## Comment  
1. Similar to the previous challenge.  
2. Not sure whats the link between two of the directory below.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Finding the correct password input to print the flag.   
## Tools Used  
**Android Studio, Jadx**  

## Writeup  
1. Similar to previous challenge, there is a button and message being displayed.  
![ScreenShot](https://imgur.com/fwcD45P.png)  
Main Activity:
```
package com.hellocmu.picoctf;

import android.content.Context;

/* loaded from: classes.dex */
public class FlagstaffHill {
    public static native String fenugreek(String str);

    public static String getFlag(String input, Context ctx) {
        String password = ctx.getString(R.string.password);
        // It retrieves a password stored in the app’s resources (R.string.password).

        return input.equals(password) ? fenugreek(input) : "NOPE";
        // checks if the input matches the password. If they match, it calls fenugreek(input), likely to generate a flag.
        // Otherwise, it returns "NOPE", denying access.
    }
}
```
2. Look like I need to find the password within the resources to match and display the flag.  
2. Since the password is store in resource->string->password, I look into that directory.  
R -> String -> Password:
```
public static final int password = 0x7f0b002f;
```
3. This int in stored in the password variable.  
4. But this doesn't seems like the answer so I look into other directory.  
Resources -> resources.arsc -> strings.xml:
```
    <string name="abc_shareactionprovider_share_with_application">Share with %s</string>
    <string name="abc_toolbar_collapse_description">Collapse</string>
    <string name="app_name">PicoCTF</string>
    <string name="bat">mink</string>
    <string name="bear">margay</string>
    <string name="cottentail">shrew</string>
    <string name="gopher">armadillo</string>
    <string name="hint">brute force not required</string>
    <string name="manatee">caribou</string>
    <string name="myotis">jackrabbit</string>
    <string name="password">opossum</string>
    <string name="porcupine">blackbuck</string>
    <string name="porpoise">mouflon</string>
    <string name="search_menu_title">Search</string>
    <string name="skunk">elk</string>
    <string name="status_bar_notification_info_overflow">999+</string>
    <string name="vole">beaver</string>
```
5. Since the password should be a string hence this directory seems the most sense.  
6. Enter the string into the app.  
![ScreenShot](https://imgur.com/KSK29oz.png)  
Flag:
```
picoCTF{pining.for.the.fjords}
```
## Stuff Learned  
1. R.string.password = r -> string -> password.  
2. To find respective resource or variable(string) = Resources -> resources.arsc -> strings.xml.  


