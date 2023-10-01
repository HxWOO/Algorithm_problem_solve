#include<iostream>

using namespace std;


int main(int argc, char const *argv[])
{
    int T[15];
    int P[15];
    int N;
    int DP[15];
    int latest=0;

    cin>>N;

    for(int i=0; i<N;i++){
        cin>>T[i]>>P[i];
    }

    (T[0] == 1)?DP[0] = 1 : DP[0] = 0;

    for(int i=1;i<N;i++){
        DP[i] = DP[i-1];
        for (int j = latest; j<=i; j++){
            if(latest+T[j]<=i+1){
                if(DP[i]<DP[i-1]+P[j]){
                    DP[i] = DP[i-1] + P[j];
                    latest = i;
                }
            }
        }
        cout<<i<<" :   "<<latest << ",     "<<DP[i]<<'\n';
    }

    cout<<DP[N-1];

    return 0;
}
