// NOT SOLVE

#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
#define MAX_SIZE 100
#define SWAP(x,y,t)((t)=(x),(x)=(y),(y)=(t))
void perm(char *,int ,int);
void main(void){
    int i,n,query,pos;
    char list[MAX_SIZE];
    printf("Enter how many  number of character : ");
    scanf("%d",&n);
    if (n<1 || n>MAX_SIZE){
        fprintf(stderr,"Impropervalue of n\n");
        exit(EXIT_FAILURE);
    }
    for (i=0;i<=n;i++){
        scanf("%c",&list[i]);
    }
    perm(list,0,n);
    
}
void perm(char *list,int i,int n){
    int j,temp;
    if (i==n){  
        for ( j = 0; j<= n; j++)
            printf("%c",list[j]);
        printf(" ");
    }
    else
        for ( j = i; j<= n; j++)
        {
            SWAP(list[i],list[j],temp);
            perm(list,i+1,n);
            SWAP(list[i],list[j],temp);
        }       
        
    }
