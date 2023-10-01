#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
    int N, num;
    cin>>N;
    vector<int> v;

    for(int i=0;i<N;i++){
        cin>>num;
        v.push_back(num);
    }
    sort(v.begin(),v.end());
    
    for(int i=0;i<N;i++){
        cout<<v.at(i)<<'\n';
    }

    return 0;
}
