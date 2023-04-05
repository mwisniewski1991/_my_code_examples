#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[]){


    if (argc != 2)
    {
        printf("Missing cli arguments!!!\n");
        return 1;
    }else{
        printf("Hello, %s\n", argv[1]);
        return 0;
    };
};

// in cli: echo $?