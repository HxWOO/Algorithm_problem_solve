#include<iostream>
#include<vector>

using namespace std;

int N, T;
vector<int> com[101];
bool vir[101];

void sp_vir(int x){
    vir[x] = true;

    for(int i=0;i<com[x].size();i++){
        if(!vir[com[x][i]]) sp_vir(com[x][i]);
    }

}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N;
    cin>>T;
    for(int i=0;i<101;i++)
        vir[i]=false;

    for(int i=0;i<T;i++){
        int a, b;
        cin >> a>> b;
        com[a].push_back(b);
        com[b].push_back(a);
    }
    sp_vir(1);

    int cnt = 0;
    for(int i=2;i<101;i++){
        if(vir[i]) cnt++;
    }
    cout<<cnt;

    return 0;
}
