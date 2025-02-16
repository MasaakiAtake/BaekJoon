#include <iostream>
using namespace std;
int P3, P4, P0, T3, T4;
int main()
{
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> P3 >> P4 >> P0;

    for (int i = 0; i <= P0; ++i)
    {
        if (((P3 + i) % 3 == 0) && ((P4 + P0 - i) % 4 == 0))
        {
            cout << ((P3 + i) / 3) << " " << ((P4 + P0 - i) / 4);
            return 0;
        }
    }

    cout << -1;
    return 0;
}