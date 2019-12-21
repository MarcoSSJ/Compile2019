grammar Cmacros;/* Process #define statements in a C file.
   TODO : develop token_sequence
*/

program : translation_unit Eof?;

translation_unit
@init {print("Cmacros last update 1436");}
    :   ( '#' preprocessor
    |     ignore
    |     NL
    )+
    ;

preprocessor
    :   pp_define
    |   pp_ignore
    ;

pp_define
    :   'define' ID '(' ID ( ',' ID )* ')' token_sequence
    |   'define' ID token_sequence
    ;

pp_ignore
    :   ignore
    ;

token_sequence
    :   ignore
    ;

ignore
    :   (ID|~NL)+ NL
    ;


Eof: EOF;

CHAR
    :   '\'' ( '\\'? . )+? '\'' ;

COMMENT
    :    '/*' .*? '*/' -> channel(HIDDEN)
    ;

HEXADECIMAL
    :   '0' [xX] [0-9a-fA-F]+
    ;

ID  :   ( ID_FIRST (ID_FIRST | DIGIT)* )
    ;

INT :   DIGIT+ ;


//NL  :   '\r'? '\n' -> channel(WHITESPACE) ;  // channel(1)
//NL  :   '\n' -> channel(HIDDEN) ;
NL  :   '\r\n'|'\n' ;

SL_COMMENT
    :   '//' .*? '\n' -> channel(HIDDEN)
    ;

SPECIAL
    :   '+' | '-' | '*' | '/' | '%' | '&' | '|' | '(' | ')' | '{' | '}' |
'[' | ']'
    |   '^' | '!' | '<' | '>' | '=' | ',' | '.' | ';' | ':' | '?'
    ;

STRING
    :   '"' ( '\\'? . )*? '"' ;

WS  :   [ \t]+ -> channel(HIDDEN) ;

fragment DIGIT  : [0-9] ;

fragment ID_FIRST : LETTER | '_' ;

fragment LETTER : [a-zA-Z] ;
