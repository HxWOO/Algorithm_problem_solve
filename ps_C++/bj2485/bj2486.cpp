#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int getdiv(int a, int b);

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int cnt = 0;
    cin>>N;
    vector<int> loc, diff;
    for(int i=0;i<N;i++){
        int num;
        cin>>num;
        loc.push_back(num);
    }
    
    for(int i=1;i<loc.size();i++){
        diff.push_back(loc[i]-loc[i-1]);
    }
    
    sort(diff.begin(),diff.end());
    int d = diff.front();
    for(int i=1;i<diff.size();i++){
        d=getdiv(diff[i],d);
    }

    cnt = (loc.back() - loc.front())/d - loc.size() + 1;
    cout<<cnt<<'\n';
    
    return 0;
}

int getdiv(int a, int b){
    if(a%b)
        return getdiv(b,a%b);
    else
        return b;
}