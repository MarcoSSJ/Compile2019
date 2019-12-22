
int strLen(char s[]){
    int i;
    for(i = 0; s[i]; i++);
    return i;
}
//
//int assertTest(int in, int gt){
//    if(in == gt){
//        printf("test success!\n");
//    }else{
//        printf("test failed!\n");
//    }
//    return 0;
//}

int calNext(char s[], int next[]){
    int i = 0;

    int j = -1;
    int len;
    //printf("0\n");
    len = strLen(s);
    //printf("1\n");
    next[0] = -1;
    //    printf("2\n");
    for(;i < len;){
    //        printf("3\n");
        if(j == -1 || s[i] == s[j]){
    //      printf("4\n");
            i ++;
     //       printf("5\n");
            j ++;
            next[i] = j;
     //       printf("6\n");
        }else{
            j = next[j];
     //       printf("7\n");
        }
      //              printf("8\n");
    }
    return 0;
}
//
//int firstIndexOf(char s[], char substr[]){
//    int i = 0;
//    int j = 0;
//    int subLen = strLen(substr);
//    int len = strLen(s);
//    int next[50];
//
//    for(int k = 0; k < subLen; k ++){
//        next[k] = 0;
//    }
//
//    calNext(substr, next);
//
//    for(int k = 0; k < subLen; k ++){
//        int val = next[k];
//        printf("next [] %d  = %d\n", k , next[k]);
//    }
//
//    for(;j < len;){
//        if (substr[i] == s[j]){
//            i ++;
//            j ++;
//        }else{
//            if(next[i] != -1){
//                i = next[i];
//            }else{
//                j ++;
//            }
//        }
//
//        if (substr[i] == 0){
//            return (j - subLen);
//        }
//    }
//
//    return -1;
//}

//int testKmp(char s[], char substr[], int gt){
//    printf("--new kmp test start:\n");
//    int output = firstIndexOf(s, substr);
//    assertTest(output, gt);
//    printf("expected %d got %d", gt, output);
//    return 0;
//}

//int unittest(){
//
////    printf("*******kmp test*********\n");
////    testKmp("aaababababababaaaaaa", "abababababaaa", 4);
////    testKmp("a", "aa", -1);
////    testKmp("b", "a", -1);
////    testKmp("aaaa", "b", -1);
////    testKmp("aaaa", "aa", 0);
//    return 0;
//}

int main(){
    char s[] = "123412341234";
    int len = strLen(s);
    printf("10\n");
    int next[50];
    printf("9\n");
    calNext(s, next);
    return 0;
}
