#include<iostream>
#include<stack>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    stack<int> S;
    stack<int> number;
    vector<int> arr;
    vector<char> result;
    cin>>n;

    for(int i=0;i<n;i++){
        int num; cin>>num;
        arr.push_back(num);
    }
    while(n){
        number.push(n);
        n--;
    }
    S.push(0);
    while(!arr.empty()){
        if(S.top()==arr.front()){
            S.pop();
            result.push_back('-');
            arr.erase(arr.begin());
        }
        else if(S.top()<arr.front()){
            S.push(number.top());
            number.pop();
            result.push_back('+');
        }
        else{
            cout<<"NO";
            return 0;
        }
    }
    for(int i=0;i<result.size();i++)
        cout<<result.at(i)<<'\n';

    return 0;
}
