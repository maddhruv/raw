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
