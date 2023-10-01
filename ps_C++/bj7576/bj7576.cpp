#include<iostream>
#include<queue>

using namespace std;

int N,M;
bool rip[1000][1000];
int tomato[1000][1000];
int dw[4] = {0, 1, 0, -1};
int dv[4] = {1, 0, -1, 0}; //오, 아, 왼, 위
queue<pair< pair<int,int>, int> > q; // (행, 열), 시간 을 쌓는 큐
int tomato_emp = 0; // 토마토 상자 빈공간의 수
int cnt = 0; // 익은 토마토 수

bool eve_rip(){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(tomato[i][j] == 0){
                return false;
            }
        }
    }
    return true;
} //들어왔을 때 모두 안 익었으면 거짓, 익었으면 참 반환

bool valid(int x, int y){
    if(x<0 || x>N-1 || y<0 || y>M-1 || rip[x][y] || tomato[x][y] == -1)
        return false;
    return true;
} // 범위 밖, 이미 익음, 토마토 없음 이면 거짓 반환

void bfs(){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(rip[i][j]){
                q.push(make_pair(make_pair(i,j),0));
            }
        }
    } //이미 익어있는 친구들 큐에 저장
    while(!q.empty()){
        int x = q.front().first.first; int y = q.front().first.second;
        int t = q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int next_x = x+dw[i]; int next_y = y+dv[i];
            if(valid(next_x,next_y)){
                q.push(make_pair(make_pair(next_x,next_y),t+1));
                rip[next_x][next_y] = true;
                cnt++;
            }
        }

        if(cnt == N*M-tomato_emp){
            cout<<t+1;
            return;
        }
    }
    cout<< -1;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin>>M>>N;

    for(int i=0;i<N;i++){
        int num;
        for(int j=0;j<M;j++){
            cin>>num;
            tomato[i][j] = num;
            if(tomato[i][j] == 1){
                rip[i][j] = true; cnt++;
            }
            else rip[i][j] = false;
            if(num == -1) tomato_emp++;
        }
    } // 초기화

    if(eve_rip()){
        cout<<0;
        return 0;
    } //이미 모두 익어 있으면 0 출력하고 종료
    bfs();

    return 0;
}
