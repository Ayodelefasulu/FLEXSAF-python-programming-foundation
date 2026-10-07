# Debugging Note

## Problem

While working on the Python exercises, I encountered an error when running a function that calculated the average score from a list of scores.

The program worked when the list contained scores, but it failed when an empty list was supplied.

## Error

The program attempted to divide the total score by the number of scores:

```python
average = sum(scores) / len(scores)
```

When `scores` was empty, `len(scores)` was `0`, resulting in:

```text
ZeroDivisionError: division by zero
```

## Cause

The function assumed that the list would always contain at least one score.

However, an empty list is valid input from the perspective of the function, so the function needed to handle that case explicitly.

## Investigation

I reproduced the problem by calling the function with:

```python
calculate_average([])
```

I then examined the calculation and identified that `len(scores)` returned `0`.

This meant the program was effectively attempting:

```python
0 / 0
```

which Python cannot perform.

## Fix

I added input validation before performing the division.

The function now checks whether the list is empty and handles the situation explicitly rather than allowing the program to fail unexpectedly.

## Lesson Learned

This debugging exercise demonstrated the importance of considering edge cases when writing functions.

A function should not only work with expected input; it should also define how it behaves when it receives unusual or invalid input.

It also reinforced the value of automated tests because an empty-list test can help detect this type of problem before the code is used elsewhere.
