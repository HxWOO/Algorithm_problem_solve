#include<iostream>

using namespace std;

int n;
int a[1001];
int dp[1001];


int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=1;i<n+1;i++) cin>>a[i];

    int max = 0;
    for(int i=1;i<n+1;i++){
        dp[i] = 1;
        for(int j=i-1;j>0;j--){
            if(a[i] > a[i-j]){
                if(dp[i]<dp[i-j]+1){
                    dp[i] = dp[i-j]+1;
                }
            }
        }
        if(max<dp[i]) max = dp[i];
    }

    cout<<max<<'\n';

    return 0;
}
