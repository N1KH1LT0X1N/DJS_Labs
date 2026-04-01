#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 10000

typedef struct {
    char data[MAX_SIZE];
    int top;
} Stack;

FILE *output_file;

// Initialize stack
Stack *createStack() {
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->top = -1;
    return s;
}

// Push element onto stack
void push(Stack *s, char ch) {
    if (s->top < MAX_SIZE - 1) {
        s->data[++s->top] = ch;
    }
}

// Pop element from stack
char pop(Stack *s) {
    if (s->top >= 0) {
        return s->data[s->top--];
    }
    return '\0';
}

// Peek at top element
char peek(Stack *s) {
    if (s->top >= 0) {
        return s->data[s->top];
    }
    return '\0';
}

// Check if stack is empty
int isEmpty(Stack *s) {
    return s->top == -1;
}

// Check if character is opening bracket
int isOpeningBracket(char ch) {
    return (ch == '(' || ch == '{' || ch == '[');
}

// Check if characters match
int matchingBrackets(char open, char close) {
    if (open == '(' && close == ')') return 1;
    if (open == '{' && close == '}') return 1;
    if (open == '[' && close == ']') return 1;
    return 0;
}

// Validate parenthesis
int isValid(char *s) {
    Stack *stack = createStack();
    int length = strlen(s);
    
    fprintf(output_file, "\nValidating string: \"%s\"\n", s);
    fprintf(output_file, "String length: %d\n", length);
    fprintf(output_file, "\nProcessing characters:\n");
    
    for (int i = 0; i < length; i++) {
        char ch = s[i];
        fprintf(output_file, "  Step %d: Character '%c' ", i + 1, ch);
        
        if (isOpeningBracket(ch)) {
            push(stack, ch);
            fprintf(output_file, "-> PUSH to stack. Stack top: '%c'\n", ch);
        } else if (ch == ')' || ch == '}' || ch == ']') {
            if (isEmpty(stack)) {
                fprintf(output_file, "-> ERROR: No matching opening bracket!\n");
                free(stack);
                return 0;
            }
            
            char top = pop(stack);
            fprintf(output_file, "-> POP from stack (got '%c'). ", top);
            
            if (!matchingBrackets(top, ch)) {
                fprintf(output_file, "ERROR: Brackets don't match! '%c' with '%c'\n", top, ch);
                free(stack);
                return 0;
            }
            fprintf(output_file, "Brackets match: '%c' with '%c'\n", top, ch);
        }
    }
    
    int result = isEmpty(stack);
    fprintf(output_file, "\nFinal stack status: %s\n", result ? "EMPTY (Valid)" : "NOT EMPTY (Invalid)");
    
    free(stack);
    return result;
}

int main() {
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("Error: Could not create output file\n");
        return 1;
    }
    
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "EXPERIMENT 9: STACK\n");
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "AIM: Validate the correctness of\n");
    fprintf(output_file, "parenthesis using Stack\n\n");
    
    char input[MAX_SIZE];
    
    printf("====== PARENTHESIS VALIDATION ======\n");
    printf("Enter a string with brackets: ");
    fgets(input, MAX_SIZE, stdin);
    
    // Remove newline if present
    size_t len = strlen(input);
    if (input[len - 1] == '\n') {
        input[len - 1] = '\0';
    }
    
    fprintf(output_file, "User Input: %s\n", input);
    
    int valid = isValid(input);
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "RESULT: ");
    if (valid) {
        fprintf(output_file, "VALID\n");
        printf("\nResult: VALID - All brackets are correctly matched!\n");
    } else {
        fprintf(output_file, "INVALID\n");
        printf("\nResult: INVALID - Bracket mismatch found!\n");
    }
    fprintf(output_file, "====================================\n");
    
    // Test with more examples
    fprintf(output_file, "\n\n====================================\n");
    fprintf(output_file, "ADDITIONAL TEST CASES:\n");
    fprintf(output_file, "====================================\n");
    
    char *testCases[] = {
        "()",
        "()[]{}", 
        "(]",
        "([])",
        "{[()]}",
        "(((",
        ")))",
        "([)]"
    };
    
    int testCount = sizeof(testCases) / sizeof(testCases[0]);
    
    for (int i = 0; i < testCount; i++) {
        fprintf(output_file, "\nTest %d: \"%s\" -> %s\n", 
                i + 1, 
                testCases[i], 
                isValid(testCases[i]) ? "VALID" : "INVALID");
    }
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "CONCLUSION:\n");
    fprintf(output_file, "Correctness of parenthesis is\n");
    fprintf(output_file, "performed using Stack successfully.\n");
    fprintf(output_file, "====================================\n");
    
    fclose(output_file);
    
    printf("\nOutput written to output.txt\n");
    return 0;
}
