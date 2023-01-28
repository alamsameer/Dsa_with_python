# def reverse_stack(stack):
#     # Base case: If the stack is empty, return
#     if not stack:
#         return
#     # Remove the top item from the stack
#     item = stack.pop()
#     # Recursively reverse the remaining stack
#     reverse_stack(stack)
#     # Insert the removed item back at the bottom of the stack
#     insert_at_bottom(stack, item)

# def insert_at_bottom(stack, item):
#     # Base case: If the stack is empty, push the item
#     if not stack:
#         stack.append(item)
#         return
#     # Remove the top item from the stack
#     temp = stack.pop()
#     # Recursively insert the removed item at the bottom
#     insert_at_bottom(stack, item)
#     # Push the removed item back onto the stack
#     stack.append(temp)

# stack = [1, 2, 3, 4, 5]
# reverse_stack(stack)
# print(stack) # Output: [5, 4, 3, 2, 1]

# ******** returning the reversed
def reverse_stack(stack):
    if not stack: #base case
        return
    last_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, last_element)
    return stack

def insert_at_bottom(stack, item):
    # if stack is empty then append item to the last
    if not stack:
        stack.append(item)
        return
    # here the code run until the stack became empty
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)

stack = [1, 2, 3, 4, 5]
reversed_stack = reverse_stack(stack)
print(reversed_stack) # Output: [5, 4, 3, 2, 1]


