#include<iostream>

using namespace std;

int n;
int c[1000][3]; //0은 빨, 1은 초, 2는 파
int dp[1000][3]; //0은 빨강으로 끝날때 최소값, 1은 초록, 2는 파랑 ...

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            cin>>c[i][j];
        }
    }
    for(int i=0;i<3;i++) dp[0][i] = c[0][i];

    for(int i=0;i<n;i++){
        for(int j=0;j<3;j++){
            if(j==0){
                dp[i][j] = (dp[i-1][1] > dp[i-1][2]) ? dp[i-1][2] + c[i][0] : dp[i-1][1] + c[i][0];
            }
            else if(j==1){
                dp[i][j] = (dp[i-1][0] > dp[i-1][2]) ? dp[i-1][2] + c[i][1] : dp[i-1][0] + c[i][1];
            }
            else{
                dp[i][j] = (dp[i-1][0] > dp[i-1][1]) ? dp[i-1][1] + c[i][2] : dp[i-1][0] + c[i][2];
            }
        }
    }
    int x = (dp[n-1][0] < dp[n-1][1]) ? (dp[n-1][0]>dp[n-1][2])?dp[n-1][2]:dp[n-1][0] : (dp[n-1][1]>dp[n-1][2])?dp[n-1][2]:dp[n-1][1];
    cout<<x<<'\n';

    return 0;
}
