// https://cs50.harvard.edu/x/2023/psets/1/credit/

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int sumcheck(string card_number){

    int card_number_lenght = strlen(card_number);
    printf("Credit card length: %d \n", card_number_lenght);


    for(int i = card_number_lenght - 1 ; i>=1; i=i-2)
    {   
        char digit = card_number[0];        

        printf("%d : %d\n", i, digit);
        sleep(1);
    };

    return 0;
};

int main(void) 
{

    // string card_number = get_string("Write credit card number: \n");
    long card_number = 2223000048400012;
    printf("%li\n", card_number);

    int reminder_10 = card_number % 10;
    int reminder_100 = card_number % 10 % 100;

    printf("%d\n", reminder_10);
    printf("%d\n", reminder_100);

    // sumcheck(card_number);
    

}
// 2223 0000 4840 0011