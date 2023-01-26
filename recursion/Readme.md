# Recursion
[concept](#concept)

[Explanation on easy Question](#easy)

[Explanation on Medium Question](#medium)

<details  >
<summary>template</summary>
<details>
<summary>code </summary>
 ```js
 ```
</details>
<details>
<summary>Expaination </summary>
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


[Explanation on Hard Question](#hard)
## Easy 
## Medium
## Hard
# Concept 
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

