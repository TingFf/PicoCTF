## Comment  
1. Proud my myself for this one as it the highest point out of all the RE challenge.  
2. Did it myself with my experience after doing many challenge.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Write a script to brute force the flag.  
## Tools Used  
**GDB, Ghidra**

## Writeup  
1. Open in ghidra to decompile the code:
```

bool main(void)

{
  bool bVar1;
  undefined8 local_118;
  undefined8 local_110;
  undefined8 local_108;
  undefined8 local_100;
  undefined8 local_f8;
  undefined8 local_f0;
  undefined8 local_e8;
  undefined8 local_e0;
  undefined8 local_d8;
  undefined8 local_d0;
  undefined8 local_c8;
  undefined8 local_c0;
  undefined8 local_b8;
  undefined8 local_b0;
  undefined8 local_a8;
  undefined8 local_a0;
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined8 local_60;
  undefined8 local_58;
  undefined8 local_50;
  undefined8 local_48;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  int local_c;
  
  local_118 = 0;
  local_110 = 0;
  local_108 = 0;
  local_100 = 0;
  local_f8 = 0;
  local_f0 = 0;
  local_e8 = 0;
  local_e0 = 0;
  local_d8 = 0;
  local_d0 = 0;
  local_c8 = 0;
  local_c0 = 0;
  local_b8 = 0;
  local_b0 = 0;
  local_a8 = 0;
  local_a0 = 0;
  local_98 = 0;
  local_90 = 0;
  local_88 = 0;
  local_80 = 0;
  local_78 = 0;
  local_70 = 0;
  local_68 = 0;
  local_60 = 0;
  local_58 = 0;
  local_50 = 0;
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  printf("Enter the password: ");
  fgets((char *)&local_118,0x100,stdin);
  local_c = check(&local_118);
  bVar1 = local_c != 1;
  if (bVar1) {
    puts("Correct!! :D");
  }
  else {
    puts("Wrong :(");
  }
  return !bVar1;
}
```
2. Seems like the check function is checking whether user input is correct or wrong.
3. The function must be 0 for the flag to be correct.  
Check function:
```

undefined8 check(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  size_t sVar3;
  undefined8 local_58;
  undefined7 local_50;
  undefined uStack_49;
  undefined7 uStack_48;
  uint local_34;
  uint local_30;
  undefined4 local_2c;
  int j;
  uint i;
  int local_20;
  int local_1c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 27) {
    local_58 = 0x617b2375f81ea7e1;
    local_50 = 0x69df5b5afc9db9;
    uStack_49 = 0xd2;
    uStack_48 = 0xf467edf4ed1bfe;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;
    for (i = 0; i < 23; i = i + 1) {
      for (j = 0; j < 8; j = j + 1) {
        if (local_20 == 0) {
          local_20 = 1;
        }
        local_30 = 1 << (7U - (char)j & 0x1f);     
        local_34 = 1 << (7U - (char)local_20 & 0x1f);
        if (0 < (int)((int)param_1[local_1c] & local_34) !=
            0 < (int)((int)*(char *)((long)&local_58 + (long)(int)i) & local_30)) {
          return 1;
        }
        local_20 = local_20 + 1;
        if (local_20 == 8) {
          local_20 = 0;
          local_1c = local_1c + 1;
        }
        sVar3 = (size_t)local_1c;
        sVar1 = strlen(param_1);
        if (sVar3 == sVar1) {
          return 0;
        }
      }
    }
    uVar2 = 0;
  }
  else {
    uVar2 = 1;
  }
  return uVar2;
}
```
4. (int)((int)*(char *)((long)&local_58 should be the flag.  
5. Checking against our input bit by bit.  
6. If the char matches, then xVar3(counter) will increase by one.  
My Understanding:
```
local_30 = 1 << (7U - (char)j & 0x1f);
local_34 = 1 << (7U - (char)local_20 & 0x1f);
```
7. This two are essential the same.
8. If J = 0
9. 0 & 0x1f = 0 (Only lowest 5 bits of j are used.)
10. 7 - 0 = 7
11. 1 << 7 = 0b10000000  
12. This will the first bit it checks  
13. It will then check for 7 bits and if all matches, the char matches and sVAR3 increase by one.  
14. When sVAR3 == 27, the flag is correct.  
Script:  
```
import string
import gdb
import time



TheList = string.ascii_lowercase + string.ascii_uppercase + string.digits + '{_}'
guess=''

gdb.execute('file ./perplexed')
gdb.execute('b *0x0040126b')
gdb.execute('b *0x004011b7')

temp = 1
for j in range(27):
    for i in TheList:
        count = 0
        with open("input.txt", "w") as f:
            f.write(guess+i+'1'*(26-j))

        gdb.execute("run < input.txt")
        for k in range(7*temp):
            try:
                gdb.execute("c")
                counter = gdb.execute("x/d $rbp-0x14", to_string=True)
                count+=1
            except gdb.error:
                gdb.execute("r")
                print("Wrong char:",i)
                break
        counter = counter[15:18]
        if int(counter) > len(guess):
            guess+=i
            temp+=1
            print("Correct char:", i)
            print(f"Flag so far: {guess}")
            time.sleep(1)
            if len(guess) == 27:
                time.sleep(10)
            break
```
15. The script I wrote will matches each char.  
16. To know the char matches, the code must be able to continue running for 7 times before the counter increase by 1.  
17. If it breaks in between then the char is wrong and just move on to the next char.  
18. To increase sVar3 by 2, it must be able to continue 14 times consecutively.  
19. Hence the gdb.execute("c") must increase as more char matches to be able to check whether the next char is correct or wrong.  
Flag:
```
Flag so far: picoCTF{0n3_bi7_4t_a_7im3}
```
## Stuff Learned  
1. It only check 7 bit maybe because the first bit in all the char are 0 hence is skip.  
2. Since picoCTF{} is the format, can always use it to test my theory.  


