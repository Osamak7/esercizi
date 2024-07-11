#include <unistd.h>

void ft_print_numbers(void){
	char  numbers = 48;
	
	while(numbers< 58){
	write(1,&numbers , 1);
	++numbers;
	}
}

int main(void){
	ft_print_numbers();
	return 0;
}
