#include<iostream>
#include<vector>

using namespace std;

int com_div(int a, int b);
int com_mul(int a, int b);

int main(int argc, char const *argv[])
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int num_A, num_B;
    int div,mul;
    cin>>num_A>>num_B;
    div = (num_A>num_B)?com_div(num_A,num_B):com_div(num_B,num_A);
    mul = (num_A>num_B)?com_mul(num_A,num_B):com_mul(num_B,num_A);
   
    cout<<div<<'\n'<<mul<<'\n';

    return 0;
}

int com_div(int a, int b){
    if(a%b)
        return com_div(b,a%b);
    else
        return b;
}

int com_mul(int a, int b){
    int num = com_div(a,b);
    return a*b/num;
}
