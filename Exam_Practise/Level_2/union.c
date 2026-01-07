#include <unistd.h>

int main(int argc, char **argv)
{
    int i;
    int printed[256] = {0};
    
    if (argc == 3)
    {
        i = 0;
        while (argv[1][i])
        {
            if (printed[(unsigned char)argv[1][i]] == 0)
            {
                write(1, &argv[1][i], 1);
                printed[(unsigned char)argv[1][i]] = 1;
            }
            i++;
        }
        
        i = 0;
        while (argv[2][i])
        {
            if (printed[(unsigned char)argv[2][i]] == 0)
            {
                write(1, &argv[2][i], 1);
                printed[(unsigned char)argv[2][i]] = 1;
            }
            i++;
        }
    }
    write(1, "\n", 1);
    return (0);
}