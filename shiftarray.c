#include <stdio.h>

int main(void) {
	int b,c,temp,a[100],i;
	scanf("%d%d",&b,&c);
	for(i=0;i<b;i++)
    {
        scanf("%d",&a[i]);
    }
	temp=a[0];
    for(i=0;i<b-1;i++)
    {
        a[i]=a[i+1];
    }
    a[b-1]=temp;
 for(i=0;i<b;i++)
    {
        printf("%d",a[i]);
        if(i!=b-1)
        {
        	printf(" ");
        }
    }
	return 0;
}
