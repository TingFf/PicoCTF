## Comment  
1. Had to use ChatGPT for these kind of challenges.  
2. The hints helped a lot.  
3. Output too long to print out.  
4. Script is provided.  

## Challenge Overview  
**Difficulty:** Medium  
**Description:** Write a script to RE engineer the output of the scrambled flag.  
## Tools Used  
NIL  

## Writeup  
```
import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1
    
  return L

def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def main():
  flag = get_flag()
  cypher = scramble(flag)
  print(cypher)
  

if __name__ == '__main__':
  main()
```
1. The output is given.
2. We cant just unscrambled the output but must only take the outer loops char based on the hint.

```
  # Hint 3: to do testing
  # Iterate the nested list
  for i in cypher:

    # Hint 2:
    # Extract hex strings, ignore inner lists
    # Filters i (which is a sublist from cypher) and keeps only elements that are strings.
    # This avoids issues with nested lists or other data types.
    hex_values = [x for x in i if isinstance(x, str)]

    # Hint 1:
    # Converts each hex string (h) into an integer (int(h, 16)) and then into a character (chr(...)).
    decoded_chars = [chr(int(h, 16)) for h in hex_values]
    print("".join(decoded_chars), end="")
```
3. Flag:
```
picoCTF{python_is_weirdef8ea0cf}
```

## Stuff Learned  
1. eval can convert hex to ascii.  


