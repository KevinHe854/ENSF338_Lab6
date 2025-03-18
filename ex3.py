import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def parse_expression(tokens):
    # Create a stack to keep track of nodes
    stack = []
    i = 0
    
    while i < len(tokens):
        if tokens[i] == '(':
            # Skip opening parenthesis
            i += 1
        elif tokens[i] == ')':
            # Skip closing parenthesis
            i += 1
        elif tokens[i] in ['+', '-', '*', '/']:
            # Create operator node
            operator = Node(tokens[i])
            
            # Pop the right operand from stack
            right = stack.pop()
            
            # Pop the left operand from stack
            left = stack.pop()
            
            # Connect operands to operator node
            operator.left = left
            operator.right = right
            
            # Push operator node to stack
            stack.append(operator)
            
            i += 1
        else:
            # Create leaf node for numbers
            stack.append(Node(int(tokens[i])))
            i += 1
    
    # Final node is the root of the expression tree
    return stack[0]

def evaluate(node):
    # If node is a leaf (operand)
    if not isinstance(node.value, str):
        return node.value
    
    # Evaluate left and right subtrees (operands)
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    
    # Perform operation based on operator
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

def infix_to_postfix(tokens):
    # Convert infix expression to postfix notation
    output = []
    stack = []
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Remove the '('
        elif token in ['+', '-', '*', '/']:
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and 
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        else:  # Operand
            output.append(token)
        
        i += 1
    
    # Pop remaining operators from stack to output
    while stack:
        output.append(stack.pop())
    
    return output

def build_tree_from_postfix(postfix_tokens):
    stack = []
    
    for token in postfix_tokens:
        if token in ['+', '-', '*', '/']:
            # Create operator node
            node = Node(token)
            
            # Pop the right and left operands (in reverse order)
            node.right = stack.pop()
            node.left = stack.pop()
            
            # Push the new subtree onto the stack
            stack.append(node)
        else:
            # Create a leaf node for operands
            stack.append(Node(int(token)))
    
    # The final item on the stack is the root of the tree
    return stack[0]

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex3.py \"expression\"")
        sys.exit(1)
    
    # Get expression from command line and tokenize
    expression = sys.argv[1]
    tokens = expression.split()
    
    # Convert to postfix and build tree
    postfix = infix_to_postfix(tokens)
    root = build_tree_from_postfix(postfix)
    
    # Evaluate expression using post-order traversal
    result = evaluate(root)
    
    # Print result
    print(result)

if __name__ == "__main__":
    main()