## Comment  
1. There is library issue with this challenge hence unable to debug.  
2. Manually getting the flag.  


## Challenge Overview  
**Difficulty:** Medium  
**Description:** Individually look at the data in memory of each of the ada__text_io__put__4 function.  
## Tools Used  
**Ghidra**

## Writeup  
Entry function:  
```
undefined4 FUN_00101fcc(undefined4 param_1,undefined8 param_2,undefined8 param_3)
{
  undefined local_10 [8];
  
  gnat_envp = param_3;
  gnat_argv = param_2;
  gnat_argc = param_1;
  __gnat_initialize(local_10);
  FUN_00101d7c();
  FUN_0010298a();
  FUN_00101d52();
  __gnat_finalize();
  return gnat_exit_status;
}
```
First and the last function doesn't seems like I could get the flag from hence look into the second function:
```
void FUN_0010298a(void)
{
  ada__calendar__delays__delay_for(1000000000000000);
  FUN_00102616();
  FUN_001024aa();
  FUN_00102372();
  FUN_001025e2();
  FUN_00102852();
  FUN_00102886();
  FUN_001028ba();
  FUN_00102922();
  FUN_001023a6();
  FUN_00102136();
  FUN_00102206();
  FUN_0010230a();
  FUN_00102206();
  FUN_0010257a();
  FUN_001028ee();
  FUN_0010240e();
  FUN_001026e6();
  FUN_00102782();
  FUN_001028ee();
  FUN_0010226e();
  FUN_00102136();
  FUN_0010226e();
  FUN_0010233e();
  FUN_001023da();
  FUN_0010230a();
  FUN_001021d2();
  FUN_00102956();
  return;
}
```
First function:
```
void FUN_00102616(void)
{
  ada__text_io__put__4(&DAT_00102cd8,&DAT_00102cb8);
  return;
}
```
Seems like ada__text_io__put__4 relates to input and output. Went to look at what is stored in this pointer:
```
                             DAT_00102cd8                                    XREF[3]:     FUN_00102616:0010261f(*), 
                                                                                          FUN_00102616:0010262d(*), 
                                                                                          FUN_00102616:00102636(*)  
        00102cd8 70              ??         70h    p
```
It seems it store a value of 70 hex at this pointer which is char 'p' in ascii encoding hence it should be clear that this is the letter p of the flag picoCTF{...}:
```
void FUN_0010298a(void)
{
  ada__calendar__delays__delay_for(1000000000000000);
  FUN_00102616(); p
  FUN_001024aa(); i 
  FUN_00102372(); c 
  FUN_001025e2(); o
  FUN_00102852(); C
  FUN_00102886(); T
  FUN_001028ba(); F
  FUN_00102922(); {
  FUN_001023a6(); d
  FUN_00102136(); 1
  FUN_00102206(); 5
  FUN_0010230a(); a
  FUN_00102206(); 5
  FUN_0010257a(); m
  FUN_001028ee(); _
  FUN_0010240e(); f
  FUN_001026e6(); t
  FUN_00102782(); w
  FUN_001028ee(); _
  FUN_0010226e(); 7
  FUN_00102136(); 1
  FUN_0010226e(); 7
  FUN_0010233e(); b
  FUN_001023da(); e
  FUN_0010230a(); a
  FUN_001021d2(); 4
  FUN_00102956(); }
  return;
}
```
picoCTF{d15a5m_ftw_717bea4}

## Stuff Learned  
NA


