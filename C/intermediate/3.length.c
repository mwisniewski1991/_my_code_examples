#include <stdio.h>
#include <cs50.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

// int main(void){

//     string name = get_string("What's your name: ");

//     int n = 0;
//     while(name[n] != '\0'){
//         n++;
//         printf("%i\n", n);
//         sleep(1);
//     };
//     printf("Lenght: %i\n", n);
// };      

// int main(void){

//     // string name = get_string("What's your name: ");
//     char name[7] = "Mat";

//     int n = 0;
//     while(name[n] != '\0'){
//         printf("%i %c\n", n, name[n]);
//         // printf("%c\n", name[n]);
//         n++;
//         sleep(1);
//     };
//     printf("Lenght: %i\n", n);
// };      

int main(void){

    // string name = get_string("What's your name: ");
    char name[7] = "Mateusz";


    printf("Lenght: %li\n", strlen(name));

};      