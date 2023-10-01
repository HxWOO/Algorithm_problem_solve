#include<iostream>
#include<stack>
using namespace std;

int main(int argc, char const *argv[])
{
    stack<int> jb;
    unsigned int K;
    cin>>K;
    unsigned int num;
    unsigned int sum=0;
    for(int i=0;i<K;i++){
        cin>>num;
        if(num)
            jb.push(num);
        else
            jb.pop();
    }

    while(!jb.empty()){
        sum+=jb.top();
        jb.pop();
    }
    cout<<sum;
    
    return 0;
}
