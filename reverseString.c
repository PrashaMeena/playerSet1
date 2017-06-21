#include<stdio.h>
#include<string.h>
main()
{
  char word[30],rev[30];
  int  i=0,j=0;
  scanf("%s",word);
  for(i=strlen(word)-1;i>=0;i--,j++)
  {
    rev[j] = word[i];
  }
  rev[j] = '\0';
  printf("%s",rev);
}
