#include<iostream>
#include<vector>
#include<string>
#include<deque>
#include<cctype>

using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin>>T;
    deque<int> Q;

    while(T--){
        int n;
        string order, arr;
        bool reverse=false;
        bool error = false;

        cin>>order;
        cin>>n;
        cin>>arr;
        string tmp;
        for(int i=0;i<arr.size();i++){
            if(isdigit(arr.at(i))){
                tmp.push_back(arr.at(i));
            }
            else{
                if(!tmp.empty()){
                    Q.push_back(stoi(tmp));
                    tmp.clear();
                }
            }
        }
        for(int i=0;i<order.size();i++){
            if(order.at(i)=='R'){
                if(reverse)
                    reverse=false;
                else
                    reverse=true;
            }
            else{
                if(Q.empty()){
                    cout<<"error"<<'\n';
                    error=true;
                    break;
                }
                if(reverse)
                    Q.pop_back();
                else
                    Q.pop_front();
            }
        }
        if(!error){
            cout<<'[';
            if(reverse && !Q.empty()){
                deque<int>::iterator it=Q.end();
                while(it!=Q.begin()){
                    it--;
                    if(it==Q.begin())
                        cout<<*it;
                    else
                        cout<<*it<<',';
                }
            }
            else if(!reverse && !Q.empty()){
                deque<int>::iterator it=Q.begin();
                while(it!=Q.end()){
                    if(it==Q.end()-1)
                        cout<<*it;
                    else
                        cout<<*it<<',';
                    it++;
                }
            }
            cout<<"]\n";
        }
        Q.clear();
    }
    return 0;
}
