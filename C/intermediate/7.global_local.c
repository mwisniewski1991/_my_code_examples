#include <stdio.h>
#include <stdint.h>

int8_t global_8;
int16_t global_16;
int32_t global_32;

int number = 10;

int main(void){

    int8_t local_8;
    int16_t local_16;
    int32_t local_32;

    printf("GLOBAL\n");
    printf("%d\n", global_8);
    printf("%d\n", global_16);
    printf("%d\n", global_32);

    printf("\n");
    printf("LOCAL\n");
    printf("%d\n", local_8);
    printf("%d\n", local_16);
    printf("%d\n", local_32);


    printf("\n");
    printf("Global vs local\n");
    printf("%d\n", number);    
    printf("Overwrite global\n");
    int number = 20;    
    printf("%d\n", number);    
};  