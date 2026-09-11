# Division in Python

## Task

Read two integers `a` and `b`, then print:
1. The floor division result using `//`
2. The true division result using `/`

## Input

Two integers:

```text
a
b
```

## Output

Print the results of:

```python
a // b
a / b
```

## Sample Input

```text
4
3
```

## Sample Output

```text
1
1.3333333333333333
```

## Solution

```python
a = int(input())

b = int(input())

print(a // b)

print(a / b)
```

## Step-by-Step Explanation

### 1. Read the first integer

```python
a = int(input())
```

`input()` reads the value as a string, and `int()` converts it to an integer.

### 2. Read the second integer

```python
b = int(input())
```

The second input is also converted to an integer.

### 3. Floor division

```python
print(a // b)
```

`//` performs **floor division**.

For example:

```python
4 // 3
```

gives:

```text
1
```

The normal result is `1.333...`, and floor division gives the floor of that value.

### 4. True division

```python
print(a / b)
```

`/` performs **true division**.

```python
4 / 3
```

gives:

```text
1.3333333333333333
```

The result is a floating-point number.

## `/` vs `//`

| Operator | Meaning | Example | Result |
|---|---|---:|---:|
| `/` | True division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |

Easy way to remember:

```text
/  → actual division result
// → floor-divided result
```

## Important: `//` Is Floor Division

For positive numbers, `//` can look like it simply removes the decimal:

```python
7 // 2
# 3
```

But technically it takes the **floor**.

That matters with negative numbers:

```python
-7 // 2
```

Normal division:

```text
-3.5
```

Floor:

```text
-4
```

So the result is:

```text
-4
```

It does not simply truncate toward zero.

## Why Does `/` Return a Decimal?

Python's `/` operator always performs true division:

```python
10 / 2
```

produces:

```text
5.0
```

Even when the mathematical result is a whole number, `/` returns a floating-point result.

## Common Mistakes

### Mistake 1: Confusing `/` and `//`

```python
a / b
```

is true division.

```python
a // b
```

is floor division.

### Mistake 2: Thinking `//` always truncates toward zero

This is incorrect for negative numbers:

```python
-7 // 2
# -4
```

### Mistake 3: Forgetting to convert input

`input()` returns a string, so arithmetic input should be converted:

```python
a = int(input())
b = int(input())
```

## Pattern

```text
Input
  ↓
Convert to integer
  ↓
Perform arithmetic
  ↓
Print result
```

## Key Concepts

- `input()` reads input as a string.
- `int()` converts input to an integer.
- `/` performs true division.
- `//` performs floor division.
- `/` produces a floating-point result.
- `//` uses floor division, which is important with negative numbers.

## Complexity

**Time Complexity:** `O(1)`

**Space Complexity:** `O(1)`

## Key Takeaway

Remember the difference:

```python
7 / 2   # 3.5
7 // 2  # 3
```

`/` asks for the actual division result.

`//` asks for the floor-divided result.
