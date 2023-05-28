#include <stdio.h>



int main(void){

    // PART 1
    // int x = 4;              // integer named x is set to 4 
    // int *address = &x;      // integer pointer named address is set to the address of x 
                               // * asterisk - modify type if is near
    // int y = *address;       // integer y is set to the thing pointed to by address       
                               // * asterisk - deep reference, go to address pointed by pointer
    // int *y_address = &y;

    // printf("%d\n", x);
    // printf("%p\n", address);

    // printf("%d\n", y);
    // printf("%p\n", y_address);


    // //PART 2
    int n = 50;
    int *p = &n;

    printf("%d\n", n);
    printf("%p\n", p);
    printf("%i\n", *p);
    printf("\n\n");


    // PART 3
    char *s = "HI!";
    printf("%p\n", s);
    printf("%s\n", s);
    

    printf("\nCHARS\n");
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("%c\n", s[3]);
    printf("%c\n", s[4]);

    printf("\nADDRESSES\n");
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);



};