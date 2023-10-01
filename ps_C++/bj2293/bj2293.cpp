#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n, k;
vector<int> coin;
int dp[10001];
int x;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n>>k;
    for(int i=1;i<n+1;i++){
        int num; cin>>num;
        coin.push_back(num);
    }
    sort(coin.begin(),coin.end());
    dp[0] = 1;
    
    
    for(int i=0;i<n;i++){
        for(int j=coin[i];j<=k;j++){
            dp[j] += dp[j-coin[i]];
        }
    }
    cout<<dp[k]<<'\n';


    return 0;
}
