#include<iostream>

using namespace std;

int stair[301];
int max_score[301];
int N;


void get_sc(int n){
    if(max_score[n-2]>max_score[n-3] + stair[n-1]){
        max_score[n] = max_score[n-2] + stair[n];
    }
    else{
        max_score[n] = max_score[n-3] + stair[n-1] + stair[n];
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>N;
    for(int i=0;i<N;i++){
        int num;
        cin>>num;
        stair[i] = num;
    }
    max_score[0] = stair[0];
    max_score[1] = (stair[0] + stair[1] > stair[1]) ? stair[0]+stair[1] : stair[1];
    max_score[2] = (stair[0] + stair[1] > stair[1] + stair[2]) ? stair[0]+stair[2] : stair[1]+stair[2];

    for(int i=3;i<N;i++){
        get_sc(i);
    }
    cout<<max_score[N-1];

    return 0;
}
