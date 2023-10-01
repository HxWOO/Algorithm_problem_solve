#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int map[25][25];
int vis[25][25];
int N;
int cnt;
int dw[4] = {-1, 0, 1, 0}; //위 , 오 , 아, 왼
int dv[4] = {0, 1, 0, -1};

void DFS(int a, int b){

    for(int i=0;i<4;i++){
        int nw = a + dw[i];
        int nv = b + dv[i];

        if(nw>=N||nw<0||nv>=N||nv<0) {
            continue;
        }

        if(vis[nw][nv]==0 && map[nw][nv]==1){
            vis[nw][nv]=1;
            cnt++;
            DFS(nw,nv);
        }
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<int> nums;
    string s;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>s;
        for(int k=0;k<s.size();k++){
            map[i][k]=s[k]-'0';
            vis[i][k]=0;
        }
    } // 맵,방문여부 저장

    for(int i=0;i<N;i++){
        for(int k=0;k<N;k++){
            if(map[i][k]==1 && vis[i][k]==0){
                vis[i][k]=1;
                cnt=1;
                DFS(i,k);
                nums.push_back(cnt);
            }
        }
    }
    sort(nums.begin(),nums.end());
    cout<<nums.size()<<'\n';
    for(int i=0;i<nums.size();i++){
        cout<<nums[i]<<'\n';
    }

    return 0;
}
