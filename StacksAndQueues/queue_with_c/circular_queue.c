#include <stdio.h>
#include <stdlib.h>

struct Queue{
    int size;
    int front;
    int rear;
    int *Q;
};

typedef struct Queue queue;

void create(queue *q, int size){
    q->size = size;
    q->front = q->rear = 0;
    q->Q = (int *)malloc(q->size*sizeof(int));
}

void enqueue(queue *q, int x){
    if((q->rear+1)%q->size == q->front){
        printf("Queue is full!\n");
    }
    else{
        q->rear = (q->rear+1)%q->size;
        q->Q[q->rear] = x;
    }
}

int dequeue(queue *q){
    int x=-1;

    if(q->front == q->rear){
        printf("Queue is Empty\n");
    }
    else{
        q->front = (q->front+1)%q->size;
        x = q->Q[q->front];
    }
    return x;
}

void display(queue q){
    int i = q.front+1;
    printf("top -> ");
    do{
        printf("%d ", q.Q[i]);
        i = (i+1)%q.size;
    }while(i != (q.rear+1)%q.size);
    printf("\n");
}

int main()
{
    queue q;
    create(&q, 5);

    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    enqueue(&q, 40);
    enqueue(&q, 50);
    enqueue(&q, 60);

    display(q);

    printf("Deleted element....: %d\n", dequeue(&q));

    enqueue(&q, 40);
    enqueue(&q, 50);

    printf("Deleted element....: %d\n", dequeue(&q));
    
    display(q);

    enqueue(&q, 40);

    display(q);

    
    return 0;
}
