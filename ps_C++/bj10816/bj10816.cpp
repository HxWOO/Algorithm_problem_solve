#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int N, M, num;
    vector<int> a, b;

    cin>>N;
    for(int i=0;i<N;i++){
        cin>>num; a.push_back(num);
    }
    cin>>M;
    for(int i=0;i<M;i++){
        cin>>num; b.push_back(num);
    }
    sort(a.begin(),a.end());

    for(int i=0;i<b.size();i++){
        cout<<upper_bound(a.begin(),a.end(),b.at(i))-lower_bound(a.begin(),a.end(),b.at(i))<<' ';
    }

    return 0;
}
