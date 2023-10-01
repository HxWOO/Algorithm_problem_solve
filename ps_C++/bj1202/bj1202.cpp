#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int n,k; //n은 보석 수 , k는 가방 수
vector< pair<int,int> > jew;
vector<int> bag;
priority_queue<int> q;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>n>>k;

    for(int i=0;i<n;i++){
        int a, b; cin>>a>>b;
        jew.push_back(make_pair(a,b)); // 무게, 가격 순으로 저장
    }
    sort(jew.begin(),jew.end());  //무게 순 정렬

    for(int i=0;i<k;i++){
        int num; cin>>num;
        bag.push_back(num);
    }
    sort(bag.begin(),bag.end()); // 수용가능 무게 순 정렬
    
    int idx =0;
    long long sum = 0;
    for(int i=0;i<k;i++){
        while(bag[i]>=jew[idx].first && idx<n){ //가방에 수용가능한 보석은 일단 우선순위 큐에 가치가 큰 수대로 저장
            q.push(jew[idx].second);
            idx++;
        }
        if(!q.empty()){ //그 중 젤 큰거 하나만 결과에 저장 하고 다음 가방
            sum+=q.top();
            q.pop();
        }
    }
    cout<<sum<<'\n';

    return 0;
}