#include<iostream>
#include<vector>

using namespace std;
int times[1000001];
int N;


void get_T(){
    int cnt= 1;
    while(cnt<N){
        int x = times[cnt] + 1;
        if(3*cnt<1000001){
            if(times[3*cnt] > x || times[3*cnt] == 0){
                times[3*cnt] = x;
            }
        }
        if(2*cnt<1000001){
            if(times[2*cnt] > x || times[2*cnt] == 0){
                times[2*cnt] = x;
            }
        }
        if(cnt+1<1000001){
            if(times[cnt+1] > x || times[cnt+1] == 0){
                times[cnt+1] = x;
            }
        }
        cnt++;
    }
}

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin>>N;
    get_T();
    cout<<times[N];

    return 0;

}
