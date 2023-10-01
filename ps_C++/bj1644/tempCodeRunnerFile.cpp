#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

int calc(vector<int> v, int n, int idx, int cnt);

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
    sosu.shrink_to_fit();

    for(int i=0; i<sosu.size();i++){
        cnt = calc(sosu,N,i,cnt);
    }
    cout<<cnt<<'\n';

    return 0;
}


int calc(vector<int> v, int n, int idx, int cnt){
    if(idx>v.size())
        return cnt;
    int rst = n - v[idx];
    if(rst>0){
        return calc(v,rst,idx+1,cnt);
    }
    else if(!rst){
        return ++cnt;
    }
    else
        return cnt;
}