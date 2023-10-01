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

    int M,N;
    cin>>M>>N;
    vector<bool> v(1000001,true);
    v.at(0)=false; v.at(1)=false;
    for (int i = 2; i <= (int)sqrt(N); i++){
        if(v.at(i)){
            for(int k=2;k*i<=N;k++){
                if(v.at(k*i)){
                    v.at(k*i)=false;
                }
            }
        }
    }
    for(int i=M;i<=N;i++){
        if(v.at(i)){
            cout<<i<<'\n';
        }
    }
        
    return 0;
}
