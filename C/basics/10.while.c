#include <stdio.h>
#include <stdbool.h>

int main(){

    int counter = 0;
    char word[] = "Hello";

    while(counter <= 10){

        printf("%d. %s\n", counter, word);
        counter++; 

        if(true){
            printf("It is true.\n");
        };
    };
};