#include <stdio.h>
#include <stdlib.h>

int main(){

    float value1 = 0.1;
    float value2 = 0.2;
    printf("%f\n", value1 + value2);
    printf("%f\n", value1 - value2);
    printf("%f\n", value1 * value2);


    int value3 = 1;
    int value4 = 2;
    printf("%d\n", value3 + value4);
    
    float value5 = 0.1;
    int value6 = 1;
    // printf("%d\n", value5 + value6);
    printf("%f\n", value5 + value6);

    return 0;
};