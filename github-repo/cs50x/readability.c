#include <ctype.h>
#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    string input=get_string("Text: ");
    float letters=0;
    float words=0;
    float sentences=0;
    for (int i=0;input[i]!='\0';i++)
    {
        if (isalnum(input[i]))
        {
            letters++;
        }
        if (input[i]==' ')
        {
            words++;
        }
        if (input[i]=='.'||input[i]=='?'||input[i]=='!')
        {
            sentences++;
        }
    }
    words++;
    float L=letters/words*100;
    float S=sentences/words*100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (index>=16)
        printf("Grade 16+\n");
    else if (index<1)
        printf("Before Grade 1\n");
    else
        printf("Grade %i\n",(int)round(index));
}
