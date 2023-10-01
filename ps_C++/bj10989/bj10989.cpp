#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    int N, num;
    vector<int> v(10001);
    cin>>N;

    for(int i=0;i<N;i++){
        cin>>num;
        v.at(num)+=1;
    }
    for(int i=1;i<N;i++){
        for(int k=0;k<v.at(i);k++){
            cout<<i<<'\n';
        }
    }

    return 0;
}
