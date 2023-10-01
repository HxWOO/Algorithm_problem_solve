#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(int argc, char const *argv[])
{
    int T;
    string rhkf;
    stack<char> st;
    cin>>T;

    for(int i=0;i<T;i++){
        cin>>rhkf;
        for(int k=0;k<rhkf.size();k++){
            if(rhkf[k]=='('){
                st.push(rhkf[k]);
            }
            else if(st.empty()){
                cout<<"NO"<<endl;
                break;
            }
            else
                st.pop();
            if(k==rhkf.size()-1){
                (st.empty())?cout<<"YES"<<endl:cout<<"NO"<<endl;
            }
        }
        while(!st.empty())
            st.pop();

    }

    return 0;
}
