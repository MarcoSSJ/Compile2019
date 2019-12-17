#include <stdio.h>
#include <stdlib.h>
struct Node {
    struct Node * next;
    int value;
};

int main(){
    struct Node node;
    node.value = 0;
    struct Node * cur = &node;
    for(int i = 1; i <= 10; i ++){
        struct Node* node = malloc(sizeof (struct Node));
        node->value = i;
        node->next = 0;
        cur->next = node;
        cur = node;
    }

    cur = &node;
    while(cur){
        printf("%d ", cur->value);
        cur = cur->next;
    }
    return 0;
}