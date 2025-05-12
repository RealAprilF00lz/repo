#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    do
    {
        change=get_int("Change in cents: ");
    }
    while (change<0);

    int coins=0;
    if (change>=25)
    {
        coins=change/25;
        change=change%25;
    }
    if (change>=10)
    {
        coins=coins+change/10;
        change=change%10;
    }
    if (change>=5)
    {
        coins=coins+change/5;
        change=change%5;
    }
    if (change>=1)
    {
        coins=coins+change;
    }
    printf("%i\n",coins);
}
