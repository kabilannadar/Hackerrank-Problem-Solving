# Weird or Not Weird

## Task

Given a positive integer `n`, perform the following conditional actions:

- If `n` is odd, print `Weird`.
- If `n` is even and in the inclusive range `2` to `5`, print `Not Weird`.
- If `n` is even and in the inclusive range `6` to `20`, print `Weird`.
- If `n` is even and greater than `20`, print `Not Weird`.

---

## Input Format

A single line containing a positive integer `n`.

## Constraints

```text
1 ≤ n ≤ 100
```

## Output Format

Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

---

## Sample Input 0

```text
3
```

## Sample Output 0

```text
Weird
```

### Explanation

`3` is odd, so the program prints:

```text
Weird
```

---

## Sample Input 1

```text
24
```

## Sample Output 1

```text
Not Weird
```

### Explanation

`24` is even and greater than `20`, so the program prints:

```text
Not Weird
```

---

# Python Solution

```python
n = int(input().strip())

if n % 2 == 1:

    print('Weird')

elif 2 <= n <= 5:

    print('Not Weird')

elif 6 <= n <= 20:

    print('Weird')

elif n > 20:

    print('Not Weird')
```

---

# Step-by-Step

## 1. Read the input

```python
n = int(input().strip())
```

### `input()`

Reads the value entered by the user as a string.

### `.strip()`

Removes leading and trailing whitespace.

### `int()`

Converts the input into an integer.

---

## 2. Check whether `n` is odd

```python
if n % 2 == 1:
    print('Weird')
```

The `%` operator gives the remainder after division.

For example:

```text
3 % 2 = 1
5 % 2 = 1
8 % 2 = 0
```

Therefore:

```python
n % 2 == 1
```

means that `n` is odd.

Any odd number is `Weird`.

---

## 3. Check the even range `2` to `5`

```python
elif 2 <= n <= 5:
    print('Not Weird')
```

This is a Python **chained comparison**.

It means:

```text
2 <= n
AND
n <= 5
```

So the condition is true when `n` is between `2` and `5`, inclusive.

---

## 4. Check the even range `6` to `20`

```python
elif 6 <= n <= 20:
    print('Weird')
```

Again, this is a chained comparison.

If `n` is between `6` and `20`, the program prints:

```text
Weird
```

Because the first condition already checks for odd numbers, reaching this branch means the number is even.

---

## 5. Check numbers greater than `20`

```python
elif n > 20:
    print('Not Weird')
```

If none of the previous conditions matched and `n > 20`, the number is an even number greater than `20`.

So the output is:

```text
Not Weird
```

---

# Decision Flow

The program checks the conditions in order:

```text
Is n odd?
│
├── Yes → Weird
│
└── No
     │
     ├── 2 ≤ n ≤ 5 → Not Weird
     │
     ├── 6 ≤ n ≤ 20 → Weird
     │
     └── n > 20 → Not Weird
```

---

# Why Use `elif`?

`elif` means:

> Check this condition only if the previous condition was false.

For example:

```python
if n % 2 == 1:
    print('Weird')

elif 2 <= n <= 5:
    print('Not Weird')
```

Once one condition is true, the remaining `elif` conditions are skipped.

This is useful when exactly one result should be printed.

---

# Important Concepts

## Modulo `%`

Used to check whether a number is odd or even:

```python
n % 2
```

If the result is:

```text
0 → even
1 → odd
```

---

## Chained Comparisons

Python allows:

```python
2 <= n <= 5
```

instead of:

```python
2 <= n and n <= 5
```

Both represent the same logical condition.

---

## `if / elif`

Use:

```python
if condition:
    ...
elif another_condition:
    ...
```

when conditions need to be checked in sequence.

---

# Test Cases

| `n` | Output | Reason |
|---:|---|---|
| `1` | `Weird` | Odd |
| `2` | `Not Weird` | Even, `2–5` |
| `4` | `Not Weird` | Even, `2–5` |
| `6` | `Weird` | Even, `6–20` |
| `10` | `Weird` | Even, `6–20` |
| `20` | `Weird` | Even, `6–20` |
| `22` | `Not Weird` | Even and greater than `20` |
| `25` | `Weird` | Odd |

---

# Key Takeaways

The main ideas in this problem are:

```python
n % 2
```

for checking odd/even numbers,

```python
2 <= n <= 5
```

for a range check,

and:

```python
if / elif
```

for evaluating multiple conditions in order.

The important reasoning pattern is:

```text
Check the most specific condition first
→ move through the remaining ranges
→ produce one result
```

---

# Complexity

**Time:** `O(1)`

**Space:** `O(1)`
