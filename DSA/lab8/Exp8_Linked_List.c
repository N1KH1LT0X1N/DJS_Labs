#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int val;
    struct Node *next;
} Node;

FILE *output_file;

// Create a new node
Node *createNode(int val) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

// Create linked list from user input
Node *createLinkedList() {
    int n, val;
    printf("Enter number of nodes: ");
    scanf("%d", &n);
    fprintf(output_file, "Number of nodes: %d\n", n);
    
    if (n <= 0) {
        return NULL;
    }
    
    printf("Enter the values in sorted order:\n");
    Node *head = NULL, *tail = NULL;
    
    for (int i = 0; i < n; i++) {
        printf("Node %d: ", i + 1);
        scanf("%d", &val);
        
        Node *newNode = createNode(val);
        
        if (head == NULL) {
            head = newNode;
        } else {
            tail->next = newNode;
        }
        tail = newNode;
    }
    
    return head;
}

// Display linked list
void displayList(Node *head, char *name) {
    fprintf(output_file, "%s: ", name);
    Node *current = head;
    if (current == NULL) {
        fprintf(output_file, "[]");
    }
    while (current != NULL) {
        fprintf(output_file, "[%d]", current->val);
        if (current->next != NULL) {
            fprintf(output_file, " -> ");
        }
        current = current->next;
    }
    fprintf(output_file, "\n");
}

// Merge two sorted linked lists
Node *mergeSortedLists(Node *list1, Node *list2) {
    fprintf(output_file, "\n=== MERGING SORTED LINKED LISTS ===\n");
    
    displayList(list1, "List 1");
    displayList(list2, "List 2");
    
    // Create a dummy node to simplify merging
    Node *dummy = createNode(0);
    Node *current = dummy;
    
    fprintf(output_file, "\nMerging process:\n");
    
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            fprintf(output_file, "  Comparing %d vs %d -> Taking %d from list1\n", 
                    list1->val, list2->val, list1->val);
            current->next = list1;
            list1 = list1->next;
        } else {
            fprintf(output_file, "  Comparing %d vs %d -> Taking %d from list2\n", 
                    list1->val, list2->val, list2->val);
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }
    
    // Attach remaining nodes
    if (list1 != NULL) {
        fprintf(output_file, "  Attaching remaining nodes from list1\n");
        current->next = list1;
    } else if (list2 != NULL) {
        fprintf(output_file, "  Attaching remaining nodes from list2\n");
        current->next = list2;
    }
    
    // The merged list starts from dummy->next
    Node *mergedHead = dummy->next;
    
    displayList(mergedHead, "Merged List");
    
    // Free dummy node
    free(dummy);
    
    return mergedHead;
}

// Free linked list
void freeList(Node *head) {
    while (head != NULL) {
        Node *temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("Error: Could not create output file\n");
        return 1;
    }
    
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "EXPERIMENT 8: LINKED LIST\n");
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "AIM: Merge two sorted Linked Lists\n\n");
    
    printf("\n--- Create First Sorted Linked List ---\n");
    fprintf(output_file, "\n--- FIRST LINKED LIST ---\n");
    Node *list1 = createLinkedList();
    
    printf("\n--- Create Second Sorted Linked List ---\n");
    fprintf(output_file, "\n--- SECOND LINKED LIST ---\n");
    Node *list2 = createLinkedList();
    
    // Merge the lists
    Node *mergedList = mergeSortedLists(list1, list2);
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "CONCLUSION:\n");
    fprintf(output_file, "Performed merging of two sorted\n");
    fprintf(output_file, "Linked Lists successfully.\n");
    fprintf(output_file, "====================================\n");
    
    fclose(output_file);
    
    // Free memory
    freeList(mergedList);
    
    printf("\nOutput written to output.txt\n");
    return 0;
}
