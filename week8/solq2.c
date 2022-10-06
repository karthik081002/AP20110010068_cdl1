#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
int i=0,top=0;
char stack[20],ip[20];

void push(char c)
{
	if (top>=20)
		printf("Stack Overflow");
	else
		stack[top++]=c;
}

void pop(void)
{
	if(top<0)
		printf("Stack underflow");
	else
		top--;
}

void error(void)
{
printf("\n\nSyntax Error!!!! String is invalid\n");
exit(0);
}

int main()
{
int n;

printf("The given grammar is\n\n");
printf("E -> TE'\n");
printf("E' -> +TE' | epsilon \n\n");
printf("T -> FT'\n");
printf("T' -> *FT' | epsilon \n\n");
printf("F -> (E) | d\n");
printf("Enter the string to be parsed:\n");
scanf("%s",ip);
n=strlen(ip);
ip[n]='$';
ip[n+1]='\0';
push('$');
push('E');
while(ip[i]!='\0')
{ if(ip[i]=='$' && stack[top-1]=='$')
  {
	printf("\n\n Successful parsing of string \n");
	return(1);
  }
  else
	if(ip[i]==stack[top-1])
	{
	   printf("\nmatch of %c occured ",ip[i]);
	   i++;pop();
	}
	else
	{
		if(stack[top-1]=='E' && (ip[i]=='d' || ip[i]=='('))
		{
		       printf(" \n E -> TE'");
		       pop();
		       push('G');
 		       push('T');
        }
		else if(stack[top-1]=='G')
		{if(ip[i]=='+'){
            printf("\n E' -> +TE'");
			pop();push('G');push('T');push('+');
        }
        else if( ip[i]==')' || ip[i]=='$'){
            printf("\n E' -> epslon");
            pop();
        }
		}
        else if( stack[top-1]=='T'){
           if(ip[i]=='d' || ip[i]=='('){
            printf("\n T -> FT'");
            pop();
            push('H');push('F');
           } 
        }
        else if(stack[top -1]=='H'){
            if(ip[i]=='+' || ip[i]==')' ||ip[i]=='$'){
                printf("\n T' -> epslon");
                pop();
            }
            else if(ip[i]=='*'){
                printf("\n T' -> *FT'");
                pop();
                push('H');push('F');push('*');
            }
        }
        else if(stack[top-1]=='F'){
            if(ip[i]=='d'){
                printf("\n F -> d");
                pop();
                push('d');
            }
            else if( ip[i]=='('){
                printf("\n F -> (E)");
                pop();
                push(')');push('E');push('(');
            }
        } else
			error();
	}
 }
}