#include <stdio.h>
int main(){
    int a=0, b=0 ,c=0;
    char A[11], B[11], C[11];
    for(int i=0; i<10; i++){
        A[i] = '0';
        B[i] = '0';
        C[i] = '0';
    }
    scanf("%s %s %s",A,B,C);
    for(a=0; A[a]!='\0';a++);
    for(b=0; B[b]!='\0';b++);
    for(c=0; C[c]!='\0';c++);
    if(A[a-1]==B[0]&&B[b-1]==C[0]){
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}