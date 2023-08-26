#include <stdio.h>
 
int main()
{
    int n, x, y;;
    scanf("%d", &n);
    int maxx = -10000, minx = 10000; // 각 좌표의 범위 끝 값
    int maxy = -10000, miny = 10000; // x, y의 최대, 최소 값을 위해 두 개 선언
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &x, &y);
        if (x >= maxx) maxx = x;
        if (x < minx) minx = x;
        if (y >= maxy) maxy = y;
        if (y < miny) miny = y;
    }
    printf("%d", (maxx - minx) * (maxy - miny));
 
    return 0;
}
