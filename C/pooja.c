#include<stdio.h>
int main(){
int x; float y;
scanf("%d", &x);
scanf("%f", &y);
if(x>0&&x<=2000&&y>=0&&y<=2000)
{
	if(y>=x+0.50)
	{
		if(x%5==0)
		{
    		y=y-x-0.50;
    		printf("the total amount left= %.2f", y);
		}
		else
		{
			printf("x is not multiple of 5");
			printf("the total amount left= %.2f", y);
		}
	}
	else{
		printf("You can not take out!");
	}

}
else{
	printf("enter value bw 0-2000\n");
	}
	printf("\n");
	return 0;

	}
