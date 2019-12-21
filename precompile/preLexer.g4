lexer grammar preLexer;
// lexer rules must start with upper case.
//@lexer::members {
//    public const int CHANNEL_COMMENT_BLOCK = 1;
//    public const int CHANNEL_COMMENT_LINE = 2;
//    protected const int EOF = Eof;
//    protected const int HIDDEN = Hidden;
//}

//=======================================================================
COMMENT_BLOCK        :    '/*'    .*?        '*/'            -> skip;
COMMENT_LINE        :    '//'    NOT_NL*                    -> skip ;
NL_ESC                :    '\\'    NL                        -> skip ;
STRING                :    '"'    (STRING_ESC|.)*?    '"'        ;
WS                    :    ' '    |    '\t'                    ;    // preprocessor cannot "skip" white space, because wb matters in several cases.
NEWLINE                :    NL                                ;    // preprocessor cannot "skip" new line, because wb matters in several cases.
PREPROCESS_BEGIN    :    '#'                                ;

//=======================================================================
// nmode doesn't seem to work for C#
// mode preprocessMode;
//=======================================================================
PREPROCESS_INCLUDE    :    'include'    ;
PREPROCESS_DEFINE    :    'define'    ;
PREPROCESS_UNDEF    :    'undef'        ;
PREPROCESS_IFDEF    :    'ifdef'        ;    // this must appear before 'if'
PREPROCESS_IFNDEF    :    'ifndef'    ;    // this must appear before 'if'
//PREPROCESS_IF        :    'if'        ;
//PREPROCESS_ELSE        :    'else'        ;
//PREPROCESS_ELIF        :    'elif'        ;
//PREPROCESS_ENDIF    :    'endif'        ;
PREPROCESS_PRAGMA    :    'pragma'    ;
PREPROCESS_ERROR    :    'error'        ;

//=======================================================================
// These must be below reserved keywords
//=======================================================================
DEFINED        :    'defined'    ;
ID            :    ID_LETTER    (ID_LETTER|DIGIT)*    ;
COMMA        :    ','                                ;
PAREN_OPEN    :    '('                                ;
PAREN_CLOSE    :    ')'                                ;
CHAR        :    '\''    .    '\''
            |    .                                // the rest of all
            ;

//=======================================================================
// fragment can be referenced only by lexer.
// fragment itself is not lexer rule so that it cannot be used by parser.
//=======================================================================
fragment ID_LETTER    :    [a-zA-Z_]            ;
fragment DIGIT        :    [0-9]                ;
fragment STRING_ESC    :    '\\'    [btnr0"\\]    ; // \b, \t, \n etc...
fragment NL            :    '\r'?    '\n'        ;
fragment NOT_NL        :    ~[\r\n]                ;