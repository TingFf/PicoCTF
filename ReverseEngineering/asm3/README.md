## Comment  
1. Another assembly challenge.  
 
 

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Know where the variable is stored and follow the logic.  
## Tools Used  
NIL  

## Writeup  
```
asm3:
	<+0>:	push   ebp                        
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xa]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xc]
	<+15>:	add    ah,BYTE PTR [ebp+0xd]
	<+18>:	xor    ax,WORD PTR [ebp+0x10]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    

```
1. Must understand how the argument is saved.
2. In x86 (32, cdecl), function arguments are pushed right to left onto the stack.
```
Stack Address          Value (Argument)
[ebp+0x4]              Return address
[ebp+0x8]              First argument (0xd73346ed)
[ebp+0xC]              Second argument (0xd48672ae)
[ebp+0x10]             Third argument (0xd3c8b139)
```
3. And little endianess is used so:
```
...
...
...
ebp + 0x8       ->      0xed
ebp + 0x9       ->      0x46
ebp + 0xa       ->      0x33
ebp + 0xb       ->      0xd7
...
...
...
```
4. First instruction, mov    ah,BYTE PTR [ebp+0xa] :
```
    EAX
      ah al               BEFORE
00 00 00 00

    EAX
      ah al               AFTER               
00 00 33 00  
```
5. <+8>:	shl    ax,0x10  Since ax is only 16 bit hence, shift the bit out of the register. 
6. (this part I just learn that when instruction is ax, it only affects register ax not the whole EAX so it does not shift into the upper 16 bit only within ax itself)
```
    EAX
      ah al               BEFORE
00 00 33 00
   
    EAX
      ah al               AFTER 
00 00 00 00
```
7. 	<+12>:	sub    al,BYTE PTR [ebp+0xc]:
```
...
...
...
ebp + 0xc       ->      0xae
ebp + 0xd       ->      0x72
ebp + 0xe       ->      0x86
ebp + 0xf       ->      0xd4
...
...
...
    EAX
      ah al               BEFORE 
00 00 00 00  (00 - ae)

    EAX
      ah al               AFTER 
00 00 00 52
```
8. 	<+15>:	add    ah,BYTE PTR [ebp+0xd]
```
    EAX
      ah al               BEFORE 
00 00 00 52  (00 + 72)

    EAX
      ah al               AFTER 
00 00 72 52
```
9. 	<+18>:	xor    ax,WORD PTR [ebp+0x10]
```
    EAX
      ah al               BEFORE 
00 00 72 52  (7252 ^ b139)

    EAX
      ah al               AFTER 
00 00 c3 6b
```
10. Flag:
```
0xc36b
```


## Stuff Learned  
1. Shifting of AH to left does not shift it to the upper 16 bit of EAX.  


