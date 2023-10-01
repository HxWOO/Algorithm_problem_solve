#include<iostream>
#include<queue>
#include<string>

using namespace std;

int main(int argc, char const *argv[])
{
    int N;
    cin>>N;
    queue<int> que;
    string str;

    for(int i=0;i<N;i++){
        cin>>str;
        if(str=="push"){
            int num; cin>>num;
            que.push(num);
        }    
        else if(str=="pop"){
            if(que.empty())
                cout<<-1<<'\n';
            else{        
                cout<<que.front()<<'\n';
                que.pop();
            }
        }
        if(str=="size")
            cout<<que.size()<<'\n';
        if(str=="empty"){
            cout<<que.empty()<<'\n';
        }
        if(str=="front"){
            if(que.empty())
                cout<<-1<<'\n';
            else
                cout<<que.front()<<'\n';
        }
        if(str=="back"){
            if(que.empty())
                cout<<-1<<'\n';
            else
                cout<<que.back()<<'\n';
        }
    }

    return 0;
}
