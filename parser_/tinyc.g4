
/*
主要参考
https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm
 */

grammar tinyc;
/*------------------------parser------------------------------*/
program //程序入口
   : (include)* translationUnit +
   ;

include //include文件 TODO:支持define预编译
   : '#include' '<' LIB '>'
   | '#include' '\'' LIB '\''
   ;

translationUnit //非头部文件
   : function
   | declaration
   ;

function //函数代码
   : typeSpecifier declarator compoundStatement
   ;

typeSpecifier //类别定义 TODO: 支持更多定义 支持static/const
    : 'int'
    | 'char'
    | 'void'
    ;

compoundStatement //函数中复合语句
   : '{' compoundUnit* '}'
   ;

compoundUnit//单元
   : declaration
   | statement
   ;

declaration // 定义语句
   : typeSpecifier initDeclaration ';'
   ;

initDeclaration //初始化部分
    : initDeclarator (',' initDeclarator)*
    ;

initDeclarator //初始化单元
    :   declarator
    ;

declarator //初始化单元具体内容
    :   IDENTIFIER
    |   IDENTIFIER '(' parameterTypeList? ')'
    ;

parameterTypeList //函数参数列表
   :  parameterList (',' '...')? ;

parameterList //函数参数列表具体内容
   :   parameterDeclaration (',' parameterDeclaration)* ;

parameterDeclaration //函数参数列表声明
   :   typeSpecifier declarator ;

statement //表达式,TODO: 暂时只支持函数和return和{}
   : '{' statement* '}'
   | ';'
   |  'return' expression ';' 
   | expression';'
   ;

expression //语句表达式
   : assignmentExpression (',' assignmentExpression)*
   ;

assignmentExpression //TODO:暂时只支持后缀表达式
   : postfixExpression
   ;

postfixExpression //() [] 为后缀的表达式,TODO:暂时只支持函数
   : primaryExpression
   | postfixExpression '(' assignmentExpression ')'
   ;

primaryExpression
   :  IDENTIFIER
   |  STRING
   |  CONSTANT
   ;

/*------------------------lexer------------------------------*/
IDENTIFIER
   :[a-zA-Z_]  (   [a-zA-Z_]  |   [0-9])*;


STRING
   : '"' CHARSEQ? '"' | '\'' CHAR '\''
   ;

CHARSEQ
   : CHAR+
   ;

CHAR //暂不支持多行
    :   ~["\\\r\n]
    |   '\\' ['"?abfnrtv0\\]
    ;

CONSTANT
   : [0-9] +
   ;

LIB : [a-zA-Z]+'.h'?;

/*------------------------注释------------------------------*/
Whitespace  :   [ \t]+  -> skip;

Newline  :   (   '\r' '\n'?   |   '\n')  -> skip;

BlockComment    :   '/*' .*? '*/'   -> skip;

LineComment   :   '//' ~[\r\n]*   -> skip;
