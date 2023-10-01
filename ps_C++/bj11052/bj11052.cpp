#include<iostream>

using namespace std;

int n;
int p[1001];
int dp[1001];

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=1;i<n+1;i++) cin>>p[i];
    dp[1] = p[1];
    for(int i=2;i<n+1;i++){
        int max = 0;
        for(int j=i;j>0;j--){
            if(max<dp[i-j]+p[j]) max = dp[i-j] + p[j];
        }
        dp[i] = max;
    }
    
    cout<<dp[n]<<'\n';

    return 0;
}
