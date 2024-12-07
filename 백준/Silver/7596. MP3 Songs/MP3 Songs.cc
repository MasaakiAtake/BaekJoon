#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> vec;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T = 0;
	string s; getline(cin, s);
	int N = stoi(s);
	while (N) {
		T++; cout << T << '\n';
		vec.clear();
		while (N--) {
			getline(cin, s);
			vec.push_back(s);
		}
		sort(vec.begin(), vec.end());
		for (auto ss : vec) cout << ss << '\n';
		getline(cin, s);
		N = stoi(s);
	}
}