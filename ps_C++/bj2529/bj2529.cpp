#include<iostream>
#include<vector>
using namespace std;

int k;
char s[10];
bool M_visited[10] = {false};
bool m_visited[10] = {false};
int max_v[10];
int min_v[10];
int a=9;
int b=0;

void MMM(int idx){
    if(s[idx] == '<'){
        MMM(idx+1);
    }
    M_visited[idx] = true;
    max_v[idx] = a;
    a--;
}

void mmm(int idx){
    if(s[idx] == '>'){
        mmm(idx+1);
    }
    m_visited[idx] = true;
    min_v[idx] = b;
    b++;
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin>>k;
    for(int i=0;i<k;i++) cin>>s[i];

    for(int i=0;i<k+1;i++){
        if(!M_visited[i]) MMM(i);
        if(!m_visited[i]) mmm(i);
    }
    
    for(int i=0;i<k+1;i++){
        cout<<max_v[i];
    }
    cout<<'\n';
    for(int i=0;i<k+1;i++){
        cout<<min_v[i];
    }
    cout<<'\n';

    return 0;
}
