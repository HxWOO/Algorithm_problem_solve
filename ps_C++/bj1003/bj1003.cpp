#include<iostream>
#include<vector>

using namespace std;

int T, N;
vector<pair<int, int> > fibo; //first는 0이 호출된 횟수, second는 1이 호출된 횟수

void fibona(int n){

    while(fibo.size() <= n && n!=0 && n!= 1){
        int t = fibo.size();
        fibo.push_back(make_pair(fibo[t-1].first + fibo[t-2].first, fibo[t-1].second + fibo[t-2].second));
    }
    cout<<fibo[n].first<<' '<<fibo[n].second<<'\n';
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>T;

    fibo.push_back(make_pair(1,0));
    fibo.push_back(make_pair(0,1));

    for(int i=0;i<T;i++){
        cin>>N;
        fibona(N);
    }

    return 0;
}
