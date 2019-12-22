#include <stdio.h>
#define ADD(a,b) a+b
#define SUB(a,b) a-b
#define TRUE 1
#define FALSE 0

int main(){
    printf("ADD(1,2) = %d\n", ADD(1,2));
    printf("SUB(5,2) = %d\n", SUB(5,2));
    printf("TRUE = %d FALSE = %d\n", TRUE, FALSE);

    return 0;
}
