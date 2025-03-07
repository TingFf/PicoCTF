## Comment  
1. Simple and easy to understand challenge.  
2. About to clear most of the RE challenge, will move on the forensic next.  
3. Register for picoCTF competition.  

## Challenge Overview  
**Difficulty:** Hard  
**Description:** Two method: Ignore the SIGALRM message or skip the set_timer() function.  
## Tools Used  
**Ghidra**

## Writeup  
1. Here is how the program run normally:  
```
└─$ ./need-for-speed 
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!
```
2. Looking the binary in ghidra.  
3. Main:
```

undefined8 main(void)

{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```
4. set_timer():
```
### The program sets up a signal handler (alarm_handler) for SIGALRM (signal 14).
### If setting the signal handler fails, it prints an error message and exits.
### Otherwise, it schedules an alarm in 1 second.
### When the alarm goes off, alarm_handler will execute (though it's not shown in this snippet).

void set_timer(void)

{
  __sighandler_t p_Var1;                                         # is a typedef for a signal handler function pointer.
  
  p_Var1 = __sysv_signal(0xe,alarm_handler);                     # is setting up a signal handler for signal 14 (0xe in hex), which is SIGALRM.
  if (p_Var1 == (__sighandler_t)0xffffffffffffffff) {
    puts("\n\nSomething bad happened here. ");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  alarm(1);
  return;
}
```
5. alarm_hander():
```
void alarm_handler(void)

{
  puts("Not fast enough. BOOM!");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```

6. get_key():
```
void get_key(void)

{
  puts("Creating key...");
  key = calculate_key();
  puts("Finished");
  return;
}
```
7. print_flag():
```

void print_flag(void)

{
  puts("Printing flag:");
  decrypt_flag(key);
  puts(flag);
  return;
}
```
8. Before the get_key() function can finish calculating the key and print the flag, the set_timer() function will force exit the program.  
9. Hence we need to skip the function.  
10. There is another way apparently is to ignore SIGAlrm.  

11. Method 1.1: Set a break point inside the set_timer() function, then skip the entire function and continue.  
```
set_timer() assemble code:
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined set_timer()
             undefined         AL:1           <RETURN>
             undefined8        Stack[-0x10]:8 local_10                                XREF[2]:     55555540084f(W), 
                                                                                                   555555400853(R)  
             undefined4        Stack[-0x14]:4 local_14                                XREF[2]:     555555400837(W), 
                                                                                                   555555400870(R)  
                             set_timer                                       XREF[4]:     Entry Point(*), 
                                                                                          main:555555400938(c), 
                                                                                          555555400aac, 555555400bd4(*)  
    55555540082f 55              PUSH       RBP
    555555400830 48 89 e5        MOV        RBP,RSP
    555555400833 48 83 ec 10     SUB        RSP,0x10
    555555400837 c7 45 f4        MOV        dword ptr [RBP + local_14],0x1
                 01 00 00 00
    55555540083e 48 8d 35        LEA        RSI,[alarm_handler]
                 c9 ff ff ff
    555555400845 bf 0e 00        MOV        EDI,0xe
                 00 00
    55555540084a e8 e1 fd        CALL       <EXTERNAL>::__sysv_signal                        __sighandler_t __sysv_signal(int
                 ff ff
    55555540084f 48 89 45 f8     MOV        qword ptr [RBP + local_10],RAX
    555555400853 48 83 7d        CMP        qword ptr [RBP + local_10],-0x1
                 f8 ff
    555555400858 75 16           JNZ        LAB_555555400870
    55555540085a 48 8d 3d        LEA        RDI,[s__Something_bad_happened_here._555555400   = "\n\nSomething bad happened he
                 a7 01 00 00
    555555400861 e8 aa fd        CALL       <EXTERNAL>::puts                                 int puts(char * __s)
                 ff ff
    555555400866 bf 00 00        MOV        EDI,0x0
                 00 00
    55555540086b e8 d0 fd        CALL       <EXTERNAL>::exit                                 void exit(int __status)
                 ff ff
                             -- Flow Override: CALL_RETURN (CALL_TERMINATOR)
```
-Take the address before it call the __sysv_signal.  
-Can use gdb command ```return``` or ```finish```.  
-Then ```continue```.  
12. Flag:  
```
Continuing.
Creating key...

Program received signal SIGALRM, Alarm clock.
Finished
Printing flag:
PICOCTF{Good job keeping bus #24c43740 speeding along!}
```
13. Method 2: Since the function creates a signal handler to handle the alarm which will print "Not fast enough. BOOM!" and terminate the program.  
```
gef➤  handle SIGALRM ignore
Signal        Stop      Print   Pass to program Description
SIGALRM       No        Yes     No              Alarm clock
gef➤  r
Starting program: /home/kali/Downloads/need-for-speed 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Keep this thing over 50 mph!
============================

Creating key...

Program received signal SIGALRM, Alarm clock.
Finished
Printing flag:
PICOCTF{Good job keeping bus #24c43740 speeding along!}
[Inferior 1 (process 989851) exited normally]
```
14. Method 1.2: Set a break point at the set_timer function and then jump to get_key function and continue:
```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined main()
             undefined         AL:1           <RETURN>
             undefined4        Stack[-0xc]:4  local_c                                 XREF[1]:     555555400922(W)  
             undefined8        Stack[-0x18]:8 local_18                                XREF[1]:     555555400925(W)  
                             main                                            XREF[4]:     Entry Point(*), 
                                                                                          _start:55555540067d(*), 
                                                                                          555555400acc, 555555400c54(*)  
    55555540091a 55              PUSH       RBP
    55555540091b 48 89 e5        MOV        RBP,RSP
    55555540091e 48 83 ec 10     SUB        RSP,0x10
    555555400922 89 7d fc        MOV        dword ptr [RBP + local_c],EDI
    555555400925 48 89 75 f0     MOV        qword ptr [RBP + local_18],RSI
    555555400929 b8 00 00        MOV        EAX,0x0
                 00 00
    55555540092e e8 a5 ff        CALL       header                                           undefined header()
                 ff ff
    555555400933 b8 00 00        MOV        EAX,0x0
                 00 00
    555555400938 e8 f2 fe        CALL       set_timer                                        undefined set_timer()
                 ff ff
    55555540093d b8 00 00        MOV        EAX,0x0
                 00 00
    555555400942 e8 36 ff        CALL       get_key                                          undefined get_key()
                 ff ff
    555555400947 b8 00 00        MOV        EAX,0x0
                 00 00
    55555540094c e8 5b ff        CALL       print_flag                                       undefined print_flag()
                 ff ff
    555555400951 b8 00 00        MOV        EAX,0x0
                 00 00
```
15. The commands to use:
```
b *0x555555400938
r
jump *0x555555400942
```
16. Flag:
```
Continuing at 0x555555400942.
Creating key...

Finished
Printing flag:
PICOCTF{Good job keeping bus #24c43740 speeding along!}
[Inferior 1 (process 991501) exited normally]
```
   

## Stuff Learned  
1. Using ```return```,```jump```,```finish``` to skip function in gdb.  
2. When a signal alarm is set,handler will handle it and can be ignore.  


