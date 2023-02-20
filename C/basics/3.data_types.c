#include <stdio.h>
#include <stdlib.h>

// int      4 bytes | %d    for printing   
// float    4 bytes | %f    for printing
// double   8 bytes | %lf   for printing
// char     1 byte  | %c    for printing  
// char[]           | %s    for printing

void numbers(){
    printf("Numbers: \n");
    int value_int = 5;
    double value_double = 12.34;
    float value_float = 10.9f;

    printf("%d \n", value_int);
    printf("%lf \n", value_double);
    printf("%f \n", value_float);
};

void chars(){
    printf("Chars: \n");
    char letter = 'A';
    char phrase[] = "Sentence";

    printf("%c \n", letter);
    printf("%d \n", letter);
    printf("%s \n", phrase);
};


int main(){

    numbers();
    printf("\n");
    chars();
    
    return 0;
};