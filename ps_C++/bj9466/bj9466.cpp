#include<iostream>
#include<vector>

using namespace std;

int T;
int n =0;
int st[100001];
bool visited[100001];
bool suc = false;
vector<int> v;
int cnt =0;

void mate(int idx){
    v.push_back(idx);
    int next_idx = st[idx]; // idx번째 학생이 가리키는 숫자
    visited[idx] = true;
    if(!visited[next_idx]){
        mate(next_idx);
    }
    if(v.front() == st[v.back()]) {
        cnt += v.size(); suc = true;
        v.pop_back(); // 담 재귀때 또 들리면 안되니깐 하나 빼주기
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin>>T;
    visited[0] = false;
    for(int i=0;i<T;i++){
        cin>>n;
        for(int j=1;j<n+1;j++){
            int num;
            cin>>num;
            st[j]=num;
            visited[j]=false;
        }
        for(int j=1;j<n+1;j++) {
            mate(j);
            if(!suc){
                for(int k=0;k<v.size();k++){
                    visited[v[k]] = false;
                }
                suc = false;
            } //만약 매칭 실패하면 안 들렀던걸로 해주기
            v.clear();
        }
        cout<<n-cnt<<'\n';
        cnt = 0;
    }
    return 0;
}
