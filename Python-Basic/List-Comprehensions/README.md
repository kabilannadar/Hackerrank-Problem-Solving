# List Comprehensions: 3D Grid Coordinates

## Task

You are given four integers:

- `x`
- `y`
- `z`
- `n`

Create a list containing every possible coordinate `[i, j, k]` where:

```text
0 ≤ i ≤ x
0 ≤ j ≤ y
0 ≤ k ≤ z
```

Exclude coordinates where:

```text
i + j + k == n
```

The problem specifically asks you to use a **list comprehension**.

---

## Python Solution

```python
x = int(input())

y = int(input())

z = int(input())

n = int(input())

data = [ [i, j, k] for i in range(0, x + 1) for j in range (0, y + 1) for k in range (0, z + 1) if i+j+k !=n ]

print(data)
```

---

# How the List Comprehension Works

The important line is:

```python
data = [ [i, j, k] for i in range(0, x + 1) for j in range (0, y + 1) for k in range (0, z + 1) if i+j+k !=n ]
```

A list comprehension generally follows this structure:

```python
[expression for item in iterable if condition]
```

Here, we have **three loops** and one condition.

```text
[i, j, k]
    ↓
for i
    ↓
for j
    ↓
for k
    ↓
if i + j + k != n
```

---

## 1. Expression

```python
[i, j, k]
```

This is what gets added to the final list.

For example:

```text
[0, 1, 2]
```

represents one possible coordinate.

---

## 2. First Loop

```python
for i in range(0, x + 1)
```

Generates:

```text
0, 1, 2, ..., x
```

`x + 1` is used because the ending value of `range()` is excluded.

---

## 3. Second Loop

```python
for j in range(0, y + 1)
```

Generates:

```text
0, 1, 2, ..., y
```

For every value of `i`, all possible values of `j` are considered.

---

## 4. Third Loop

```python
for k in range(0, z + 1)
```

Generates:

```text
0, 1, 2, ..., z
```

For every combination of `i` and `j`, every possible `k` is checked.

---

## 5. Condition

```python
if i+j+k != n
```

Only coordinates whose sum is **not** equal to `n` are added.

For example, if:

```text
n = 3
```

then:

```text
[0, 1, 2]
```

is excluded because:

```text
0 + 1 + 2 = 3
```

But:

```text
[0, 1, 1]
```

is included because:

```text
0 + 1 + 1 = 2
```

---

# Equivalent Nested Loops

The exact same logic could be written using regular nested loops:

```python
data = []

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j + k != n:
                data.append([i, j, k])

print(data)
```

The list comprehension simply puts the same logic into a compact form:

```python
data = [
    [i, j, k]
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
    if i + j + k != n
]
```

---

# Important Point: Order of the Loops

The list comprehension:

```python
[
    [i, j, k]
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
]
```

works exactly like:

```python
for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
```

So the order matters.

It generates coordinates in lexicographic order:

```text
[0, 0, 0]
[0, 0, 1]
[0, 0, 2]
[0, 1, 0]
[0, 1, 1]
...
```

---

# Understanding the `range()`

### Why `x + 1`?

Suppose:

```text
x = 2
```

Then:

```python
range(0, x + 1)
```

becomes:

```python
range(0, 3)
```

which generates:

```text
0, 1, 2
```

That gives all values satisfying:

```text
0 ≤ i ≤ 2
```

The same logic applies to `y` and `z`.

---

# Example

Suppose:

```text
x = 1
y = 1
z = 1
n = 2
```

All coordinates are:

```text
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
```

Now remove coordinates where:

```text
i + j + k = 2
```

That removes:

```text
[0, 1, 1]
[1, 0, 1]
[1, 1, 0]
```

The remaining coordinates are stored in `data`.

---

# Pattern

This problem practices:

- List comprehensions
- Nested iteration
- `range()`
- Conditional filtering
- Creating nested lists
- Working with multiple variables

---

# List Comprehension Mental Model

When you see:

```python
[expression for x in iterable if condition]
```

think:

```text
Generate
→ Check condition
→ Keep valid values
```

For nested comprehensions:

```python
[
    [i, j, k]
    for i in ...
    for j in ...
    for k in ...
    if ...
]
```

think:

```text
Generate every combination
→ Filter invalid combinations
→ Store the remaining combinations
```

---

# Common Mistakes

## 1. Forgetting `+ 1`

Incorrect:

```python
range(0, x)
```

This stops at `x - 1`.

Correct:

```python
range(0, x + 1)
```

This includes `x`.

---

## 2. Using the wrong condition

The requirement is to exclude coordinates where the sum equals `n`.

Correct:

```python
if i + j + k != n
```

---

## 3. Changing the loop order

The order:

```python
for i ...
for j ...
for k ...
```

affects the order in which coordinates are generated.

---

# Key Takeaway

The main idea is understanding how multiple `for` clauses work inside one list comprehension.

This:

```python
[
    [i, j, k]
    for i in range(0, x + 1)
    for j in range(0, y + 1)
    for k in range(0, z + 1)
    if i + j + k != n
]
```

is simply a compact version of:

```python
for i in ...:
    for j in ...:
        for k in ...:
            if ...:
                append(...)
```

Once you can mentally expand a list comprehension into its equivalent loops, complex comprehensions become much easier to understand.

---

# Complexity

There are:

```text
(x + 1) × (y + 1) × (z + 1)
```

possible coordinate combinations before filtering.

**Time:** `O((x + 1)(y + 1)(z + 1))`

**Space:** `O((x + 1)(y + 1)(z + 1))` in the worst case for the resulting list.
