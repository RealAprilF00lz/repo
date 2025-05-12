#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        height=get_int("Height: ");
    }
    while (height<1);
    int width=0;
    int spaces=height;
    for (int h=0;h<height;h+=1)
    {
        width+=1;
        spaces-=1;
        for (int s=0;s<spaces;s+=1)
        {
            printf(" ");
        }
        for (int w=0;w<width;w+=1)
        {
            printf("#");
        }
        printf("\n");
    }
}
