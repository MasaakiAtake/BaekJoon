// woohyeon.kim
// kim519620.tistory.com
#include <iostream>
using namespace std;
int main(){
    ios::sync_with_stdio(false), cin.tie(NULL);
    register int N, ans = 0;
    char arr1[100001], arr2[100001];
    cin >> N;
    cin >> arr1 >> arr2;
    for(register int n = 0; n < N; ++n)
        if(arr1[n] != arr2[n])
            ++ans;
    cout << ans;
    return 0;
}
// *&)*@*