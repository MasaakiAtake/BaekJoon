#include <stdio.h>

int main(){
    int cut, piece = 1, a = 1, i;
    scanf("%d", &cut);
    for(i = 0; i < cut; i++){
        if(i%2 != 0){
            a += 1;
        }
        piece += a;
    }
    printf("%d", piece);
    return 0;
}