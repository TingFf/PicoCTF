## Comment  
1. Another asm challenge.  
2. Straight forward and simple.   

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Understand assembly code.  
## Tools Used  
NIL  

## Writeup  
```
asm2(0x4,0x21) -> Store from right to left

asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] 	  
	<+9>:	mov    DWORD PTR [ebp-0x4],eax 		0x21
	<+12>:	mov    eax,DWORD PTR [ebp+0x8] 	 
	<+15>:	mov    DWORD PTR [ebp-0x8],eax		0x4
	<+18>:	jmp    0x509 <asm2+28>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1		
	<+24>:	add    DWORD PTR [ebp-0x8],0x74		
	<+28>:	cmp    DWORD PTR [ebp-0x8],0xfb46	
	<+35>:	jle    0x501 <asm2+20>				Loop until 0x4 > 0xfb46
	<+37>:	mov    eax,DWORD PTR [ebp-0x4]  Flag
	<+40>:	leave  
	<+41>:	ret    
```
1. Translate to python.
```
ebp_0x8 = int("0x4", 16)
ebp_0x4 = int("0x21", 16)

while ebp_0x8 <= int("0xfb46", 16):
    ebp_0x8 += int("0x74",16)
    ebp_0x4 += int("0x1",16)

print(hex(ebp_0x4))
```
2. Flag
```
0x24c
```
## Stuff Learned  
1. Argument is stored onto the stack from right to left.  

