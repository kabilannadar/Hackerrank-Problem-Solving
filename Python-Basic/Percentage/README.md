# Finding the Percentage

## Task

You are given a dictionary containing student names as keys and their marks as values.

For a given `query_name`, calculate the student's **average marks** and print the result rounded to **2 decimal places**.

---

## Python Solution

```python
n = int(input())

student_marks = {}

for _ in range(n):

    name, *line = input().split()

    scores = list(map(float, line))

    student_marks[name] = scores

query_name = input()

marks_avg = sum(student_marks[query_name]) / len(student_marks[query_name])

print(f'{marks_avg:.2f}')
```

---

# Step-by-Step

## 1. Read the number of students

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For example:

```text
3
```

becomes:

```python
n = 3
```

---

## 2. Create an empty dictionary

```python
student_marks = {}
```

The dictionary will store each student's name and their marks.

Example:

```python
{
    "alpha": [20.0, 30.0, 40.0],
    "beta": [30.0, 50.0, 70.0]
}
```

Here:

```text
key   → student name
value → list of marks
```

---

## 3. Read each student's record

```python
for _ in range(n):
```

The loop runs `n` times.

The `_` is used because we do not need the loop variable itself.

---

## 4. Split the input

```python
name, *line = input().split()
```

Suppose the input is:

```text
beta 30 50 70
```

First:

```python
input().split()
```

produces:

```python
["beta", "30", "50", "70"]
```

Then Python uses **sequence unpacking**:

```python
name, *line
```

So:

```text
name → "beta"
line → ["30", "50", "70"]
```

The `*` means:

> Put all remaining values into `line`.

---

# Understanding `*line`

This is an important Python feature.

For:

```python
name, *line = ["beta", "30", "50", "70"]
```

Python assigns:

```python
name = "beta"
line = ["30", "50", "70"]
```

Without `*`:

```python
name, line = ["beta", "30", "50", "70"]
```

Python would raise an unpacking error because there are more values than variables.

---

## 5. Convert the marks to floats

```python
scores = list(map(float, line))
```

At this point:

```python
line
```

contains strings:

```python
["30", "50", "70"]
```

`map(float, line)` converts each value into a floating-point number:

```python
[30.0, 50.0, 70.0]
```

`list()` stores those values as a list.

---

## 6. Store the student in the dictionary

```python
student_marks[name] = scores
```

For:

```text
name = "beta"
scores = [30.0, 50.0, 70.0]
```

the dictionary becomes:

```python
{
    "beta": [30.0, 50.0, 70.0]
}
```

After reading all students:

```python
{
    "alpha": [20.0, 30.0, 40.0],
    "beta": [30.0, 50.0, 70.0]
}
```

---

## 7. Read the student to query

```python
query_name = input()
```

Suppose:

```text
beta
```

Then:

```python
query_name = "beta"
```

---

## 8. Look up the student's marks

```python
student_marks[query_name]
```

If:

```python
query_name = "beta"
```

then:

```python
student_marks["beta"]
```

returns:

```python
[30.0, 50.0, 70.0]
```

---

## 9. Calculate the average

```python
marks_avg = sum(student_marks[query_name]) / len(student_marks[query_name])
```

For:

```python
[30.0, 50.0, 70.0]
```

`sum()` gives:

```text
30 + 50 + 70 = 150
```

`len()` gives:

```text
3
```

Therefore:

```text
150 / 3 = 50.0
```

So:

```python
marks_avg = 50.0
```

---

## 10. Format to 2 decimal places

```python
print(f'{marks_avg:.2f}')
```

The format:

```text
:.2f
```

means:

```text
.2 → 2 digits after the decimal point
f  → floating-point format
```

Therefore:

```text
50.0
```

is printed as:

```text
50.00
```

Another example:

```python
marks_avg = 26.5
```

prints:

```text
26.50
```

---

# Example

### Input

```text
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

### Dictionary after reading the records

```python
{
    "Krishna": [67.0, 68.0, 69.0],
    "Arjun": [70.0, 98.0, 63.0],
    "Malika": [52.0, 56.0, 60.0]
}
```

### Query

```text
Malika
```

Marks:

```text
52, 56, 60
```

Average:

```text
(52 + 56 + 60) / 3
= 168 / 3
= 56
```

Formatted result:

```text
56.00
```

### Output

```text
56.00
```

---

# Important Concepts

## Dictionary

A dictionary stores data as:

```text
key → value
```

In this problem:

```text
student name → marks
```

Example:

```python
student_marks["Malika"]
```

returns:

```python
[52.0, 56.0, 60.0]
```

---

## Sequence Unpacking

This:

```python
name, *line = input().split()
```

separates the first value from all remaining values.

For:

```text
Malika 52 56 60
```

the result is:

```text
name → Malika
line → ["52", "56", "60"]
```

---

## `map()`

```python
map(float, line)
```

applies `float()` to every element in `line`.

Conceptually:

```text
"52" → 52.0
"56" → 56.0
"60" → 60.0
```

---

## `sum()`

```python
sum(scores)
```

adds all values in the list.

Example:

```python
sum([52, 56, 60])
```

gives:

```text
168
```

---

## `len()`

```python
len(scores)
```

returns the number of elements.

Example:

```python
len([52, 56, 60])
```

gives:

```text
3
```

---

# Why Use `float()`?

Marks may contain decimal values.

For example:

```text
26.5
```

Using:

```python
float()
```

allows both:

```text
26
```

and:

```text
26.5
```

to be represented correctly.

---

# Common Mistakes

## 1. Forgetting `*` in unpacking

Incorrect:

```python
name, line = input().split()
```

There can be more than two values.

Correct:

```python
name, *line = input().split()
```

---

## 2. Forgetting to convert the marks

Incorrect:

```python
scores = line
```

The marks remain strings.

Correct:

```python
scores = list(map(float, line))
```

---

## 3. Forgetting the query lookup

The average must be calculated only for the requested student:

```python
student_marks[query_name]
```

---

## 4. Forgetting `.2f`

Incorrect:

```python
print(marks_avg)
```

This may produce:

```text
50.0
```

Correct:

```python
print(f'{marks_avg:.2f}')
```

which produces:

```text
50.00
```

---

# Pattern

This problem practices:

- Dictionaries
- Lists
- Input parsing
- `split()`
- Sequence unpacking
- `*` unpacking
- `map()`
- `float()`
- Dictionary lookup
- `sum()`
- `len()`
- Average calculation
- Float formatting

---

# Overall Flow

```text
Read number of students
        ↓
Create dictionary
        ↓
Read name + marks
        ↓
Separate name from marks
        ↓
Convert marks to floats
        ↓
Store name → marks
        ↓
Read query name
        ↓
Look up marks
        ↓
sum(marks) / len(marks)
        ↓
Format to 2 decimal places
        ↓
Print
```

---

# Key Takeaway

The core pattern is:

```python
name, *line = input().split()
scores = list(map(float, line))
student_marks[name] = scores
```

This is a useful way to parse an input line containing:

```text
one identifier + multiple numeric values
```

Then the average can be calculated with:

```python
sum(student_marks[query_name]) / len(student_marks[query_name])
```

and formatted using:

```python
f'{marks_avg:.2f}'
```

---

# Complexity

Let `n` be the number of students and `m` be the number of marks per student.

Reading and storing the records takes:

**Time:** `O(n × m)`

The dictionary lookup is approximately:

**Time:** `O(1)` average

Calculating the queried student's average takes:

**Time:** `O(m)`

**Space:** `O(n × m)` for storing all student marks.
