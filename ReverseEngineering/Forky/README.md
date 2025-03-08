## Comment  
1. Need to understand fork function.   

## Challenge Overview  
**Difficulty:** Hard    
**Description:** Understand how many child process there is and mutiple the number of process.  
## Tools Used  
**Ghidra**  

## Writeup  
1. Main function:
```
undefined4 main(void)

{
  int *piVar1;
  
  piVar1 = (int *)mmap((void *)0x0,4,3,0x21,-1,0);
  *piVar1 = 1000000000;
  fork();
  fork();
  fork();
  fork();
  *piVar1 = *piVar1 + 1234567890;
  doNothing(*piVar1);
  return 0;
}
```
2. Fork process doubles the number of child process each time, so there are 16 process in total since there is 4 fork().  
```
1 -> 2 -> 4 -> 16                                               
```
3. But we have to consider the number being overflow hence using python.  
```
from numpy import int32

print(int32(1000000000) + int32(16)*int32(0x499602d2))
```
4. Flag:  
```
picoCTF{-721750240}
```


## Stuff Learned  
Shared Memory (mmap with MAP_SHARED)
- Unlike regular variables, mmap ensures that all forked processes modify the same memory location, causing cumulative changes.

Process Forking (fork())
- Each fork doubles the number of processes, leading to 16 total processes.

Concurrent Updates (piVar1 = piVar1 + 1234567890)
- Since all 16 processes modify the same shared memory, the value keeps increasing.

Pointer Size is 32 bit which depends on the system architecture
```
vuln: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=836c8d5ecaad6d64f4a358cf73d060d0c5050e87, not stripped
```

