
/*
https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm
 */

grammar tinyc;
/*------------------------parser------------------------------*/
program //程序入口
   : (include)* translationUnit+ EOF
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
   : typeSpecifier declarator compoundStatement //TODO:应该有declaration
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
    |   declarator '=' initializer
    ;

initializer //TODO:支持数组初始化
    :   assignmentExpression
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
   : compoundStatement
   |  returnStatement
   | expressionStatement
   | iterationStatement
   ;

returnStatement
    :  'return' expression? ';'
    ;

expressionStatement
    : expression? ';'
    ;

iterationStatement
    : 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'for' '(' declaration expression? ';' expression? ')' statement
    ;

expression //语句表达式
   : assignmentExpression (',' assignmentExpression)*
   ;

assignmentExpression //TODO:暂时只支持后缀表达式,表示一个值
   : conditionalExpression
   | postfixExpression assignmentOperator assignmentExpression   
   ;

postfixExpression //() [] 为后缀的表达式,TODO:暂时只支持函数,只支持接收一个函数参数值
   : primaryExpression
   | postfixExpression '++'
   | postfixExpression '--'
   | postfixExpression '(' argumentExpressionList? ')'
   ;

argumentExpressionList
    : assignmentExpression
    | argumentExpressionList ',' assignmentExpression
    ;

unaryExpression
    :   postfixExpression
    |   '++' unaryExpression
    |   '--' unaryExpression
    |   unaryOperator unaryExpression
    ;

multiplicativeExpression
    :   unaryExpression
    |   multiplicativeExpression '*' postfixExpression
    |   multiplicativeExpression '/' postfixExpression
    |   multiplicativeExpression '%' postfixExpression
    ;

additiveExpression
    :   multiplicativeExpression
    |   additiveExpression '+' multiplicativeExpression
    |   additiveExpression '-' multiplicativeExpression
    ;

shiftExpression
    :   additiveExpression
    |   shiftExpression '<<' additiveExpression
    |   shiftExpression '>>' additiveExpression
    ;

relationalExpression
    :   shiftExpression
    |   relationalExpression '<' shiftExpression
    |   relationalExpression '>' shiftExpression
    |   relationalExpression '<=' shiftExpression
    |   relationalExpression '>=' shiftExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression '==' relationalExpression
    |   equalityExpression '!=' relationalExpression
    ;

andExpression
    :   equalityExpression
    |   andExpression '&' equalityExpression
    ;

exclusiveOrExpression
    :   andExpression
    |   exclusiveOrExpression '^' andExpression
    ;

inclusiveOrExpression
    :   exclusiveOrExpression
    |   inclusiveOrExpression '|' exclusiveOrExpression
    ;

logicalAndExpression
    :   inclusiveOrExpression
    |   logicalAndExpression '&&' inclusiveOrExpression
    ;

logicalOrExpression
    :   logicalAndExpression
    |   logicalOrExpression '||' logicalAndExpression
    ;

conditionalExpression
    :   logicalOrExpression ('?' expression ':' conditionalExpression)?
    ;

assignmentOperator
    :   '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    ;

unaryOperator
    :   '+' | '-' | '~' | '!'
    ;

primaryExpression
   :  IDENTIFIER
   |  mString
   |  CONSTANT
   ;

/*------------------------lexer------------------------------*/
IDENTIFIER
   :[a-zA-Z_]  (   [a-zA-Z_]  |   [0-9])*;

mString
    :STRING
    ;

STRING
   : '"' CHARSEQ? '"' | '\'' CHAR '\''
   ;

fragment //WARNING!: 这里必须式fragment 否则由于
//https://stackoverflow.com/questions/29777778/antlr-4-5-mismatched-input-x-expecting-x
//https://stackoverflow.com/questions/17715217/antlr4-mismatched-input
//所述错误识别
CHARSEQ
   : CHAR+
   ;

fragment
CHAR //暂不支持多行
    :   ~["\\\r\n]
    |   '\\' ['"?abfnrtv0\\]
    ;

CONSTANT
   : [0-9]+
   ;

LIB : [a-zA-Z]+'.h'?;

/*------------------------注释------------------------------*/
//Whitespace  :(' ' | '\t')+  -> skip;
//
//Newline  :(   '\r' '\n'?   |   '\n')  -> skip;

BlockComment    :'/*' .*? '*/'   -> skip;

LineComment   :'//' ~[\r\n]*   -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines