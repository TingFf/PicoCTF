## Comment  
1. New type of challenge that does not have a password checker.  
2. Uses bytes and assembly code to get the flag.  
3. Fun and learn something new.  
4. Had to look at writeups.  
[https://www.youtube.com/watch?v=LopkxFmxk2E]  
[https://ctftime.org/writeup/27055]  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** 
## Tools Used  
**IDA, MD5 Hash Generator, Online Assembler&Disassembler**  

## Writeup  
Entry:
```
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int v3; // eax
  __int64 v4; // rdx
  int i; // [rsp+8h] [rbp-F8h]
  int j; // [rsp+8h] [rbp-F8h]
  int block_num; // [rsp+Ch] [rbp-F4h]
  void (__fastcall *shellcode)(__int64 (__fastcall *)()); // [rsp+10h] [rbp-F0h]
  _BYTE *output; // [rsp+18h] [rbp-E8h]
  int offset[4]; // [rsp+20h] [rbp-E0h]
  __int64 v12[2]; // [rsp+30h] [rbp-D0h]
  char random_str[48]; // [rsp+40h] [rbp-C0h] BYREF
  char input[64]; // [rsp+70h] [rbp-90h] BYREF
  char dest[72]; // [rsp+B0h] [rbp-50h] BYREF
  unsigned __int64 v16; // [rsp+F8h] [rbp-8h]

  v16 = __readfsqword(0x28u);
  setbuf(stdout, 0LL);
  strcpy(random_str, "GpLaMjEWpVOjnnmkRGiledp6Mvcezxls");
  offset[0] = 8;
  offset[1] = 2;
  offset[2] = 7;
  offset[3] = 1;
  memset(input, 0, sizeof(input));
  memset(dest, 0, 0x40uLL);
  printf("Password: ");
  fgets(input, 64, stdin);
  input[strlen(input) - 1] = 0;
  for ( i = 0; i <= 3; ++i )                    // Copies 4 bytes of password + 8 bytes of random_string into dest
  {                                             // Loops 4 times hence password must be 16 bytes long
                                                // 
    strncat(dest, &input[4 * i], 4uLL);
    strncat(dest, &random_str[8 * i], 8uLL);
  }
  output = malloc(0x40uLL);
  v3 = strlen(dest);
  md5_related((__int64)output, (__int64)dest, v3);
  for ( j = 0; j <= 3; ++j )                    // copy 4 bytes of MD5 to shellcode
                                                // 
  {
    for ( block_num = 0; block_num <= 3; ++block_num )
      *((_BYTE *)v12 + 4 * block_num + j) = output[16 * block_num + j + offset[block_num]];
  }                                             // MD5(????GpLaMjEW) bytes 8-11
                                                // MD5(????pVOjnnmk) bytes 2-5
                                                // MD5(????RGiledp6) bytes 7-10
                                                // MD5(????Mvcezxls) bytes 1-4
                                                // 
  shellcode = (void (__fastcall *)(__int64 (__fastcall *)()))mmap(0LL, 0x10uLL, 7, 34, -1, 0LL);
  v4 = v12[1];
  *(_QWORD *)shellcode = v12[0];
  *((_QWORD *)shellcode + 1) = v4;
  shellcode(flag);
  free(output);
  return 0LL;
}
```
1. In the first loop, it concatenate every 4 bytes of input with 8 bytes of the random_string.  
2. Then every set is hash using md5.  
3. Then based on the offset of the bytes, every bytes in each set is used to create a shellcode.  
```
MD5(D1v1GpLaMjEW) = 23f144e08b603e724889fe489f78fa53
```
4. Given the first hints, the first 4 bytes is given and the specific bytes that is extracted is from bytes 8-11.  
```
        23 f1 44 e0 8b 60 3e 72 48 89 fe 48 9f 78 fa 53
Bytes:  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16

Result = 4889fe48
```
5. Putting the result into the online disassemble to get the corresponding assembly code.  
```
0:  48 89 fe                mov    rsi,rdi
3:  48                      rex.W
```
6. The shellcode is stored in rsi and the flag to pass in as argument is in rdi.
```
.text:0000000000000E0B                 lea     rdi, flag
.text:0000000000000E12                 call    rax
.text:0000000000000E14                 mov     rax, [rbp+output]
.text:0000000000000E1B                 mov     rdi, rax        ; ptr
.text:0000000000000E1E                 call    _free
.text:0000000000000E23                 mov     eax, 0
.text:0000000000000E28                 mov     rsi, [rbp+var_8]
.text:0000000000000E2C                 xor     rsi, fs:28h
```
7. Then looking in to flag checking function:  
```
unsigned __int64 __fastcall flag(__int64 a1)
{
  FILE *stream; // [rsp+18h] [rbp-98h]
  char s[136]; // [rsp+20h] [rbp-90h] BYREF
  unsigned __int64 v4; // [rsp+A8h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  if ( a1 == 0x7B3DC26F1LL )
  {
    stream = fopen("flag", "r");
    if ( !stream )
    {
      puts("Flag file not found. Contact an admin.");
      exit(1);
    }
    fgets(s, 128, stream);
    puts(s);
  }
  else
  {
    puts("Hmmmmmm... not quite");
  }
  return __readfsqword(0x28u) ^ v4;
}
```
8. The argument must be 0x7B3DC26F1.  
9. Using the online assembler:  
```
mov    rsi,rdi
movabs rdi,0x7B3DC26F1LL
call   rsi
```
10. Result:
```
0:  48 89 fe                mov    rsi,rdi
3:  48 bf f1 26 dc b3 07    movabs rdi,0x7b3dc26f1
a:  00 00 00
d:  ff d6                   call   rsi
```
11. So the bytes showing above is what we have to get from the hashing of the password and random_string from above.
```
MD5(D1v1GpLaMjEW) =  ,  ,  ,  ,  ,  ,  ,  ,48,89,fe,48,  ,  ,  ,  , 
MD5(????pVOjnnmk) =  ,  ,bf,f1,26,dc,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,
MD5(????RGiledp6) =  ,  ,  ,  ,  ,  ,  ,b3,07,00,00,  ,  ,  ,  ,  ,
MD5(????Mvcezxls) =  ,00,ff,d6,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,
```
12. Basically, the 8-11 bytes of the md5 hash of D1v1GpLaMjEW must be 48 89 fe 48.  
13. Then we must brute force the rest of the set so that the hash result matches the bytes in the corresponding bytes positions.  
14. Script (Based on write up):  
```
from hashlib import md5
import string
import itertools
All_combi = string.ascii_letters+string.digits

temp2="bff126dc"
temp3="b3070000"
temp4="00ffd6"
check2="pVOjnnmk"
check3="RGiledp6"
check4="Mvcezxls"

solved = 0

for x in itertools.product(All_combi,repeat=4):
      h2 = md5(("".join(x)+check2).encode()).hexdigest()
      h3 = md5(("".join(x)+check3).encode()).hexdigest()
      h4 = md5(("".join(x)+check4).encode()).hexdigest()
      if h2[4:12]==temp2:
            print("H2:"+"".join(x))
            s2="".join(x)
            solved+=1
      if h3[14:22]==temp3:
            print("H3:"+"".join(x))
            s3="".join(x)
            solved+=1
      if h4[2:8]==temp4:
            print("H4:"+"".join(x))
            s4="".join(x)
            solved+=1
      if solved==3:
            print("D1v1"+s2+s3+s4)
            break
  ```
15. Result:  
```
D1v1d3AndC0nqu3r
```
16. Flag:  
```
nc mercury.picoctf.net 11220
Password: D1v1d3AndC0nqu3r
picoCTF{r011ing_y0ur_0wn_crypt0_15_h4rd!_18d12289}
```

## Stuff Learned  
1. Using IDA to dissamble seems to be better for this challenge.  



