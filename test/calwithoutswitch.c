// chuchong
// usage: monitor a calculator
// do not support monocular operator such as -1
// using two stack
#include <stdio.h>
#define TRUE 1
#define FALSE 0
#define MAXSIZE 100

char priTable[7][7]={
    /*			+	-	*	/	(	)	\0	*/
    /*  +  */	{'>','>','<','<','<','>','>'},
    /* -  */	{'>','>','<','<','<','>','>'},
    /* *  */	{'>','>','>','>','<','>','>'},
    /* /  */	{'>','>','>','>','<','>','>'},
    /* (  */	{'<','<','<','<','<','=',' '},
    /* )  */	{' ',' ',' ',' ',' ',' ',' '},
    /*  \0 */	{'<','<','<','<','<',' ','='}
};

int op2pri(char op){
    if(op == '+')
        return 0;
    if(op == '-')
        return 1;
    if(op == '*')
        return 2;
    if(op == '/')
        return 3;
    if(op == '(')
        return 4;
    if(op == ')')
        return 5;
    if(op == '\0')
        return 6;
    return -1;
}

int strLen(char s[]){
    int i;
    for(i = 0; s[i]; i++);
    return i;
}

void assertTest(int in, int gt){
    if(in == gt){
        printf("test success!\n");
    }else{
        printf("test failed!\n");
        printf("expected %d but get %d\n",gt,in);
    }
}

int cal(int le, char op, int ri){
    if (op == '+')
        return le + ri;
    if (op == '-')
        return le - ri;
    if (op == '*')
        return le * ri;
    if (op == '/')
        return le / ri;
}

int isDigit(char c){
    return (c <= '9') && (c >= '0');
}

int eval(char s[]){
    int opSt[MAXSIZE];
    int valSt[MAXSIZE];
    int opSize = 0;
    int valSize = 0;
    int len = strLen(s);
    int i = 0;
    char op;
    int ri, le;
    int ans;
    char cmp;
    opSt[opSize ++] = '\0';
    while(opSize && i <= len){
        if(isDigit(s[i])){
            valSt[valSize++] = s[i] - '0';
            while(isDigit(s[++i])){
                valSt[valSize - 1] = valSt[valSize - 1] * 10 + s[i] - '0';
            }
        }else{
            cmp = priTable[op2pri(opSt[opSize - 1])][op2pri(s[i])];
            if(cmp == '>'){
                op = opSt[--opSize];
                ri = valSt[--valSize];
                le = valSt[--valSize];
                valSt[valSize ++] = cal(le, op, ri);
            }else if(cmp == '<'){
                opSt[opSize++] = s[i];
                i ++;
            }else if(cmp == '='){
               opSize --;
                i ++;
            }
        }
    }
    ans = valSt[--valSize];
    if(! valSize){
        // 异常处理
        return ans;
    }
    return ans;
}

void testCal(char s[], int gt){
    printf("--new calculator test start:\n");
    int output = eval(s);
    assertTest(output, gt);
}

void unittest(){
    printf("*******calculator test*********\n");
    testCal("1", 1);
    testCal("1+2", 3);
    testCal("3*4", 12);
    testCal("2*(3*4)", 24);
    testCal("1+(2*3+4)", 11);
    testCal("1/2",0);
    testCal("1*2*3*4*5/6",20);
    testCal("1-2",-1);
    int complex = 123/(24+(26/6)*32/(4+1)-20);
    testCal("123/(24+(26/6)*32/(4+1)-20)", complex);
}

int main(){
    unittest();
    return 0;
}