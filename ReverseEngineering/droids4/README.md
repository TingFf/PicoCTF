## Comment  
1. This challenge requires me to used previously learned skill and apply plus bit more to get the flag.  
2. Educational series of challenge.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Get the secret password and modify the code to print the flag.  
## Tools Used  
**Android Studio, jadx, apktool, keytool ,jarsigner**  

## Writeup  
FlagstaffHill:  
```
package com.hellocmu.picoctf;

import android.content.Context;

/* loaded from: classes.dex */
public class FlagstaffHill {
    public static native String cardamom(String str);

    public static String getFlag(String input, Context ctx) {
        StringBuilder ace = new StringBuilder("aaa");
        StringBuilder jack = new StringBuilder("aaa");
        StringBuilder queen = new StringBuilder("aaa");
        StringBuilder king = new StringBuilder("aaa");
        ace.setCharAt(0, (char) (ace.charAt(0) + 4));
        ace.setCharAt(1, (char) (ace.charAt(1) + 19));
        ace.setCharAt(2, (char) (ace.charAt(2) + 18));
        jack.setCharAt(0, (char) (jack.charAt(0) + 7));
        jack.setCharAt(1, (char) (jack.charAt(1) + 0));
        jack.setCharAt(2, (char) (jack.charAt(2) + 1));
        queen.setCharAt(0, (char) (queen.charAt(0) + 0));
        queen.setCharAt(1, (char) (queen.charAt(1) + 11));
        queen.setCharAt(2, (char) (queen.charAt(2) + 15));
        king.setCharAt(0, (char) (king.charAt(0) + 14));
        king.setCharAt(1, (char) (king.charAt(1) + 20));
        king.setCharAt(2, (char) (king.charAt(2) + 15));
        String password = "".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString());
        return input.equals(password) ? "call it" : "NOPE";
    }
}
```
1. Looking at the code above, there is two parts to solve.  
   -Get the secret password.  
   -Making the code to call cardamon if the input matches the password.  
2. To get the password, it seem just shifting the char in ascii value and joining them together.  
3. Changing the calling function is the same as the previous challenge while referencing to droid1 challenge by opening the decompiling apk.  
4. Script:  
```
ace = ['a','a','a']
jack = ['a','a','a']
queen = ['a','a','a']
king = ['a','a','a']

string1= ""


ace[0] = ord(ace[0]) + 4
ace[1] = ord(ace[1]) + 19
ace[2] = ord(ace[2]) + 18

jack[0] = ord(jack[0]) + 7
jack[1] = ord(jack[1]) + 0
jack[2] = ord(jack[2]) + 1

queen[0] = ord(queen[0]) + 0
queen[1] = ord(queen[1]) + 11
queen[2] = ord(queen[2]) + 15

king[0] = ord(king[0]) + 14
king[1] = ord(king[1]) + 20
king[2] = ord(king[2]) + 15

string1="".join(chr(i) for i in queen)
string1+="".join(chr(i) for i in jack)
string1+="".join(chr(i) for i in ace)
string1+="".join(chr(i) for i in king)

print(string1)
```
5. Password:  
```
alphabetsoup
```
6. Next step is to decompile the apk and modify it.  
7. Similar to the previous challenge.  
8. Decompile droid1 challenge apk:  
```
    if-eqz v1, :cond_0

    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->fenugreek(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    return-object v1
```
9. Referencing above:  
```
    if-eqz v5, :cond_0

    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->cardamom(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    return-object v5
```
10. After that build the apk, sign and install in the emulator.  
Flag:  
![ScreenShot](https://imgur.com/sE8PWLw.png)
11. Entering alphabetsoup without modifying should just print "call it".\
Flag:
```
picoCTF{not.particularly.silly}
```

## Stuff Learned  
NA


