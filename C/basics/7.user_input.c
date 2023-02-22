#include <stdio.h>
#include <stdlib.h>

int main(){

    // int age;
    // printf("Enter your age: ");
    // scanf("%d", &age);
    // printf("You are %d years old.\n", age);

    // char name[20];
    // printf("Enter your name: ");
    // scanf("%s", name); //
    // printf("Your name is %s\n", name);

    //fgets will take input from above if code
    //fgets is better

    char full_name[50];
    printf("Enter your name and surname: \n");
    fgets(full_name, 50, stdin);
    printf("You are %s\n", full_name);

    return 0;
};