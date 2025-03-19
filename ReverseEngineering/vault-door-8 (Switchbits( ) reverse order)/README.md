## Comment  
1. Last few challenges in picoCTF for RE.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Understand switchBits and reverse the order of the bit switching.  
## Tools Used  
**Jadx**  

## Writeup  
1. First I start by running the java file.  
```
└─$ java VaultDoor8 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: 
```
2. Open the java file using jadx.  
```
package defpackage;

import java.util.Arrays;
import java.util.Scanner;

/* loaded from: VaultDoor8.class */
class VaultDoor8 {
    VaultDoor8() {
    }

    public static void main(String[] strArr) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String next = scanner.next();
        if (new VaultDoor8().checkPassword(next.substring(8, next.length() - 1))) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    public char[] scramble(String str) {
        char[] charArray = str.toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            charArray[i] = switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(charArray[i], 1, 2), 0, 3), 5, 6), 4, 7), 0, 1), 3, 4), 2, 5), 6, 7);
        }
        return charArray;
    }

    public char switchBits(char c, int i, int i2) {
        char c2 = (char) (1 << i);
        char c3 = (char) (1 << i2);
        char c4 = (char) (c & c2);
        char c5 = (char) (c & c3);
        char c6 = (char) (c & ((c2 | c3) ^ (-1)));
        char c7 = (char) (i2 - i);
        return (char) ((c4 << c7) | (c5 >> c7) | c6);
    }

    public boolean checkPassword(String str) {
        return Arrays.equals(scramble(str), new char[]{244, 192, 151, 240, 'w', 151, 192, 228, 240, 'w', 164, 208, 197, 'w', 244, 134, 208, 165, 'E', 150, '\'', 181, 'w', 194, 210, 149, 164, 240, 210, 210, 193, 149});
    }
}
```
3. So it seems like every char from user input is being scrambled and checking against the fixed char array.  
4. Lets look at the switchBits function:  
```
public char switchBits(char c, int i, int i2) {
        char c2 = (char) (1 << i);
        char c3 = (char) (1 << i2);
        char c4 = (char) (c & c2);
        char c5 = (char) (c & c3);
        char c6 = (char) (c & ((c2 | c3) ^ (-1)));
        char c7 = (char) (i2 - i);
        return (char) ((c4 << c7) | (c5 >> c7) | c6);
    }
```
5. Lets do an example:  
```
switchBits(p,3,4)

public char switchBits(char c, int i, int i2) {
        char c2 = (char) (1 << i);     i = 3 -> shift 00000001 by 3 to the left == 00001000
        char c3 = (char) (1 << i2);    i2 = 4 -> shift 00000001 by 4 to the left == 00010000
        char c4 = (char) (c & c2);     p = 01110000 & 00001000 == 0000'0'000 (4th bit)
        char c5 = (char) (c & c3);     p = 01110000 & 00010000 == 000'1'0000 (5th bit)
        char c6 = (char) (c & ((c2 | c3) ^ (-1))); 1st: c2 | c3 = 00001000 | 00010000 == 00011000 -> 2nd: ^ (-1) -> 3rd: 11100111 & 01110000 -> Result: 01100000
        char c7 = (char) (i2 - i);  4 - 3 == 1
        return (char) ((c4 << c7) | (c5 >> c7) | c6);  0000'0'000 << 1 | 000'1'0000 >> 1 | 01100000 -> 000'0'0000 | 0000'1'000 | 01100000 == 01101000
    }
```
6. Comparing ```01110000``` with ```01101000```, we can see that i and i2 bits are swap hence switchbit it a function that switches the bit base on the argument.  
7. Now reversing the logic.  
```
switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(charArray[i], 1, 2), 0, 3), 5, 6), 4, 7), 0, 1), 3, 4), 2, 5), 6, 7);
```
8. For example if charArray[i] == p, and we get 255 and the sequence is:  
```
1. Swapping bit 1 and 2
2. Swapping bit 0 and 3
3. Swapping bit 5 and 6
4. Swapping bit 4 and 7
5. Swapping bit 0 and 1
6. Swapping bit 3 and 4
7. Swapping bit 2 and 5
8. Swapping bit 6 and 7
```
9. Then we must reverse the squence and swap back the bits.  
```
1. Swapping bit 6 and 7
2. Swapping bit 2 and 5
3. Swapping bit 3 and 4
4. Swapping bit 0 and 1
5. Swapping bit 4 and 7
6. Swapping bit 5 and 6
7. Swapping bit 0 and 3
8. Swapping bit 1 and 2
```
10. Here is the script:  
```
package defpackage;

import java.util.Arrays;
import java.util.Scanner;

/* loaded from: VaultDoor8.class */
class VaultDoor8 {
    VaultDoor8() {
    }
    public static void main(String[] strArr) {
        char[] scrambledPassword = {244, 192, 151, 240, 'w', 151, 192, 228, 240, 'w', 164, 208, 197, 'w', 244, 134, 208, 165, 'E', 150, '\'', 181, 'w', 194, 210, 149, 164, 240, 210, 210, 193, 149};
        String scrambledString = new String(scrambledPassword);
        char[] originalPassword = unscramble(scrambledString);
        System.out.println("Recovered Password: " + new String(originalPassword));
    }
    public static char[] unscramble(String str) {
    char[] charArray = str.toCharArray();
    for (int i = 0; i < charArray.length; i++) {
        // Apply swaps in reverse order
        charArray[i] = switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(switchBits(
            charArray[i], 6, 7), 2, 5), 3, 4), 0, 1), 4, 7), 5, 6), 0, 3), 1, 2);
    }
    return charArray;
}
    public static char switchBits(char c, int i, int i2) {
        char c2 = (char) (1 << i); 
        char c3 = (char) (1 << i2);
        char c4 = (char) (c & c2);
        char c5 = (char) (c & c3);
        char c6 = (char) (c & ((c2 | c3) ^ (-1)));
        char c7 = (char) (i2 - i);
        return (char) ((c4 << c7) | (c5 >> c7) | c6);
    }

}
```
11. Flag:  
```
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_89eb3994e}
```

## Stuff Learn
1. Must understand what does the switchbit function do. Does it require reversing or we can get back the input based on output.  
2. Since the switch bit is fixed and there are overlapping bits, we must do in reverse otherwise should be doesnt matter if the bit does not overlap.  


 
