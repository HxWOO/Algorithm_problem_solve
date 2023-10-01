#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef long long ll;

int N;
vector<pair<ll, ll> > v;
ll road = 0;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int a;

    cin>>N;

    v.push_back(make_pair(0,0));
    for(int i=1;i<N;i++){
        ll num;
        cin>>num;
        road += num;
        v.push_back(make_pair(road,0));
    } // 전체 길의 길이가 road에 저장, v[i].first에 출발점으로부터의 거리 저장

    for(int i=0;i<N;i++){
        cin>>v[i].second;
    }


    sort(v.rbegin(),v.rend());

    ll low = v.back().second;
    ll prev =0;
    ll cost =0;
    while(prev != road){
        if(v.back().second<low) {
            ll dis = v.back().first - prev;
            prev = v.back().first;
            cost += dis*low;
            low = v.back().second;
        }
        v.pop_back();
        if(v.empty()){
            cost += low*(road-prev);
            break;
        }
    }
    cout<<cost<<'\n';

    return 0;
}
