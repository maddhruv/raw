# Python 2.7 and 3.x Functions and Methods
## Strings
### Operations
Operation | Interpretation
--- | ---
s.find('pa') | Search
s.rstrip() | Remove Whitespace
s.replace('pa', 'xx') | Replacement
s.split(',') | Split on delimiter
s.isdigit() | Content test
s.lower() | Case conversion
s.endswith('spam') | Case test
### Escape Characters
Escape | Meaning
--- | ---
\newline | Ignored(continuation line)
\\\ | Backslash
\' or \" | Quotes
\a | Bell
\b | Backspace
\f | Formfeed
\n | Newline
\r | Carriage Return
\t | Horizontal tab
\v | Vertical tab
\xhh | Character with hex value hh
\ooo | Character with octal value ooo
\0 | Null: binary 0 character
\N{id} | Unicode Database ID
### Conversions
Function | Operation
--- | ---
ord('s') | returns the ASCII value
chr(115) | returns corresponding character
int('1101', 2) | Convert binary to integer
bin(13) | Convert integer to binary
### String Formatting Type Codes
Code | Meaning
--- | ---
s | String
r | same as s, but uses repr, not str
c | Character (int or str)
d | Decimal
i | integer
o | octal
x | hex
X | same as x, but with uppercase letters
f | floating point
F | same as f, but with uppercase letters
### Formatting Methods
* tem = '{0}, {1}, {2}' > tem.format('a', 'b', 'c')
* tem = '{a}, {b}, {c}' > tem.format(a='A', b='B', c='C')
---
## Lists and Dictionaries
### Operations
Operation | Interpretation
--- | ---
L.insert(i,x) | Insert element at *i* index
L.index(X) | search element *X*
L.count(X) | counts the appearance of *X*
L.sort() | Sorting
L.reverse() | Reversing
D.keys() | All keys
D.values() | All values
D.items() | All keys+values tuples
D.update(D2) | Merge by keys
D.get(key, default?) | fetch by key, if absent default (or None)
D.pop(key, defualt?) | remove by key, if absent default (or error)
D.setdefault(key, default?) | fetch by key, if absent set default (or None)
D.popitem() | remove/return any (key,value) pair
---
## Tuples
---
## Files
Operation | Interpretation
--- | ---
output = open('filename', 'w') | Create output file, 'w' means write
input = open('data', 'r') | Create input file, 'r' means read
input = open('data', 'rb') | binary file (bytes)
aString = input.read() | read entire file into a single string
aString = input.read(N) | read upto N character into a string
aString = input.readline() | read next line (include \n) into a string
aList = input.readlines() | read entire file into a list of line strings (with \n)
output.write(aString) | write a string of characters into the file
output.writelines(aList) | write all line strings in a list into the file
output.close() | manually close
output.flush() | flush output buffer to disk without closing
anyFile.seek(N) | change the file position to offset N for next operation
open('filename').readline().rstrip() | remove end-of-line
