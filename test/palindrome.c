// chuchong 
// usage: to check thether a string is palindrome 
#include <stdio.h>
#define TRUE 1
#define FALSE 0

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
            return FALSE;
    }
    return TRUE;
}

void assertTest(int in, int gt){
    if(in == gt){
        printf("test success!\n");
    }else{
        printf("test failed!\n");
    }
}

void testPalindrome(char s[], int gt){
    printf("--new palindrome test start:\n");
    int output = isPalindrome(s);
    assertTest(output, gt);
}

void unittest(){
    printf("*******palindrome test*********\n");
    testPalindrome("", TRUE);
    testPalindrome("a", TRUE);
    testPalindrome("aa", TRUE);
    testPalindrome("ab", FALSE);
    testPalindrome("aaaaaaaaa", TRUE);
    testPalindrome("aaaabaaaa", TRUE);
    testPalindrome("aaabaaaa", FALSE);
}

int main(){
    unittest();
    return 0;
}