#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    queue<pair<int, int> > q;
    vector<int> v;
    int N;
    cin>>N;
    for(int i=0; i<N;i++){
        int size, M;
        cin>>size>>M;
        for(int k=0;k<size;k++){
               int imp;
               cin>>imp;
               pair<int,int> p(imp,k);
               q.push(p);
               v.push_back(imp);
        }
        sort(v.begin(),v.end());
        int cnt=1;
        while(1){
            if(q.front().first==v.back()){
                if(q.front().second==M){
                    cout<<cnt<<'\n';
                    break;
                }
                else{
                    q.pop();
                    cnt++;
                    v.pop_back();
                }
            }
            else{
                pair<int,int> tmp=q.front();
                q.pop();
                q.push(tmp);
            }
        }
        v.clear();
        while(!q.empty()){
            q.pop();
        }
    }

    return 0;
}
