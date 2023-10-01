#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n;
vector<int> v;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n;
    for(int i=0;i<n;i++){
        int num; cin>>num;
        v.push_back(num);
    }
    sort(v.begin(),v.end());

    int max = 0;
    for(int i=0;i<n;i++){
        if((n-i)*v[i]>max) max = (n-i)*v[i];
    }

    cout<<max<<'\n';
    
    return 0;
}
