#include<stdio.h>

int main(void){
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);
    int count = z - y > y - x ? z - y : y - x;
    printf("%d", count - 1);
}