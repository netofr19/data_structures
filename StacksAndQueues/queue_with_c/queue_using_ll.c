#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node *next;
} *front = NULL, *rear = NULL;

typedef struct Node node;

void enqueue(int x)
{
    node *t;
    t = (node *)malloc(sizeof(node));

    if(t==NULL){
        printf("Queue is full!\n");
    }
    else{
        t->data=x;
        t->next = NULL;
        if (front==NULL){
            front = rear = t;
        }
        else {
            rear->next = t;
            rear = t;
        }
    }
}

int dequeue(){
    int x=-1;
    node *t;

    if (front == NULL){
        printf("Queue is Empty!\n");
    } else {
        x = front->data;
        t = front;
        front = front->next;
        free(t);
    }

    return x;
}

void display(){
    node *p;
    p = front;
    printf("front -> ");
    while(p){
        printf("%d ", p->data);
        p=p->next;
    }
    printf("\n");
}

int main()
{

    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    enqueue(50);
    enqueue(60);

    display();

    printf("Deleted element...: %d\n", dequeue());
    printf("Deleted element...: %d\n", dequeue());
    printf("Deleted element...: %d\n", dequeue());

    display();
    
    return 0;
}
