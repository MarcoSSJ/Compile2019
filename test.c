
int testMulti(){
//    test(1,1,1);
    int i = 1;
    int j = i ++;
    int k = ++ i;
    int u = k --;
    int v = -- k;
    int w = -v;
    printf("%d%d%d%d%d%d",i,j,k,u,v,w);
    return 0;
}

int main(){
    for(int i = 1; i < 10; i++){
        printf("%d\n", i);
        i = i + 1;
    }

    testMulti();
    return 0;
}

