#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height=get_int("Height: ");
    int width=get_int("Width: ");
    for (int i=0;i<height;i+=1)
    {
        for (int j=0;j<width;j+=1)
        {
            printf("# ");
        }
        printf("\n");
    }
}
