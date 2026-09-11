# Runner-Up Score in Python

## Task

Given a list of scores, find the **runner-up score**.

The runner-up score is the **second-highest distinct score** in the list.

For example:

```text
Scores: 2 3 6 6 5
Highest: 6
Runner-up: 5
```

The duplicate `6` does not count as a separate ranking.

---

## Input

### First line

An integer `n`, representing the number of scores.

### Second line

`n` space-separated integers representing the scores.

Example:

```text
5
2 3 6 6 5
```

---

## Output

Print the runner-up score.

For the sample input:

```text
5
2 3 6 6 5
```

the output is:

```text
5
```

---

## Solution

```python
n = int(input())

arr = [ int(i) for i in input().split() ]

mx = arr[0]

for score in arr:

    if score > mx:

        mx = score

sm = -101

for score in arr:

    if score > sm and score < mx:

        sm = score

print(sm)
```

---

# Step-by-Step Explanation

## 1. Read the number of scores

```python
n = int(input())
```

`input()` reads the value as a string.

`int()` converts it into an integer.

For:

```text
5
```

we get:

```python
n = 5
```

---

## 2. Read all scores

```python
arr = [ int(i) for i in input().split() ]
```

This is a **list comprehension**.

First:

```python
input()
```

reads something like:

```text
2 3 6 6 5
```

Then:

```python
.split()
```

breaks it into separate strings:

```python
["2", "3", "6", "6", "5"]
```

Then:

```python
int(i)
```

converts each string into an integer.

So `arr` becomes:

```python
[2, 3, 6, 6, 5]
```

---

# Finding the Highest Score

## 3. Start with the first score as the maximum

```python
mx = arr[0]
```

Instead of assuming a particular maximum value, we use the first element as the initial maximum.

For:

```python
arr = [2, 3, 6, 6, 5]
```

we initially have:

```python
mx = 2
```

---

## 4. Find the maximum score

```python
for score in arr:

    if score > mx:

        mx = score
```

The loop checks every score.

### Example

Starting with:

```text
mx = 2
```

Check:

```text
2 > 2 → False
```

Check:

```text
3 > 2 → True
mx = 3
```

Check:

```text
6 > 3 → True
mx = 6
```

Next:

```text
6 > 6 → False
```

Finally:

```text
5 > 6 → False
```

So:

```python
mx = 6
```

The highest score has been found.

---

# Finding the Runner-Up

## 5. Start the second-highest value

```python
sm = -101
```

`sm` is used to store the runner-up score.

The important part is that the initial value must be **lower than any valid score** according to the problem's constraints.

Here, `-101` is being used as the starting value.

---

## 6. Find the largest score below the maximum

```python
for score in arr:

    if score > sm and score < mx:

        sm = score
```

This condition has **two parts**.

### Condition 1

```python
score > sm
```

The current score must be greater than the runner-up found so far.

This allows us to keep improving `sm`.

### Condition 2

```python
score < mx
```

The score must be **less than the highest score**.

This is what prevents the maximum from becoming the runner-up.

Both conditions must be true.

---

## Example Walkthrough

Given:

```python
arr = [2, 3, 6, 6, 5]
```

we already found:

```python
mx = 6
```

and:

```python
sm = -101
```

Now check every score.

### Score = 2

```text
2 > -101 → True
2 < 6    → True
```

So:

```python
sm = 2
```

### Score = 3

```text
3 > 2 → True
3 < 6 → True
```

So:

```python
sm = 3
```

### Score = 6

```text
6 > 3 → True
6 < 6 → False
```

The second condition fails.

Therefore, the highest score is ignored.

### Next score = 6

Same thing:

```text
6 < 6 → False
```

Ignored again.

### Score = 5

```text
5 > 3 → True
5 < 6 → True
```

So:

```python
sm = 5
```

Therefore:

```text
Runner-up = 5
```

---

# Why Do We Need `score < mx`?

This is the most important condition in the solution.

Without:

```python
score < mx
```

the maximum itself could replace `sm`.

For example:

```python
arr = [2, 3, 6, 6, 5]
```

If we only checked:

```python
if score > sm:
```

then `6` would eventually become `sm`.

That would give:

```text
sm = 6
```

which is wrong.

The runner-up must be **strictly smaller than the maximum**.

So:

```python
score < mx
```

means:

> Only consider scores that are below the highest score.

---

# Why Do Duplicate Maximums Not Matter?

Suppose:

```python
arr = [2, 3, 6, 6, 5]
```

There are two `6`s.

But both fail:

```python
score < mx
```

because:

```text
6 < 6 → False
```

Therefore, both maximum values are ignored.

The next largest distinct value is:

```text
5
```

which is the runner-up.

---

# Final Output

```python
print(sm)
```

After the second loop, `sm` contains the second-highest distinct score.

So:

```text
5
```

is printed.

---

# Important Concepts

## 1. Finding a maximum manually

Instead of using:

```python
max(arr)
```

the solution manually finds the maximum:

```python
mx = arr[0]

for score in arr:
    if score > mx:
        mx = score
```

This is an important basic pattern.

---

## 2. Finding the second-highest distinct value

The key idea is:

```text
Find maximum
       ↓
Ignore maximum
       ↓
Find largest remaining value
```

In code:

```python
score > sm and score < mx
```

---

## 3. List Comprehension

This:

```python
arr = [ int(i) for i in input().split() ]
```

is a compact way of doing:

```python
arr = []

for i in input().split():
    arr.append(int(i))
```

Both produce the same type of list.

---

# Common Mistakes

### Mistake 1: Treating the second occurrence of the maximum as the runner-up

For:

```text
2 3 6 6 5
```

the runner-up is **5**, not **6**.

The runner-up must be a distinct score.

---

### Mistake 2: Forgetting `score < mx`

This could allow the maximum itself to become `sm`.

Correct:

```python
if score > sm and score < mx:
```

---

### Mistake 3: Initializing `sm` too high

The initial value of `sm` must be below valid scores.

This solution uses:

```python
sm = -101
```

because that fits the problem's score constraints.

---

### Mistake 4: Assuming `n` is used in the loops

`n` tells us how many scores should be provided, but the actual loops iterate directly over:

```python
arr
```

So:

```python
for score in arr:
```

means:

> Take each score from the list one by one.

---

# Pattern

This problem uses a **two-pass selection pattern**:

```text
Input scores
     ↓
Find maximum
     ↓
Ignore maximum
     ↓
Find largest value below maximum
     ↓
Print runner-up
```

The important logical pattern is:

```python
if score > sm and score < mx:
    sm = score
```

---

# Complexity

There are two loops over the array.

First loop:

```text
O(n)
```

Second loop:

```text
O(n)
```

Together:

```text
O(n) + O(n) = O(n)
```

### Time Complexity

```text
O(n)
```

### Space Complexity

The input list stores `n` scores:

```text
O(n)
```

The extra variables `mx` and `sm` use constant space:

```text
O(1)
```

Overall auxiliary space:

```text
O(1)
```

If counting the input array itself, total storage is `O(n)`.

---

# Key Takeaways

1. The runner-up means the **second-highest distinct value**.
2. First find the maximum.
3. During the second pass, ignore anything equal to the maximum.
4. Keep updating `sm` whenever a larger valid runner-up is found.
5. The key condition is:

```python
if score > sm and score < mx:
```

Think of it as:

```text
greater than my current runner-up
AND
still below the highest score
```

That is the entire trick. Humans have apparently decided that sorting a list is too straightforward, so we now get to practice maintaining a ranking manually.
