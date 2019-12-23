#include <stdio.h>
#define ADD(a,b) a+b
#define SUB(a,b) a-b
#define TRUE 1
#define FALSE 0
#define repeat(R) for(int i = 1; i < 10; i = i + 1) R;

int main(){
    printf("ADD(1,2) = %d\n", ADD(1,2));
    printf("SUB(5,2) = %d\n", SUB(5,2));
    printf("TRUE = %d FALSE = %d\n", TRUE, FALSE);
    repeat(printf("hello world.\n"));

    return 0;
}
