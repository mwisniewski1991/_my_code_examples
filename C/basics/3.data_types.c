#include <stdio.h>
#include <stdlib.h>

// int      4 bytes | %d    for printing   
// long     8 bytes | %li   for printing 
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

void long_number(){
    printf("Adding integers and long integers:\n");
    int number1 = 2000000000;
    int number2 = 2000000000;

    long number3 = 2000000000;
    long number4 = 2000000000;
    
    printf("Integer: %d\n", number1 + number2);
    printf("Long Integer %li\n", number3 + number4);
};

void type_casting(){
    printf("Type casting:\n");
    int x = 1;
    int y = 3;

    float z = x / y;
    printf("%f\n", z);

    float c = (float) x / (float) y;
    printf("%f\n", c);

    printf("%.20f\n", c); //floating point imprecision

};


// int main(){

//     numbers();

//     printf("\n");
//     chars();
    
//     printf("\n");
//     long_number();

//     printf("\n");
//     type_casting();
    
//     return 0;
// };

int main(){

    int x = 1073741824;
    int y = 1073741824;

    long x1 = 1073741824;
    long y2 = 1073741824;

    printf("%d\n", x + y);
    printf("%li\n", x1 + y2);
};