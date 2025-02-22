## Comment  
1. First experience in touch with gdb and python scripting.
2. Reference from two write up videos.  
[https://www.youtube.com/watch?v=h8CDUKCVZ3U]  
[https://www.youtube.com/watch?v=ceTyGWkB3Lo]    

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Brute forcing the secret string checking.  
## Tools Used  
NIL  

## Writeup  
Main Function:  
```
undefined8 main(int param_1,undefined8 *param_2)
{
  byte bVar1;
  char cVar2;
  int buffer;
  undefined8 uVar3;
  long in_FS_OFFSET;
  int i;
  int local_ec;
  char input [100];
  undefined k;
  char local_78 [104];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 < 2) {
    printf("USAGE: %s [KEY]\n",*param_2);
    uVar3 = 1;
  }
  else {
    strncpy(input,(char *)param_2[1],100);
    k = 0;
    i = 0;
    while( true ) {
      buffer = valid_char((int)input[i]);
      if (buffer == 0) break;
      if (i == 0) {
        cVar2 = jumble((int)input[0]);
        local_78[0] = cVar2 % '\x10';
      }
      else {
        cVar2 = jumble((int)input[i]);
        bVar1 = (byte)((int)cVar2 + (int)local_78[i + -1] >> 0x1f);
        local_78[i] = ((char)((int)cVar2 + (int)local_78[i + -1]) + (bVar1 >> 4) & 0xf) -
                      (bVar1 >> 4);
      }
      i = i + 1;
    }
    for (local_ec = 0; local_ec < i; local_ec = local_ec + 1) {
      local_78[local_ec] = local_78[local_ec] + 'a';
    }
    if (i == 100) {
      buffer = strncmp(local_78,
                       "occdpnkibjefihcgjanhofnhkdfnabmofnopaghhgnjhbkalgpnpdjonblalfciifiimkaoenpea libelmkdpbdlcldicplephbo"
                       ,100);
      if (buffer == 0) {
        puts("You got the key, congrats! Now xor it with the flag!");
        uVar3 = 0;
        goto LAB_5555554009ea;
      }
    }
    puts("Invalid key!");
    uVar3 = 1;
  }
LAB_5555554009ea:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar3;
```
1. The program ask for user input of length 100.  
2. Pass through some algorithm.  
3. Output is check with a pre-fixed string.  
4. Input can only consist hex-decimal char.
5. Wrote a script to brute force.
```
  GNU nano 8.3                                                Script.py                                                         
import gdb
import operator

gdb.execute('file ./otp')
gdb.execute('b strncmp@plt')
hexa = list('0123456789abcdef')
guess=''
for j in range(100):
        for i in hexa:
                gdb.execute('run '+guess+i+'1'*(99-j))
                sofar = gdb.execute('x/s $rdi',to_string=True)
                compare = gdb.execute('x/s $rsi',to_string=True)
                sofar=sofar[17:117]
                compare=compare[17:117]
                print("A:"+sofar)
                print("B:"+compare)
                if sofar[j]==compare[j]:
                        guess += i
                        print("C:"+guess)
                        break
```
output: 
```
720867e7c4d89fd29be5bb459c1498d1b4888380fb675c3ddc7123af25ad5e30e9027373c1a6dec9b87c6114bc4a5e6cd45e
```

6. After getting the string.  
7. XOR with the given flag in the flag text file.  
8. Convert the hex_decimal string in cyberchef to get the flag:
```
picoCTF{cust0m_jumbl3s_4r3nt_4_g0Od_1d3A_15e89ca4}
```

## Stuff Learned  
1. Using gdb in a python script to brute force the challenge.  


