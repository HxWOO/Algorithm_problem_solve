#include<iostream>

using namespace std;

int dp[1001];
int n;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    dp[1] = 1; dp[2] = 2;

    for(int i=3;i<=n;i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 10007; //수가 커져서 이렇게 저장
    }

    cout<<dp[n]<<'\n';

    return 0;
}
