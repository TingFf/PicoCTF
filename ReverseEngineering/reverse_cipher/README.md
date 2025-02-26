## Comment  
1. Pretty simple challenge.  
2. Similar to caesar ciper where char are shifted in specific order.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Given the output, reverse the algorithm and get input.  
## Tools Used  
**IDA**

## Writeup  
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char ptr[23]; // [rsp+0h] [rbp-50h] BYREF
  char v5; // [rsp+17h] [rbp-39h]
  int v6; // [rsp+2Ch] [rbp-24h]
  FILE *v7; // [rsp+30h] [rbp-20h]
  FILE *flag; // [rsp+38h] [rbp-18h]
  int j; // [rsp+44h] [rbp-Ch]
  int i; // [rsp+48h] [rbp-8h]
  char v11; // [rsp+4Fh] [rbp-1h]

  flag = fopen("flag.txt", "r");
  v7 = fopen("rev_this", "a");
  if ( !flag )
    puts("No flag found, please make sure this is run on the server");
  if ( !v7 )
    puts("please run this on the server");
  v6 = fread(ptr, 0x18uLL, 1uLL, flag);         // Read 24 chars in flag
  if ( v6 <= 0 )
    exit(0);
  for ( i = 0; i <= 7; ++i )                    // Just copies the first 8 char to the rev_this file 
  {
    v11 = ptr[i];
    fputc(v11, v7);
  }
  for ( j = 8; j <= 22; ++j )
  {
    v11 = ptr[j];
    if ( (j & 1) != 0 )
      v11 -= 2;                                // Ascii_char - 2 when j is even else Ascii_char + 2
    else
      v11 += 5;
    fputc(v11, v7);
  }
  v11 = v5;
  fputc(v5, v7);
  fclose(v7);
  return fclose(flag);
}
```
1. Given then modified flag, find the original flag.
2. After the 8 char of the flag (picoCTF{...}), if j is even, the char - 2 in ascii value else if odd, +5.  
3. So by reversing the algorithm, I came up with a simple script.
Script:
```
flag=""
string = "w1{1wq8/7376j.:"
for j in range(len(string)):
        if j % 2 == 0:
                flag+=chr(ord(string[j])-5)
        else:
                flag+=chr(ord(string[j])+2)
print(flag)
```
4. Flag:
```
r3v3rs312528e05
```
## Stuff Learned  
1. Reversing the algorithm to get back the original flag.  


