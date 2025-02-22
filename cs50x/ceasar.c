#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc,string argv[])
{
	if (argc!=2)
	{
		printf("Usage: ./ceasar KEY\n");
		return 1;
	}
	for (int i=0;argv[1][i]!='\0';i++)
	{
		if (isdigit(argv[1][i])==0)
		{
			printf("Usage: ./ceasar KEY\n");
			return 1;
		}
	}
	string text=get_string("Plaintext: ");
	int key=atoi(argv[1]);
	for (int i=0;text[i]!='\0';i++)
	{
		if (isalpha(text[i]))
		{
			if (isupper(text[i])&&text[i]+key>90)
			{
				text[i]-=26;
			}
			if (islower(text[i])&&text[i]+key>122)
			{
				text[i]-=26;
			}
			text[i]+=key;
		}
	}
	printf("Ciphertext: %s\n",text);

}

