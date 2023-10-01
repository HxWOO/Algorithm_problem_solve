#include<iostream>
#include<vector>
#include<queue>
#include<string>

using namespace std;

int N, M;
vector<vector<int> > map;
bool vis[1000][1000];
queue<pair<int,int>,pair<int,int> > q; //<위치>와 <거리,벽을 부순 횟수> 저장하는 큐
int dw[4] = {0, 1, 0, -1};
int dv[4] = {1, 0, -1, 0}; //오, 아, 왼, 위

bool valid(int x, int y){
    if(x<0 || x>N-1 || y<0 || y>M-1 || vis[x][y] || map[x][y] == 1)
        return false;
    return true;
} //x,y 가 범위를 벗어나거나, 방문한 곳이거나, 벽으로 막혀있으면 거짓

void bfs(){
    int x = q.front().first.first; int y = q.front().first.second;
    int dis = q.front().second.first; int wall = q.front().second.second;
    vis[x][y]=true;
    q.pop();

    while(!q.empty()){
        for(int i=0;i<4;i++){
            int next_x = x+dw[i]; int next_y = y+dv[i];
            if(valid(x,y)){
                q.push(make_pair(next_x,next_y),make_pair(dis+1,wall));
            }

        }
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N>>M;

    for(int i=0;i<1000;i++){
        for(int j=0;j<1000;j++){
            vis[i][j] = false;
        }
    }
    for(int i=0;i<N;i++){
        string s;
        cin>>s;
        for(int j=0;j<M;j++){
            map[i][j]=s[j]-'0';
        }
    }//초기화


    return 0;
}
