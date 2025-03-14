## Comment  
1. Finally manage to get the script working. T_T  
2. Applied what I have learn from OTPImplemention challenge.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Based on the counter and brute force the flag.  
## Tools Used  
**Ghidra, GDB**  

## Writeup   
1. Main Entry function.
```
undefined4 FUN_565559af(void)

{
  char *__s;
  size_t sVar1;
  undefined4 uVar2;
  int iVar3;
  
  __s = (char *)calloc(0x200,1);
  printf("input the flag: ");
  fgets(__s,0x200,_stdin);
  sVar1 = strnlen(&DAT_56557008,0x200);
  uVar2 = FUN_5655582b(__s,sVar1);
  FUN_565557c2(uVar2,sVar1,1);
  iVar3 = FUN_565558c4(uVar2,sVar1);
  if (iVar3 == 1) {
    puts("Correct!");
  }
  else {
    puts("Incorrect.");
  }
  return 0;
}
```
2. First, looking at each of the different functions to get a rough idea.
3. FUN_5655582b:
```
char * FUN_5655582b(char *param_1,uint param_2)
{
  size_t __n;
  char *__dest;
  undefined4 uVar1;
  uint local_1c;
  
  uVar1 = 0x56555837;
  __n = (param_2 & 0xfffffffc) + 4;
  __dest = (char *)malloc((param_2 & 0xfffffffc) + 5);
  strncpy(__dest,param_1,__n);
  for (local_1c = 0xabcf00d; local_1c < 0xdeadbeef; local_1c = local_1c + 0x1fab4d) {
    FUN_565556bd(__dest,__n,local_1c,uVar1);
  }
  return __dest;
}
```
4. FUN_565557c2:
```
void FUN_565557c2(undefined4 param_1,uint param_2,int param_3)

{
  uint local_c;
  int local_8;
  
  if (param_3 < 1) {
    for (local_8 = param_2 - 1; 0 < local_8; local_8 = local_8 + -1) {
      FUN_56555751(param_1,param_2,local_8);
    }
  }
  else {
    for (local_c = 1; local_c < param_2; local_c = local_c + 1) {
      FUN_56555751(param_1,param_2,local_c);
    }
  }
  return;
}
```
5. It seems these two function does some manipulation to the user input.
6. The main function seems to be FUN_565558c4 which should return a 1 if the flag is correct.
7. FUN_565558c4:
```
undefined4 FUN_565558c4(char *param_1,uint param_2)
{
  char *__dest;
  char *__dest_00;
  uint local_18;
  
  __dest = (char *)calloc(param_2 + 1,1);
  strncpy(__dest,param_1,param_2);
  FUN_565557c2(__dest,param_2,0xffffffff);
  __dest_00 = (char *)calloc(param_2 + 1,1);
  strncpy(__dest_00,&DAT_56557008,param_2);
  FUN_565557c2(__dest_00,param_2,0xffffffff);
  puts("checking solution...");
  local_18 = 0;
  while( true ) {
    if (param_2 <= local_18) {
      return 1;
    }
    if (__dest[local_18] != __dest_00[local_18]) break;
    local_18 = local_18 + 1;
  }
  return 0xffffffff;
}
```
8. There is a checking of the pre-stored flag with the modified input and a counter that increase if they matches.
9. Firstly, to test and play around. I set break point(*0x565559a7) after the counter to whether does it increase if the char matches.
```
                             LAB_56555978                                    XREF[1]:     565559a5(j)  
        56555978 8b 55 f0        MOV        EDX,dword ptr [EBP + local_14]
        5655597b 8b 45 ec        MOV        EAX,dword ptr [EBP + local_18]
        5655597e 01 d0           ADD        EAX,EDX
        56555980 0f b6 10        MOVZX      EDX,byte ptr [EAX]
        56555983 8b 4d f4        MOV        ECX,dword ptr [EBP + local_10]
        56555986 8b 45 ec        MOV        EAX,dword ptr [EBP + local_18]
        56555989 01 c8           ADD        EAX,ECX
        5655598b 0f b6 00        MOVZX      EAX,byte ptr [EAX]
        5655598e 38 c2           CMP        DL,AL
        56555990 74 09           JZ         LAB_5655599b
        56555992 c7 45 e8        MOV        dword ptr [EBP + local_1c],0xffffffff
                 ff ff ff ff
        56555999 eb 0c           JMP        LAB_565559a7
                             LAB_5655599b                                    XREF[1]:     56555990(j)  
        5655599b 83 45 ec 01     ADD        dword ptr [EBP + local_18],0x1
                             LAB_5655599f                                    XREF[1]:     56555976(j)  
        5655599f 8b 45 ec        MOV        EAX,dword ptr [EBP + local_18]
        565559a2 3b 45 0c        CMP        EAX,dword ptr [EBP + param_2]
        565559a5 72 d1           JC         LAB_56555978
                             LAB_565559a7                                    XREF[1]:     56555999(j)  
        565559a7 8b 45 e8        MOV        EAX,dword ptr [EBP + local_1c]
        565559aa 8b 5d fc        MOV        EBX,dword ptr [EBP + local_8]
        565559ad c9              LEAVE
        565559ae c3              RET
```
10. GDB:
```
gef➤  b *0x565559a7
Breakpoint 1 at 0x565559a7
gef➤  r
Starting program: /home/kali/Downloads/brute 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
input the flag: 0
gef➤  x/d $ebp-0x14
0xffffcf94:     0
input the flag: p
gef➤  x/d $ebp-0x14
0xffffcf94:     1
input the flag: picoCTF
gef➤  x/d $ebp-0x14
0xffffcf94:     7
```
11. When p causes the counter to increase, I would assume the flag starts with picoCTF.
12. Hence based on this, I created a script to brute force, try all combination and based on the counter to know whether the flag is correct or wrong.
13. Here is the script:
```
import string
import gdb


TheList = string.ascii_lowercase + string.ascii_uppercase + string.digits + '{_}'
guess=''

gdb.execute('file ./brute')
gdb.execute('b *0x565559a7')

for j in range(30):
        for i in TheList:
                with open("input.txt", "w") as f:
                        f.write(guess+i+'1'*(29-j))
                gdb.execute("run < input.txt")
                count = gdb.execute("x/d $ebp-0x14",to_string=True)
                count = count[12:14]
                print(count)    
                if int(count) > len(guess):
                        guess+=i
                        print("Flag is:",guess)
                        break
```
11. Flag:
```
Flag is: picoCTF{I_5D3_A11DA7_61b3a698}
```

## Stuff Learned  
1. The script cant having multiple gdb run cmd.  
2. Indentation:
```
with open("input.txt", "w") as f:
      f.write(guess+i+'1'*(29-j))
gdb.execute("run < input.txt")
```
3. To run the script:
```
gdb -q -x Script.py
```

