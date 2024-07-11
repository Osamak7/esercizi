#include <unistd.h>

void ft_is_negative(int n){
	
	char segno;
	if (n>=0){	
		segno='P';
		write(1,&segno,1);
	}
	else if (n<0){
		segno='N';
		write(1,&segno,1);
	}

}

int main (void){
	ft_is_negative(-7);
	return 0;
}
