#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int n,m,t;
int cnt;

bool cmp(pair<int,int> x, pair<int,int> y){
    if(x.first == y.first){
        return (x.second > y.second)?x>y:y>x;
    }
    else
        return (x.first>y.first)?x>y:y>x;
} 


int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> t;

    while(t--){
        cnt = 0;
        vector<pair<int,int> > st;
        bool visited[1001];
        cin>>n>>m;
        for(int i=0;i<m;i++){
            int a, b; cin>>a>>b;
            st.push_back(make_pair(a,b));
        }
        sort(st.begin(),st.end(),cmp);

        for(int i=0;i<m;i++){
            for(int j=st[i].first;j<=st[i].second;j++){
                if(!visited[j]){
                    visited[j] = true;
                    cnt++;
                }
            }
        }
        cout<<cnt<<'\n';
    }

    return 0;
}
