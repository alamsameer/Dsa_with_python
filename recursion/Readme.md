# Recursion
[concept](#concept)

[Explanation on easy Question](#easy)

[Explanation on Hard Question](#hard)
## Easy 
<details  >
<summary>Reverse stack using recursion </summary>
<details>
<summary>code </summary>

```py

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

```
 </details>
<details>
<summary>Expaination </summary>
The reverse_stack() function is the main function that is responsible for reversing the stack using recursion. It works by following these steps:

The function first checks if the stack is empty (base case), if so it returns without doing anything.
If the stack is not empty, it removes the last element from the stack and stores it in a variable called last_element.
Then the function calls itself recursively on the remaining stack, this recursive call will continue until the base case is reached, which is when the stack is empty.
Once the recursion reaches the base case, it starts to unwind the stack, and in each call, it calls the insert_at_bottom() function, passing the stack and the last_element as arguments.
The insert_at_bottom() function is a helper function that is used to insert an element at the bottom of the stack. It works by following these steps:

The function first checks if the stack is empty, if so it simply pushes the item to the stack and returns.
If the stack is not empty, the function removes the last element from the stack and stores it in a temporary variable called temp.
Then the function calls itself recursively on the remaining stack and the item as arguments.
Once the recursion reaches the base case, it starts to unwind the stack and in each call, it pushes the removed temp variable back to the stack.
The combination of these two functions allows reversing the stack. The reverse_stack() function is responsible for removing the last element and calling the insert_at_bottom() function recursively. The insert_at_bottom() function is responsible for inserting the removed element at the bottom of the stack using recursion.

</details>
</details> 
 
<details  >
<summary>Count good Number </summary>
<details>
<summary>code </summary>

```js

    def count_good_numbers(n):
    def is_good_digit(d, idx):
        if (idx % 2 == 0 and d % 2 == 0) or (idx % 2 != 0 and d in (2, 3, 5, 7)):
            return True
        return False

    def helper(n, idx):
        if idx == n:
            return 1
        count = 0
        for d in range(10):
            if is_good_digit(d, idx):
                print("before",count)
                count += helper(n, idx + 1)
                print("after",count)

        print("inside helper",n,idx,count)
        return count
    return helper(n, 0)

```
 </details>
<details>
<summary>Expaination </summary>
 the `helper(n, idx)` function is a recursive function that takes two arguments:

n: the number of digits in the number we're trying to generate
idx: the current index of the digit we're generating in the number
The function starts by checking if the current index (idx) is equal to the total number of digits (n). If it is, it means that we've generated a number with n digits and all the digits are valid according to the definition of a good number, so it returns 1 to indicate that this is a good number.

If the current index is not equal to the total number of digits, the function enters a loop where it iterates over all digits from 0 to 9. For each digit, it checks if the digit is a valid digit according to the definition of a good number by calling the is_good_digit(d, idx) function and passing the current digit and the index as arguments. If the digit is valid it calls the helper function recursively with the number of digits (n) and the current index incremented by 1.

The function keeps on adding the count of good numbers for each digit and index.

Finally, the function returns the count variable which contains the number of good numbers with n digits.
The helper(n, 0) function is called with the number of digits (n) and 0 as the initial index of the digit, it returns the final value of the count variable which contains the number of good numbers with n digits.
</details>
</details> 


## Medium
## Hard
# Concept 
[join method](#join-method)

[filter method](#filter-method)

[Backtracking](#backtracking)
## Join method 
The `join()` method in Python is a string method that is used to concatenate a `list` of strings with a specified delimiter. The delimiter is specified as a string argument to the join() method, and the list of strings is passed as an argument to the method. The resulting string is the concatenation of the list of strings, with the delimiter inserted between each string. For example:
```py
>>> list_of_strings = ["Hello", "world", "!"]
>>> delimiter = " "
>>> final_string = delimiter.join(list_of_strings)
>>> print(final_string)
"Hello world !"
```
## filter method

The filter() method in Python is a built-in function that is used to filter a given iterable (list, tuple, etc.) with a specified function, and return an iterator with only the elements that return True when passed to the function. The function is specified as the first argument to the filter() method, and the iterable is passed as the second argument.

For example:
```py
>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> def is_even(num):
...     return num % 2 == 0
...
>>> even_numbers = filter(is_even, numbers)
>>> print(list(even_numbers))
[2, 4, 6, 8, 10]
```
It can also be used with a lambda function:

```py
>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> even_numbers = filter(lambda x: x % 2 == 0, numbers)
>>> print(list(even_numbers))
[2, 4, 6, 8, 10]
```
In python 3.x filter method return filter` object` which needs to be converted to `list or tuple or set` to see the result.

## Backtracking

### overview
A backtracking algorithm is a problem-solving algorithm that uses a brute force approach for finding the desired output.
The Brute force approach tries out all the possible solutions and chooses the desired/best solutions.

Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

Example : For example, consider the SudoKo solving Problem, we try filling digits one by one.

### useCase
Backtracking algorithms are often used in `combinatorial search problems`, where the goal is to find all possible combinations of elements that satisfy certain constraints. These problems include `generating permutations`,` subsets`, or `combinations of elements`,` finding paths in graphs`, `solving mazes`, `solving puzzles`, and so on.

Backtracking is a `depth-first search (DFS) algorithm` that visits all nodes of a tree or a graph in a depth-first manner and prunes (abandon) branches that are not promising. It can be implemented using recursion or using a stack to keep track of the progress of the algorithm

example: for generating paranthesis
```py
def generateParenthesis(n):
    def backtrack(combination, open_count, close_count, n):
        if len(combination) == 2 * n:
            result.append(combination)
            return
        if open_count < n:
            backtrack(combination + '(', open_count + 1, close_count, n)
        if close_count < open_count:
            backtrack(combination + ')', open_count, close_count + 1, n)
            
    result = []
    backtrack('', 0, 0, n)
    return result

```
Explaination:

The function backtrack() takes four parameters:

* combination: a string that represents the current combination of parentheses.
* open_count: the number of open parentheses used in the current combination.
* close_count: the number of close parentheses used in the current combination.
* n: the maximum number of pairs of parentheses to generate.
The function uses the following logic:

* If the length of the combination is equal to 2 * n, it means that we have used the maximum number of parentheses, so the combination is added to the result.

* If the number of open parentheses used is less than n, we add an open parenthesis to the combination and make a recursive call to backtrack().
* If the number of close parentheses used is less than the number of open parentheses used, we add a close parenthesis to the combination and make a recursive call to backtrack().