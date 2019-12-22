
// chuchong
// usage: using kmp to check whether a string is a substring of another
// only support string less than 50 letters
//
int strLen(char s[]){
    int i;
    for(i = 0; s[i]; i++);
    return i;
}
//
int assertTest(int in, int gt){
    if(in == gt){
        printf("test success!\n");
    }else{
        printf("test failed!\n");
    }
    return 0;
}

int calNext(char s[], int next[]){
    int i = 0;
    int j = -1;
    int len;
    len = strLen(s);

    next[0] = -1;
    for(;i < len;){
        if(j == -1 || s[i] == s[j]){
            i ++;
            j ++;
            next[i] = j;
        }else{
            j = next[j];
        }
    }
    return 0;
}
//
int firstIndexOf(char s[], char substr[]){
    int i = 0;
    int j = 0;
    int subLen = strLen(substr);
    int len = strLen(s);
    int next[50];

    for(int k = 0; k < subLen; k ++){
        next[k] = 0;
    }

    calNext(substr, next);

    for(int k = 0; k < subLen; k ++){
        int val = next[k];
        printf("next [] %d  = %d\n", k , next[k]);
    }

    for(;j < len;){
        if (substr[i] == s[j]){
            i ++;
            j ++;
        }else{
            if(next[i] != -1){
                i = next[i];
            }else{
                j ++;
            }
        }

        if (substr[i] == 0){
            return (j - subLen);
        }
    }

    return -1;
}

int testKmp(char s[], char substr[], int gt){
    printf("--new kmp test start:\n");
    int output = firstIndexOf(s, substr);
    assertTest(output, gt);
    printf("expected %d got %d", gt, output);
    return 0;
}

int unittest(){
    char s[] = "123412341234";
    int len = strLen(s);
    int next[50];
    calNext(s, next)
    printf("*******kmp test*********\n");
    testKmp("aaababababababaaaaaa", "abababababaaa", 4);
    testKmp("a", "aa", -1);
    testKmp("b", "a", -1);
    testKmp("aaaa", "b", -1);
    testKmp("aaaa", "aa", 0);
    return 0;
}

int main(){
    unittest();
    return 0;
}
