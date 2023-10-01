#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int len;
    int N;
    vector<int> v;
    cin>>len;
    for(int i=0;i<len;i++){
        cin>>N;
        v.push_back(N);
    }
    sort(v.begin(),v.end());
    cout<<v.front()*v.back()<<'\n';

    return 0;
}
