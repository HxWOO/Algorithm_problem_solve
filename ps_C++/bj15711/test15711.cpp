#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
typedef long long ll;
const int PN = 2000000;
bool isprime[PN + 5];
vector<int> prime;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	for (ll i = 2; i <= PN; i++) isprime[i] = true;
	for (ll i = 2; i <= PN; i++)
		if (isprime[i])
			for (ll j = i * i; j <= PN; j += i) {
				isprime[j] = false;
			}

	for (int i = 2; i <= PN; i++) {
		if (isprime[i]) prime.push_back(i);
	}

	int tc;
	cin >> tc;
	for (int i = 0; i < tc; i++) {
		ll a, b;
		cin >> a >> b;
		ll S = a + b;
		if (S % 2 == 0) {
			if (S == 2) {
				cout << "NO\n";
			}
			else {
				cout << "YES\n";
			}
		}
		else {
			bool check = true;
			S -= 2;
			if (S <= PN) {
				if (isprime[S]) cout << "YES\n";
				else cout << "NO\n";
			}
			else {
				for (int j = 0; j < prime.size(); j++) {
					if (S % prime[j]==0) {
						check = false;
						break;
					}
				}
				if (check) cout << "YES\n";
				else cout << "NO\n";
			}
		}
	}
}