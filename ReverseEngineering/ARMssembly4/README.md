## Comment  
1. Manually follow the logic of the assembly code before I realise it can be assemble to object file and compile into exe.
2. Pretty straight forward but hope I correct with the logic.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Understand assembly code.  
## Tools Used  
**CMD line**  
```
aarch64-linux-gnu-as -o chall_4.o chall_4.S
aarch64-linux-gnu-gcc -static -o chall_4 chall_4.o
```

## Writeup  
```
	.arch armv8-a
	.file	"chall_4.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]	# 
	ldr	w0, [x29, 28]	# w0 = 1215610622
	cmp	w0, 100		# 	
	bls	.L2
	ldr	w0, [x29, 28]	
	add	w0, w0, 100	# w0 = 1215610722
	bl	func2		      # 1. Goes func2
	b	.L3
.L2:
	ldr	w0, [x29, 28]
	bl	func3
.L3:
	ldp	x29, x30, [sp], 32
	ret
	.size	func1, .-func1
	.align	2
	.global	func2
	.type	func2, %function
func2:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]	# 
	ldr	w0, [x29, 28]	# w0 = 1215610722
	cmp	w0, 499			
	bhi	.L5           # 2. Goes .L5
	ldr	w0, [x29, 28]	
	sub	w0, w0,
	bl	func4
	b	.L6
.L5:
	ldr	w0, [x29, 28]	 # w0 = 1215610722
	add	w0, w0, 13	   # w0 = 1215610735
	bl	func5          # 3. Goes func5
.L6:
	ldp	x29, x30, [sp], 32  
	ret                # 7. End of code
	.size	func2, .-func2
	.align	2
	.global	func3
	.type	func3, %function
func3:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]		# 1215610737 = [x29, 28]
	ldr	w0, [x29, 28]		# w0 = 1215610737
	bl	func7	
	ldp	x29, x30, [sp], 32
	ret
	.size	func3, .-func3
	.align	2
	.global	func4
	.type	func4, %function
func4:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	mov	w0, 17
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func1
	str	w0, [x29, 44]
	ldr	w0, [x29, 28]
	ldp	x29, x30, [sp], 48
	ret
	.size	func4, .-func4
	.align	2
	.global	func5
	.type	func5, %function
func5:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]	      # 1215610735 = [x29, 28]
	ldr	w0, [x29, 28]	      # w0 = 1215610735
	bl	func8               # 4. Goes func8
	str	w0, [x29, 28]	      # 1215610737 = [x29, 28]
	ldr	w0, [x29, 28]	      # w0 = 1215610737
	ldp	x29, x30, [sp], 32
	ret                     # 6. Back to .L5
	.size	func5, .-func5
	.align	2
	.global	func6
	.type	func6, %function
func6:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 314
	str	w0, [sp, 24]
	mov	w0, 1932
	str	w0, [sp, 28]
	str	wzr, [sp, 20]
	str	wzr, [sp, 20]
	b	.L14
.L15:
	ldr	w1, [sp, 28]
	mov	w0, 800
	mul	w0, w1, w0
	ldr	w1, [sp, 24]
	udiv	w2, w0, w1
	ldr	w1, [sp, 24]
	mul	w1, w2, w1
	sub	w0, w0, w1
	str	w0, [sp, 12]
	ldr	w0, [sp, 20]
	add	w0, w0, 1
	str	w0, [sp, 20]
.L14:
	ldr	w0, [sp, 20]
	cmp	w0, 899
	bls	.L15
	ldr	w0, [sp, 12]
	add	sp, sp, 32
	ret
	.size	func6, .-func6
	.align	2
	.global	func7
	.type	func7, %function
func7:
	sub	sp, sp, #16			
	str	w0, [sp, 12]		[sp, 12] = 1215610737
	ldr	w0, [sp, 12]		w0 = 1215610737
	cmp	w0, 100			
	bls	.L18
	ldr	w0, [sp, 12]		w0 = 1215610737
	b	.L19
.L18:
	mov	w0, 7
.L19:
	add	sp, sp, 16
	ret
	.size	func7, .-func7
	.align	2
	.global	func8
	.type	func8, %function
func8:
	sub	sp, sp, #16
	str	w0, [sp, 12]	# 1215610735 = [sp, 12]
	ldr	w0, [sp, 12]	# w0 = 1215610735
	add	w0, w0, 2	    # w0 = 1215610737
	add	sp, sp, 16
	ret               # 5.Back to func5 
	.size	func8, .-func8
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

## Stuff Learned  
1. This kind of challenge can compile, enter the given input and run.  


