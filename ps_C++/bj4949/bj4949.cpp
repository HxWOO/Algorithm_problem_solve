#include<iostream>
#include<stack>
using namespace std;

int main(int argc, char const *argv[])
{
    char s[100];
    stack<int> st;

    while(1){
        while(!st.empty())
            st.pop();

        for(int i=0; s[i-1]=='\n'&&s[i]=='.';i++){
            cin>>s
        }
        for(int i=0;i<s.size();i++){
            if(s[i]=='(')
                st.push(1);
            else if(s[i]=='[')
                st.push(2);
            
            switch (st.top())
            {
            case 1:
                if(s[i]==')')
                    st.pop();
                break;
            case 2:
                if(s[i]==']')
                    st.pop();
                break;
            default:
                break;
            }
        }

        if(st.empty())
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
        if(s.size()==1&&s.front()=='.')
            break;
    }

    return 0;
}
