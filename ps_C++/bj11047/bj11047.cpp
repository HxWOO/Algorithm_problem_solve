#include<iostream>

using namespace std;

int n, k;
int coin[11];
int cnt = 0;


int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n>>k;

    for(int i=1;i<n+1;i++) cin>>coin[i];

    while(k){
        for(int i=n;i>0;i--){
            if(coin[i]<=k){
                k -= coin[i];
                cnt++;
                i++;
            }
        }
    }

    cout<<cnt<<'\n';

    return 0;
}
