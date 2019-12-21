#include <stdio.h>
int main()
{
    int i, sum = 0;

    for ( i = 1; i <=10; i++ ) {
        sum += i;
    }
    int j = i;
    j *= 2;
    int k = i;
    k /= 2;
    int w = i;
    w %= 2;
    printf("sum = %d %d %d %d\n", sum,j,k,w);



    return 0;
}
