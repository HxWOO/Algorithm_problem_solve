#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main(int argc, char const *argv[])
{
    stack<int> st;
    int num;
    int N; // 명령의 수
    string order;
    cin>>N;

    for(int i=0;i<N;i++){
        cin>>order;
        if(order=="push"){
            cin>>num;
            st.push(num);
        }
        else if(order=="pop"){
            if(st.empty()){
                cout<<-1<<'\n';
            }
            else{
                cout<<st.top()<<'\n';
                st.pop();
            }
        }
        else if(order=="size"){
            cout<<st.size()<<'\n';
        }
        else if(order=="empty"){
            if(st.empty()){
                cout<<1<<'\n';
            }
            else
                cout<<0<<'\n';
        }
        else if(order=="top"){
            if(st.empty()){
                cout<<-1<<'\n';
            }
            else
                cout<<st.top()<<'\n';
        }
    }

    return 0;
}
