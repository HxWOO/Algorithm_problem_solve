#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<bool> e(1000001,true);
    vector<int> Pnum;
    e[0] = false; e[1] = false;

    for(int i=0; i<=1000; i++){
        if(e[i]){
            for(int k=2;k*i<=1000001;k++){
                e[i*k]=false;
            }
        }
    } //소수만 true
    for(int i=0;i<1000001;i++){
        if(i%2&&e[i]){
            Pnum.push_back(i);
        }
    }//홀수면서 소수를 저장

    int num=1;
    while(num){
        cin>>num;
        bool real = true;
        for(int i=0;i<Pnum.size();i++){
            if(binary_search(Pnum.begin(),Pnum.end(),num-Pnum[i])){
                cout<<num<<" = "<<Pnum[i]<<" + "<<num-Pnum[i]<<'\n';
                real = false;
                break;
            }
        }
        if(num==0){
            break;
        }
        else if(real){
            cout<<"\"Goldbach's conjecture is wrong\"\n";
        }
    }


    return 0;
}
