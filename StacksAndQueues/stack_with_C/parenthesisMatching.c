#include <stdio.h>
#include <stdlib.h>

struct Node
{
    char data;
    struct Node *next;
} *top = NULL;

typedef struct Node node;

void push(char x)
{
    node *t;
    t = (node *)malloc(sizeof(node));

    if (t == NULL){
        printf("Stack is full!\n");
    }
    else{
        t->data = x;
        t->next = top;
        top=t;
    }
}

char pop()
{
    node *t;
    char x = -1;

    if (top == NULL){
        printf("Stack is Empty!\n");
    } else {
        t = top;
        top=top->next;
        x = t->data;
        free(t);
    }
    return x;
}

void display()
{
    node *p;
    p = top;
    printf("top -> ");
    while (p!=NULL){
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

int isBalanced(char *exp){
    int i;

    for(i=0; exp[i]!='\0'; i++){
        if(exp[i] == '('){
            push(exp[i]);
        } else if(exp[i] == ')'){
            if (top==NULL){
                return 0;
            }
            else {
                pop();
            }
        }
    }
    if (top==NULL){
        return 1;
    }
    else {
        return 0;
    }
}

int main()
{
    char *exp = "((a+b)*(c-d)))";

    printf("%d\n", isBalanced(exp));
    
    return 0;
}
