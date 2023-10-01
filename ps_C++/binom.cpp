#include<iostream>
#include<vector>

using namespace std;

int n,k;
int dp[1000][1000];

bool bnd(int a){
    if(a<0 || a>n) return false;
    return true;
}

void binom(int a){
    dp[a][a] = 1;
    dp[0][a] = 1;

    for(int j=1;j<a+1;j++){
        dp[j][a] = dp[j][a-1] + dp[j-1][a-1];
    }
}


int main(){
    cin>>n>>k;

    for(int i=1;i<n+1;i++){
        binom(i);
    }


    cout<<dp[k][k];
}