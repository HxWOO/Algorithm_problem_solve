#include<iostream>
#include<queue>

using namespace std;

#define MAX 100000
int N, K, res;
bool vis[MAX+1];
queue<pair<int,int> > path;

bool judge(int n){
    if(n<0 || n>MAX || vis[n])
        return false;
    return true;
}

void find_path(){
    vis[N]=true;
    pair<int,int> a(N,0);
    path.push(a);
    while(!path.empty()){
        int num = path.front().first;
        int lv = path.front().second;
        path.pop();
        
        if(num == K){
            res = lv;
            break;
        }

        if(judge(num-1)){
            path.push(make_pair(num-1,lv+1));
            vis[num-1] = true;
        }
        if(judge(num+1)){
            path.push(make_pair(num+1,lv+1));
            vis[num+1] = true;
        }
        if(judge(num*2)){
            path.push(make_pair(num*2,lv+1));
            vis[num*2] = true;
        }
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin>>N>>K;
    for(int i=0;i<=MAX;i++){
        vis[i]=false;
    }

    find_path();

    cout<<res;

    return 0;
}
