// chuchong 
// usage: to check thether a string is palindrome

int strLen(char s[]){
    int i;
    for(i = 0; s[i]; i++);
    return i;
}

int isPalindrome(char s[]){
    int len;
    int i;
    len = strLen(s);
    for(i = 0; i < len; i ++){
        if(s[i] != s[len - i - 1])
            return 0;
    }
    return 1;
}

void assertTest(int in, int gt){
    if(in == gt){
        printf("test success!\n");
    }else{
        printf("test failed!\n");
    }
    return;
}

void testPalindrome(char s[], int gt){
    printf("--new palindrome test start:\n");
    int output = isPalindrome(s);
    assertTest(output, gt);
    return;
}

void unittest(){
//    printf("*******palindrome test*********\n");
    testPalindrome("", 1);
//    testPalindrome("a", 1);
//    testPalindrome("aa", 1);
//    testPalindrome("ab", 0);
//    testPalindrome("aaaaaaaaa", 1);
//    testPalindrome("aaaabaaaa", 1);
//    testPalindrome("aaabaaaa", 0);
    return;
}

int main(){
    unittest();
    return 0;
}