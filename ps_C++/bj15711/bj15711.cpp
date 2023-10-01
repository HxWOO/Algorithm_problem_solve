#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<bool> isPrime(2000001,true);
    
    isPrime[0] = false; isPrime[1] = false;
    
    for(int i=2;i<=sqrt(2000000);i++){
        if(isPrime[i]){
            for(int k=i*i;k<=2000000;k+=i){
                isPrime[k]=false;
            }
        }
    }
    vector<int> prime;
    for(int i=0;i<isPrime.size();i++){
        if(isPrime[i])
            prime.push_back(i);
    }
    long long a, b;
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>a>>b;
        long long sum = a+b;

        if(sum%2==0){
            if(sum==2){
                cout<<"NO\n";
            }
            else{
                cout<<"YES\n";
            }
        } //짝수일땐 골드바흐의 추측으로 2제외하곤 예스
        else{
            sum-=2;
            bool res = true;
            if(sum<=2000000){
                if(isPrime[sum]){
                    cout<<"YES\n";
                }
                else{
                    cout<<"NO\n";
                }
            }
            else{
                for(int k=0;k<prime.size();k++){
                    if(sum%prime[k]==0){
                        res = false;
                        break;
                    }
                }
                if(res) cout<<"YES'\n";
                else cout<<"NO'\n";
            }
        }
    }

    return 0;
}
