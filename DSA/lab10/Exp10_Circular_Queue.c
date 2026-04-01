#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int front;
    int rear;
    int size;
    int capacity;
} CircularQueue;

FILE *output_file;

// Create circular queue
CircularQueue *createQueue(int capacity) {
    CircularQueue *q = (CircularQueue *)malloc(sizeof(CircularQueue));
    q->data = (int *)malloc(capacity * sizeof(int));
    q->front = -1;
    q->rear = -1;
    q->size = 0;
    q->capacity = capacity;
    return q;
}

// Enqueue element
void enqueue(CircularQueue *q, int val) {
    if (q->size == q->capacity) {
        fprintf(output_file, "Queue is full!\n");
        return;
    }
    
    if (q->front == -1) {
        q->front = 0;
    }
    
    q->rear = (q->rear + 1) % q->capacity;
    q->data[q->rear] = val;
    q->size++;
    fprintf(output_file, "  Enqueued: %d (rear at index %d)\n", val, q->rear);
}

// Dequeue element
int dequeue(CircularQueue *q) {
    if (q->size == 0) {
        fprintf(output_file, "Queue is empty!\n");
        return -1;
    }
    
    int val = q->data[q->front];
    fprintf(output_file, "  Dequeued: %d (from index %d)\n", val, q->front);
    
    if (q->size == 1) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % q->capacity;
    }
    
    q->size--;
    return val;
}

// Display queue
void displayQueue(CircularQueue *q, char *label) {
    fprintf(output_file, "\n%s (size: %d): ", label, q->size);
    
    if (q->size == 0) {
        fprintf(output_file, "[ Empty ]\n");
        return;
    }
    
    fprintf(output_file, "[ ");
    int count = 0;
    int i = q->front;
    while (count < q->size) {
        fprintf(output_file, "%d ", q->data[i]);
        i = (i + 1) % q->capacity;
        count++;
    }
    fprintf(output_file, "]\n");
}

// Find winner of circular game
int findWinner(int n, int k) {
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "FINDING WINNER OF CIRCULAR GAME\n");
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "Number of friends (n): %d\n", n);
    fprintf(output_file, "Count step (k): %d\n", k);
    
    CircularQueue *q = createQueue(n);
    
    // Enqueue all friends
    fprintf(output_file, "\nInitializing queue with friends:\n");
    for (int i = 1; i <= n; i++) {
        enqueue(q, i);
    }
    displayQueue(q, "Initial Queue");
    
    fprintf(output_file, "\n--- ELIMINATION PROCESS ---\n");
    
    int eliminationStep = 1;
    
    while (q->size > 1) {
        fprintf(output_file, "\nStep %d:\n", eliminationStep);
        fprintf(output_file, "Counting %d friends:\n", k);
        
        // Count k friends and eliminate the k-th one
        for (int i = 1; i < k; i++) {
            int friend = dequeue(q);
            enqueue(q, friend);
            fprintf(output_file, "  Count %d: Friend %d (moves to back)\n", i, friend);
        }
        
        // Eliminate the k-th friend
        int eliminated = dequeue(q);
        fprintf(output_file, "  Count %d: Friend %d (ELIMINATED!)\n", k, eliminated);
        
        displayQueue(q, "Queue after elimination");
        
        eliminationStep++;
    }
    
    int winner = q->data[q->front];
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "WINNER: Friend %d\n", winner);
    fprintf(output_file, "====================================\n");
    
    free(q->data);
    free(q);
    
    return winner;
}

int main() {
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("Error: Could not create output file\n");
        return 1;
    }
    
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "EXPERIMENT 10: CIRCULAR QUEUE\n");
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "AIM: Find the Winner of the Circular\n");
    fprintf(output_file, "Game using Queue\n\n");
    
    int n, k;
    printf("====== CIRCULAR QUEUE GAME ======\n");
    printf("Enter number of friends (n): ");
    scanf("%d", &n);
    printf("Enter count step (k): ");
    scanf("%d", &k);
    
    fprintf(output_file, "User Input:\n");
    fprintf(output_file, "Number of friends: %d\n", n);
    fprintf(output_file, "Count Step: %d\n", n);
    
    if (n <= 0 || k <= 0) {
        fprintf(output_file, "Invalid input!\n");
        printf("Invalid input!\n");
        fclose(output_file);
        return 1;
    }
    
    int winner = findWinner(n, k);
    
    printf("\nWinner: Friend %d\n", winner);
    
    // Test cases
    fprintf(output_file, "\n\n====================================\n");
    fprintf(output_file, "TEST CASES:\n");
    fprintf(output_file, "====================================\n");
    
    fprintf(output_file, "\nTest Case 1: n=5, k=2\n");
    fprintf(output_file, "Expected Winner: 3\n");
    findWinner(5, 2);
    
    fprintf(output_file, "\n\nTest Case 2: n=6, k=5\n");
    fprintf(output_file, "Expected Winner: 1\n");
    findWinner(6, 5);
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "CONCLUSION:\n");
    fprintf(output_file, "Game based on queue is implemented\n");
    fprintf(output_file, "using Circular Queue successfully.\n");
    fprintf(output_file, "====================================\n");
    
    fclose(output_file);
    
    printf("\nOutput written to output.txt\n");
    return 0;
}
