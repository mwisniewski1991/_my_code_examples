#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void){

    char text[50] = "Ala ma kota kot ma Ale.";
    printf("Text length: %li\n", strlen(text));

    // for (int i = 0; i < strlen(text); i++)
    // {
    //     if(text[i] >= 'a' &&  text[i] <='z'){
    //         text[i] = text[i] - 32;
    //         text[i] = toupper(text[i]);
    //     }
    // };


    for (int i = 0; i < strlen(text); i++)
    {
        text[i] = toupper(text[i]);
    };

    printf("%s\n", text);
};




