## Comment  
1. Quite a educational challenge with explanation and guidance.  


## Challenge Overview  
**Difficulty:** Hard  
**Description:** Convert the decimal -> hex -> ascii -> flag.
## Tools Used  
**CyberChef**

## Writeup  
```
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class VaultDoor7 {
    public static void main(String args[]) {
        VaultDoor7 vaultDoor = new VaultDoor7();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }
    public int[] passwordToIntArray(String hex) {    // bytes to array function
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24             // Places the first byte in the highest 8 bits.
                 | hexBytes[i*4+1] << 16             // Places the second byte in the second-highest 8 bits.
                 | hexBytes[i*4+2] << 8              // Places the third byte in the second-lowest 8 bits.
                 | hexBytes[i*4+3];                  // Keeps the last byte in the lowest 8 bits.
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097 0x415F6231 A_b1
            && x[1] == 1952395366 0x745F3066 t_0f
            && x[2] == 1600270708 0x5F623174 _b1t
            && x[3] == 1601398833 0x5F736831 _sh1
            && x[4] == 1716808014 0x6654694E fTiN
            && x[5] == 1734293296 0x675F3730 g_70
            && x[6] == 842413104  0x32363430 2640
            && x[7] == 1684157793;0x64623561 db5a
    }
}
```
1. Flag:
```
picoCTF{A_b1t_0f_b1t_sh1fTiNg_702640db5a}
```

## Stuff Learned  
Each character can be represented as a byte value using its
ASCII encoding. Each byte contains 8 bits, and an int contains
32 bits, so we can "pack" 4 bytes into a single int. Here's an
example: if the hex string is "01ab", then those can be
represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
bytes are represented as binary, they are:
0x30: 00110000
0x31: 00110001
0x61: 01100001
0x62: 01100010
If we put those 4 binary numbers end to end, we end up with 32
bits that can be interpreted as an int.
00110000001100010110000101100010 -> 808542562
Since 4 chars can be represented as 1 int, the 32 character password can
be represented as an array of 8 ints.


