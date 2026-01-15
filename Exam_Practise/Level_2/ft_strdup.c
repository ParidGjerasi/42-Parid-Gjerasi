 #include <stdlib.h>

char    *ft_strdup(char *src){
    int  i;
    char *kak;

    i=0;
    while(src[i]){
        i++;
    }

    kak = malloc(i+1);
    if(!kak)
    return(NULL);

    i=0;
    while(src[i]){
        kak[i] = src[i];
        i++;
    }
    kak[i]= '\0';
    return(kak);
 }