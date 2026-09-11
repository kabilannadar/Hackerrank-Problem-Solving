# What's Your Next Move? - Conditional Statements

## Problem

Given a positive integer `n`, perform the following conditional actions:

- If `n` is odd, print `Weird`.
- If `n` is even and in the inclusive range `2` to `5`, print `Not Weird`.
- If `n` is even and in the inclusive range `6` to `20`, print `Weird`.
- If `n` is even and greater than `20`, print `Not Weird`.

## Input Format

A single line containing a positive integer `n`.

## Constraints

`1 <= n <= 100`

## Output Format

Print `Weird` if the number is weird. Otherwise, print `Not Weird`.

---

## Examples

### Sample Input 0

```text
3
```

### Sample Output 0

```text
Weird
```

### Explanation

`3` is odd, so it is `Weird`.

---

### Sample Input 1

```text
24
```

### Sample Output 1

```text
Not Weird
```

### Explanation

`24` is even and greater than `20`, so it is `Not Weird`.

---

## Logic

| Condition | Output |
|---|---|
| `n` is odd | `Weird` |
| `n` is even and `2 <= n <= 5` | `Not Weird` |
| `n` is even and `6 <= n <= 20` | `Weird` |
| `n` is even and `n > 20` | `Not Weird` |

## Python Solution

```python
n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
```

## How It Works

### 1. Check whether `n` is odd

```python
n % 2 != 0
```

If the remainder after dividing by `2` is not `0`, the number is odd.

### 2. Check the even range `2` to `5`

```python
2 <= n <= 5
```

Python allows chained comparisons like this.

### 3. Check the even range `6` to `20`

```python
6 <= n <= 20
```

If `n` falls in this range, print `Weird`.

### 4. Handle everything else

```python
else:
    print("Not Weird")
```

At this point, the remaining case is an even number greater than `20`.

## Pattern

This problem is mainly about:

- `if / elif / else`
- Modulo `%`
- Range checking
- Chained comparisons

## Complexity

**Time:** `O(1)`

**Space:** `O(1)`
