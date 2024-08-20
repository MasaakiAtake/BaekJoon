#include <iostream>
#include <string>
using namespace std;
 
char alpa[26];
//A = 65
int main() {
    int t;
    string n;
    string rule;
    cin >> t;
 
    getline(cin, n);
    while (t--) {
        getline(cin, n);
        cin >> rule;
 
        for (int i = 0; i < rule.size(); i++) {
            alpa[i] = rule[i];
        }
 
        for (int i = 0; i < n.size(); i++) {
            if (n[i] == ' ') {
                cout << ' ';
            }
            else {
                cout << alpa[n[i] - 65];
            }
        }
        cout << '\n';
        getline(cin, n);
    }
}
