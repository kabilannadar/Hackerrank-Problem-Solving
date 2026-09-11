# Arithmetic Operators

## Task

The provided code stub reads two integers, `a` and `b`, from STDIN.

Print three lines:

1. The sum of `a` and `b`
2. The difference of `a` and `b`
3. The product of `a` and `b`

---

## Python Solution

```python
a = int(input())

b = int(input())

print(a + b)

print(a - b)

print(a * b)
```

---

## Step-by-Step

### 1. Read the first integer

```python
a = int(input())
```

- `input()` reads a value from the user.
- `int()` converts the input from a string to an integer.
- The result is stored in `a`.

### 2. Read the second integer

```python
b = int(input())
```

The second input is converted to an integer and stored in `b`.

### 3. Add the two numbers

```python
print(a + b)
```

The `+` operator performs **addition**.

Example:

```text
3 + 2 = 5
```

### 4. Subtract the second number from the first

```python
print(a - b)
```

The `-` operator performs **subtraction**.

Example:

```text
3 - 2 = 1
```

### 5. Multiply the two numbers

```python
print(a * b)
```

The `*` operator performs **multiplication**.

Example:

```text
3 * 2 = 6
```

---

# Arithmetic Operators Used

| Operator | Operation | Example | Result |
|---|---|---|---:|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `3 - 2` | `1` |
| `*` | Multiplication | `3 * 2` | `6` |

---

## Example

For:

```text
a = 3
b = 2
```

The program prints:

```text
5
1
6
```

Because:

```text
3 + 2 = 5
3 - 2 = 1
3 * 2 = 6
```

---

# Input and Output Flow

```text
Input a
   ↓
Input b
   ↓
a + b → print
   ↓
a - b → print
   ↓
a * b → print
```

---

# Important Concepts

## `input()`

```python
input()
```

reads input as a **string**.

For example:

```python
a = input()
```

If the user enters:

```text
3
```

then `a` contains the string:

```python
"3"
```

To use it as an integer:

```python
a = int(input())
```

---

## Arithmetic Operators

Python provides operators for common mathematical operations.

```python
a + b  # addition
a - b  # subtraction
a * b  # multiplication
```

---

# Common Mistake

### Forgetting to convert input to integers

Incorrect:

```python
a = input()
b = input()

print(a + b)
```

If the inputs are:

```text
3
2
```

the result is:

```text
32
```

because strings are concatenated.

Correct:

```python
a = int(input())
b = int(input())

print(a + b)
```

Now:

```text
3 + 2 = 5
```

---

# Key Takeaway

For basic arithmetic:

```python
+  → addition
-  → subtraction
*  → multiplication
```

And when reading integer input:

```python
int(input())
```

---

# Complexity

Each arithmetic operation takes constant time.

**Time:** `O(1)`

**Space:** `O(1)`
