#include <iostream>
using namespace std;
bool isVisited[577397];
int N, A;
int main()
{
    ios::sync_with_stdio(0), cin.tie(0);

    cin >> N;

    for (int i = 1; i <= N; ++i)
    {
        isVisited[A] = true;
        int nextA = A - i;

        if (nextA < 0 || isVisited[nextA])
        {
            nextA = A + i;
        }

        A = nextA;
    }

    cout << A;
    return 0;
}