#include <unistd.h>

void ft_print_reverse_alphabet(void){
	
	char rev_alph = 'z';
	
	while(rev_alph > 96){
		write(1, &rev_alph , 1);
		-- rev_alph;
	}
	
}

int main(void){
	ft_print_reverse_alphabet();
	return 0;
}
