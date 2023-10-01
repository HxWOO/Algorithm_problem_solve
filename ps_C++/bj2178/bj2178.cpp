#include<iostream>
#include<string>
#include<queue>

using namespace std;

int N,M;
int maze[100][100];
bool visited[100][100];
int dw[4]={0, 1, 0 , -1}; // 오, 아, 왼, 위
int dv[4]={1, 0, -1, 0};
queue<pair<pair<int,int>,int> > q; //위치 + 몇번 갔는지 저장

bool valid(int a, int b){
    if(a<0 || a>N-1 || b<0 || b>M-1){
        return false;
    }
    if(visited[a][b] || maze[a][b] == 0){
        return false;
    }
    return true;
} //인덱스가 미로 범위를 벗어나거나, 이미 방문한적 있거나, 길이 없으면 false를 반환

void bfs(){

    while(!q.empty()){
        int x = q.front().first.first; int y = q.front().first.second;
        int lv = q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int next_x = x + dw[i]; int next_y = y+dv[i];
            if(next_x == N-1 && next_y == M-1){
                cout<<lv+1;
                return;
            }
            if(valid(next_x,next_y)){
                q.push(make_pair(make_pair(next_x, next_y),lv+1));
                visited[next_x][next_y] = true;
            }
        }
    }
}


int main(int argc, char const *argv[])
{
    string s;
    cin>>N>>M;

    for(int i=0;i<N;i++){
        cin>>s;
        for(int j=0;j<s.size();j++){
            visited[i][j] = false;
            maze[i][j] = s[j] - '0';
        }
    } //초기화
    
    q.push(make_pair(make_pair(0,0), 1));
    visited[0][0] = true;
    bfs();

    return 0;
}
