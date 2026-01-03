#include <stdlib.h>

char    *ft_strdup(char *src){

    int i;
    char *dup;

    i = 0;
    while(src[i])
    i++;

    dup = malloc(i+1);

    if(dup == NULL)
    return(NULL);

    i = 0;
    while(src[i]){
        dup[i] = src[i];
        i++;
    }
    dup[i] = '\0';
    return(dup);

}




#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *copy = ft_strdup("hello");
    if (copy)
    {
        printf("%s\n", copy);  // prints "hello"
        free(copy);  // IMPORTANT: free allocated memory!
    }
    return 0;
}