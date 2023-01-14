#include <stdio.h>
#include <stdlib.h>

void hello_world(){
        printf("Hello world\n");
};

void greet(char* name){
        printf("Hello %s \n", name);
};

void variables(){

    int age = 32;
    printf("Age: %d \n", age);

    age = 30;
    printf("Age: %d \n", age);

    int next_age = age;
    printf("Next age: %d \n", next_age);

};


int main(){
    // hello_world();
    // variables();
    char[] name = "Mateusz"
    greet(name);

    return 0;
};