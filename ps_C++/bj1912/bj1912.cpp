#include<iostream>

using namespace std;

int n;
int nums[100000];
int dp[100000];

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n;i++) cin>>nums[i];

    dp[0] = nums[0];

    for(int i=0;i<n;i++){
        if(dp[i-1]>0){
            dp[i] = dp[i-1] + nums[i];
        }
        else{
            dp[i] = nums[i];
        }
    }
    int max= -1001;
    for(int i=0;i<n;i++){
        if(max<dp[i]) max = dp[i];
    }
    cout<<max<<'\n';

    return 0;
}