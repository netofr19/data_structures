#include <stdio.h>

struct Queue{
    int size;
    int front;
    int rear;
    int *Q;
};

typedef struct Queue queue;

void create(queue *q, int size){
    q->size = size;
    q->front = q->rear = -1;
    q->Q = (int *)malloc(q->size*sizeof(int));
}

void enqueue(queue *q, int x){
    if(q->rear == q->size-1){
        printf("Queue is full!\n");
    }
    else {
        q->rear++;
        q->Q[q->rear]=x;
    }
}

int dequeue(queue *q){
    int x = -1;

    if (q->front == q->rear){
        printf("Queue is Empty\n");
    }
    else {
        q->front++;
        x = q->Q[q->front];
    }
    return x;
}

void display(queue q){
    printf("Front -> ");
    for (int i = q.front+1; i<=q.rear; i++){
        printf("%d ", q.Q[i]);
    }
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

    display(q);

    printf("Deleted element: %d\n", dequeue(&q));
    printf("Deleted element: %d\n", dequeue(&q));

    display(q);
    
    return 0;
}
