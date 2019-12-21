
grammar postCompile;
// Asttumptions for the input statement:
// 1. No block/line comment exists.
// 2. No '#' character exists.
// 3. No preprocessor keywords exists except "defined"
import preLexer;

statement    :    sToken+  EOF ;

sToken      :    stDefined
            |    stFunctionCall
            |    stVariable
            |    stOther
            ;

stDefined    :    DEFINED    WS+    stdId    ;
stdId        :    PAREN_OPEN    WS*    stdId    WS*    PAREN_CLOSE
            |    stdiId
            ;
stdiId        :    ID    ;

stVariable    :    ID    ;

stFunctionCall    :    ID    WS*    PAREN_OPEN    stfcArguments    PAREN_CLOSE    ;
stfcArguments    :    stfcaArgument    ( COMMA    stfcaArgument )*    ;
stfcaArgument    :    ( PAREN_OPEN    stfcaArgument    PAREN_CLOSE | STRING | WS | ID | CHAR )*    ;

stOther        :    ( STRING | WS | COMMA | PAREN_OPEN | PAREN_CLOSE | CHAR )    ;

// Logic operator
LOP_AND    :    '&&'    ;
LOP_OR    :    '||'    ;
LOP_NOT    :    '!'    ;

// Bit operator
BOP_NOT    :    '~'    ;
BOP_XOR    :    '^'    ;
BOP_AND    :    '&'    ;
BOP_OR    :    '|'    ;
BOP_SHL    :    '<<'    ;
BOP_SHR    :    '>>'    ;

// Arithmatic operator
AOP_ADD    :    '+'    ;
AOP_SUB    :    '-'    ;
AOP_MUL    :    '*'    ;
AOP_DIV    :    '/'    ;
AOP_MOD    :    '%'    ;

// Comparison operator
CMP_EQ    :    '=='    ;
CMP_NE    :    '!='    ;
CMP_LE    :    '<='    ;
CMP_LT    :    '<'    ;
CMP_GE    :    '>='    ;
CMP_GT    :    '>'    ;

// Ternary conditional
TER_IF    :    '?'    ;
TER_ELS    :    ':'    ;

// Parentheses
PAREN_OPEN    :    '('    ;
PAREN_CLOSE    :    ')'    ;

// Reserved keyword
DEFINED    :    'defined'    ;
TRUE    :    'true'    ;
FALSE    :    'false'    ;

// typed values
FLOAT    :    DIGIT+    '.'    DIGIT*    'f'?            // match 1. 39. 3.14159 etc...
        |            '.'    DIGIT+    'f'?            // match .1 .14159
        ;
INT        :    [1-9]    DIGIT*
        |    '0'
        ;
HEX        :    '0x'    DIGIT+    ;    // 0x000
OCT        :    '0'        DIGIT+    ;    // 0123
ID        :    ID_LETTER    (ID_LETTER|DIGIT)*    ;

// skip
NL_ESC    :    '\\'    '\r'?    '\n'    -> skip ;
WS        :    [ \t]+                    -> skip ;
STRING                :    '"'    (STRING_ESC|.)*?    '"'        ;
COMMA        :    ','                                ;
CHAR        :    '\''    .    '\''
            |    .                                // the rest of all
            ;

// fragments
fragment ID_LETTER    :    [a-zA-Z_]    ;
fragment DIGIT        :    [0-9]    ;
fragment STRING_ESC    :    '\\'    [btnr0"\\]    ; // \b, \t, \n etc...