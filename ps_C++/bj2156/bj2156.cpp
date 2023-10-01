#include<iostream>
using namespace std;

int arr[10001];
int dp[10001];
int n;

int max(int a, int b){
    if(a>b) return a;
    else return b;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin>>n;
    for(int i=1;i<n+1;i++){
        cin>>arr[i];
    }
    dp[1] = arr[1];
    dp[2] = max(arr[1], arr[1] + arr[2]);
    
    for(int i=3;i<n+1;i++){
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i]);
        if(dp[i]<dp[i-1]) dp[i] = dp[i-1];
    }

    cout<<dp[n]<<'\n';

    return 0;
}
