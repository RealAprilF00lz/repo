#include <stdio.h>
#include <cs50.h>
#include <ctype.h>

int scrabble(string input);

int main(void)
{
    string letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int scores[]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    string input[2];
    int score[2]={0};
    input[0]=get_string("Player 1: ");
    input[1]=get_string("Player 2: ");
    for (int i=0;i<2;i++)
    {
        for (int j=0;input[i][j]!='\0';j++)
        {
            for (int k=0;letters[k]!='\0';k++)
            {
                if (letters[k]==toupper(input[i][j]))
                {
                    score[i]=score[i]+scores[k];
                }
            }
        }
    }
    printf("Player 1 score: %i\nPlayer 2 score: %i\n",score[0],score[1]);
    if (score[0]>score[1])
    {
        printf("Player 1 wins!\n");
    }
    else if (score[0]<score[1])
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}




