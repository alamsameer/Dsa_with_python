# Recursion

## Concept used
- [join method](#join-method)

- [filter method](#filter-method)

- [Backtracking](#backtracking)
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
> Refercences
- [https://www.programiz.com/dsa/backtracking-algorithm](https://www.programiz.com/dsa/backtracking-algorithm)

Self notes for Recursion

- Brute Force approach finds all the possible solutions and selects desired solution per given the constraints.
- Dynamic Programming also uses Brute Force approach to find the OPTIMUM solution, either maximum or minimum.
- Backtracking also uses Brute Force approach but to find ALL the solutions.
- Solutions to the Backtracking problems can be represented as State-Space Tree.
- The constrained applied to find the solution is called Bounding function.
- Backtracking follows Depth-First Search method.
- Branch and Bound is also a Brute Force approach, which uses Breadth-First Search method.
### overview
The term `backtracking `suggests that if the current solution is not suitable,` then backtrack and try other solutions`. Thus, `recursion` is used in this approach.

A backtracking algorithm is a problem-solving algorithm that for finding the desired output.
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