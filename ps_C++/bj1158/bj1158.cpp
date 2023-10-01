#include<iostream>
#include<queue>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, k;
    cin>>N>>k;
    queue<int> Q;
    vector<int> v;
    for(int i=0; i<N;i++){
        Q.push(i+1);
    }
    while(!Q.empty()){
        for(int i=1;i<k;i++){
            int tmp = Q.front();
            Q.pop();
            Q.push(tmp);
        }
        v.push_back(Q.front());
        Q.pop();
    }
    cout<<'<';
    for(int i=0;i+1<v.size();i++){
        cout<<v.at(i)<<", ";
    }
    cout<<v.back()<<'>';

    return 0;
}
