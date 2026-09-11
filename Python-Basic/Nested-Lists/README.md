# Nested Lists: Find the Second Lowest Score

## Task

Given the names and scores of `n` students, store each student's data in a **nested list**.

Find the **second lowest distinct score** and print the names of all students who have that score.

If multiple students have the second lowest score, their names should be printed in alphabetical order.

---

## Python Solution

```python
n = int(input())

data = []

for i in range(n):

    name = input()

    score = float(input())

    data.append([score, name])

data.sort()

lowest = data[0][0]

for score, name in data:

    if score > lowest:

        second = score

        break

for score, name in data:

    if score == second:

        print(name)
```

---

# Understanding Nested Lists

The main data structure is:

```python
data = []
```

Each student is stored as a smaller list:

```python
[score, name]
```

For example:

```text
[37.21, "Harry"]
```

After reading multiple students:

```python
[
    [37.21, "Harry"],
    [37.21, "Berry"],
    [37.2, "Tina"],
    [41.0, "Akriti"],
    [39.0, "Harsh"]
]
```

This is a **nested list** because a list contains other lists.

```text
data
 ├── [37.21, "Harry"]
 ├── [37.21, "Berry"]
 ├── [37.2, "Tina"]
 ├── [41.0, "Akriti"]
 └── [39.0, "Harsh"]
```

---

# Step-by-Step

## 1. Read the number of students

```python
n = int(input())
```

This tells us how many student records need to be read.

---

## 2. Create an empty list

```python
data = []
```

This will hold all student records.

---

## 3. Read each student's name and score

```python
for i in range(n):

    name = input()

    score = float(input())

    data.append([score, name])
```

For each student, the name and score are stored together:

```python
data.append([score, name])
```

For example:

```python
data.append([37.21, "Harry"])
```

creates:

```text
[[37.21, "Harry"]]
```

After another student:

```text
[[37.21, "Harry"], [37.21, "Berry"]]
```

---

# Why Store `[score, name]`?

The solution stores:

```python
[score, name]
```

instead of:

```python
[name, score]
```

because the list is later sorted:

```python
data.sort()
```

Python compares the first element first.

Since the score is first, the records are primarily sorted by score.

Example:

```python
[
    [41.0, "Akriti"],
    [37.2, "Tina"],
    [39.0, "Harsh"],
    [37.21, "Harry"]
]
```

after:

```python
data.sort()
```

becomes:

```python
[
    [37.2, "Tina"],
    [37.21, "Harry"],
    [39.0, "Harsh"],
    [41.0, "Akriti"]
]
```

---

# Accessing Elements Inside a Nested List

Suppose:

```python
data = [
    [37.2, "Tina"],
    [37.21, "Harry"]
]
```

Then:

```python
data[0]
```

gives:

```text
[37.2, "Tina"]
```

And:

```python
data[0][0]
```

gives:

```text
37.2
```

While:

```python
data[0][1]
```

gives:

```text
Tina
```

So:

```python
lowest = data[0][0]
```

means:

> Take the first inner list, then take its score.

---

# Finding the Lowest Score

```python
data.sort()

lowest = data[0][0]
```

Because `data` is sorted in ascending order, the first record contains the lowest score.

For example:

```text
[
    [37.2, "Tina"],
    [37.21, "Berry"],
    [37.21, "Harry"],
    [39.0, "Harsh"],
    [41.0, "Akriti"]
]
```

Therefore:

```python
data[0][0]
```

is:

```text
37.2
```

---

# First Loop: Find the Second Lowest Score

```python
for score, name in data:

    if score > lowest:

        second = score

        break
```

Each inner list is unpacked automatically.

For:

```python
[37.21, "Harry"]
```

Python assigns:

```text
score = 37.21
name = "Harry"
```

The condition:

```python
score > lowest
```

ignores the lowest score and looks for the first larger score.

Because the list is sorted, the first score greater than `lowest` is the **second lowest distinct score**.

---

## Why `break`?

```python
break
```

stops the loop immediately.

Once we find:

```text
second = 37.21
```

there is no need to continue searching because the list is already sorted.

---

# Second Loop: Find Matching Students

```python
for score, name in data:

    if score == second:

        print(name)
```

Now the second lowest score is known.

The loop checks every student and prints the names whose score matches:

```python
second
```

For example:

```text
[37.21, "Berry"]
[37.21, "Harry"]
```

both match.

---

# Why Are Names Alphabetical?

Because `data` is sorted using:

```python
data.sort()
```

The score is the first element.

When two students have the same score, Python compares the second element, which is the name.

For:

```python
[37.21, "Harry"]
[37.21, "Berry"]
```

the scores are equal, so Python compares:

```text
"Harry"
"Berry"
```

and places `Berry` before `Harry`.

Therefore the final loop prints the names alphabetically.

---

# Nested List vs Nested Loop

These are different concepts.

### Nested List

A list containing other lists:

```python
data = [
    [37.21, "Harry"],
    [37.21, "Berry"]
]
```

### Nested Loop

A loop inside another loop:

```python
for i in range(n):
    for j in range(n):
        ...
```

This solution uses a **nested list**, but it does not use a loop inside another loop.

It uses two separate loops over the same nested list.

---

# List Unpacking

This:

```python
for score, name in data:
```

works because every inner list contains exactly two values:

```python
[score, name]
```

For example:

```python
[37.21, "Harry"]
```

is automatically unpacked into:

```text
score → 37.21
name  → "Harry"
```

The longer equivalent is:

```python
for student in data:
    score = student[0]
    name = student[1]
```

Unpacking makes the loop cleaner.

---

# Example

### Input

```text
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

### Nested list before sorting

```python
[
    [37.21, "Harry"],
    [37.21, "Berry"],
    [37.2, "Tina"],
    [41.0, "Akriti"],
    [39.0, "Harsh"]
]
```

### After sorting

```python
[
    [37.2, "Tina"],
    [37.21, "Berry"],
    [37.21, "Harry"],
    [39.0, "Harsh"],
    [41.0, "Akriti"]
]
```

### Lowest score

```text
37.2
```

### Second lowest score

```text
37.21
```

### Matching names

```text
Berry
Harry
```

### Output

```text
Berry
Harry
```

---

# Pattern

This problem practices:

- Nested lists
- `append()`
- `sort()`
- Indexing
- Looping through nested data
- List unpacking
- Finding the second lowest distinct value
- `break`
- Comparing values
- Alphabetical ordering

---

# Common Mistakes

## 1. Storing `[name, score]`

If you use:

```python
data.append([name, score])
```

then:

```python
data.sort()
```

will primarily sort by name.

The solution intentionally uses:

```python
data.append([score, name])
```

so sorting is primarily based on score.

---

## 2. Taking `data[1][0]`

This can fail when the lowest score appears multiple times.

For example:

```text
37.2
37.2
37.21
```

The second lowest **distinct** score is:

```text
37.21
```

not `37.2`.

That is why the solution searches for:

```python
if score > lowest:
```

---

## 3. Forgetting `float()`

Scores can contain decimal values:

```text
37.21
```

so:

```python
score = float(input())
```

is required.

---

# Key Takeaways

The overall flow is:

```text
Read student
      ↓
Store [score, name]
      ↓
Sort nested list
      ↓
data[0][0] → lowest score
      ↓
Find first score > lowest
      ↓
That is the second lowest distinct score
      ↓
Loop through data again
      ↓
Print matching names
```

Important nested-list operations:

```python
data.append([score, name])
```

```python
data.sort()
```

```python
data[0][0]
```

and:

```python
for score, name in data:
```

---

# Complexity

Let `n` be the number of students.

### Building the list

**Time:** `O(n)`

### Sorting

```python
data.sort()
```

**Time:** `O(n log n)`

### Finding the second lowest

**Time:** `O(n)` in the worst case.

### Finding matching names

**Time:** `O(n)`

### Overall

**Time:** `O(n log n)`

**Space:** `O(n)` for storing the nested list.
