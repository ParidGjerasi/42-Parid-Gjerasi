#include <stdlib.h>

char    *ft_strdup(char *src){


    int i;
    char *temp;

    i = 0;
    while(src[i]){
        i++;
    }

    temp = malloc (i+1);

    if(temp = NULL)
    return(NULL);

    i = 0;
    while(src[i]){
        (temp[i]= src[i]);
        i++;
    }
    temp[i]= '\0';
    return(temp);
}
    