#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

int M, N, K;

bool visited[100][100];
vector<int> v; // 각 영역의 크기를 저장하는 벡터
queue<pair<int,int> > q;
int S = 0;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0 , -1, 0}; //오, 아, 왼, 위
int cnt = 0;

bool valid(int x, int y){
    if(x<0 || x>M-1 || y<0 || y>N-1 || visited[x][y])
        return false;
    return true;
}

void bfs(){
    S=1;
    while(!q.empty()){
        int x = q.front().first; int y=q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int next_x = x+dx[i]; int next_y = y+dy[i];
            if(valid(next_x,next_y)){
                q.push(make_pair(next_x,next_y));
                visited[next_x][next_y] = true;
                S++;
            }
        }
    }
    v.push_back(S);
    cnt++;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>M>>N>>K;

    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            visited[i][j] = false;
        }
    }

    for(int i=0;i<K;i++){
        int x, y, a, b;
        cin>>x>>y>>a>>b;
        for(int j=x;j<a;j++){
            for(int k=y;k<b;k++){
                visited[k][j] = 1;
            }
        }
    }

    for(int i=0;i<M;i++){
        for(int j=0;j<N;j++){
            if(!visited[i][j]){
                q.push(make_pair(i,j));
                visited[i][j] = true;
                bfs();
            }
        }
    }
    sort(v.begin(),v.end());

    cout<<cnt<<'\n';
    for(int i=0;i<v.size();i++){
        cout<<v[i]<<' ';
    }

    return 0;
}

