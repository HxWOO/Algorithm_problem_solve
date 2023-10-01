#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

bool cmp(string a, string b){
    if(!(a.length()==b.length()))
        return a.length()<b.length();
    else
        return a<b;
}

int main()
{
    vector<string> v;
    int N;
    string s;

    cin>>N;
    for(int i=0;i<N;i++){
        cin>>s;
        v.push_back(s);
    }

    sort(v.begin(),v.end(),cmp);
    v.erase(unique(v.begin(),v.end()),v.end());

    for(int i=0;i<N;i++){
        cout<<v.at(i)<<endl;
    }

    return 0;
}
