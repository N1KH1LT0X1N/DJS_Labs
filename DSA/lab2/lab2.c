#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
 * Simple Singly Linked List Implementation in C
 *
 * Each node contains an integer value and a pointer to the next node.
 * The list supports basic operations: insertion at head/tail, deletion,
 * search, traversal (print), and freeing the list.
 *
 * This C program demonstrates the structure and operations of a
 * singly linked list with a short main() driver.
 */

// --- node definition --------------------------------------------------------

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// --- utility functions ------------------------------------------------------

// allocate a new node with given value
Node *create_node(int value) {
    Node *n = (Node *)malloc(sizeof(Node));
    if (!n) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    n->data = value;
    n->next = NULL;
    return n;
}

// insert at beginning of list
void insert_head(Node **head, int value) {
    Node *n = create_node(value);
    n->next = *head;
    *head = n;
}

// insert at end of list
void insert_tail(Node **head, int value) {
    Node *n = create_node(value);
    if (*head == NULL) {
        *head = n;
        return;
    }
    Node *cur = *head;
    while (cur->next != NULL)
        cur = cur->next;
    cur->next = n;
}

// search for value; return pointer or NULL
Node *search(Node *head, int value) {
    Node *cur = head;
    while (cur != NULL) {
        if (cur->data == value)
            return cur;
        cur = cur->next;
    }
    return NULL;
}

// delete first occurrence of value
bool delete_value(Node **head, int value) {
    Node *cur = *head;
    Node *prev = NULL;
    while (cur != NULL) {
        if (cur->data == value) {
            if (prev == NULL) {
                // deleting head
                *head = cur->next;
            } else {
                prev->next = cur->next;
            }
            free(cur);
            return true;
        }
        prev = cur;
        cur = cur->next;
    }
    return false;
}

// print list contents
void print_list(Node *head) {
    Node *cur = head;
    printf("[ ");
    while (cur != NULL) {
        printf("%d ", cur->data);
        cur = cur->next;
    }
    printf("]\n");
}

// free whole list
void free_list(Node *head) {
    Node *cur = head;
    while (cur != NULL) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }
}

// --- driver to demonstrate operations -------------------------------------

int main(void) {
    Node *list = NULL; // initially empty

    printf("Inserting at head: 3, 2, 1\n");
    insert_head(&list, 3);
    insert_head(&list, 2);
    insert_head(&list, 1);
    print_list(list);  // should print [ 1 2 3 ]

    printf("Appending at tail: 4, 5\n");
    insert_tail(&list, 4);
    insert_tail(&list, 5);
    print_list(list);  // [ 1 2 3 4 5 ]

    printf("Searching for 3... ");
    Node *found = search(list, 3);
    if (found)
        printf("found (data=%d)\n", found->data);
    else
        printf("not found\n");

    printf("Deleting value 2...\n");
    if (delete_value(&list, 2))
        print_list(list);  // [ 1 3 4 5 ]
    else
        printf("Value not present\n");

    printf("Deleting head (1) and tail (5)...\n");
    delete_value(&list, 1);
    delete_value(&list, 5);
    print_list(list);  // [ 3 4 ]

    printf("Freeing list\n");
    free_list(list);
    list = NULL;

    return 0;
}
