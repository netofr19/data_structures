#include <stdio.h>

struct Node
{
    int data;
    struct Node *next;
} *top=NULL;

typedef struct Node Node;

void push(int x){
    Node *t;
    t = (Node *) malloc(sizeof(Node));

    if(t==NULL){
        printf("Stack is Full!\n");
    }
    else{
        t->data = x;
        t->next = top;
        top=t;
    }
}

int pop(){
    int x = -1;

    if (top == NULL){
        printf("Stack is Empty!\n");
    } else {
        Node *t;
        t = top;
        top = top->next;
        x = t->data;
        free(t);
    }

    return x;
}

void display(){
    Node *p;
    p = top;
    printf("top -> ");
    while(p!=NULL){
        printf("%d ", p->data);
        p=p->next;
    }
    printf("\n");
}



int main()
{ 

    push(10);
    push(20);
    push(30);
    push(40);

    display();

    printf("Deleted element...: %d\n", pop());
    printf("Deleted element...: %d\n", pop());
    printf("Deleted element...: %d\n", pop());

    display();
    
    return 0;
}
