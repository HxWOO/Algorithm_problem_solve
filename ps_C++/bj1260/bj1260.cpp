#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
vector<int> adj[1001];
vector<int> show_dfs;
vector<int> show_bfs;
vector<bool> visited_A(1001, false);
vector<bool> visited_B(1001, false);

void DFS(int start){
    visited_A[start]=true;
    show_dfs.push_back(start);
    for(int i=0;i<adj[start].size();i++){
        if(visited_A[adj[start][i]]){
            continue;
        }
        DFS(adj[start][i]);
    }
}

void BFS(int start){
    visited_B[start]=true;
    show_bfs.push_back(start);
    for(int i=0;i<show_bfs.size();i++){
        for (int k=0;k<adj[show_bfs[i]].size();k++){
            if(visited_B[adj[show_bfs[i]][k]]) continue;
            show_bfs.push_back(adj[show_bfs[i]][k]);
            visited_B[adj[show_bfs[i]][k]]=true;
        }
    }
    
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, V;

    cin>>N>>M>>V;
    for(int i=0;i<M;i++){
        int a, b;
        cin>>a>>b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    } // 간선을 받아서 저장
    
    for(int i=1;i<=N;i++){
        sort(adj[i].begin(),adj[i].end());
    } //우선수위 따라 정렬

    DFS(V); //DFS 실행
    BFS(V); //BFS 실행

    for(int i=0;i<show_dfs.size();i++){
        cout<<show_dfs[i]<<" ";
    }
    cout<<'\n';
    for(int i=0;i<show_dfs.size();i++){
        cout<<show_bfs[i]<<" ";
    }

    return 0;
}
