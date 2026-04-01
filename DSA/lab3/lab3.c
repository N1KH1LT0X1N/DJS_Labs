#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_EXPR_LEN 1024
#define OP_STACK_SIZE 256

// Simple stack for operators (chars)
typedef struct {
    char items[OP_STACK_SIZE];
    int top;
} OpStack;

void opstack_init(OpStack *s) { s->top = -1; }
int opstack_is_empty(OpStack *s) { return s->top == -1; }
int opstack_is_full(OpStack *s) { return s->top == OP_STACK_SIZE - 1; }
void opstack_push(OpStack *s, char c) { if (!opstack_is_full(s)) s->items[++s->top] = c; }
char opstack_pop(OpStack *s) { if (opstack_is_empty(s)) return '\0'; return s->items[s->top--]; }
char opstack_peek(OpStack *s) { if (opstack_is_empty(s)) return '\0'; return s->items[s->top]; }

// Operator utilities
int is_operator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

int precedence(char op) {
    switch (op) {
        case '^': return 3;
        case '*': case '/': return 2;
        case '+': case '-': return 1;
        default: return 0;
    }
}

// Convert infix expression (null-terminated C string) to postfix.
// The output buffer must be large enough; tokens in postfix are space-separated.
// Supports multi-character alphanumeric operands, operators + - * / ^ and parentheses.
void infix_to_postfix(const char *infix, char *postfix, size_t out_size) {
    OpStack st;
    opstack_init(&st);
    postfix[0] = '\0';

    size_t out_len = 0;
    size_t i = 0;
    while (infix[i] != '\0') {
        if (isspace((unsigned char)infix[i])) { i++; continue; }

        // Operand: alphanumeric sequence (identifier or number)
        if (isalnum((unsigned char)infix[i])) {
            char token[128];
            size_t t = 0;
            while (isalnum((unsigned char)infix[i]) && t + 1 < sizeof(token)) {
                token[t++] = infix[i++];
            }
            token[t] = '\0';
            // append token and space
            size_t needed = strlen(token) + 1;
            if (out_len + needed + 1 < out_size) {
                strcat(postfix, token);
                out_len += strlen(token);
                postfix[out_len++] = ' ';
                postfix[out_len] = '\0';
            } else {
                // insufficient space; truncate
                break;
            }
            continue;
        }

        // Left parenthesis
        if (infix[i] == '(') {
            opstack_push(&st, '(');
            i++;
            continue;
        }

        // Right parenthesis: pop until left paren
        if (infix[i] == ')') {
            while (!opstack_is_empty(&st) && opstack_peek(&st) != '(') {
                char op = opstack_pop(&st);
                size_t needed = 2;
                if (out_len + needed + 1 < out_size) {
                    postfix[out_len++] = op;
                    postfix[out_len++] = ' ';
                    postfix[out_len] = '\0';
                }
            }
            if (!opstack_is_empty(&st) && opstack_peek(&st) == '(') opstack_pop(&st);
            i++;
            continue;
        }

        // Operator
        if (is_operator(infix[i])) {
            char curr = infix[i];
            while (!opstack_is_empty(&st) && is_operator(opstack_peek(&st))) {
                char top = opstack_peek(&st);
                int prec_top = precedence(top);
                int prec_curr = precedence(curr);
                // '^' is right-associative
                if ( (prec_top > prec_curr) || (prec_top == prec_curr && curr != '^') ) {
                    char op = opstack_pop(&st);
                    size_t needed = 2;
                    if (out_len + needed + 1 < out_size) {
                        postfix[out_len++] = op;
                        postfix[out_len++] = ' ';
                        postfix[out_len] = '\0';
                    }
                    continue;
                }
                break;
            }
            opstack_push(&st, curr);
            i++;
            continue;
        }

        // Unknown character: skip
        i++;
    }

    // Pop remaining operators
    while (!opstack_is_empty(&st)) {
        char op = opstack_pop(&st);
        if (op == '(' || op == ')') continue;
        size_t needed = 2;
        if (out_len + needed + 1 < out_size) {
            postfix[out_len++] = op;
            postfix[out_len++] = ' ';
            postfix[out_len] = '\0';
        } else break;
    }

    // Trim trailing space if any
    if (out_len > 0 && postfix[out_len - 1] == ' ') postfix[out_len - 1] = '\0';
}

// Small interactive/demo main
int main(void) {
    char infix[MAX_EXPR_LEN];
    char postfix[MAX_EXPR_LEN];

    printf("Infix to Postfix Converter (enter empty line to exit)\n");
    printf("Supports operators: + - * / ^ and parentheses.\n\n");

    while (1) {
        printf("Enter infix expression: ");
        if (!fgets(infix, sizeof(infix), stdin)) break;
        // remove newline
        size_t len = strlen(infix);
        if (len > 0 && infix[len - 1] == '\n') infix[len - 1] = '\0';
        if (infix[0] == '\0') break;

        postfix[0] = '\0';
        infix_to_postfix(infix, postfix, sizeof(postfix));
        printf("Postfix: %s\n\n", postfix);
    }

    printf("Goodbye.\n");
    return 0;
}
