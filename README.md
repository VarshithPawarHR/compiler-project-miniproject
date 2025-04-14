# Compiler-Design-Project

### 📌 Problem Statement:

Design a lexer and parser for the following i/p grammar

```
int main() 
begin 
int n1, n2, n3; 
if( expr relop expr ) 
begin 
printf( n1); 
end 
if ( expr relop expr ) 
begin 
printf( n2); 
end 
if( expr relop expr ) 
begin 
printf( n3); 
end 
end
```

### Info

- Type of parsing used: `Recursive Descent parsing`
- Recursive Descent Parser uses the technique of Top-Down Parsing without backtracking. It can be defined as a Parser that uses the various recursive procedure to process the input string with no backtracking. It can be simply performed using a Recursive language. The first symbol of the string of R.H.S of production will uniquely determine the correct alternative to choose.

### Steps to run the file

- Navigate to the folder where the file `lex.py` and `RD_parser.py` is present
- Make sure you have Python installed in your PC
- Run the file using the command

```
python lex.py
python RD_parser.py
```

