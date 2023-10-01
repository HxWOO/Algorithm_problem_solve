#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    int N, num;
    vector<int> a,b;
    int sum=0;

    cin>>N;

    for(int i=0;i<N;i++){
        cin>>num;
        a.push_back(num);
    }
    for(int i=0;i<N;i++){
        cin>>num;
        b.push_back(num);
    }
    vector<int> c(b);
    sort(a.begin(),a.end());
    sort(c.rbegin(),c.rend());

    for(int i=0;i<N;i++){
        sum += a.at(i)*c.at(i);
    }
    cout<<sum;
    return 0;
}
