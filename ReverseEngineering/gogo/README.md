## Comment  
1. Had to look at write up to get hints.  
2. Most of the challenge will have to compare the password with some pre-stored password.  


## Challenge Overview  
**Difficulty:** Hard  
**Description:** Find out about what the password checking with.  
## Tools Used  
**Ghidra, Gdb**  

## Writeup  
In the main function, there is a checkpassword funtion:

```
void main.main(void)

{
  int iVar1;
  int *in_GS_OFFSET;
  undefined4 *in_stack_ffffffac;
  undefined4 *puVar2;
  char cVar3;
  undefined *local_30;
  undefined **local_2c;
  undefined *local_28;
  undefined **local_24;
  undefined *local_20;
  undefined **local_1c;
  undefined *local_18 [2];
  undefined *local_10;
  undefined **local_c;
  undefined *local_8;
  undefined4 *local_4;
  undefined **ppuVar4;
  
  while (&stack0x00000000 <= *(undefined **)(*(int *)(*in_GS_OFFSET + -4) + 8)) {
    local_4 = (undefined4 *)0x80d4a7b;
    runtime.morestack_noctxt();
  }
  runtime.newobject(&DAT_080e8860);
  fmt.Printf(&DAT_080fea50,0x10,0,0,0);
  local_18[0] = &DAT_080e1300;
  ppuVar4 = local_18;
  fmt.Scanf(&DAT_080fd1b6,3,ppuVar4,1,1);
  cVar3 = (char)ppuVar4;
  main.checkPassword(*in_stack_ffffffac,in_stack_ffffffac[1]);
  if (cVar3 == '\0') {
    local_10 = &DAT_080e8860;
    local_c = &main.statictmp_3;
    fmt.Println(&local_10,1,1);
  }
  else {
    local_20 = &DAT_080e8860;
    local_1c = &main.statictmp_0;
    fmt.Println(&local_20,1,1);
    local_28 = &DAT_080e8860;
    local_24 = &main.statictmp_1;
    fmt.Println(&local_28,1,1);
    local_30 = &DAT_080e8860;
    local_2c = &main.statictmp_2;
    puVar2 = (undefined4 *)0x1;
    fmt.Println(&local_30,1,1);
    runtime.newobject(&DAT_080e8860);
    local_8 = &DAT_080e1300;
    local_4 = puVar2;
    fmt.Scanf(&DAT_080fd1b6,3,&local_8,1,1);
    main.ambush(*puVar2,puVar2[1]);
    iVar1 = runtime.deferproc(0,&PTR_main.get_flag_081046a0);
    if (iVar1 != 0) {
      runtime.deferreturn();
      return;
    }
  }
  runtime.deferreturn();
  return;
}
```
In the function, it check against a variable after being xored with the input:
```
void main.checkPassword(int param_1,uint param_2)

{
  uint uVar1;
  int iVar2;
  int *in_GS_OFFSET;
  char local_40 [32];
  byte local_20 [28];
  undefined4 uStack_4;
  
  while (&stack0x00000000 <= *(undefined **)(*(int *)(*in_GS_OFFSET + -4) + 8)) {
    uStack_4 = 0x80d4b72;
    runtime.morestack_noctxt();
  }
  if ((int)param_2 < 0x20) {
    os.Exit(0);
  }
  FUN_08090b18();
  local_40[0] = '8';
  local_40[1] = '6';
  local_40[2] = '1';
  local_40[3] = '8';
  local_40[4] = '3';
  local_40[5] = '6';
  local_40[6] = 'f';
  local_40[7] = '1';
  local_40[8] = '3';
  local_40[9] = 'e';
  local_40[10] = '3';
  local_40[11] = 'd';
  local_40[12] = '6';
  local_40[13] = '2';
  local_40[14] = '7';
  local_40[15] = 'd';
  local_40[16] = 'f';
  local_40[17] = 'a';
  local_40[18] = '3';
  local_40[19] = '7';
  local_40[20] = '5';
  local_40[21] = 'b';
  local_40[22] = 'd';
  local_40[23] = 'b';
  local_40[24] = '8';
  local_40[25] = '3';
  local_40[26] = '8';
  local_40[27] = '9';
  local_40[28] = '2';
  local_40[29] = '1';
  local_40[30] = '4';
  local_40[31] = 'e';
  FUN_08090fe0();
  uVar1 = 0;
  iVar2 = 0;
  while( true ) {
    if (0x1f < (int)uVar1) {
      if (iVar2 == 32) {
        return;
      }
      return;
    }
    if ((param_2 <= uVar1) || (31 < uVar1)) break;
    if ((byte)(*(byte *)(param_1 + uVar1) ^ local_40[uVar1]) == local_20[uVar1]) {
      iVar2 = iVar2 + 1;
    }
    uVar1 = uVar1 + 1;
  }
  runtime.panicindex();
  do {
    invalidInstructionException();
  } while( true );
}
```
Look at its assembly code:
```
                             LAB_080d4b0f                                    XREF[1]:     080d4b0c(j)  
        080d4b0f 83 f8 20        CMP        EAX,0x20
        080d4b12 7d 26           JGE        LAB_080d4b3a
        080d4b14 39 d0           CMP        EAX,EDX
        080d4b16 73 4e           JNC        LAB_080d4b66
        080d4b18 0f b6 2c 01     MOVZX      EBP,byte ptr [ECX + EAX*0x1]
        080d4b1c 83 f8 20        CMP        EAX,32
        080d4b1f 73 45           JNC        LAB_080d4b66
        080d4b21 0f b6 74        MOVZX      ESI,byte ptr [ESP + EAX*0x1 + 0x4]
                 04 04
        080d4b26 31 f5           XOR        EBP,ESI
        080d4b28 0f b6 74        MOVZX      ESI,byte ptr [ESP + EAX*0x1 + 0x24]
                 04 24
        080d4b2d 95              XCHG       EAX,EBP
        080d4b2e 87 de           XCHG       ESI,EBX
        080d4b30 38 d8           CMP        AL,BL
        080d4b32 87 de           XCHG       ESI,EBX
        080d4b34 95              XCHG       EAX,EBP
        080d4b35 75 d7           JNZ        LAB_080d4b0e
        080d4b37 43              INC        EBX
        080d4b38 eb d4           JMP        LAB_080d4b0e
```
Base on the assembly code:  

Input is stored in $ecs
```
gef➤  hexdump byte $ecx
0x1846e060     31 32 33 34 35 36 37 38 39 31 32 33 34 35 36 37    1234567891234567
0x1846e070     38 39 30 31 32 33 34 35 36 37 38 39 30 31 32 33    8901234567890123
0x1846e080     34 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    4...............
0x1846e090     00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00    ................
```
XORED value is in $esp+0x4
```
gef➤  hexdump byte $esp+0x4
0x1843df28     38 36 31 38 33 36 66 31 33 65 33 64 36 32 37 64    861836f13e3d627d
0x1843df38     66 61 33 37 35 62 64 62 38 33 38 39 32 31 34 65    fa375bdb8389214e
0x1843df48     4a 53 47 5d 41 45 03 54 5d 02 5a 0a 53 57 45 0d    JSG]AE.T].Z.SWE.
0x1843df58     05 00 5d 55 54 10 01 0e 41 55 57 4b 45 50 46 01    ..]UT...AUWKEPF.
```
Output check being against
```
gef➤  hexdump byte $esp+0x24
0x1843df48     4a 53 47 5d 41 45 03 54 5d 02 5a 0a 53 57 45 0d    JSG]AE.T].Z.SWE.
0x1843df58     05 00 5d 55 54 10 01 0e 41 55 57 4b 45 50 46 01    ..]UT...AUWKEPF.
0x1843df68     c2 48 0d 08 60 e0 46 18 21 00 00 00 ac df 43 18    .H..`.F.!.....C.
0x1843df78     01 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00    ................
```
XORing the expected output with the key to get the orginal password:
```
from pwn import *
data1 = "4a53475d414503545d025a0a5357450d05005d555410010e4155574b45504601"
key = "861836f13e3d627dfa375bdb8389214e"

# Perform XOR directly on hex strings
result = xor(unhex(data1), key)

# Print as readable text
print(result)  # Convert to string
```
b'reverseengineericanbarelyforward'

Enter the password:
```
└─$ nc mercury.picoctf.net 6516
Enter Password: reverseengineericanbarelyforward
=========================================
This challenge is interrupted by psociety
What is the unhashed key?
```
Looking at other function to get a idea of what hashing algo is used and should be md5:
```
void main.ambush(undefined4 param_1,undefined4 param_2)

{
  char cVar1;
  uint uVar2;
  int *in_GS_OFFSET;
  int local_88;
  uint local_84;
  uint local_80;
  undefined local_70 [16];
  char local_60 [31];
  undefined local_40 [32];
  undefined local_20 [12];
  undefined local_14 [16];
  undefined4 uStack_4;
  
  while (local_14 <= *(undefined **)(*(int *)(*in_GS_OFFSET + -4) + 8)) {
    uStack_4 = 0x80d4e4b;
    runtime.morestack_noctxt();
  }
  runtime.stringtoslicebyte(local_40,param_1,param_2);
  crypto/md5.Sum(local_88,local_84,local_80);
  FUN_08091008();
  FUN_08090b18();
  local_60[0] = '8';
  local_60[1] = '6';
  local_60[2] = '1';
  local_60[3] = '8';
```

Using online decryptor:
```
goldfish
```

Enter the unhased key:
```
Enter Password: reverseengineericanbarelyforward
=========================================
This challenge is interrupted by psociety
What is the unhashed key?
goldfish
Flag is:  picoCTF{p1kap1ka_p1c001b3038b}
```

## Stuff Learned  
1. Hexdump bytes to get the data in bytes in gdb.  
2. Since the input and key is xored in their bytes form, must do the same but in reverse to get the input.  

