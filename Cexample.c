#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define MALLOC(p,s)\
    if (!((p)=malloc(s))){\
       fprintf(stderr,"Insufficient memory");\
       exit(EXIT_FAILURE);\
   }
#define SWAP(x,y,t)((t)=(x),(x)=(y),(y)=(t))
void swap(int * ,int *);
void main(){
   float i,*pi;
   float f,*pf;
   float *temp=NULL;
//    pi=NULL;
//    pf=NULL;
//    pi=(int *)malloc(sizeof(int));
//    pf=(float *)malloc(sizeof(float));
// //    *pi=1024;
// //    *pf=3.14;
//    printf("an integer = %d , a float = %f \n",*pi,*pf);
//    free(pi);
//    free(pf);

    if ((pi=(int *)malloc(sizeof(int)))==NULL||
   (pf=(float *)malloc(sizeof(float)))==NULL){
       fprintf(stderr,"Insufficient memory");
       exit(EXIT_FAILURE);
//    }
//     if (!(pi=(int *)malloc(sizeof(int)))||
//    !(pf=(float *)malloc(sizeof(float)))){
//        fprintf(stderr,"Insufficient memory");
//        exit(EXIT_FAILURE);
//    }
// After define micro we write easy way
   MALLOC(pi,sizeof(int));
   MALLOC(pf,sizeof(int));
   // pi=malloc(sizeof(int));
   // pi=(int*)pi;
   *pi=1024;
   *pf=3;
   // swap(pi,pf);
   
   SWAP(pi,pf,temp);
   printf("an integer = %f , a float = %f \n",*pi,*pf);
   free(pi);
   free(pf);


    
}


// void swap(int *x ,int *y){
//    int temp=*x;
//    *x=*y;
//    *y=temp;
// }