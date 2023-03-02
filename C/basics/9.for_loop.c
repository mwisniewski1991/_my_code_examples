#include <stdio.h>
#include <stdlib.h>

int main(void){

    char word[] = "HAU HAU";

    for (int i = 0; i < 3; i++)
    {
        printf("\n");
        printf("MEOW !!!\n");

        printf("\n");

        printf("%d\n", i);
        printf("%s !!!\n", word);

        printf("\n");
        printf("%d %s\n", i, word);

        printf("----\n");

    };
};