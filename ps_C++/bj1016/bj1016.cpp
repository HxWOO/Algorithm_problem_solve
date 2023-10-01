#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

typedef long long ll;
#define MT 1000000

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    ll min, max;
    int num=0;
    vector<bool> sqn(MT+1,true);
    vector<ll> v;
    sqn[0] = false; sqn[1]=false;

    cin>>min>>max;
    num = max-min+1;
    for(int i=0;i<=1000;i++){
        if(sqn[i]){
            for(int k=i*i;k<=MT;k+=i){
                sqn[k]=false;
            }
        }
    }
    for(int i=2;i<=MT;i++){
        if(sqn[i]){
            ll n = i*i;
            v.push_back(n);
        }
    }
    
    for(int i=0;i<=max-min;i++){
        for(int k=0;min+i>=v[k];k++){
                if((min+i)%v[k]==0){
                num--;
                break;
            }
        }
    }    

    cout<<num<<'\n';

    return 0;
}
