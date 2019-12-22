//// chuchong
//// usage: monitor a calculator
//// do not support monocular operator such as -1
//// using two stack
#include <stdio.h>
//#define TRUE 1
//#define FALSE 0
//#define MAXSIZE 100
//
//char priTable[7][7]={
//    /*			+	-	*	/	(	)	\0	*/
//    /*  +  */	{'>','>','<','<','<','>','>'},
//    /* -  */	{'>','>','<','<','<','>','>'},
//    /* *  */	{'>','>','>','>','<','>','>'},
//    /* /  */	{'>','>','>','>','<','>','>'},
//    /* (  */	{'<','<','<','<','<','=',' '},
//    /* )  */	{' ',' ',' ',' ',' ',' ',' '},
//    /*  \0 */	{'<','<','<','<','<',' ','='}
//};
//
//int op2pri(char op){
//    switch(op){
//        case '+': return 0; break;
//        case '-': return 1; break;
//        case '*': return 2; break;
//        case '/': return 3; break;
//        case '(': return 4; break;
//        case ')': return 5; break;
//        case '\0': return 6; break;
//        default: return -1; break;
//    };
//}
//
//int strLen(char s[]){
//    int i;
//    for(i = 0; s[i]; i++);
//    return i;
//}
//
void assertTest(int in, int gt){
    if(in == gt){
        printf("test success!\n");
    }else{
        printf("test failed!\n");
        printf("expected %d but get %d\n",gt,in);
    }
}

int cal(int le, char op, int ri){
    printf("cal: le=%d, op=%c, ri=%d\n", le, op, ri);
    switch(op){
        case '+':
            return le + ri;
            break;
        case '-':
            return le - ri;
            break;
        case '*':
            return le * ri;
            break;
        case '/':
            return le / ri;
            break;
    };
}

//int eval(char s[]){
//    int opSt[MAXSIZE];
//    int valSt[MAXSIZE];
//    int opSize = 0;
//    int valSize = 0;
//    int len = strLen(s);
//    int i = 0;
//    char op;
//    int ri, le;
//    int ans;
//    char cmp;
//    opSt[opSize ++] = '\0';
//    while(opSize && i <= len){
//        if(isDigit(s[i])){
//            valSt[valSize++] = s[i] - '0';
//            while(isDigit(s[++i])){
//                valSt[valSize - 1] = valSt[valSize - 1] * 10 + s[i] - '0';
//            }
//        }else{
//            cmp = priTable[op2pri(opSt[opSize - 1])][op2pri(s[i])];
//            switch(cmp){
//                case '>':
//                    op = opSt[--opSize];
//                    ri = valSt[--valSize];
//                    le = valSt[--valSize];
//                    valSt[valSize ++] = cal(le, op, ri);
//                    break;
//                case '<':
//                    opSt[opSize++] = s[i];
//                    i ++;
//                    break;
//                case '=':
//                    opSize --;
//                    i ++;
//                    break;
//                default:
//                    break;
//            };
//        }
//    }
//    ans = valSt[--valSize];
//    if(! valSize){
//        // 异常处理
//        return ans;
//    }
//    return ans;
//}

#include <stdio.h>

int strLen(char ch[])
{
	int i;
	for (i = 0; ch[i]; i++);
	return i;
}

int check_left(char x)
{
	int p = 0;
	if (x == '*' || x == '/')
		p = 5;
	else if (x == '+' || x == '-')
		p = 4;
	else if (x== ')')
		p = 6;
	else if (x== '(')
		p = 2 ;
	return p;
}
int check_right(char x)
{
	int p = 1;
	if (x == '*' || x == '/')
		p = 5;
	else if (x == '+' || x == '-')
		p = 4;
	else if (x== ')')
		p = 2;
	else if (x== '(')
		p = 6;
	return p;
}
int eval(char input[])
{
    printf("%s", input);
	int len = strLen(input);
	int val_stack[50];
	int val_stack_index = 0;
	int op_stack[50];
	int op_stack_index = 0;
//	op_stack[op_stack_index++] = '#';
    int i;
	for (i = 0; i <= len; i++)
	{
	    // 处理数字情况
	    printf("i:%d %c\n", i, input[i]);
		if (input[i] >= '0' && input[i] <= '9') {
		    int val = input[i] - '0';
		    while (1) {
		        i++;
                if (input[i] >= '0' && input[i] <= '9'){
                    int single_val = input[i] - '0';
                    val = val * 10 + single_val;
                }
                else {
                    i--;
                    break;
               }
		    };
		    val_stack[val_stack_index++] = val;
		    printf("val=%d val_index=%d\n", val, val_stack_index);
		}
		else
		{
		    int check_le = check_left(op_stack[op_stack_index-1]);
		    int check_ri = check_right(input[i]);
		    printf("le=%d, %c, ri=%d %c op_index=%d\n", check_le,op_stack[op_stack_index-1] ,check_ri, input[i],op_stack_index);
			if (check_le < check_ri)
			{
			    op_stack[op_stack_index] = input[i];
			    op_stack_index++;
			    printf("afetr add op_index=%d\n", op_stack_index);
			}
			else if (check_le >= check_ri) {
			    int val_ri = val_stack[--val_stack_index];
			    int val_le = val_stack[--val_stack_index];
			    printf("-===%d  %c\n", op_stack_index, op_stack[op_stack_index]);
//			    op_stack_index--;
                int val_cal = cal(val_le, op_stack[op_stack_index-1], val_ri);
                op_stack_index--;
                printf("---%d %c\n", op_stack_index, op_stack[op_stack_index]);

//                op_stack_index--;
                printf("opstackindex=%c %c %d", op_stack[op_stack_index], input[i], op_stack_index);
                if (op_stack[op_stack_index-1] == '(' && input[i] == ')')  op_stack_index--;
                else i--;
                printf("ri=%d, le=%d, %val_cal=%d val_index=%d\n", val_ri, val_le, val_cal);
                val_stack[val_stack_index++] = val_cal;
			};
		}
	}
	return val_stack[val_stack_index-1];
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
    testCal("2*3+4", 10);
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