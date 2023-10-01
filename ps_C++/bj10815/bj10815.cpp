#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
    int N, M, num;
    vector<int> a, b;

    cin>>N;
    
    for(int i=0;i<N;i++){
        cin>>num;
        a.push_back(num); //상근꺼
    }

    cin>>M;
    for(int i=0;i<M;i++){
        cin>>num;
        b.push_back(num); //비교
    }
    sort(a.begin(),a.end());

    for(int i=0;i<M;i++){
        if(binary_search(a.begin(),a.end(),b.at(i)))
            cout<<1<<' ';
        else
            cout<<0<<' ';        
    }

    return 0;
}
