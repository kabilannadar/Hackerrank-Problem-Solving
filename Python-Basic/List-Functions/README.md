# Python Lists: Command-Based List Operations

## Task

Consider a list initialized as:

```python
data = []
```

You are given `N` commands. Each command performs one of the following operations on the list:

1. `insert i e` → Insert integer `e` at position `i`.
2. `print` → Print the current list.
3. `remove e` → Delete the first occurrence of integer `e`.
4. `append e` → Insert integer `e` at the end of the list.
5. `sort` → Sort the list in ascending order.
6. `pop` → Remove the last element from the list.
7. `reverse` → Reverse the list.

Process all commands in the order they are given.

---

## Input Format

- The first line contains an integer `n`, the number of commands.
- Each of the next `n` lines contains one of the seven commands described above.

## Constraints

- The elements added to the list are integers.

## Output Format

For every command of type `print`, print the current list on a new line.

---

## Example

### Sample Input

```text
4
append 1
append 2
insert 1 3
print
```

### Step-by-Step

Start with:

```python
data = []
```

#### 1. `append 1`

```python
data.append(1)
```

List becomes:

```text
[1]
```

#### 2. `append 2`

```python
data.append(2)
```

List becomes:

```text
[1, 2]
```

#### 3. `insert 1 3`

```python
data.insert(1, 3)
```

Insert `3` at index `1`:

```text
[1, 3, 2]
```

#### 4. `print`

Prints:

```text
[1, 3, 2]
```

---

## Sample Input 0

```text
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
```

## Sample Output 0

```text
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
```

---

# Python Solution

```python
N = int(input())

data = []

for i in range(N):

    command = input().split(' ')

    if command[0] == 'insert':

        data.insert(int(command[1]), int(command[2]))

    elif command[0] == 'print':

        print(data)

    elif command[0] == 'remove':

        data.remove(int(command[1]))

    elif command[0] == 'append':

        data.append(int(command[1]))

    elif command[0] == 'sort':

        data.sort()

    elif command[0] == 'pop':

        data.pop()

    elif command[0] == 'reverse':

        data.reverse()

    else:

        pass
```

---

# Step-by-Step Explanation

## 1. Read the number of commands

```python
N = int(input())
```

`N` tells us how many command lines must be processed.

---

## 2. Create the list

```python
data = []
```

The list starts empty.

Every command modifies this same list.

---

## 3. Process commands one by one

```python
for i in range(N):
```

The loop runs exactly `N` times, once for each command.

---

## 4. Split the command

```python
command = input().split(' ')
```

Suppose the input is:

```text
insert 1 3
```

After splitting:

```python
command = ["insert", "1", "3"]
```

The command name is at:

```python
command[0]
```

The arguments are at:

```python
command[1]
command[2]
```

---

# Understanding Each List Operation

## `insert`

Command:

```text
insert i e
```

Code:

```python
data.insert(int(command[1]), int(command[2]))
```

Example:

```python
data = [1, 2]
data.insert(1, 3)
```

Result:

```text
[1, 3, 2]
```

The first argument is the index, and the second is the value.

---

## `print`

Command:

```text
print
```

Code:

```python
print(data)
```

Prints the current list.

---

## `remove`

Command:

```text
remove e
```

Code:

```python
data.remove(int(command[1]))
```

Removes the **first occurrence** of the specified value.

Example:

```python
data = [1, 2, 2, 3]
data.remove(2)
```

Result:

```text
[1, 2, 3]
```

Only the first `2` is removed.

---

## `append`

Command:

```text
append e
```

Code:

```python
data.append(int(command[1]))
```

Adds the value to the end of the list.

Example:

```python
data = [1, 2]
data.append(3)
```

Result:

```text
[1, 2, 3]
```

---

## `sort`

Command:

```text
sort
```

Code:

```python
data.sort()
```

Sorts the list in ascending order.

Example:

```python
data = [5, 2, 9, 1]
data.sort()
```

Result:

```text
[1, 2, 5, 9]
```

---

## `pop`

Command:

```text
pop
```

Code:

```python
data.pop()
```

Removes the last element.

Example:

```python
data = [1, 2, 3]
data.pop()
```

Result:

```text
[1, 2]
```

---

## `reverse`

Command:

```text
reverse
```

Code:

```python
data.reverse()
```

Reverses the current order of the list.

Example:

```python
data = [1, 2, 3]
data.reverse()
```

Result:

```text
[3, 2, 1]
```

---

# Why Use `command[0]`?

Every command starts with its operation name.

For example:

```text
insert 0 5
append 9
remove 5
print
```

After splitting:

```python
["insert", "0", "5"]
["append", "9"]
["remove", "5"]
["print"]
```

So:

```python
command[0]
```

tells the program **which list operation to perform**.

The `if / elif` chain then chooses the matching operation.

---

# Why Convert `command[1]` and `command[2]` to `int`?

`input().split(' ')` produces strings.

For:

```text
append 9
```

we get:

```python
["append", "9"]
```

But list operations need the number `9`, not the string `"9"`.

So:

```python
int(command[1])
```

converts:

```text
"9" → 9
```

For `insert`, both arguments are integers:

```python
int(command[1])
int(command[2])
```

---

# Equivalent Command Mapping

| Command | Python List Method | Purpose |
|---|---|---|
| `insert i e` | `data.insert(i, e)` | Insert at an index |
| `print` | `print(data)` | Display the list |
| `remove e` | `data.remove(e)` | Remove first matching value |
| `append e` | `data.append(e)` | Add to the end |
| `sort` | `data.sort()` | Sort ascending |
| `pop` | `data.pop()` | Remove last element |
| `reverse` | `data.reverse()` | Reverse the list |

---

# Understanding the Full Flow

```text
Read N
  ↓
Create empty list
  ↓
Read command
  ↓
Split command into parts
  ↓
Check command[0]
  ↓
Run corresponding list operation
  ↓
Repeat N times
```

The program is essentially acting like a small **command interpreter** for a Python list.

---

# Common Mistakes

## 1. Forgetting `int()`

Incorrect:

```python
data.append(command[1])
```

This adds a string.

Correct:

```python
data.append(int(command[1]))
```

---

## 2. Confusing `remove()` and `pop()`

```python
data.remove(5)
```

removes the first occurrence of the **value** `5`.

```python
data.pop()
```

removes the **last element**.

They do different things.

---

## 3. Confusing `insert()` arguments

The syntax is:

```python
data.insert(index, value)
```

So:

```python
data.insert(1, 3)
```

means:

> Insert `3` at index `1`.

---

## 4. Forgetting that list methods modify the list

Methods such as:

```python
data.append(...)
data.sort()
data.reverse()
```

change the original list.

They do not require assigning the result back to `data`.

For example:

```python
data = [3, 1, 2]
data.sort()
```

is correct.

Do **not** write:

```python
data = data.sort()
```

because `sort()` modifies the list in place and returns `None`.

---

# Key Takeaways

This problem is mainly about understanding Python list methods and using conditions to map text commands to those methods.

The important methods are:

```python
insert()
append()
remove()
sort()
pop()
reverse()
```

And the central pattern is:

```text
Read command
→ identify operation
→ extract arguments
→ perform operation
→ continue
```

---

# Complexity

The complexity depends on the command:

| Operation | Typical Time |
|---|---:|
| `append()` | `O(1)` amortized |
| `pop()` | `O(1)` |
| `insert()` | `O(n)` |
| `remove()` | `O(n)` |
| `sort()` | `O(n log n)` |
| `reverse()` | `O(n)` |
| `print()` | `O(n)` |

Where `n` is the current size of the list.
