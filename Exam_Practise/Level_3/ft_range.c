#include <stdlib.h>

int *ft_range(int start, int end)
{
    int i;
    int len;
    int *arr;
    
    if (start <= end)
        len = end - start + 1;
    else
        len = start - end + 1;
    
    arr = malloc(len * sizeof(int));
    if (!arr)
        return (NULL);
    
    i = 0;
    while (i < len)
    {
        arr[i] = start;
        i++;
        if (start < end)
            start++;
        else
            start--;
    }
    
    return (arr);
}