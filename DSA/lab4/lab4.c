#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_QUEUE_SIZE 10

typedef struct {
	int items[MAX_QUEUE_SIZE];
	int front;
	int rear;
	int size;
} Queue;

void init_queue(Queue *q) {
	q->front = 0;
	q->rear = -1;
	q->size = 0;
}

bool is_empty(Queue *q) {
	return q->size == 0;
}

bool is_full(Queue *q) {
	return q->size == MAX_QUEUE_SIZE;
}

bool enqueue(Queue *q, int value) {
	if (is_full(q)) return false;
	q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
	q->items[q->rear] = value;
	q->size++;
	return true;
}

bool dequeue(Queue *q, int *out) {
	if (is_empty(q)) return false;
	*out = q->items[q->front];
	q->front = (q->front + 1) % MAX_QUEUE_SIZE;
	q->size--;
	return true;
}

bool peek(Queue *q, int *out) {
	if (is_empty(q)) return false;
	*out = q->items[q->front];
	return true;
}

void display(Queue *q) {
	if (is_empty(q)) {
		printf("Queue is empty\n");
		return;
	}
	printf("Queue (front -> rear): ");
	for (int i = 0, idx = q->front; i < q->size; i++, idx = (idx + 1) % MAX_QUEUE_SIZE) {
		printf("%d", q->items[idx]);
		if (i < q->size - 1) printf(" -> ");
	}
	printf("\n");
}

int demo_enqueue_values[] = {10, 20, 30, 40, 50, 60, 70};

int main(void) {
	Queue q;
	init_queue(&q);

	printf("Linear Queue Demo (max size %d)\n", MAX_QUEUE_SIZE);

	printf("Enqueueing values: ");
	for (int i = 0; i < (int)(sizeof(demo_enqueue_values)/sizeof(demo_enqueue_values[0])); i++) {
		int v = demo_enqueue_values[i];
		printf("%d ", v);
		if (!enqueue(&q, v)) {
			printf("\nFailed to enqueue %d: queue full\n", v);
			break;
		}
	}
	printf("\n");

	display(&q);

	int val;
	printf("\nDequeue two elements:\n");
	for (int i = 0; i < 2; i++) {
		if (dequeue(&q, &val)) {
			printf("  Dequeued: %d\n", val);
		}
	}
	display(&q);

	printf("\nEnqueueing to demonstrate wrap-around: 80, 90, 100\n");
	enqueue(&q, 80);
	enqueue(&q, 90);
	enqueue(&q, 100);
	display(&q);

	if (peek(&q, &val)) printf("\nPeek front: %d\n", val);

	printf("\nDequeue until empty:\n");
	while (dequeue(&q, &val)) {
		printf("  %d\n", val);
	}
	display(&q);

	return 0;
}


