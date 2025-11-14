# Week 2: Python Intermediate Concepts - Study Guide

## Table of Contents
1. [String Formatting](#string-formatting)
2. [Unpacking](#unpacking)
3. [Comprehensions](#comprehensions)
4. [Generators](#generators)
5. [Functional Programming](#functional-programming)
6. [Itertools and Factorial Design](#itertools-and-factorial-design)
7. [Exceptions and Tracebacks](#exceptions-and-tracebacks)
8. [Quick Reference](#quick-reference)

---

## String Formatting

### Three Main Approaches

Python offers multiple ways to format strings, but **f-strings** are the modern, preferred method.

#### 1. String Interpolation Operator `%` (Older Style)

```python
import math

i = 5
s = "pi"

"The value of i is %d" % i  # %d => decimal integer
# "The value of i is 5"

"%s: %f %.2f" % (s, math.pi, math.pi)  # str, float, float with 2 decimals
# "pi: 3.141593 3.14"
```

**Common format specifiers:**
- `%d` - integer
- `%f` - float
- `%s` - string
- `%.2f` - float with 2 decimal places

#### 2. The `format` Function (Rarely Used)

```python
"The value of i is {}".format(i)
"{s}: {pi:f} {pi:.2f}".format(s=s, pi=math.pi)
```

#### 3. F-strings (Preferred ✓)

```python
f"The value of i is {i}"
# "The value of i is 5"

f"{s}: {math.pi:f} {math.pi:.2f}"
# "pi: 3.141593 3.14"
```

### Advanced F-string Features

**Dynamic width formatting:**
```python
width = 5
s = "hi"

print(f"|{s:<{width}}|")  # Left align:  |hi   |
print(f"|{s:>{width}}|")  # Right align: |   hi|
print(f"|{s:^{width}}|")  # Center:      | hi  |
```

**Expressions inside f-strings:**
```python
name = 'David'
age = 40

print(f'Age after five years will be {age+5}')
# "Age after five years will be 45"

print(f'Name with quotes = {name!r}')
# "Name with quotes = 'David'"
```

**Format specifiers:**
- `!r` - repr() representation (adds quotes for strings)
- `!s` - str() representation
- `:<` - left align
- `:>` - right align
- `:^` - center align
- `:.2f` - 2 decimal places

---

## Unpacking

### Basic Tuple Unpacking

**Multiple assignments:**
```python
# Multiple return values
def count_punct(s):
    return (num_periods, num_commas, num_questions)

np, nc, nq = count_punct(s)
```

**Swapping variables:**
```python
a, b = b, a  # No temporary variable needed!
```

**Unpacking strings:**
```python
a, b, c = "abc"
# a='a', b='b', c='c'
```

### Wildcard Unpacking with `*`

**Head/rest pattern:**
```python
L = [5, 6, 7, 8, 9]
head, *rest = L
# head = 5
# rest = [6, 7, 8, 9]
```

**Get first and last:**
```python
first, *middle, last = L
# first = 5
# middle = [6, 7, 8]
# last = 9
```

### Function Arguments: `*args` (Tuple Packing)

Accept variable number of positional arguments:

```python
def max(*args):
    result = args[0]
    for arg in args:
        if arg > result:
            result = arg
    return result

max(4, 5)         # Works
max(4, 5, 6, 7)   # Also works - variable arguments
```

**How it works:**
- `args` becomes a **tuple** containing all positional arguments
- Can be any name, but `*args` is conventional

### Function Arguments: `**kwargs` (Dict Packing)

Accept variable number of keyword arguments:

```python
def f(**kwargs):
    for k in kwargs:
        if k.startswith("_"):
            print(k, kwargs[k])

f(a=1, b=2, _c=3)
# Prints: _c 3
```

**How it works:**
- `kwargs` becomes a **dict** with keyword argument names as keys
- Can be any name, but `**kwargs` is conventional

### Unpacking at Call Time

**Unpack sequences with `*`:**
```python
def f(a, b, c, d):
    print(a + b + c + d)

ab = (1, 2)
f(*ab, 3, 4)  # Unpacks to: f(1, 2, 3, 4)
```

**Unpack dictionaries with `**`:**
```python
cd = {"c": 3, "d": 4}
f(1, 2, **cd)  # Unpacks to: f(1, 2, c=3, d=4)
```

**Combined unpacking:**
```python
ab = (1, 2)
cd = {"c": 3, "d": 4}
f(*ab, **cd)  # f(1, 2, c=3, d=4)
```

### Merging Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"a": 7, "c": 3, "d": 4}

d = {**d1, **d2}
# {"a": 7, "b": 2, "c": 3, "d": 4}
# Note: d2 overwrites d1 for key "a"
```

---

## Comprehensions

### List Comprehensions

**Basic syntax:**
```python
L = [0, 1, 2, 3, 4]
M = [x**2 for x in L]
# [0, 1, 4, 9, 16]
```

**Equivalent to:**
```python
M = []
for x in L:
    M.append(x**2)
```

**With filtering:**
```python
# Only squares of even numbers
M = [x**2 for x in L if x % 2 == 0]
# [0, 4, 16]
```

**Nested comprehensions:**
```python
N = [[1, 2, 3], [4, 5, 6]]
P = [x**2 for M in N for x in M]
# [1, 4, 9, 16, 25, 36]
# Flattens and squares
```

**Equivalent nested loops:**
```python
P = []
for M in N:          # Outer loop comes first
    for x in M:      # Inner loop comes second
        P.append(x**2)
```

### Set Comprehensions

```python
s = {x**2 for x in L}
# Creates a set: {0, 1, 4, 9, 16}
# Note: Uses {} instead of []
```

### Dict Comprehensions

**Basic dict comprehension:**
```python
d = {x: x**2 for x in L}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Inverting a dictionary:**
```python
d = {'a': 17, 'b': 20, 'c': 25}
inverted = {d[k]: k for k in d}
# {17: 'a', 20: 'b', 25: 'c'}
```

**Filtering dict items:**
```python
d = {'a': 17, 'b': 20, 'c': 25}
odd_values = [k for k in d if d[k] % 2 == 1]
# ['a', 'c']
```

### Mathematical Set-Builder Notation

Comprehensions parallel mathematical notation:

**Mathematics:**
$$S = \{x^2 : x \in \{0, 1, 2, 3, 4\}\}$$

**Python:**
```python
S = {x**2 for x in [0, 1, 2, 3, 4]}
```

---

## Generators

### What are Generators?

**Generators yield values one at a time** instead of returning all values at once.

**Benefits:**
- Save memory (don't create entire lists)
- "Lazy" execution - compute only when needed
- Essential for large datasets or infinite sequences

### Basic Generator with `yield`

```python
def gen_squares(start, stop):
    for i in range(start, stop):
        yield i**2

# Doesn't compute all values immediately
for sq in gen_squares(0, 1000000):
    if sq > 100:
        break
    print(sq)
# Prints: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```

**Key difference:**
- `return` gives back one value and exits
- `yield` gives back one value and **pauses** (remembers state)

### Infinite Generators

```python
def all_the_ints():
    i = 0
    while True:
        yield i
        i += 1

for i in all_the_ints():
    if i > 100:
        break
    print(i)
```

This would be **impossible** with a regular function - you can't return an infinite list!

### Practical Example: Reading Large Files

**Bad approach - loads entire file:**
```python
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")  # MemoryError on large files!
    return result
```

**Good approach - reads one line at a time:**
```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

row_count = 0
for row in csv_reader('some_enormous_file.csv'):
    row_count += 1
```

### `yield from`

Delegate to another generator:

```python
def subgen1():
    yield 1
    yield 2

def subgen2():
    yield 3
    yield 4

def gen():
    yield from subgen1()
    yield from subgen2()

list(gen())  # [1, 2, 3, 4]
```

### Generator Comprehensions

Use `()` instead of `[]`:

```python
gc = (x for x in range(20) if x % 2 == 0)

for x in gc:
    print(x)
# Prints: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
```

**⚠️ Warning:** Generators are **exhausted** after iteration:

```python
gc = (x for x in range(5))
list(gc)  # [0, 1, 2, 3, 4]
list(gc)  # [] - empty! Generator exhausted
```

### Example: Pythagorean Triples

**With generator function:**
```python
def pythagorean_triples(n):
    for x in range(1, n):
        for y in range(x, n):
            for z in range(y, n):
                if x**2 + y**2 == z**2:
                    yield (x, y, z)

list(pythagorean_triples(20))
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
```

**With generator comprehension:**
```python
triples = ((x, y, z)
           for x in range(1, 30)
           for y in range(x, 30)
           for z in range(y, 30)
           if x**2 + y**2 == z**2)

list(triples)
```

---

## Functional Programming

### Core Principles

**Functional programming emphasizes:**
1. Functions as building blocks
2. Avoiding side effects
3. Functions as first-class objects (can be passed around)
4. Composition and reusability

### Functions Without Side Effects

**Bad - has side effect:**
```python
def concat(x, y):
    x += y  # Modifies argument!
    return x
```

**Good - no side effects:**
```python
def concat(a, b):
    return a + b  # Creates new value
```

**Why avoid side effects?**
- Easier to test
- Easier to debug
- More predictable
- Can be parallelized

### `any` and `all`

**`any` - returns True if any element is True:**
```python
any([False, False, True, False])  # True
any([False, False, False])        # False
```

**`all` - returns True if all elements are True:**
```python
all([True, True, True])    # True
all([True, False, True])   # False
```

**Practical example:**
```python
def even(n):
    return n % 2 == 0

L = [17, 19, 23, 31, 32]
all(not even(x) for x in L)  # False (32 is even)
any(even(x) for x in L)      # True (32 is even)
```

### `map` - The Central Higher-Order Function

**Map a function over a sequence:**

```python
list(map(len, ["a", "cat", "and", "a", "dog"]))
# [1, 3, 3, 1, 3]
```

**With lambda:**
```python
list(map(lambda x: x**2, [4, 5, 6]))
# [16, 25, 36]
```

**With multiple sequences:**
```python
list(map(lambda x, y: x * y, [1, 2, 3, 4], [5, 1, 5, 1]))
# [5, 2, 15, 4]
```

**Modern alternative - comprehension:**
```python
[x**2 for x in [4, 5, 6]]  # Often more readable
```

### Higher-Order Functions

Functions that take functions as arguments or return functions:

```python
# sorted with custom key function
sorted([-10, -5, 0, 5], key=lambda x: x**2)
# [0, -5, 5, -10]  # Sorted by magnitude
```

**Common higher-order functions:**
- `map(func, iterable)`
- `filter(func, iterable)`
- `sorted(iterable, key=func)`
- `min(iterable, key=func)` / `max(iterable, key=func)`

### Callbacks

**Functions passed to other code to be called later:**

```python
def train_model(data, progress_callback=None):
    for epoch in range(100):
        # Training code...
        if progress_callback:
            progress_callback(epoch)

def print_progress(epoch):
    print(f"Completed epoch {epoch}")

train_model(data, progress_callback=print_progress)
```

**Common uses:**
- GUI programming (button click handlers)
- Event-driven programming
- Training callbacks in ML frameworks
- Async programming

### DRY Principle (Don't Repeat Yourself)

**Bad - magic number repeated:**
```python
def init():
    return random.randrange(640), random.randrange(640)

def move(x, y, dx, dy):
    if x + dx <= 640:
        x += dx
    if y + dy <= 640:
        y += dy
```

**Better - extract the constant:**
```python
GRID_SIZE = 640

def init():
    return random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)

def move(x, y, dx, dy):
    if x + dx <= GRID_SIZE:
        x += dx
    if y + dy <= GRID_SIZE:
        y += dy
```

---

## Itertools and Factorial Design

### The `itertools` Module

Provides powerful tools for creating iterators for efficient looping.

### `itertools.combinations`

**All r-length combinations:**

```python
import itertools

# Handshake problem - who shakes hands?
people = ['a', 'b', 'c', 'd', 'e']
handshakes = list(itertools.combinations(people, r=2))
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'),
#  ('b', 'c'), ('b', 'd'), ('b', 'e'),
#  ('c', 'd'), ('c', 'e'),
#  ('d', 'e')]
```

**With filtering:**
```python
result = []
for handshake in itertools.combinations('abcde', r=2):
    if 'a' in handshake and 'b' in handshake:
        continue  # a and b don't shake hands
    if 'b' in handshake and 'd' in handshake:
        continue  # b and d don't shake hands
    result.append(handshake)
```

### `itertools.product` - Cartesian Product

**All combinations across multiple iterables:**

```python
import itertools

for x, y in itertools.product([1, 2], ['a', 'b']):
    print(x, y)

# Output:
# 1 a
# 1 b
# 2 a
# 2 b
```

### Factorial Design of Experiments

**Use case: Hyperparameter tuning**

```python
def neural_network(alpha, beta, gamma):
    return (alpha * random.random() +
            (1 - beta) * random.randrange(2) / gamma)

# Define hyperparameters to test
alphas = [0.0, 0.1, 0.2]
betas = [0, 1]
gammas = [0.9, 0.99, 0.999, 0.9999]

# Test all combinations
for alpha, beta, gamma in itertools.product(alphas, betas, gammas):
    result = neural_network(alpha, beta, gamma)
    print(f"α={alpha}, β={beta}, γ={gamma}: {result}")
```

**Benefits:**
- No nested for-loops needed
- Easy to add/remove parameters
- Clean, readable code
- Perfect for grid search in ML

**Total combinations:**
```python
len(alphas) * len(betas) * len(gammas)  # 3 * 2 * 4 = 24
```

### Other Useful `itertools` Functions

| Function | Description |
|----------|-------------|
| `permutations(iterable, r)` | All r-length permutations (order matters) |
| `combinations_with_replacement()` | Combinations allowing repeats |
| `count(start, step)` | Infinite counter |
| `cycle(iterable)` | Repeat iterable infinitely |
| `chain(*iterables)` | Concatenate iterables |
| `islice(iterable, stop)` | Slice an iterator |

---

## Exceptions and Tracebacks

### Common Exception Types

| Exception | Cause | Example |
|-----------|-------|---------|
| `NameError` | Variable/function not defined | `sin(3.0)` without `import math` |
| `IndexError` | Invalid list index | `[1, 2, 3][10]` |
| `KeyError` | Invalid dict key | `{'a': 1}['b']` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `ValueError` | Invalid value for operation | `sqrt(-3)` |
| `TypeError` | Wrong type for operation | `(1, 2, 3)[0] = 5` (tuples immutable) |
| `FileNotFoundError` | File doesn't exist | `open('missing.txt')` |
| `AttributeError` | Attribute doesn't exist | `"abc".nonexistent()` |

### Reading Tracebacks

**Example causing an error:**
```python
def f(x):
    return x + 1

def g(x):
    return f(x) * 2

def h(x):
    return g(x) - 1

def j(x):
    return 1 / h(x)

j(-0.5)
```

**Traceback:**
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    j(-0.5)
  File "<stdin>", line 2, in j
    return 1 / h(x)
  File "<stdin>", line 2, in h
    return g(x) - 1
  File "<stdin>", line 2, in g
    return f(x) * 2
  File "<stdin>", line 2, in f
    return x + 1
ZeroDivisionError: division by zero
```

**How to read:**
1. Start at the bottom - that's the actual error
2. Work upward to see the call sequence
3. "Most recent call last" means read bottom-up
4. Each level shows file, line number, function, and code

### Handling Exceptions with `try`-`except`

**Basic structure:**
```python
try:
    # Code that might raise an exception
    risky_operation()
except SomeException:
    # Handle the exception
    print("Something went wrong")
```

**Multiple exception types:**
```python
def f(d, k, x):
    try:
        print(x / d[k])
    except KeyError:
        print(f"The key {k} doesn't exist in {d}")
    except ZeroDivisionError:
        print("You tried to divide by zero")
    except:
        print("Something else bad happened")
```

**Catching multiple exceptions together:**
```python
try:
    risky_operation()
except (ValueError, TypeError):
    print("Got a ValueError or TypeError")
```

**Accessing the exception object:**
```python
try:
    int("not a number")
except ValueError as e:
    print(f"Error: {e}")
# Error: invalid literal for int() with base 10: 'not a number'
```

### Raising Exceptions

**Validate function inputs:**

```python
from math import sqrt

def herons_formula(x, y, z):
    """Calculate triangle area using Heron's formula.
    
    >>> herons_formula(3, 4, 5)
    6.0
    
    >>> herons_formula(10, 2, 2)
    Traceback (most recent call last):
    ...
    ValueError: No such triangle exists with sides 2, 2, 10
    """
    # Order sides so that x <= y <= z
    x, y, z = sorted((x, y, z))
    
    # Validate: sum of two smaller sides must exceed largest
    if x + y < z:
        raise ValueError(f"No such triangle exists with sides {x}, {y}, {z}")
    
    # Apply Heron's formula
    s = (x + y + z) / 2.0
    area = sqrt(s * (s - x) * (s - y) * (s - z))
    return area
```

**Common exceptions to raise:**
- `ValueError` - invalid value (wrong range, type)
- `TypeError` - wrong type entirely
- `RuntimeError` - generic runtime problem
- `NotImplementedError` - feature not implemented yet

### Try-Except-Else-Finally

**Complete structure:**
```python
try:
    # Code that might raise exception
    result = risky_operation()
except SomeException:
    # Handle exception
    print("Error occurred")
else:
    # Runs if NO exception occurred
    print("Success!")
finally:
    # ALWAYS runs (cleanup code)
    close_resources()
```

**Use cases:**
- `else` - code that should only run if try succeeded
- `finally` - cleanup code (closing files, connections)

### Testing Exceptions in Doctests

```python
def divide(a, b):
    """
    >>> divide(10, 2)
    5.0
    
    >>> divide(10, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b
```

**Format:**
1. `Traceback (most recent call last):`
2. `...` (represents omitted traceback)
3. Exception type and message

---

## Quick Reference

### String Formatting Cheat Sheet

```python
# F-strings (preferred)
f"{var}"              # Simple substitution
f"{var:.2f}"          # 2 decimal places
f"{var:10}"           # Width 10
f"{var:<10}"          # Left align, width 10
f"{var:>10}"          # Right align, width 10
f"{var:^10}"          # Center, width 10
f"{expr + 5}"         # Expressions allowed
f"{var!r}"            # repr() format
```

### Unpacking Patterns

```python
a, b = (1, 2)               # Basic unpacking
a, b, c = "abc"             # String unpacking
first, *rest = [1,2,3,4]    # Wildcard unpacking
*start, last = [1,2,3,4]    # Last element
a, *mid, z = [1,2,3,4,5]    # First and last

# Function definitions
def f(*args):               # Variable positional args (tuple)
def f(**kwargs):            # Variable keyword args (dict)

# Function calls
f(*sequence)                # Unpack sequence
f(**dictionary)             # Unpack dict
```

### Comprehension Patterns

```python
# List comprehension
[expr for item in iterable]
[expr for item in iterable if condition]
[expr for x in L1 for y in L2]  # Nested

# Set comprehension
{expr for item in iterable}

# Dict comprehension
{key: value for item in iterable}

# Generator comprehension
(expr for item in iterable)
```

### Generator Patterns

```python
def gen():
    yield value              # Basic yield
    yield from other_gen()   # Delegate

# Generator comprehension
gen = (x for x in range(10))

# Convert to list (exhausts generator)
list(gen)
```

### Functional Programming Tools

```python
# Higher-order functions
map(func, iterable)
filter(func, iterable)
sorted(iterable, key=func)

# Boolean aggregation
any(iterable)
all(iterable)

# Lambda
lambda x: x**2
lambda x, y: x + y
```

### Itertools Essentials

```python
import itertools

# Combinations (order doesn't matter)
itertools.combinations(iterable, r)

# Permutations (order matters)
itertools.permutations(iterable, r)

# Cartesian product
itertools.product(iter1, iter2, ...)

# Other useful ones
itertools.chain(*iterables)      # Concatenate
itertools.count(start, step)     # Infinite counter
itertools.cycle(iterable)        # Infinite repeat
```

### Exception Handling Patterns

```python
# Basic try-except
try:
    code()
except ExceptionType:
    handle()

# Multiple exceptions
try:
    code()
except (Type1, Type2):
    handle()

# Access exception
try:
    code()
except ExceptionType as e:
    print(e)

# Complete structure
try:
    code()
except ExceptionType:
    handle()
else:
    success_code()
finally:
    cleanup()

# Raise exception
raise ValueError("message")
```

### Common Patterns

**Check if all items meet condition:**
```python
all(condition(x) for x in iterable)
```

**Check if any item meets condition:**
```python
any(condition(x) for x in iterable)
```

**Apply function to all items:**
```python
[func(x) for x in iterable]
# or
list(map(func, iterable))
```

**Filter items:**
```python
[x for x in iterable if condition(x)]
# or
list(filter(condition, iterable))
```

**Read large file efficiently:**
```python
def read_file(filename):
    for line in open(filename):
        yield line.strip()
```

**Hyperparameter grid search:**
```python
for params in itertools.product(param1_values, param2_values):
    model.train(*params)
```

---

## Key Takeaways

### Modern Python Style
- **Use f-strings** for string formatting
- **Use comprehensions** instead of manual loops (when readable)
- **Use generators** for large datasets or streams
- **Avoid side effects** when possible

### Memory and Performance
- Generators save memory through lazy evaluation
- Comprehensions are often faster than loops
- `itertools` provides efficient combinatorics

### Code Quality
- Handle exceptions gracefully with try-except
- Raise exceptions for invalid inputs (fail fast)
- Use DRY principle - extract repeated code
- Write functions without side effects when possible

### Functional Programming
- Functions are first-class objects
- Higher-order functions enable powerful abstractions
- `map`, `filter`, `any`, `all` for common patterns
- Callbacks for flexibility and customization

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 2*
