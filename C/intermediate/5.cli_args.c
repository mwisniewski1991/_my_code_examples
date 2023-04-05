#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[]){

    printf("Number of args: %i\n", argc);

    for (int i = 0; i <= 10; i++)
    {
        printf("Hello, %s\n", argv[i]);
    }
    
    return 0;
};