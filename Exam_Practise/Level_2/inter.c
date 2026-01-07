int main(int argc, char **argv){

    int i;
    int temp;
    int printed[256] ={0};

    if(argc == 3){
        i=0;

    while(argv[1][i]){
        if(printed[(unsigned char)argv[1][i]] =0){
            temp = 0;
        
        while(argv[2][0]){
            if(argv[1][i] == argv[2][0]){
                write(1, &argv[1][i], 1);
                printed[(unsigned char)argv[1][i]] = 1;
                break
            }
            temp++;
        }
        }
        i++;
    }
    }
    write(1, "\n", 1);
}