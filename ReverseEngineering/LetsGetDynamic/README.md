## Comment  
1. Finally have new stuff to learn.  
2. Didnt know .S file can compile into exe file to debug.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Look at the secret flag that the input is being compare with in the memory.  
## Tools Used  
**Ghidra, Gdb**  

## Writeup  
According to the hints, I tried to debug the file but is in .S file hence need to compile to exe:  
```
gcc -c chall.S -o chall.o
gcc chall.o -o chall
```
First I open in ghidra and look like the flag is store in local_118:
```

bool main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  int local_11c;
  byte local_118 [64];
  char local_d8 [64];
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 local_70;
  undefined2 local_68;
  undefined8 local_58;
  undefined8 local_50;
  undefined8 local_48;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined2 local_28;
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  local_98 = 0xefef8db97e511c7b;
  local_90 = 0x27e37ee776fb3190;
  local_88 = 0x15aa8eba0ac2a4be;
  local_80 = 0x91a06065f557aa8a;
  local_78 = 0xd690a4ec1d83ac33;
  local_70 = 0x728e067eb3817536;
  local_68 = 0xe9;
  local_58 = 0x80bccfed01236718;
  local_50 = 0x649d51955a8c52ef;
  local_48 = 0x4edcb9c466f7c889;
  local_40 = 0xef9e1e1fc801d3b0;
  local_38 = 0xbdc9e7bd1ec1eb5f;
  local_30 = 0x2a830177bfdd783c;
  local_28 = 0xb7;
  fgets(local_d8,0x31,stdin);
  local_11c = 0;
  while( true ) {
    sVar2 = strlen((char *)&local_98);
    if (sVar2 <= (ulong)(long)local_11c) break;
    local_118[local_11c] =
         (byte)local_11c ^
         *(byte *)((long)&local_98 + (long)local_11c) ^ *(byte *)((long)&local_58 + (long)local_11c)
         ^ 0x13;
    local_11c = local_11c + 1;
  }
  iVar1 = memcmp(local_d8,local_118,0x31);
  if (iVar1 == 0) {
    puts("No, that\'s not right.");
  }
  else {
    puts("Correct! You entered the flag.");
  }
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return iVar1 == 0;
}
```
Seems like its stored in register $rbp-0x110:
```
    5555555552e1 48 8d 8d        LEA        RCX=>local_118,[RBP + -0x110]
                 f0 fe ff ff
    5555555552e8 48 8d 85        LEA        RAX=>local_d8,[RBP + -0xd0]
                 30 ff ff ff
    5555555552ef ba 31 00        MOV        EDX,0x31
                 00 00
    5555555552f4 48 89 ce        MOV        RSI,RCX
    5555555552f7 48 89 c7        MOV        RDI,RAX
    5555555552fa e8 61 fd        CALL       <EXTERNAL>::memcmp                               int memcmp(void * __s1, void * _
                 ff ff
    5555555552ff 85 c0           TEST       EAX,EAX
```
Setting break point, run until the break point and display whats in the register:
```
gef➤  x/s $rbp-0x110
0x7fffffffdce0: "picoCTF{dyn4m1c_4n4ly1s_1s_5up3r_us3ful_17e4690d}\335\377\377\377\177"
```

## Stuff Learned  
1. .S -> .o -> .exe


