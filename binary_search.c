#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<stdlib.h>
#define MAX_SIZE 101
#define SWAP(x,y,t)((t)=(x),(x)=(y),(y)=(t))
#define COMPARE(x,y)(((x)<(y))?-1:((x)==(y))?0:1)
void sort(int [],int);
int binsearch(int [],int ,int ,int);
void main(void){
    int i,n,query,pos;
    int list[MAX_SIZE];
    printf("Enter the number of numbers to generate: ");
    scanf("%d",&n);
    if (n<1 || n>MAX_SIZE){
        fprintf(stderr,"Impropervalue of n\n");
        exit(EXIT_FAILURE);
    }
    for (i=0;i<n;i++){
        list[i]=rand()%1000;
        printf("%d ",list[i]);
    }
    sort(list,n);
    printf("\nSorted array : \n");
    for (i=0;i<n;i++){
        printf("%d ",list[i]);
    }
    printf("\nEnter your Query : ");
    scanf("%d",&query);
    pos=binsearch(list ,query,0,n-1);
    if ((pos==-1))
    {
        printf("Your query is not present\n");
    }
    else{
        printf("Your query position is %d",pos+1);
    }
}
int binsearch(int list[],int query,int left,int right){
    int middle;
    while(left<=right){
        middle=left+right;
        switch (COMPARE(list[middle],query))
        {
        case -1:
            left=middle=1;
            break;
        case 0:
            return middle;
        case 1:
            right=middle-1;
            break;
        default:
            break;
        }
    }
    return-1;
}
void sort(int list[],int n){
    int i,j,min,temp;
    for (i=0;i<n-1;i++){
        min=i;
        for (j=i+1;j<n;j++){
            if(list[j]<list[min]){
                min=j;
            }    
        }
        SWAP(list[i],list[min],temp);
    }
}

// int binsearch(int list[],int query,int left,int right){
//     int middle;
//     if(left<=right){
//         middle=left+right;
//         switch (COMPARE(list[middle],query))
//         {
//         case -1:
//            return binsearch( list, query, middle+1, right);
            
//         case 0:
//             return middle;
//         case 1:
//            return binsearch(list,query, left, middle-1);
//         default:
//             break;
//         }
//     }
//     return-1;
// }