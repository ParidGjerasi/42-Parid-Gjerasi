typedef struct s_list
{
    int             data;
    struct s_list   *next;
} t_list;


t_list	*sort_list(t_list* lst, int (*cmp)(int, int)){

	t_list *i;
	t_list *j;
	int merda;

	if(!lst)
	return(NULL);

	i = lst;

	while(i){
		j = i->next;

	while(j){

		if(!cmp(i->data, j->data)){
			merda = i->data;
			i->data = j->data;
			j->data = merda;
		}
		j = j->next;
	}
	i = i->next;
}
	return(lst);
}