# DSA Labs Complete Guide

This guide explains everything you need to know about your Data Structures and Algorithms labs. Each lab covers fundamental concepts that are essential for programming.

---

## Table of Contents

1. [Lab 0: Searching Algorithms](#lab-0-searching-algorithms)
2. [Lab 1: Sorting Algorithms](#lab-1-sorting-algorithms)
3. [Lab 2: Singly Linked List](#lab-2-singly-linked-list)
4. [Lab 3: Infix to Postfix Conversion](#lab-3-infix-to-postfix-conversion)
5. [Lab 4: Linear Queue](#lab-4-linear-queue)
6. [Lab 5: Binary Search Tree](#lab-5-binary-search-tree)
7. [Lab 6: Searching and Sorting](#lab-6-searching-and-sorting)
8. [Lab 7: Hashing](#lab-7-hashing)
9. [Lab 8: Merging Sorted Linked Lists](#lab-8-merging-sorted-linked-lists)
10. [Lab 9: Stack for Parenthesis Validation](#lab-9-stack-for-parenthesis-validation)
11. [Lab 10: Circular Queue](#lab-10-circular-queue)

---

## Lab 0: Searching Algorithms

### What is Searching?

Searching is the process of finding a specific element in a collection of data. The two main searching algorithms you learned are:

### 1. Linear Search

**How it works:**
- Checks each element from start to end, one by one
- Returns the index if found, returns -1 if not found

**Time Complexity:** O(n) - Linear time
- Best case: O(1) (element at first position)
- Worst case: O(n) (element at last position or not found)
- Average case: O(n/2) ≈ O(n)

**When to use:**
- Small arrays
- Unsorted data
- When you only search once

**Example:**
```c
int linear_search(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}
```

### 2. Binary Search

**How it works:**
- Array MUST be sorted first
- Repeatedly divides the search interval in half
- Checks the middle element and eliminates half of the remaining elements

**Time Complexity:** O(log n) - Logarithmic time
- Much faster than linear search for large arrays
- log₂(1000) ≈ 10 comparisons vs 1000 for linear search

**When to use:**
- Large sorted arrays
- When you search multiple times in the same data

**Example:**
```c
int binary_search(int arr[], int n, int key) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key)
            return mid;
        if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}
```

**Key Takeaway:** Binary search is exponentially faster but requires sorted data. The trade-off is the cost of sorting first.

---

## Lab 1: Sorting Algorithms

### What is Sorting?

Sorting arranges elements in a specific order (usually ascending). You learned two important sorting algorithms.

### 1. Selection Sort

**How it works:**
- Find the minimum element in the unsorted portion
- Swap it with the first unsorted element
- Repeat for the remaining unsorted portion

**Time Complexity:** O(n²) for all cases
- Always makes the same number of comparisons regardless of input
- Not stable (can change relative order of equal elements)

**Space Complexity:** O(1) - sorts in place

**When to use:**
- Small datasets
- When memory is limited
- Educational purposes

**Example:**
```c
void selection_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        // Swap
        int temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }
}
```

### 2. Quick Sort

**How it works:**
- Choose a "pivot" element
- Partition array so elements < pivot are on left, > pivot are on right
- Recursively sort left and right partitions

**Time Complexity:**
- Average case: O(n log n)
- Worst case: O(n²) - when pivot is always smallest/largest
- Best case: O(n log n)

**Space Complexity:** O(log n) - recursive stack space

**When to use:**
- Large datasets
- General-purpose sorting
- When average performance matters more than worst case

**Example:**
```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    // Swap pivot to correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    
    return i + 1;
}
```

**Performance Analysis from your lab:**
- Quick Sort is significantly faster than Selection Sort for large arrays
- Selection Sort: Predictable O(n²) but slow
- Quick Sort: Average O(n log n) - industry standard

---

## Lab 2: Singly Linked List

### What is a Linked List?

A linked list is a linear data structure where elements are stored in nodes. Each node contains:
- **Data:** The actual value
- **Next:** A pointer to the next node

Unlike arrays, linked lists are not stored in contiguous memory locations.

### Structure
```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

### Key Operations

**1. Insert at Head (Beginning):**
```c
void insert_head(Node **head, int value) {
    Node *n = create_node(value);
    n->next = *head;
    *head = n;
}
```
- Time: O(1) - constant time

**2. Insert at Tail (End):**
```c
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
```
- Time: O(n) - must traverse to end

**3. Search:**
```c
Node *search(Node *head, int value) {
    Node *cur = head;
    while (cur != NULL) {
        if (cur->data == value)
            return cur;
        cur = cur->next;
    }
    return NULL;
}
```
- Time: O(n) - linear search

**4. Delete:**
```c
bool delete_value(Node **head, int value) {
    Node *cur = *head;
    Node *prev = NULL;
    while (cur != NULL) {
        if (cur->data == value) {
            if (prev == NULL)
                *head = cur->next;  // Deleting head
            else
                prev->next = cur->next;
            free(cur);
            return true;
        }
        prev = cur;
        cur = cur->next;
    }
    return false;
}
```
- Time: O(n)

### Advantages vs Arrays

| Linked List | Array |
|-------------|-------|
| Dynamic size | Fixed size |
| Easy insertion/deletion | Insertion/deletion is expensive |
| No wasted memory | May have wasted memory |
| No random access | O(1) random access |
| Extra memory for pointers | No extra memory |

### When to use Linked Lists:
- When you need frequent insertions/deletions
- When size changes frequently
- When you don't need random access

---

## Lab 3: Infix to Postfix Conversion

### What are these notations?

**Infix Notation:** `A + B` (operator between operands) - How we normally write expressions
**Postfix Notation:** `A B +` (operator after operands) - Also called Reverse Polish Notation

### Why convert to Postfix?

Postfix is easier for computers to evaluate because:
- No need for parentheses
- No need to consider operator precedence during evaluation
- Can be evaluated using a simple stack

### Conversion Algorithm (Using Stack)

**Rules:**
1. Scan the infix expression left to right
2. If operand → add to output
3. If '(' → push to stack
4. If ')' → pop from stack to output until '(' is found
5. If operator → pop operators with higher/equal precedence from stack to output, then push current operator
6. At end, pop all remaining operators

**Precedence (highest to lowest):**
- `^` (exponentiation) - 3
- `*`, `/` - 2
- `+`, `-` - 1

**Example:**
```
Infix:  A + B * C
Postfix: A B C * +

Steps:
1. A → output: A
2. + → stack: +
3. B → output: A B
4. * → * has higher precedence than +, push: stack: + *
5. C → output: A B C
6. End → pop all: output: A B C * +
```

### Stack Implementation for Conversion

```c
void infix_to_postfix(const char *infix, char *postfix) {
    OpStack st;
    opstack_init(&st);
    
    while (*infix != '\0') {
        if (isalnum(*infix)) {
            // Operand - add to output
            // ...
        } else if (*infix == '(') {
            opstack_push(&st, '(');
        } else if (*infix == ')') {
            // Pop until '('
            // ...
        } else if (is_operator(*infix)) {
            // Handle operator precedence
            // ...
        }
        infix++;
    }
    
    // Pop remaining operators
    // ...
}
```

### Key Concept
The stack helps us defer operators until we know their operands are ready. This is the classic use case for stacks in expression processing.

---

## Lab 4: Linear Queue

### What is a Queue?

A Queue is a FIFO (First In, First Out) data structure. Think of it like a line at a store:
- First person to arrive gets served first
- New people join at the back
- People leave from the front

### Basic Operations

**Enqueue:** Add element to rear
**Dequeue:** Remove element from front
**Peek:** Look at front element without removing
**isEmpty:** Check if queue is empty
**isFull:** Check if queue is full

### Circular Implementation

A circular queue reuses empty spaces at the front after dequeues. Without circular implementation, once you reach the end of the array, you can't add more elements even if there's space at the front.

**Key formula:** `(index + 1) % MAX_SIZE` - wraps around to beginning

```c
typedef struct {
    int items[MAX_QUEUE_SIZE];
    int front;
    int rear;
    int size;
} Queue;

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
```

### Time Complexities
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)

### Real-world Applications
- Print job scheduling
- Task scheduling in operating systems
- BFS (Breadth-First Search) in graphs
- Call center phone systems

---

## Lab 5: Binary Search Tree (BST)

### What is a Binary Search Tree?

A BST is a tree data structure where:
- Each node has at most 2 children (left and right)
- Left child < parent < right child
- All nodes in left subtree < parent < all nodes in right subtree

This property enables efficient searching.

### Structure
```c
typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} Node;
```

### Insertion

```c
Node* insertNode(Node* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data) {
        root->left = insertNode(root->left, data);
    } else if (data > root->data) {
        root->right = insertNode(root->right, data);
    }
    
    return root;
}
```

**Time Complexity:**
- Average: O(log n) - balanced tree
- Worst: O(n) - skewed tree (like a linked list)

### Tree Traversals

**1. Inorder (Left → Root → Right):**
```c
void inorder(Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}
```
- Result: Sorted order!
- Time: O(n)

**2. Preorder (Root → Left → Right):**
```c
void preorder(Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}
```
- Used to create a copy of the tree

**3. Postorder (Left → Right → Root):**
```c
void postorder(Node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}
```
- Used to delete a tree (delete children before parent)

### Why BST?
- Fast search: O(log n) average
- Fast insert: O(log n) average
- Maintains sorted order
- Dynamic size

---

## Lab 6: Searching and Sorting (Reinforcement)

This lab reinforces concepts from Labs 0 and 1:
- **Linear Search:** O(n) - works on any array
- **Binary Search:** O(log n) - requires sorted array
- **Bubble Sort:** O(n²) - simple but slow sorting algorithm

### Bubble Sort

**How it works:**
- Compare adjacent elements
- Swap if they're in wrong order
- Repeat until no swaps needed

```c
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

**Time Complexity:** O(n²) for all cases
**Space Complexity:** O(1)

### Key Takeaway
Binary search is much faster than linear search, but requires the array to be sorted first. The sorting cost (O(n²)) must be considered if you only search once.

---

## Lab 7: Hashing

### What is Hashing?

Hashing is a technique to map data of arbitrary size to fixed-size values using a **hash function**. It enables O(1) average-case search, insert, and delete operations.

### Hash Function

A hash function converts a key into an index:
```c
int hashFunction(int key) {
    return key % TABLE_SIZE;  // Modulo operation
}
```

**Example:** If TABLE_SIZE = 7
- Key 15 → 15 % 7 = 1 → index 1
- Key 22 → 22 % 7 = 1 → index 1 (collision!)

### Collision Resolution

When two keys map to the same index, it's called a **collision**. Your lab uses **Linear Probing**:

**Linear Probing:** If index i is occupied, try i+1, i+2, etc.

```c
void insert(HashEntry *hashTable, int key, int value) {
    int hkey = hashFunction(key);
    int i = 0;
    int index;
    
    while (i < TABLE_SIZE) {
        index = (hkey + i) % TABLE_SIZE;  // Linear probing
        
        if (hashTable[index].used == 0) {
            hashTable[index].key = key;
            hashTable[index].value = value;
            hashTable[index].used = 1;
            return;
        }
        i++;
    }
}
```

### Time Complexity
- Average case: O(1)
- Worst case: O(n) - when all keys collide

### Advantages
- Very fast lookups
- Good for caching
- Used in databases, hash tables, dictionaries

### Disadvantages
- Collisions can degrade performance
- Not good for range queries
- Hash function quality matters

---

## Lab 8: Merging Sorted Linked Lists

### Problem

Given two sorted linked lists, merge them into one sorted linked list.

### Approach

Use a two-pointer technique:
1. Compare heads of both lists
2. Take the smaller node
3. Advance that list's pointer
4. Repeat until one list is exhausted
5. Attach remaining nodes from the other list

```c
Node *mergeSortedLists(Node *list1, Node *list2) {
    Node *dummy = createNode(0);  // Dummy node to simplify
    Node *current = dummy;
    
    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            current->next = list1;
            list1 = list1->next;
        } else {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }
    
    // Attach remaining nodes
    if (list1 != NULL) {
        current->next = list1;
    } else if (list2 != NULL) {
        current->next = list2;
    }
    
    return dummy->next;
}
```

### Time Complexity
O(n + m) where n and m are lengths of the two lists

### Space Complexity
O(1) - only uses a few pointers

### Key Concept
The dummy node simplifies the code by handling edge cases (empty lists, first node selection) automatically.

---

## Lab 9: Stack for Parenthesis Validation

### Problem

Check if a string has balanced parentheses: `()`, `[]`, `{}`

### Examples
- Valid: `()`, `()[]{}`, `([])`, `{[()]}`
- Invalid: `(]`, `([)]`, `(((`, `)))`

### Stack-Based Solution

**Algorithm:**
1. Scan string left to right
2. If opening bracket → push to stack
3. If closing bracket → pop from stack and check if it matches
4. At end, stack should be empty

```c
int isValid(char *s) {
    Stack *stack = createStack();
    
    for (int i = 0; s[i] != '\0'; i++) {
        char ch = s[i];
        
        if (isOpeningBracket(ch)) {
            push(stack, ch);
        } else if (isClosingBracket(ch)) {
            if (isEmpty(stack)) return 0;  // No matching opening
            
            char top = pop(stack);
            if (!matchingBrackets(top, ch)) {
                return 0;  // Mismatched brackets
            }
        }
    }
    
    return isEmpty(stack);  // Valid if stack is empty
}
```

### Time Complexity
O(n) - single pass through string

### Space Complexity
O(n) - worst case all opening brackets

### Key Concept
Stacks are perfect for matching nested structures because they naturally handle the LIFO (Last In, First Out) nature of nested brackets.

---

## Lab 10: Circular Queue (Josephus Problem)

### Circular Queue

A circular queue is a queue where the last position is connected back to the first position, forming a circle.

**Key difference from linear queue:**
- Can reuse empty spaces at the front
- No wasted memory

```c
typedef struct {
    int *data;
    int front;
    int rear;
    int size;
    int capacity;
} CircularQueue;

void enqueue(CircularQueue *q, int val) {
    if (q->size == q->capacity) return;
    
    if (q->front == -1) {
        q->front = 0;
    }
    
    q->rear = (q->rear + 1) % q->capacity;  // Circular wrap
    q->data[q->rear] = val;
    q->size++;
}
```

### Josephus Problem (Circular Game)

**Problem:** n people stand in a circle. Count k people and eliminate the k-th person. Repeat until one person remains. Who survives?

**Example:** n=5, k=2
- People: 1 2 3 4 5
- Count 2: eliminate 2 → 1 3 4 5
- Count 2: eliminate 4 → 1 3 5
- Count 2: eliminate 1 → 3 5
- Count 2: eliminate 5 → 3
- **Survivor: 3**

### Solution Using Circular Queue

```c
int findWinner(int n, int k) {
    CircularQueue *q = createQueue(n);
    
    // Enqueue all friends
    for (int i = 1; i <= n; i++) {
        enqueue(q, i);
    }
    
    while (q->size > 1) {
        // Count k-1 friends and move them to back
        for (int i = 1; i < k; i++) {
            int friend = dequeue(q);
            enqueue(q, friend);  // Move to back
        }
        
        // Eliminate the k-th friend
        dequeue(q);
    }
    
    return q->data[q->front];
}
```

### Time Complexity
O(n × k) - each elimination requires k operations

### Real-world Applications
- Round-robin scheduling
- Resource allocation
- Gaming algorithms

---

## Summary of Time Complexities

| Operation | Array | Linked List | Stack | Queue | BST (avg) | Hash Table |
|-----------|-------|-------------|-------|-------|-----------|------------|
| Access | O(1) | O(n) | O(n) | O(n) | O(log n) | O(1) |
| Search | O(n) | O(n) | O(n) | O(n) | O(log n) | O(1) |
| Insert | O(n) | O(1) head | O(1) | O(1) | O(log n) | O(1) |
| Delete | O(n) | O(n) | O(1) | O(1) | O(log n) | O(1) |

---

## Key Concepts to Remember

### 1. Time Complexity
- **O(1):** Constant time - best possible
- **O(log n):** Logarithmic - very fast (binary search, BST)
- **O(n):** Linear - proportional to input size
- **O(n log n):** Efficient sorting (quick sort, merge sort)
- **O(n²):** Quadratic - slow for large inputs (bubble sort, selection sort)

### 2. Space Complexity
- **O(1):** Constant extra space
- **O(n):** Linear extra space
- **O(log n):** Logarithmic space (recursive stack)

### 3. When to Use What

**Array:**
- Need fast random access
- Size is known/fixed
- Few insertions/deletions

**Linked List:**
- Frequent insertions/deletions
- Unknown size
- Don't need random access

**Stack:**
- LIFO behavior needed
- Expression evaluation
- Backtracking algorithms
- Parenthesis matching

**Queue:**
- FIFO behavior needed
- Scheduling
- BFS traversal
- Buffer management

**BST:**
- Need fast search + dynamic size
- Need data in sorted order
- Range queries

**Hash Table:**
- Need O(1) average lookups
- Don't need order
- Caching, counting

### 4. Common Patterns

**Two Pointers:** Used in merging, searching
**Dummy Node:** Simplifies linked list operations
**Modulo Operation:** Used for circular structures
**Recursion:** Used for tree traversals
**Hash Function:** Maps keys to indices

---

## Exam Tips

1. **Understand, don't memorize:** Know WHY algorithms work, not just HOW
2. **Practice time complexity:** Be able to analyze any algorithm
3. **Know trade-offs:** When to use which data structure
4. **Draw it out:** Visualize trees, linked lists, arrays
5. **Edge cases:** Empty structures, single elements, full structures
6. **Pointer basics:** Understand `*`, `&`, `->` in C

---

## Common Mistakes to Avoid

1. **Forgetting to free memory:** Always `free()` malloc'd memory
2. **Off-by-one errors:** Check loop conditions carefully
3. **NULL pointer dereference:** Always check if pointer is NULL before using
4. **Not handling edge cases:** What if array is empty? What if queue is full?
5. **Confusing array indices:** 0-indexed vs 1-indexed
6. **Infinite loops:** Make sure recursion/loops have base cases

---

## Final Notes

These labs cover the fundamental data structures and algorithms that every programmer should know. They form the foundation for more advanced topics like:
- Graph algorithms
- Dynamic programming
- Advanced tree structures (AVL, Red-Black trees)
- String algorithms

**Best way to learn:**
1. Understand the concept
2. Implement it yourself
3. Test with different inputs
4. Analyze time/space complexity
5. Practice variations

Good luck with your studies!
