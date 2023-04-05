#include <stdio.h> 
#include <cs50.h>

int main(void){

    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    printf("%i %i %i \n", c1, c2, c3);
    printf("\n");

    string s = "HI!";
    printf("%s \n", s);
    printf("%c %c %c %c \n", s[0], s[1], s[2], s[3]);
    printf("%i %i %i %i \n", s[0], s[1], s[2], s[3]);
    printf("\n");

    char ss[3] = "HI";
    printf("%s \n", ss);
    printf("%c %c\n", ss[0], ss[1]);
    printf("%i %i\n", ss[0], ss[1]);
    printf("\n");

    

//     string name = get_string("What's your name:");
//     printf("Hello %s \n", name);    

//     return 0;
}