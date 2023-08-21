#include <stdio.h>

int a, x, y;
int maxi = -1;

int main() {
    for (int i = 1; i <= 9; i++) {
        for (int k = 1; k <=9; k++) {
            scanf("%d", &a);
            
            if (maxi <= a) {
                maxi = a;
                x = i;
                y = k;
            }
        }
    }
    
    printf("%d \n%d %d", maxi, x, y);
    
    return 0;
}