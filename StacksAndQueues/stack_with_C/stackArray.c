#include <stdio.h>
#include <stdlib.h>

struct Stack{
    int size;
    int top;
    int *s;
};

typedef struct Stack stack;

void create(stack *st){
    printf("Enter size....: ");
    scanf("%d", &st->size);

    st->top = -1;

    st->s = (int *)malloc(st->size*sizeof(int));
}

void display(stack st){
    int i;
    printf("top-> ");
    for (i=st.top; i>=0; i--){
        printf("%d ", st.s[i]);
    }
    printf("\n");
}

void push(stack *st, int x){
    if (st->top == st->size-1){
        printf("Stack Overflow!\n");
    } else {
        st->top++;
        st->s[st->top] = x;
    }
}

int pop(stack *st){
    int x = -1;

    if (st->top == -1){
        printf("Stack Underflow!\n");
    } else {
        x = st->s[st->top];
        st->top--;
    }
    return x;
}

int peek (stack st, int index){
    int x = -1;
    if(st.top-index<0){
        printf("Invalid Index!\n");
    }
    x = st.s[st.top-index+1];

    return x;
}

int isEmpty(stack st){
    if (st.top == -1){
        return 1;
    }
    return 0;
}

int isFull(stack st){
    return st.top == st.size-1;
}

int stackTop(stack st){
    if(!isEmpty(st)){
        return st.s[st.top];
    }
    return -1;
}

int main()
{
    stack st;
    create(&st);

    push(&st, 10);
    push(&st, 20);
    push(&st, 30);
    push(&st, 40);
    push(&st, 50);

    display(st);

    printf("Deleted element....: %d\n", pop(&st));

    display(st);

    printf("Peek: %d \n", peek(st, 2));


    return 0;
}

