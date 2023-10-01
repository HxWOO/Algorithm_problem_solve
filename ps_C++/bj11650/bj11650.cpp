#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    pair<int,int> s;
    vector<pair<int,int> > dot;
    cin>>N;

    for(int i=0;i<N;i++){
        cin>>s.first>>s.second;
        dot.push_back(s);
    }
    sort(dot.begin(),dot.end());

    for(int i=0;i<dot.size();i++){
        cout<<dot.at(i).first<<' '<<dot.at(i).second<<'\n';
    }

    return 0;
}
