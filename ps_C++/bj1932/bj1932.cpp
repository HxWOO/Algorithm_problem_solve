#include<iostream>
#include<vector>
using namespace std;

int tr[500][500];
int n;
int dp[500][500];

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=n-1;i>=0;i--){
        int num;
        for(int j=0;j<n-i;j++){
            cin>>num;
            tr[i][j] = num;
        }
    } //거꾸로 받기

    for(int i=0;i<n;i++) dp[0][i] = tr[0][i];

    for(int i=1;i<n;i++){
        for(int j=0;j<n-i;j++){
            dp[i][j] = ( dp[i-1][j] > dp[i-1][j+1] ) ? dp[i-1][j] + tr[i][j] : dp[i-1][j+1] + tr[i][j];
        }
    }

    cout<< dp[n-1][0] << '\n';

    return 0;
}
