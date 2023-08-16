#include <stdio.h>

int main(){
    int a, b, c, d;
    scanf("%d %d", &a, &b);
    if(a < b)
        printf("-1");
    else{
        c = (a+b)/2;
        d= (a-b)/2;
        if(c+d == a && c-d == b)
            printf("%d %d", c, d);
        else
            printf("-1");
    }
    return 0;
}