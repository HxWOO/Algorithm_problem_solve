#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int N;
int L, P;
vector<pair<int, int> > v;
priority_queue<pair<int,int> > q;
int e = 0; //엔진에 남은 기름 양;
int cnt = 0;
int idx = 0;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin>>N;
    for(int i=0;i<N;i++){
        int a,b;
        cin >> a>> b;
        v.push_back(make_pair(b,a)); //기름, 거리 순으로 넣음
    }
    cin >> L >> P;
    e = P;
    while(e<=v[idx].second){
        q.push(v[idx]);
        idx++;
    }

    while(e<L){
        while(e<v[idx].second){
            e += q.top().first;
            cnt++;
            q.pop();
        }
        q.push(v[idx]);
        idx++;
    }

    cout<<cnt<<'\n';

    return 0;
}
