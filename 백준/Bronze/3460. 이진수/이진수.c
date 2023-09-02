#include<stdio.h>
int main()
{
    int t, n;
    scanf("%d", &t);
    
    for(int k = 0; k < t; k++){
        scanf("%d", &n);
        
        int i = 0;
        int num[100000] = { 0, };
        
        while(n >= 1){
            num[i] = n % 2;
            n = n / 2;
            
            i++;
        }
        if(n == 1){
            num[i] = 1;
        }
        for (int j = 0; j <= i; j++){
            if(num[j] == 1){
                printf("%d ", j);
            }
        }
    }
    return 0;
}