#include <stdio.h>
#include <stdlib.h>

int main(){

    int numbers[] = {1, 2, 3, 4, 5};

    printf("%d\n", numbers[0]);
    printf("%d\n", numbers[1]);
    printf("%d\n", numbers[2]);
    printf("%d\n", numbers[3]);
    printf("%d\n", numbers[4]);

    numbers[4] = 500;
    printf("%d\n", numbers[4]);

    printf("---\n");
    int new_numbers[2];
    new_numbers[0] = 123;

    printf("%d\n", new_numbers[0]);


    return 0;
};