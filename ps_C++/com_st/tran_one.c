#include<stdio.h>

int main(int argc, char const *argv[])
{
    int i; //$t1
    int result; //$s2
    int* MemArray; //$s0

    i = 0; // addi $t1, $0, $0
    while(1){
        int num = *MemArray; // lw $s1, 0($s0)
        result += num; //add $s2, $s2, $s1
        MemArray++; //addi $s0, $s0, 4
        i++; //addi $t1, $t1, 1
        int tmp = (i<100)?1:0; //slti $t2, $t1, 100
        if(tmp == 0) break; //bne $t2, $0, LOOP
    }

    return 0;
}


int sum(){
    int result =0;
    int* MemArray;

    for(int i=0; i<100;i++){
        result += *(MemArray++);
    }

    return 0;
}