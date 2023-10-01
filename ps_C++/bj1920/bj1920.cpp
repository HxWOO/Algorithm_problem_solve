#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    int num;
    vector<int> a;
    vector<int> b;

    cin>>N;
    for(int i=0;i<N;i++){
        cin>>num;
        a.push_back(num);
    }

    cin>>N;
    for(int i=0;i<N;i++){
        cin>>num;
        b.push_back(num);
    }

    sort(a.begin(),a.end());

    for(int i=0;i<b.size();i++){
        if(binary_search(a.begin(),a.end(),b.at(i)))
            cout<<1<<'\n';
        else
            cout<<0<<'\n';
    }

    return 0;
}