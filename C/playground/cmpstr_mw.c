#include <stdio.h>
#include <cs50.h>

int strcmp_mw(char *first_word, char *second_word){

    for (int i = 0; i <= 7; i++)
    {
        printf("%c %d : %c %d\n", first_word[i],first_word[i], second_word[i], second_word[i]);

        if(first_word[i] == 0 | second_word[i] == 0){
            
            return 0;

        }else{
            
            if(first_word[i] != second_word[i]){
                return 1;
            }

        }

    };
    return 0;
};


int main(){
    
    string first_word = "Cl ang";
    string second_word= "Cl angystr";

    int result = strcmp_mw(first_word, second_word);
    printf("Result %d\n", result);

};