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
    int *Pointer;
    int value = 5;

    Pointer = &value;

    printf("Address: %p\n\r", Pointer);
    printf("Value  : %d\n\r", *Pointer);

    printf("Address: %p\n\r", &value);
    printf("Value  : %d\n\r", value);
    

    value = 7;

    printf("After change Address: %p\n\r", Pointer);
    printf("After change Value  : %d\n\r", *Pointer);

    *Pointer = 9;

    printf("After change Address: %p\n\r", Pointer);
    printf("After change Value  : %d\n\r", *Pointer);

    return 0;
};