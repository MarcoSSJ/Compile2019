<<<<<<< Updated upstream
// chuchong 
// usage: using kmp to check whether a string is a substring of another
// only support string less than 50 letters
=======
>>>>>>> Stashed changes
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
    int i = 0;
    int j = -1;
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
    return;
}

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
<<<<<<< Updated upstream
=======
        int val = next[k];
>>>>>>> Stashed changes
        printf("next [] %d  = %d\n", k , next[k]);
    }

    for(;j < len;){
        if (substr[i] == s[j]){
            i ++;
            j ++;
        }else{
            if(next[i] != -1){
                i = next[i];
//                continue;
            }
            j ++;
        }

        if (substr[i] == 0){
            return (j - subLen);
        }
    }

    return -1;
}

void testKmp(char s[], char substr[], int gt){
    printf("--new kmp test start:\n");
    int output = firstIndexOf(s, substr);
    assertTest(output, gt);
<<<<<<< Updated upstream
=======
    printf("%d expected %d got %d", gt, output);
>>>>>>> Stashed changes
    return;
}

void unittest(){
    printf("*******kmp test*********\n");
    testKmp("aaabaaa", "baaa", 3);
    testKmp("a", "aa", -1);
<<<<<<< Updated upstream
    testKmp("b", "a", -1);
=======
    testKmp("b", "a",  -1);
>>>>>>> Stashed changes
    testKmp("aaaa", "b", -1);
    testKmp("aaaa", "aa", 0);
    return;
}

int main(){
    unittest();
    return 0;
}
