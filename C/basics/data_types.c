#include <stdio.h>
#include <stdlib.h>

// int      4 bytes | %d    for printing   
// double   8 bytes | %lf   for printing
// float    4 bytes | %f    for printing
// char     1 byte  | %c    for printing  

void numbers(){
    int value_1 = 5;
    double value_2 = 12.34;
    float value_3 = 10.9f;

    printf("%d \n", value_1);
    printf("%lf \n", value_2);
    printf("%f \n", value_3);
};

void chars(){
    char letter = 'A';

    printf("%c \n", letter);
    printf("%d \n", letter);
}

int main(){
    numbers();
    chars();
    return 0;
};