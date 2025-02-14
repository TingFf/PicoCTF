## Comment  
1. Another ARM assembly challenge.  
2. Took me 1 hr to understand.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Understand assembly code.  
## Tools Used  
NIL  

## Writeup  
Basically, while it keeps dividing the arg by two. If the arg is odd, it will increase a value by 3 until the arg reach 0:
```
        .arch armv8-a 
        .file   "chall_3.c"
        .text
        .align  2
        .global func1
        .type   func1, %function
func1:
        stp     x29, x30, [sp, -48]!
        add     x29, sp, 0
        str     w0, [x29, 28]   # [x29, 28] = 4012702611
        str     wzr, [x29, 44]  # [x29, 44] = 0
        b       .L2
.L4:
        ldr     w0, [x29, 28]   # 4012702611
        and     w0, w0, 1       # check odd or even
        cmp     w0, 0           # if odd, go function 2
        beq     .L3
        ldr     w0, [x29, 44]   # w0=0
        bl      func2
        str     w0, [x29, 44]   # If even or after function 2 is return, L3 will be execute. 
.L3:
        ldr     w0, [x29, 28]   # 4012702611
        lsr     w0, w0, 1       # 4012702611/2
        str     w0, [x29, 28]   # Store back and checks again. 
.L2:
        ldr     w0, [x29, 28]   # w0=4012702611 
        cmp     w0, 0           # if 0, w0=0
        bne     .L4             # if not
        ldr     w0, [x29, 44]   
        ldp     x29, x30, [sp], 48
        ret
        .size   func1, .-func1
        .align  2
        .global func2
        .type   func2, %function
func2:
        sub     sp, sp, #16
        str     w0, [sp, 12]
        ldr     w0, [sp, 12]
        add     w0, w0, 3      # 0+3
        add     sp, sp, 16
        ret
        .size   func2, .-func2
        .section        .rodata
        .align  3
.LC0:
        .string "Result: %ld\n"
        .text
        .align  2
        .global main
        .type   main, %function
main:
        stp     x29, x30, [sp, -48]!
        add     x29, sp, 0
        str     w0, [x29, 28]
        str     x1, [x29, 16]
        ldr     x0, [x29, 16]
        add     x0, x0, 8
        ldr     x0, [x0]
        bl      atoi
        bl      func1
        str     w0, [x29, 44]
        adrp    x0, .LC0
        add     x0, x0, :lo12:.LC0
        ldr     w1, [x29, 44]
        bl      printf
        nop
        ldp     x29, x30, [sp], 48
        ret
        .size   main, .-main
        .ident  "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
        .section        .note.GNU-stack,"",@progbits
```
Equivalent in python:
```
def func2(arg):
    return arg+3

def func1(arg):
    value = 0
    while arg > 0:
        if arg%2==1:
            value=func2(value)
        arg = arg//2
    return value
result=func1(4012702611)
print(result)
```
## Stuff Learned  
1. After .L3, next instruction will be .L2 and not return to caller.(Didn't understand this part)
```
.L3:
        ldr     w0, [x29, 28]    
        lsr     w0, w0, 1        
        str     w0, [x29, 28]  ->| 
.L2:                             |
        ldr     w0, [x29, 28]  <-| 
        cmp     w0, 0            
        bne     .L4              
        ldr     w0, [x29, 44]   
        ldp     x29, x30, [sp], 48
        ret
        .size   func1, .-func1
        .align  2
        .global func2
        .type   func2, %function
```


