#include<iostream>
#include<queue>
#include<vector>

using namespace std;

int cheese[100][100];
int N,M;
queue< pair< pair<int,int>,int> > q;
queue< pair<int,int> > a;
bool visited[100][100];
bool air[100][100];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0}; // 오, 아, 왼, 위

bool valid(int x, int y){
    if(x<0 || x>N-1 || y<0 || y>M-1)
        return false;
    return true;
}

void is_air(){

    while(a.empty()){
        int x = a.front().first; int y = a.front().second;
        air[x][y] = true;
        a.pop();

        for(int i=0;i<4;i++){
            int next_x = x + dx[i]; int next_y = y+dy[i];
            if(valid(next_x,next_y) && !air[next_x][next_y]){
                a.push(make_pair(next_x,next_y));
            }
        }
    }
} //air 2차원 배열에 공기 여부 저장

void bfs(){
    for(int i=0;i<N;i++){

    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            int num;
            cin >>num;
            cheese[i][j] = num;
            visited[i][j] = false;
            air[i][j] = false;
        }
    }


    return 0;
}

