# Print a String of Numbers

## Task

Given an integer `n`, print all integers from `1` through `n` as a **single continuous string**, without spaces or new lines between the numbers.

For example, if:

```text
n = 5
```

the output should be:

```text
12345
```

---

## Python Solution

```python
n = int(input())

for i in range(1, n+1):

    print(i, end = '')
```

---

# Step-by-Step

## 1. Read the input

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

If the input is:

```text
5
```

then:

```python
n = 5
```

---

## 2. Loop from `1` to `n`

```python
for i in range(1, n+1):
```

`range(1, n+1)` generates:

```text
1, 2, 3, ..., n
```

The `+1` is necessary because the ending value of `range()` is **not included**.

For:

```text
n = 5
```

the loop values are:

```text
1
2
3
4
5
```

---

## 3. Print without a newline

```python
print(i, end = '')
```

Normally:

```python
print(i)
```

prints the value and then moves to the next line.

The argument:

```python
end = ''
```

replaces the default newline with an empty string.

So the values are printed next to each other:

```text
1
12
123
1234
12345
```

Conceptually, the output is built as:

```text
1
↓
12
↓
123
↓
1234
↓
12345
```

The final output is:

```text
12345
```

---

# Understanding `print()` and `end`

By default:

```python
print(i)
```

is approximately:

```python
print(i, end='\n')
```

The default `end` is a newline.

When we use:

```python
print(i, end='')
```

there is no newline after each value.

### Example

```python
print(1)
print(2)
print(3)
```

Output:

```text
1
2
3
```

But:

```python
print(1, end='')
print(2, end='')
print(3, end='')
```

Output:

```text
123
```

---

# Understanding `range()`

The general form is:

```python
range(start, stop)
```

It includes `start` but excludes `stop`.

Therefore:

```python
range(1, n+1)
```

means:

```text
start at 1
→ continue up to n
→ include n
```

### Example

```python
range(1, 4)
```

produces:

```text
1, 2, 3
```

It does not produce `4`.

That's why the code uses:

```python
range(1, n+1)
```

instead of:

```python
range(1, n)
```

---

# Example

### Input

```text
5
```

### Loop values

```text
i = 1
i = 2
i = 3
i = 4
i = 5
```

### Output

```text
12345
```

---

# Equivalent `while` Loop

The same logic can be written using a `while` loop:

```python
n = int(input())

i = 1

while i <= n:
    print(i, end='')
    i += 1
```

The `for` loop is shorter because `range()` already controls the sequence.

---

# Pattern

This problem practices:

- `for` loops
- `range()`
- Inclusive ranges using `n + 1`
- `print()`
- The `end` parameter
- Printing values on the same line

---

# Common Mistakes

## 1. Using `range(1, n)`

```python
for i in range(1, n):
```

This stops at `n - 1`.

For:

```text
n = 5
```

it produces:

```text
1, 2, 3, 4
```

The correct version is:

```python
range(1, n+1)
```

---

## 2. Forgetting `end=''`

If you write:

```python
for i in range(1, n+1):
    print(i)
```

the output becomes:

```text
1
2
3
4
5
```

But the problem requires:

```text
12345
```

So use:

```python
print(i, end='')
```

---

## 3. Adding a space

This:

```python
print(i, end=' ')
```

produces:

```text
1 2 3 4 5
```

which is different from the required:

```text
12345
```

---

# Key Takeaways

### Generate `1` through `n`

```python
range(1, n+1)
```

### Print without moving to a new line

```python
print(i, end='')
```

### Overall flow

```text
Read n
↓
Generate 1 → n
↓
Take each i
↓
Print i
↓
Do not add a newline
↓
Next i
↓
Final continuous output
```

---

# Complexity

The loop runs `n` times.

**Time:** `O(n)`

**Space:** `O(1)`
