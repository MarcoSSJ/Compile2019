// chuchong 
// usage: using kmp to check whether a string is a substring of another
// only support string less than 50 letters
#include <stdio.h>
#define TRUE 1
#define FALSE 0
#define NOTSUBSTR -1
#define MAXSIZE 50
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
    }
    return;
}

void calNext(char s[], int next[]){
    int i = 0;//i to s
    int j = -1;//j to next
    int len;
    len = strLen(s);

    next[0] = -1;
    for(;i < len - 1;){
        if(j == -1 || s[i] == s[j]){
            i ++;
            j ++;
            if(s[i] != s[j])
                next[i] = j;
            else
                next[i] = next[j];
        }else{
            i = next[i];
        }
    }
}

int firstIndexOf(char s[], char substr[]){
    // NOTSUBSTR -1: failed
    int i = 0;
    int j = 0;
    int subLen = strLen(substr);
    int len = strLen(s);
    int next[MAXSIZE];
    calNext(substr, next);

    for(;j < len;){
        if (substr[i] == s[j]){
            i ++;
            j ++;
        }else{
            if(next[i] != -1){
                i = next[i];
                continue;
            }
            j ++;
        }

        if (substr[i] == 0){
            return (j - subLen);
        }
    }

    return NOTSUBSTR;
}

void testKmp(char s[], char substr[], int gt){
    printf("--new kmp test start:\n");
    int output = firstIndexOf(s, substr);
    assertTest(output, gt);
    return;
}

void unittest(){
    printf("*******kmp test*********\n");
    testKmp("aaabaaa", "baaa", 3);
    testKmp("a", "aa", NOTSUBSTR);
    testKmp("b", "a", NOTSUBSTR);
    testKmp("aaaa", "b", NOTSUBSTR);
    testKmp("aaaa", "aa", 0);
    return;
}

int main(){
    unittest();
    return 0;
}
