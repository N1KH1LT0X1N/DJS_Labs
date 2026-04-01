#include <stdio.h>
#include <stdlib.h>

// Structure for Tree Node
typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to insert a node in Binary Search Tree
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

// Inorder Traversal: Left -> Root -> Right
void inorder(Node* root, FILE* fp) {
    if (root == NULL) {
        return;
    }
    
    inorder(root->left, fp);
    printf("%d ", root->data);
    fprintf(fp, "%d ", root->data);
    inorder(root->right, fp);
}

// Preorder Traversal: Root -> Left -> Right
void preorder(Node* root, FILE* fp) {
    if (root == NULL) {
        return;
    }
    
    printf("%d ", root->data);
    fprintf(fp, "%d ", root->data);
    preorder(root->left, fp);
    preorder(root->right, fp);
}

// Postorder Traversal: Left -> Right -> Root
void postorder(Node* root, FILE* fp) {
    if (root == NULL) {
        return;
    }
    
    postorder(root->left, fp);
    postorder(root->right, fp);
    printf("%d ", root->data);
    fprintf(fp, "%d ", root->data);
}

// Function to free memory
void deleteTree(Node* root) {
    if (root == NULL) {
        return;
    }
    
    deleteTree(root->left);
    deleteTree(root->right);
    free(root);
}

// Main function
int main() {
    Node* root = NULL;
    int choice, data, numNodes;
    FILE* fp;
    
    printf("\n========== BINARY TREE TRAVERSAL ==========\n");
    
    // Open file for writing output
    fp = fopen("output.txt", "w");
    if (fp == NULL) {
        printf("Error: Could not open file for writing!\n");
        return 1;
    }
    
    fprintf(fp, "========== BINARY TREE TRAVERSAL OUTPUT ==========\n\n");
    
    // Take input for number of nodes
    printf("\nEnter the number of nodes to insert: ");
    scanf("%d", &numNodes);
    fprintf(fp, "Number of nodes inserted: %d\n", numNodes);
    fprintf(fp, "Nodes in order of insertion: ");
    
    // Insert nodes based on user input
    printf("\nEnter %d values to insert in the tree:\n", numNodes);
    for (int i = 0; i < numNodes; i++) {
        printf("Enter node %d value: ", i + 1);
        scanf("%d", &data);
        root = insertNode(root, data);
        fprintf(fp, "%d ", data);
    }
    fprintf(fp, "\n\n");
    
    // Display menu for traversal options
    while (1) {
        printf("\n========== TREE TRAVERSAL MENU ==========\n");
        printf("1. Inorder Traversal (Left -> Root -> Right)\n");
        printf("2. Preorder Traversal (Root -> Left -> Right)\n");
        printf("3. Postorder Traversal (Left -> Right -> Root)\n");
        printf("4. Display All Traversals\n");
        printf("5. Exit\n");
        printf("========================================\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);
        
        fprintf(fp, "\n");
        
        switch (choice) {
            case 1:
                printf("\nInorder Traversal (Left -> Root -> Right): ");
                fprintf(fp, "Inorder Traversal (Left -> Root -> Right): ");
                inorder(root, fp);
                printf("\n");
                fprintf(fp, "\n");
                break;
                
            case 2:
                printf("\nPreorder Traversal (Root -> Left -> Right): ");
                fprintf(fp, "Preorder Traversal (Root -> Left -> Right): ");
                preorder(root, fp);
                printf("\n");
                fprintf(fp, "\n");
                break;
                
            case 3:
                printf("\nPostorder Traversal (Left -> Right -> Root): ");
                fprintf(fp, "Postorder Traversal (Left -> Right -> Root): ");
                postorder(root, fp);
                printf("\n");
                fprintf(fp, "\n");
                break;
                
            case 4:
                printf("\n--- All Traversals ---\n");
                fprintf(fp, "--- All Traversals ---\n");
                
                printf("Inorder Traversal (Left -> Root -> Right): ");
                fprintf(fp, "Inorder Traversal (Left -> Root -> Right): ");
                inorder(root, fp);
                printf("\n\n");
                fprintf(fp, "\n\n");
                
                printf("Preorder Traversal (Root -> Left -> Right): ");
                fprintf(fp, "Preorder Traversal (Root -> Left -> Right): ");
                preorder(root, fp);
                printf("\n\n");
                fprintf(fp, "\n\n");
                
                printf("Postorder Traversal (Left -> Right -> Root): ");
                fprintf(fp, "Postorder Traversal (Left -> Right -> Root): ");
                postorder(root, fp);
                printf("\n\n");
                fprintf(fp, "\n\n");
                break;
                
            case 5:
                printf("\nExiting... Output saved to output.txt\n");
                fprintf(fp, "\n========== END OF OUTPUT ==========\n");
                fprintf(fp, "CONCLUSION: Thus, we have successfully implemented different tree traversal techniques.\n");
                fclose(fp);
                deleteTree(root);
                return 0;
                
            default:
                printf("Invalid choice! Please enter a valid option (1-5).\n");
        }
    }
    
    return 0;
}
