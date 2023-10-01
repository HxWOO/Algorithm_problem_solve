#include<iostream>
#include<queue>
#include<vector>

using namespace std;

int N,M,H;
bool rip[100][100][100];
int tomato[100][100][100];
int dw[6] = {0, 1, 0, 0, -1, 0};
int dv[6] = {1, 0, 0, -1, 0, 0}; //오, 아, 상, 왼, 위, 하
int dh[6] = {0, 0, 1, 0, 0, -1};
queue<pair< pair<int,int>,pair<int, int> > > q; // (행, 열),(높이, 시간) 을 쌓는 큐
int tomato_emp = 0; // 토마토 상자 빈공간의 수
int cnt = 0; // 익은 토마토 수
vector<pair< pair<int,int>,pair<int, int> > > v;

bool eve_rip(){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            for(int k=0;k<H;k++){
                if(tomato[i][j][k] == 0){
                    return false;
                }
            }
        }
    }
    return true;
} //들어왔을 때 모두 안 익었으면 거짓, 익었으면 참 반환

bool valid(int x, int y, int z){
    if(x<0 || x>N-1 || y<0 || y>M-1 || z<0 || z>H-1 || rip[x][y][z] || tomato[x][y][z] == -1)
        return false;
    return true;
} // 범위 밖, 이미 익음, 토마토 없음 이면 거짓 반환

void bfs(){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            for(int k=0;k<H;k++){
                if(rip[i][j][k]){
                    q.push(make_pair(make_pair(i,j),make_pair(k,0)));
                }
            }
        }
    } //이미 익어있는 친구들 큐에 저장
    while(!q.empty()){
        int x = q.front().first.first; int y = q.front().first.second;
        int z = q.front().second.first; int t = q.front().second.second;
        q.pop();

        for(int i=0;i<6;i++){
            int next_x = x+dw[i]; int next_y = y+dv[i]; int next_z = z+dh[i];
            if(valid(next_x,next_y,next_z)){
                q.push(make_pair(make_pair(next_x,next_y),make_pair(next_z,t+1)));
                rip[next_x][next_y][next_z] = true;
                cnt++;
            }
        }
        

        if(cnt == N*M*H-tomato_emp){
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

    cin>>M>>N>>H;

    for(int k=0;k<H;k++){ //아래층 부터 넣기 때문에 높이가 앞에 와야 함
        int num;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                cin>>num;
                tomato[i][j][k] = num;
                if(tomato[i][j][k] == 1){
                    rip[i][j][k] = true; cnt++;
                }
                else rip[i][j][k] = false;
                if(num == -1) tomato_emp++;
            }
        }
    } // 초기화

    if(eve_rip()){
        cout<<0;
        return 0;
    } //이미 모두 익어 있으면 0 출력하고 종료
    bfs();

    return 0;
}
