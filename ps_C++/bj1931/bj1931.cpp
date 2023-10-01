#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int n;
vector< pair<int,int> > v;


int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n;i++){
        int a, b;
        cin>>a>>b;
        v.push_back(make_pair(b,a));
    }
    sort(v.begin(),v.end());

    int prev = v[0].first;
    int cnt = 1;
    for(int i=1;i<n;i++){
        if(prev<=v[i].second){
            prev = v[i].first;
            cnt++;
        }
    }

    cout<<cnt<<'\n';

    return 0;
}
