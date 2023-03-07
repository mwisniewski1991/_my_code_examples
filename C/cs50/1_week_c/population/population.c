#include <stdio.h>
#include <cs50.h>

int main(void)
{

    int population_size;
    do
    {
        population_size = get_int("Start size: ");
    }
    while(population_size < 1);

    int population_end_size;
    do
    {
        population_end_size = get_int("End size: ");
    } while (population_end_size < population_size);
    


    int years = 0;
    while (population_size < population_end_size)
    {
        
        int borned = population_size / 3;
        int dead = population_size / 4;

        population_size = population_size + borned - dead;
        years = years + 1;
    };
    
    printf("Years: %d\n", years);

    return 0;
}
