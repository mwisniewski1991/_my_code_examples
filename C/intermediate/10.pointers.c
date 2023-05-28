#include <stdio.h>

int main(void){

    int n = 50;
    int *p = &n;

    printf("%p\n", p);
    printf("%i\n", *p);
    printf("\n\n");

    char *s = "HI!";
    printf("%p\n", s);
    printf("%s\n", s);
    

    printf("\n");
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("%c\n", s[3]);
    printf("%c\n", s[4]);


    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);

};