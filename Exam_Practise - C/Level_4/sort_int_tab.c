void sort_int_tab(int *tab, unsigned int size){

    unsigned int i =0;
    unsigned int j =0;
    int temp;

    while(i< size){

        j=0;
        while(j< size-i-1){
            if(tab[j]>tab[j+1]){
                temp = tab[j];
                tab[j] = tab[j+1];
                tab[j+1] = temp;
            }
            j++;
        }
        i++;
    }
}