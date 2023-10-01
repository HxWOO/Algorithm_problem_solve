#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;


int main(int argc, char const *argv[])
{
    int N;
    cin>>N;
    vector<int> sosu;
    vector<bool> v(N+1,true);
    v[0]=false; v[1]=false;
    for(int i=2; i <= (int)sqrt(N); i++){
        if(v[i]){
            for(int k=2;k*i<=N+1;k++){
                if(v[i*k])
                    v[i*k]=false;
            }
        }
    }
    //에라토스
    for(int i=0;i<N+1;i++){
        if(v[i]){
            sosu.push_back(i);
        }
    }

    int cnt = 0;
    int sum = N;

    for(int i=0; i<sosu.size();i++){
        sum-=v[i];
        if(sum>0){
            for(int idx=1;idx<sosu.size();idx++){
                sum-=v[i+idx];
                if(!sum){
                    cnt++;
                    break;
                }
                else if(sum<0){
                    sum = N;
                    break;
                }
            }
        }
        if(!sum){
            cnt++;
        }
        sum = N;
    }
    cout<<cnt<<'\n';

    return 0;
}