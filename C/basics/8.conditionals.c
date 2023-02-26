#include <stdio.h>
#include <stdlib.h>

int main(){
    int x;
    int y;
    
    printf("Enter x:");
    scanf("%d", &x);

    printf("Enter y:");
    scanf("%d", &y);

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if(x > y)
    {
        printf("y is less than x\n");
    }
    else
    {
        printf("y is equal x\n");
    };

    return 0;
};

// int main(){
    
//     char agreed[2];
//     printf("Enter value:");
//     fgets(agreed, 2, stdin);

//     if(agreed == "y" || agreed == "Y")
//     {
//         printf("You agreed");
//     }
//     else if(agreed == "n" || agreed == "N" )
//     {
//         printf("You disagreed");
//     }
//     else{
//         printf("..%s..\n", agreed);
//     }
// };