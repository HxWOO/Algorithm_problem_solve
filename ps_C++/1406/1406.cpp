#include<iostream>
#include<list>
#include<string>
using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    string s;
    cin>>s;
    list<char> ed;
    for(int i=0;i<s.size();i++){
        ed.push_back(s.at(i));
    }

    list<char>::iterator it = ed.end();
    cin>>n;
    while(n--){
        char ord;
        cin>>ord;
        if(ord=='L'){
            if(it!=ed.begin())
                it--;
        }
        else if(ord=='D'){
            if(it!=ed.end())
                it++;
        }
        else if(ord=='B'){
            if(it!=ed.begin()){
                it--;
                it=ed.erase(it);
            }
        }
        else if(ord=='P'){
            cin>>ord;
            it=ed.insert(it,ord);
            it++;
        }
    }
    while(!ed.empty()){
        cout<<ed.front();
        ed.pop_front();
    }

    return 0;
}
