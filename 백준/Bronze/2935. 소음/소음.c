#include<stdio.h>
#include<string.h>
int main()
{
    int i;
    char arr[105];
    char op;
    char arr2[105];
    char arr3[105];
    scanf("%s", arr);
    getchar();
    scanf("%c", &op);
    getchar();
    scanf("%s", arr2);
    getchar();
    if (op == '+')
    {
        if (strlen(arr) >= strlen(arr2))
        {
            strcpy(arr3, arr);
            arr3[strlen(arr) - strlen(arr2)] += 1;
        }
        else
        {
            strcpy(arr3, arr2);
            arr3[strlen(arr2) - strlen(arr)] += 1;
        }
        printf("%s", arr3);
    }
    else
    {
        printf("1");
        for (i = 0; i < strlen(arr)+strlen(arr2) -2; i++)
        {
            printf("0");
        }
    }
}