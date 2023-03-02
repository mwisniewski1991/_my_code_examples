#include <stdio.h>

int main(void){

    int col_len;
    int row_len;

    do
    {
        printf("Give rows number:");
        scanf("%d", &row_len);
    }
    while (row_len < 0);

    do
    {
        printf("Give columns number:");
        scanf("%d", &col_len);
    }
    while (col_len < 0);

    for(int row = 0; row < row_len; row++){
        for(int col=0; col < col_len; col++){
            printf("#");
        };
        printf("\n");
    }; 
};