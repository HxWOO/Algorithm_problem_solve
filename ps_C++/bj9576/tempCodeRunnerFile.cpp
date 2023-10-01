#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

int n,m,t;
bool visited[1001];
int cnt;

bool cmp(pair<int,int> a, pair<int,int> b){
    if(a.first == b.first){
        if(a.second<b.second) return a<b;
    }
    else if(a.first<b.first) return a<b;
    else return b<a;
} 


void gave(vector<pair<int,int> > v, int idx){
    int x = v[idx].first; int y = v[idx].second;

    for(int i=x;i<y+1;i++){
        if(!visited[i]){
            visited[i] = true;
            cnt++;
        }
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> t;

    while(t--){
        cnt = 0;
        vector<pair<int,int> > st;
        cin>>n>>m;
        for(int i=0;i<m;i++){
            int a, b; cin>>a>>b;
            st.push_back(make_pair(a,b));
        }
        sort(st.begin(),st.end(),cmp);

        for(int i=0;i<m;i++){
            gave(st,i);
        }
        
        cout<<cnt<<'\n';
        memset(visited,0,sizeof(visited));

    }
    return 0;
}
