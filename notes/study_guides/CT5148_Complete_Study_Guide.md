# CT5148 Programming Tools for AI - Complete Study Guide

## Table of Contents

1. [Programming Fundamentals](#1-programming-fundamentals)
2. [Data Structures & Computational Complexity](#2-data-structures--computational-complexity)
3. [Intermediate Programming Concepts](#3-intermediate-programming-concepts)
4. [Numerical Computing & Linear Algebra](#4-numerical-computing--linear-algebra)
5. [Data Analysis & Visualization](#5-data-analysis--visualization)
6. [Machine Learning Foundations](#6-machine-learning-foundations)
7. [Object-Oriented Programming](#7-object-oriented-programming)
8. [Graph Theory & Networks](#8-graph-theory--networks)
9. [Formal Languages & Automata](#9-formal-languages--automata)
10. [Code Reference](#10-code-reference)

---

# 1. Programming Fundamentals

## 1.1 Theoretical Foundations

### What is an Algorithm?

An **algorithm** is a finite sequence of well-defined instructions for solving a problem or performing a computation. Key properties:

- **Definiteness:** Each step is precisely defined
- **Finiteness:** Terminates after a finite number of steps
- **Input/Output:** Takes inputs and produces outputs
- **Effectiveness:** Each step can be carried out in finite time

A **program** is a concrete implementation of an algorithm in a specific programming language.

### The Execution Model

Python uses an **interpreted execution model**:

1. Source code is parsed into an Abstract Syntax Tree (AST)
2. AST is compiled to bytecode
3. Python Virtual Machine executes bytecode

Understanding this helps explain why Python is slower than compiled languages but more flexible.

### The Substitution Model

Expressions are evaluated **from the inside out**, just like mathematical expressions:

```
f(g(x + 1))
= f(g(5))      # if x = 4
= f(10)        # if g returns input × 2
= 20           # if f returns input × 2
```

This model explains how nested function calls, complex expressions, and operator precedence work.

### Namespaces and Scope

A **namespace** is a mapping from names to objects. Python uses the **LEGB rule** for name resolution:

1. **Local:** Inside the current function
2. **Enclosing:** In enclosing functions (closures)
3. **Global:** Module-level names
4. **Built-in:** Python's built-in names

**Why scope matters:**
- Prevents name collisions between different parts of code
- Enables code reuse and modularity
- Essential for managing complexity in large programs

### Type Systems

Python is **dynamically typed** (types checked at runtime) and **strongly typed** (no implicit type coercion):

| Type | Example | Mutability |
|------|---------|------------|
| `bool` | `True`, `False` | Immutable |
| `int` | `42`, `-17` | Immutable |
| `float` | `3.14` | Immutable |
| `str` | `"hello"` | Immutable |
| `list` | `[1, 2, 3]` | Mutable |
| `tuple` | `(1, 2, 3)` | Immutable |
| `dict` | `{"a": 1}` | Mutable |
| `set` | `{1, 2, 3}` | Mutable |

**Everything in Python is an object**, including functions, classes, and modules.

## 1.2 Control Flow

### Conditional Execution

Programs make decisions using **boolean logic**:

```python
if condition1:
    # executes if condition1 is True
elif condition2:
    # executes if condition1 is False and condition2 is True
else:
    # executes if all conditions are False
```

**Ternary expression:** `result = value_if_true if condition else value_if_false`

### Iteration

**Definite iteration** (for loops): Known number of iterations
```python
for item in iterable:
    process(item)
```

**Indefinite iteration** (while loops): Unknown number of iterations
```python
while condition:
    # continues until condition becomes False
```

### Functions as Abstractions

Functions provide **procedural abstraction**—hiding implementation details behind a simple interface:

```python
def function_name(parameters):
    """Docstring explaining purpose."""
    # Implementation
    return result
```

**Benefits:**
- **Modularity:** Break complex problems into smaller pieces
- **Reusability:** Write once, use many times
- **Testability:** Test components in isolation
- **Readability:** Give meaningful names to operations

### Doctests

**Doctests** are executable examples embedded in docstrings that serve as both documentation and tests. They use the `>>>` prompt to simulate interactive Python sessions.

**Basic Syntax:**
```python
def square(x):
    """
    Return the square of a number.
    
    >>> square(5)
    25
    >>> square(0)
    0
    >>> square(-3)
    9
    """
    return x ** 2
```

**Running Doctests:**
```python
# Method 1: Run all doctests in a module
import doctest
doctest.testmod()

# Method 2: Run doctests for a specific function
import doctest
doctest.run_docstring_examples(square, globals(), verbose=True)

# Method 3: From command line
# python -m doctest mymodule.py -v
```

**Why Use Doctests:**
- **Documentation:** Examples show how to use a function
- **Testing:** Automatically verify examples still work
- **Specification:** Define expected behavior clearly
- **Regression:** Catch bugs when code changes

**Best Practices:**
- Keep examples simple and focused
- Test edge cases (empty input, zero, negative values)
- Use for functions with predictable, simple outputs
- For complex testing, use `unittest` or `pytest` instead

**Example with Multiple Cases:**
```python
def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    >>> is_palindrome("radar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    """
    return s == s[::-1]
```

### Call-by-Value vs Call-by-Reference

Python uses **call-by-object-reference**:

- **Immutable objects:** Behave like call-by-value (changes don't affect original)
- **Mutable objects:** Behave like call-by-reference (changes affect original)

```python
def modify(x, L):
    x = x + 1      # Creates new int, doesn't affect original
    L.append(1)    # Modifies original list

a = 5
M = [1, 2, 3]
modify(a, M)
print(a)  # Still 5
print(M)  # [1, 2, 3, 1] - modified!
```

---

# 2. Data Structures & Computational Complexity

## 2.1 Abstract Data Types

An **Abstract Data Type (ADT)** defines a data type by its behavior (operations) rather than implementation.

### Sequence ADT
- Ordered collection of elements
- Operations: access by index, iterate, slice
- Implementations: `list`, `tuple`, `str`

### Mapping ADT
- Associates keys with values
- Operations: insert, lookup, delete by key
- Implementation: `dict`

### Set ADT
- Unordered collection of unique elements
- Operations: add, remove, membership test, union, intersection
- Implementation: `set`, `frozenset`

## 2.2 Data Structure Implementations

### Arrays (Python Lists)

**Internal structure:** Contiguous block of memory containing pointers to objects.

**Trade-offs:**
- ✅ O(1) random access by index
- ✅ O(1) append (amortized)
- ❌ O(n) insert/delete at beginning (must shift elements)
- ❌ O(n) search (must check each element)

### Hash Tables (Python Dicts and Sets)

**Concept:** Use a **hash function** to map keys to array indices.

**How hashing works:**
1. Compute `hash(key)` → integer
2. Calculate index: `hash(key) % table_size`
3. Store/retrieve value at that index

**Collision handling:** When two keys hash to same index:
- **Linear probing:** Check next slot until empty one found
- **Chaining:** Store linked list at each slot

**Why O(1) average case:**
- Hash computation is constant time
- Array access is constant time
- With good hash function, collisions are rare

**Amortized analysis:** Occasional O(n) rehashing operations are spread across many O(1) operations, yielding O(1) average.

### Trees

**Binary tree properties:**
- Each node has at most 2 children
- Height h tree has at most 2^h - 1 nodes
- Tree with n nodes has height at least log₂(n)

**Applications:** File systems, expression parsing, decision trees, search structures.

## 2.3 Computational Complexity Theory

### Why Complexity Matters

**Wall-clock time** is a poor measure because:
- Hardware speed varies
- Other processes affect timing
- Small inputs mask inefficiency

**Computational complexity** measures how runtime scales with input size—independent of hardware.

### Big O Notation

**Definition:** f(n) = O(g(n)) means f(n) ≤ c·g(n) for some constant c and all sufficiently large n.

**How to calculate:**
1. Count operations as function of input size n
2. Keep only the fastest-growing term
3. Drop constant coefficients

**Example:** 3n² + 5n + 100 → O(n²)

### Complexity Classes

| Class | Name | Growth | Example |
|-------|------|--------|---------|
| O(1) | Constant | Flat | Array access |
| O(log n) | Logarithmic | Very slow | Binary search |
| O(n) | Linear | Proportional | Linear search |
| O(n log n) | Linearithmic | Slightly superlinear | Merge sort |
| O(n²) | Quadratic | Fast | Nested loops |
| O(2ⁿ) | Exponential | Very fast | Subset enumeration |
| O(n!) | Factorial | Extremely fast | Permutation enumeration |

### Practical Implications

For n = 1,000,000:
- O(log n) ≈ 20 operations
- O(n) ≈ 1,000,000 operations
- O(n log n) ≈ 20,000,000 operations
- O(n²) ≈ 1,000,000,000,000 operations (infeasible)

### Worst-Case vs Average-Case

- **Worst-case:** Maximum time for any input of size n (most common analysis)
- **Average-case:** Expected time over all inputs (requires probability distribution)
- **Amortized:** Average over sequence of operations (for data structures)

### Space Complexity

Memory usage also has complexity classes. Trade-offs exist between time and space (e.g., memoization trades space for time).

## 2.4 Python Data Structure Complexity

| Operation | List | Dict/Set | Notes |
|-----------|------|----------|-------|
| Index access | O(1) | N/A | `L[i]` |
| Key access | N/A | O(1)* | `d[k]` |
| Search | O(n) | O(1)* | `x in container` |
| Append | O(1)* | O(1)* | Add to end/add element |
| Insert at start | O(n) | N/A | Must shift elements |
| Delete | O(n) | O(1)* | List must shift |
| Iteration | O(n) | O(n) | Visit each element |
| Sort | O(n log n) | N/A | Timsort algorithm |

\* Average case (amortized)

---

# 3. Intermediate Programming Concepts

## 3.1 Functional Programming Paradigm

### Core Principles

**Functional programming** treats computation as evaluation of mathematical functions:

1. **Pure functions:** Output depends only on inputs (no side effects)
2. **Immutability:** Data is never modified, only transformed
3. **First-class functions:** Functions can be passed as arguments, returned, assigned
4. **Declarative style:** Describe *what* to compute, not *how*

### Why Avoid Side Effects?

**Side effect:** Any modification of state outside the function's local scope.

**Problems with side effects:**
- Harder to test (need to set up external state)
- Harder to debug (behavior depends on history)
- Harder to parallelize (race conditions)
- Harder to reason about (must track global state)

```python
# Bad: Has side effect
total = 0
def add_to_total(x):
    global total
    total += x  # Modifies external state

# Good: Pure function
def add(a, b):
    return a + b  # Only uses inputs, returns new value
```

### Higher-Order Functions

A **higher-order function** takes functions as arguments or returns functions.

**Common patterns:**
- `map(f, iterable)`: Apply f to each element
- `filter(pred, iterable)`: Keep elements where pred is True
- `reduce(f, iterable)`: Accumulate results

**Why useful:** Enable abstraction over behavior, not just data.

### Closures

A **closure** is a function that captures variables from its enclosing scope:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # 'factor' captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
```

Each closure maintains its own captured environment.

## 3.2 Iteration Abstractions

### Comprehensions

**List comprehension** provides declarative syntax for transforming sequences:

```python
[expression for item in iterable if condition]
```

Equivalent to:
```python
result = []
for item in iterable:
    if condition:
        result.append(expression)
```

**Set and dict comprehensions:**
```python
{x**2 for x in range(10)}           # Set
{x: x**2 for x in range(10)}        # Dict
```

### Generators and Lazy Evaluation

**Lazy evaluation** delays computation until results are needed. A normal function is "eager" (does all work immediately), while a generator is "lazy" (does just enough for now, then suspends).

#### The `yield` Keyword

**Generator function:** Uses `yield` instead of `return`:

```python
def count_up(n):
    i = 0
    while i < n:
        yield i  # Pauses here, resumes on next iteration
        i += 1
```

**How `yield` works:**
- `yield` is like `return`, but only gives back one value and **suspends** the generator
- When the caller asks for the **next** value, the generator **resumes** from where it left off
- Resuming is NOT like calling the generator again from the start—it continues execution
- When the generator function ends (or returns), `StopIteration` is raised automatically

```python
def gen_squares(start, stop):
    """Yields squares one at a time instead of building a huge list."""
    for i in range(start, stop):
        yield i ** 2

# Memory efficient - only one value in memory at a time
for sq in gen_squares(0, 1000000):
    if sq > 100:
        break
    print(sq)
```

**Benefits:**
- **Memory efficient:** Only one element in memory at a time
- **Infinite sequences:** Can represent unbounded data
- **Composability:** Chain operations without intermediate lists

#### Infinite Generators

Since generators don't compute all values upfront, they can be infinite:

```python
def all_the_ints():
    """Infinite generator of all non-negative integers."""
    i = 0
    while True:
        yield i
        i += 1

# Consumer decides when to stop
for i in all_the_ints():
    if i > 100:
        break
    print(i)
```

#### `yield from` - Delegating to Sub-generators

`yield from` is a shorthand to yield each item from another iterable or sub-generator:

```python
def subgen1():
    yield 1
    yield 2

def subgen2():
    yield 3
    yield 4

def combined_gen():
    yield from subgen1()  # Yields 1, then 2
    yield from subgen2()  # Yields 3, then 4

for item in combined_gen():
    print(item)  # Prints 1, 2, 3, 4
```

**Use cases for `yield from`:**
- Flattening nested structures
- Depth-first tree traversal
- Composing multiple generators into one

```python
def flatten(nested_list):
    """Flatten arbitrarily nested lists."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # Recursively yield from sublists
        else:
            yield item

list(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
```

#### Generator Comprehensions (Generator Expressions)

A **generator comprehension** uses round brackets `()` instead of square brackets:

```python
# List comprehension - creates full list in memory
squares_list = [x**2 for x in range(1000000)]

# Generator comprehension - lazy, memory efficient
squares_gen = (x**2 for x in range(1000000))
```

**Important:** After a generator has been consumed, it is **exhausted**:

```python
gc = (x for x in range(5))
print(list(gc))  # [0, 1, 2, 3, 4]
print(list(gc))  # [] - exhausted, nothing left!
```

#### Practical Example: Memory-Efficient File Reading

```python
# BAD: Reads entire file into memory (MemoryError for large files)
def read_csv_eager(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

# GOOD: Yields one line at a time
def read_csv_lazy(file_name):
    for row in open(file_name, "r"):
        yield row

# Process huge files without running out of memory
for row in read_csv_lazy('enormous_file.csv'):
    process(row)
```

#### Example: Pythagorean Triples Generator

```python
def pythagorean_triples(n):
    """Generate Pythagorean triples where x <= y <= z < n."""
    for x in range(1, n):
        for y in range(x, n):
            for z in range(y, n):
                if x**2 + y**2 == z**2:
                    yield (x, y, z)

for x, y, z in pythagorean_triples(30):
    print(f"{x}² + {y}² = {z}²")
```

Equivalent generator comprehension:
```python
triples = ((x, y, z) 
           for x in range(1, 30)
           for y in range(x, 30) 
           for z in range(y, 30) 
           if x**2 + y**2 == z**2)
```

### The Iterator Protocol

Any object implementing `__iter__()` and `__next__()` can be iterated:

```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current - 1
```

## 3.3 Error Handling

### Exception Hierarchy

Exceptions form a class hierarchy:
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError
    ├── TypeError
    ├── KeyError
    ├── IndexError
    └── ...
```

### Defensive Programming

**Fail fast:** Detect and report errors as early as possible.

```python
def sqrt(x):
    if x < 0:
        raise ValueError(f"Cannot take sqrt of negative: {x}")
    return x ** 0.5
```

**EAFP vs LBYL:**
- **EAFP** (Easier to Ask Forgiveness than Permission): Try, catch exception
- **LBYL** (Look Before You Leap): Check conditions first

Python prefers EAFP:
```python
# EAFP (Pythonic)
try:
    value = d[key]
except KeyError:
    value = default

# LBYL (less Pythonic)
if key in d:
    value = d[key]
else:
    value = default
```

---

# 4. Numerical Computing & Linear Algebra

## 4.1 Floating-Point Representation

### IEEE 754 Standard

Computers represent real numbers using **floating-point** format:

**64-bit double precision:**
- 1 bit: sign
- 11 bits: exponent
- 52 bits: mantissa (significand)

**Value:** (-1)^sign × 1.mantissa × 2^(exponent - 1023)

### Fundamental Limitations

**The core problem:** Infinite real numbers, finite bits.

**Consequences:**
1. **Rounding errors:** Most decimals can't be represented exactly
2. **Overflow:** Numbers too large become infinity
3. **Underflow:** Numbers too small become zero
4. **Catastrophic cancellation:** Subtracting nearly equal numbers loses precision

### Practical Implications

**Never use `==` for floats:**
```python
0.1 + 0.2 == 0.3  # False!
0.1 + 0.2         # 0.30000000000000004

# Correct approach:
import numpy as np
np.allclose(0.1 + 0.2, 0.3)  # True
abs(0.1 + 0.2 - 0.3) < 1e-9  # True
```

**Special values:**
- `inf`: Positive infinity (overflow)
- `-inf`: Negative infinity
- `nan`: Not a Number (0/0, inf - inf)

## 4.2 Linear Algebra Foundations

### Vectors

A **vector** is an ordered collection of numbers: **v** = [v₁, v₂, ..., vₙ]

**Operations:**
- **Addition:** [a₁, a₂] + [b₁, b₂] = [a₁+b₁, a₂+b₂]
- **Scalar multiplication:** c·[a₁, a₂] = [c·a₁, c·a₂]
- **Dot product:** [a₁, a₂]·[b₁, b₂] = a₁b₁ + a₂b₂

**Geometric interpretation:**
- Vectors represent points or directions in n-dimensional space
- Dot product measures similarity (cos θ = (a·b)/(|a||b|))

### Matrices

A **matrix** is a 2D array of numbers with shape (m × n).

**Key operations:**
- **Element-wise:** Apply operation to corresponding elements (requires same shape)
- **Matrix multiplication:** (m × n) @ (n × p) = (m × p)

**Matrix multiplication intuition:**
- Each output element is dot product of row from A and column from B
- Represents composition of linear transformations

### Broadcasting

**Broadcasting** extends operations to arrays of different shapes by virtually replicating smaller arrays.

**Rules (align from right):**
1. Dimensions must be equal, OR
2. One dimension must be 1 (gets stretched), OR
3. One dimension is missing (gets added)

**Example:**
```
A: (3, 4)    +    B: (4,)     =    Result: (3, 4)
             +       (1, 4)   =    (broadcasted)
```

## 4.3 Vectorization

### Why Vectorization?

**Loop overhead in Python:**
- Type checking for each operation
- Function call overhead
- No compiler optimization

**Vectorized operations:**
- Execute in optimized C/Fortran
- Use SIMD instructions (Single Instruction, Multiple Data)
- Typical speedup: 10-100x

### Thinking in Arrays

**Imperative (avoid):**
```python
result = []
for i in range(len(x)):
    result.append(x[i] ** 2 + y[i])
```

**Vectorized (prefer):**
```python
result = x**2 + y
```

**Key insight:** Describe the transformation on entire arrays, not element-by-element.

## 4.4 NumPy Essentials

### Array Creation
```python
import numpy as np

np.array([1, 2, 3])              # From list
np.zeros((3, 4))                 # 3×4 zeros
np.ones((2, 3))                  # 2×3 ones
np.eye(3)                        # 3×3 identity
np.linspace(0, 1, 100)           # 100 points from 0 to 1
np.arange(0, 10, 0.5)            # Like range for floats
np.random.randn(3, 4)            # Random normal
```

### Array Properties
```python
arr.shape    # Dimensions tuple
arr.ndim     # Number of dimensions
arr.size     # Total elements
arr.dtype    # Data type
```

### Indexing and Slicing
```python
A[i, j]           # Element at row i, col j
A[i, :]           # Entire row i
A[:, j]           # Entire column j
A[1:3, 0:2]       # Slice: rows 1-2, cols 0-1
A[A > 5]          # Boolean indexing
```

### Common Operations
```python
# Element-wise math
np.sqrt(x), np.exp(x), np.log(x)
np.sin(x), np.cos(x)

# Statistics
np.mean(x), np.std(x), np.var(x)
np.min(x), np.max(x), np.sum(x)
np.median(x), np.percentile(x, 75)

# Linear algebra
A @ B             # Matrix multiply
A.T               # Transpose
np.linalg.inv(A)  # Inverse
np.linalg.det(A)  # Determinant
np.dot(a, b)      # Dot product
```

---

# 5. Data Analysis & Visualization

## 5.1 The Data Analysis Pipeline

### Typical Workflow

1. **Load:** Import data from files/databases
2. **Clean:** Handle missing values, fix errors
3. **Explore:** Visualize distributions, relationships
4. **Transform:** Feature engineering, normalization
5. **Model:** Apply statistical/ML methods
6. **Evaluate:** Assess model quality
7. **Communicate:** Present findings

### Exploratory Data Analysis (EDA)

**Goals:**
- Understand data distributions
- Identify patterns and anomalies
- Generate hypotheses
- Guide modeling decisions

**Key questions:**
- What is the shape of distributions?
- Are there outliers?
- How do variables relate to each other?
- Is data missing? Why?

## 5.2 Statistical Measures

### Central Tendency

- **Mean (μ):** Sum divided by count; sensitive to outliers
- **Median:** Middle value; robust to outliers
- **Mode:** Most frequent value

### Dispersion

- **Variance (σ²):** Average squared deviation from mean
- **Standard deviation (σ):** Square root of variance; same units as data
- **Range:** Max - min
- **Interquartile range (IQR):** Q3 - Q1; robust to outliers

### Correlation

**Pearson correlation (r):** Linear relationship between variables
- r = 1: Perfect positive linear relationship
- r = 0: No linear relationship
- r = -1: Perfect negative linear relationship

**Limitations:** Only measures *linear* relationships; causation ≠ correlation

## 5.3 Regression Metrics

### Root Mean Squared Error (RMSE)

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

**Properties:**
- Same units as target variable
- Penalizes large errors more (squared)
- Lower is better
- Sensitive to outliers

### Coefficient of Determination (R²)

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

**Interpretation:**
- R² = 1: Perfect predictions
- R² = 0: Model no better than predicting mean
- R² < 0: Model worse than predicting mean

**When to use each:**
- **RMSE:** When absolute error magnitude matters
- **R²:** When comparing models or assessing fit quality

## 5.4 Visualization Theory

### Principles of Effective Visualization

**Edward Tufte's principles:**
1. **Data-ink ratio:** Maximize ink used for data vs decoration
2. **Chartjunk:** Avoid unnecessary visual elements
3. **Small multiples:** Use repeated similar charts for comparison

### Choosing Chart Types

| Data Type | Chart Type | Use For |
|-----------|------------|---------|
| Distribution (1 var) | Histogram, KDE, boxplot | Understanding spread |
| Relationship (2 vars) | Scatter plot | Correlation, patterns |
| Comparison (categories) | Bar chart, boxplot | Group differences |
| Trend (time series) | Line plot | Change over time |
| Composition | Pie chart, stacked bar | Part-to-whole |
| Distribution (2 vars) | Contour, heatmap | Joint distribution |

### Common Pitfalls

- **Truncated axes:** Can exaggerate differences
- **3D charts:** Usually harder to read than 2D
- **Too many colors:** Limit to ~7 distinguishable categories
- **Missing labels:** Always include axis labels, units, titles

## 5.5 Pandas and Matplotlib

### Pandas Essentials
```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()                    # First 5 rows
df.describe()                # Summary statistics
df['column']                 # Single column
df[['col1', 'col2']]         # Multiple columns
df[df['col'] > 5]            # Filter rows
df.groupby('cat').mean()     # Group and aggregate
```

### Matplotlib Essentials
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='Line')
ax.scatter(x, y, label='Points')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Title')
ax.legend()
plt.savefig('figure.pdf')
```

### Seaborn for Statistical Plots
```python
import seaborn as sns

sns.pairplot(df, hue='category')     # All pairwise relationships
sns.boxplot(x='cat', y='val', data=df)  # Distribution by category
sns.heatmap(corr_matrix, annot=True)    # Correlation heatmap
```

---

# 6. Machine Learning Foundations

## 6.1 Core Concepts

### What is Machine Learning?

**Machine learning** is the study of algorithms that improve through experience.

**Types:**
- **Supervised:** Learn mapping from inputs to outputs (labeled data)
- **Unsupervised:** Find patterns in data (no labels)
- **Reinforcement:** Learn through interaction and rewards

### The Learning Problem

**Given:** Training data {(x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ)}
**Find:** Function f such that f(x) ≈ y for new, unseen x

**Key challenge:** Generalization—performing well on data not seen during training.

### Bias-Variance Tradeoff

**Total Error = Bias² + Variance + Irreducible Noise**

- **Bias:** Error from overly simplistic assumptions (underfitting)
- **Variance:** Error from sensitivity to training data fluctuations (overfitting)

**Underfitting (high bias):**
- Model too simple to capture patterns
- Poor performance on both training and test data

**Overfitting (high variance):**
- Model memorizes training data, including noise
- Good training performance, poor test performance

### Regularization

**Regularization** constrains model complexity to reduce overfitting:
- **L1 (Lasso):** Encourages sparse solutions (feature selection)
- **L2 (Ridge):** Shrinks coefficients toward zero
- **Early stopping:** Stop training before overfitting
- **Dropout:** Randomly disable neurons during training

## 6.2 Model Evaluation

### Train-Test Split

**Why split?** Evaluate generalization on unseen data.

**Typical split:** 70-80% training, 20-30% testing

**Critical rule:** Never use test data during training or model selection.

### Cross-Validation

**Problem with single split:** Results depend on random split.

**K-fold cross-validation:**
1. Split data into k equal folds
2. For each fold i:
   - Train on all folds except i
   - Evaluate on fold i
3. Average the k scores

**Benefits:**
- All data used for both training and validation
- More reliable performance estimate
- Variance estimate (from k scores)

### Metrics

**Classification:**
- **Accuracy:** (TP + TN) / Total
- **Precision:** TP / (TP + FP) — "Of predicted positive, how many correct?"
- **Recall:** TP / (TP + FN) — "Of actual positive, how many found?"
- **F1 Score:** Harmonic mean of precision and recall
- **ROC-AUC:** Area under ROC curve

**Regression:**
- **MSE/RMSE:** Average squared error
- **MAE:** Average absolute error
- **R²:** Proportion of variance explained

### Confusion Matrix

```
                Predicted
              Neg    Pos
Actual  Neg   TN     FP
        Pos   FN     TP
```

- **True Positive (TP):** Correctly predicted positive
- **False Positive (FP):** Incorrectly predicted positive (Type I error)
- **False Negative (FN):** Incorrectly predicted negative (Type II error)
- **True Negative (TN):** Correctly predicted negative

## 6.3 Feature Engineering

### Why Features Matter

**"Coming up with features is difficult, time-consuming, requires expert knowledge. Applied machine learning is basically feature engineering."** — Andrew Ng

### Common Techniques

**Scaling:**
- **Standardization:** (x - μ) / σ → mean 0, std 1
- **Normalization:** (x - min) / (max - min) → range [0, 1]
- **Why:** Many algorithms assume features on similar scales

**Encoding categoricals:**
- **One-hot encoding:** Category → binary vector
- **Label encoding:** Category → integer (use with caution)

**Handling missing values:**
- **Imputation:** Replace with mean/median/mode
- **Indicator:** Add binary feature for missingness
- **Deletion:** Remove rows/columns (lose data)

**Creating new features:**
- **Polynomial features:** x² , x₁x₂
- **Domain knowledge:** ratios, aggregations, time-based

### Data Leakage

**Data leakage:** Using information during training that wouldn't be available at prediction time.

**Common causes:**
- Computing statistics (mean, std) on entire dataset including test
- Features that encode the target
- Time-series: using future data to predict past

**Prevention:** Always fit transformers on training data only.

## 6.4 Scikit-Learn Workflow

### Standard Pattern
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Pipeline prevents data leakage
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# Fit and evaluate
pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
predictions = pipe.predict(X_new)
```

### Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'model__C': [0.1, 1, 10],
    'model__penalty': ['l1', 'l2']
}

grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

---

# 7. Object-Oriented Programming

## 7.1 OOP Principles

### The Four Pillars

**1. Encapsulation**
Bundle data (attributes) and methods that operate on data into a single unit (class). Hide internal details, expose clean interface.

**2. Abstraction**
Provide simplified interface to complex systems. Users don't need to know implementation details.

**3. Inheritance**
Create new classes based on existing classes. Child inherits attributes and methods from parent.

**4. Polymorphism**
Same interface for different underlying types. "One interface, multiple implementations."

### Why OOP?

**Benefits:**
- **Modularity:** Divide complex systems into manageable pieces
- **Reusability:** Inherit and extend existing code
- **Maintainability:** Changes localized to relevant classes
- **Modeling:** Natural way to represent real-world entities

### Classes vs Objects

- **Class:** Blueprint/template defining attributes and methods
- **Object:** Instance of a class with specific attribute values
- **Method:** Function defined within a class

## 7.2 Python OOP

### Class Definition
```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age
    
    def greet(self):          # Instance method
        return f"Hello, I'm {self.name}"
```

### Special Methods (Dunder Methods)

| Method | Purpose | Triggered By |
|--------|---------|--------------|
| `__init__` | Constructor | `Person()` |
| `__repr__` | Developer string | `repr(obj)` |
| `__str__` | User string | `str(obj)`, `print(obj)` |
| `__len__` | Length | `len(obj)` |
| `__eq__` | Equality | `obj == other` |
| `__lt__` | Less than | `obj < other` |
| `__add__` | Addition | `obj + other` |
| `__iter__` | Iteration | `for x in obj` |

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### Duck Typing

**"If it walks like a duck and quacks like a duck, it's a duck."**

Python doesn't check types—it checks capabilities:

```python
def process(obj):
    obj.do_something()  # Works if obj has do_something method

# Any object with do_something() works—no inheritance required
```

## 7.3 Design Patterns

### The Scikit-Learn Estimator Pattern

**Uniform interface enables polymorphism:**

```python
from sklearn.base import BaseEstimator, ClassifierMixin

class MyClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, param=1.0):
        self.param = param
    
    def fit(self, X, y):
        # Training logic
        self.classes_ = np.unique(y)  # Learned attributes end with _
        return self  # Always return self
    
    def predict(self, X):
        # Prediction logic
        return predictions
```

**API conventions:**
- `fit(X, y)` → returns `self`
- `predict(X)` → returns predictions
- `score(X, y)` → returns performance metric
- Learned attributes have trailing underscore

---

# 8. Graph Theory & Networks

## 8.1 Graph Fundamentals

### Definitions

A **graph** G = (V, E) consists of:
- **V:** Set of vertices (nodes)
- **E:** Set of edges connecting vertices

**Types:**
- **Undirected:** Edges have no direction (friendship)
- **Directed:** Edges have direction (Twitter follow)
- **Weighted:** Edges have values (distances)
- **Unweighted:** All edges are equal

### Key Properties

**Degree:** Number of edges connected to a vertex
- In directed graphs: **in-degree** (incoming) and **out-degree** (outgoing)

**Path:** Sequence of vertices connected by edges

**Cycle:** Path that starts and ends at same vertex

**Connected:** Path exists between any two vertices

**Tree:** Connected graph with no cycles

### Graph Representations

**Adjacency Matrix:** n×n matrix where A[i][j] = 1 if edge exists
- Space: O(n²)
- Edge lookup: O(1)
- Good for dense graphs

**Adjacency List:** Each vertex stores list of neighbors
- Space: O(n + m) where m = edges
- Good for sparse graphs

## 8.2 Centrality Measures

Centrality measures identify important nodes in a network.

### Degree Centrality

**Idea:** Important nodes have many connections.

$$C_D(v) = \frac{deg(v)}{n-1}$$

**Limitation:** Doesn't consider network structure.

### Betweenness Centrality

**Idea:** Important nodes lie on many shortest paths between others.

$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

Where σ_st is number of shortest paths from s to t, and σ_st(v) is number passing through v.

**Interpretation:** High betweenness = broker position, controls information flow.

### Eigenvector Centrality (PageRank)

**Idea:** A node is important if connected to important nodes.

**PageRank algorithm:**
1. Start with equal scores for all nodes
2. Iteratively: each node's score = sum of neighbors' scores / their out-degree
3. Repeat until convergence

**Application:** Google's original web page ranking algorithm.

## 8.3 Graph Algorithms

### Traversal Algorithms

**Depth-First Search (DFS):**
- Explore as deep as possible before backtracking
- Uses stack (recursion)
- Applications: Cycle detection, topological sort, path finding

**Breadth-First Search (BFS):**
- Explore level by level
- Uses queue
- Finds shortest path in unweighted graphs
- Applications: Shortest path, level-order traversal

### Shortest Path

**Dijkstra's Algorithm:**
- For weighted graphs with non-negative edges
- Complexity: O((V + E) log V) with priority queue

**Algorithm:**
1. Set distance to source = 0, all others = ∞
2. Visit unvisited node with smallest distance
3. Update distances to neighbors
4. Repeat until target reached

### Topological Sort

**Definition:** Linear ordering of vertices in a DAG such that for every edge (u, v), u comes before v.

**Algorithm:**
1. Find vertex with no incoming edges
2. Remove it and its edges, add to output
3. Repeat until graph is empty

**Applications:**
- Task scheduling with dependencies
- Build systems
- Course prerequisites

## 8.4 NetworkX

```python
import networkx as nx

# Create graph
G = nx.Graph()           # Undirected
D = nx.DiGraph()         # Directed

# Add nodes/edges
G.add_node(1)
G.add_edges_from([(1, 2), (2, 3)])

# Analysis
nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.pagerank(D)

# Algorithms
nx.shortest_path(G, source, target)
list(nx.topological_sort(D))
nx.is_connected(G)
```

---

# 9. Formal Languages & Automata

## 9.1 Finite State Machines

### Definition

A **Finite State Machine (FSM)** is a mathematical model of computation:

- **States:** Finite set of conditions
- **Alphabet:** Finite set of input symbols
- **Transitions:** Rules for moving between states
- **Start state:** Initial state
- **Accept states:** States indicating valid input

### Deterministic vs Non-deterministic

**DFA (Deterministic):** Exactly one transition for each state-symbol pair
**NFA (Non-deterministic):** Multiple possible transitions (theoretically equivalent to DFA)

### Applications

1. **Protocol design:** Network communication states
2. **Lexical analysis:** Tokenizing programming languages
3. **Game AI:** Character behavior states
4. **Input validation:** Pattern matching
5. **Hardware design:** Digital circuit control

### Implementation
```python
class FSM:
    def __init__(self, transitions, initial, accepting):
        self.transitions = transitions
        self.initial = initial
        self.accepting = accepting
    
    def accepts(self, input_string):
        state = self.initial
        for symbol in input_string:
            if symbol not in self.transitions.get(state, {}):
                return False
            state = self.transitions[state][symbol]
        return state in self.accepting
```

## 9.2 Regular Expressions

### Equivalence with FSMs

**Kleene's Theorem:** Regular expressions and finite automata are equivalent—any language described by one can be described by the other.

### Formal Definition

Regular expressions over alphabet Σ:
1. ε (empty string) is a regex
2. Any symbol a ∈ Σ is a regex
3. If R and S are regexes, so are:
   - RS (concatenation)
   - R|S (alternation)
   - R* (Kleene star: zero or more)

### Practical Syntax (Python)

| Pattern | Matches |
|---------|---------|
| `.` | Any character |
| `^`, `$` | Start, end of string |
| `*`, `+`, `?` | 0+, 1+, 0-1 occurrences |
| `[abc]`, `[^abc]` | Character class, negated class |
| `\d`, `\w`, `\s` | Digit, word char, whitespace |
| `(...)` | Capturing group |
| `\|` | Alternation |
| `{n,m}` | n to m occurrences |

### Python re Module
```python
import re

re.match(pattern, string)      # Match at start
re.search(pattern, string)     # Search anywhere
re.findall(pattern, string)    # All matches
re.sub(pattern, repl, string)  # Replace
```

## 9.3 Context-Free Grammars

### Definition

A **Context-Free Grammar (CFG)** G = (V, Σ, R, S):
- **V:** Set of non-terminals
- **Σ:** Set of terminals (alphabet)
- **R:** Production rules
- **S:** Start symbol

### Backus-Naur Form (BNF)

```
<expr>   ::= <term> + <expr> | <term>
<term>   ::= <factor> * <term> | <factor>
<factor> ::= ( <expr> ) | <number>
<number> ::= 0 | 1 | 2 | ...
```

### Parse Trees

CFGs generate **parse trees** showing structure of derived strings:
- Root: Start symbol
- Internal nodes: Non-terminals
- Leaves: Terminals
- Children: Right-hand side of production

### Chomsky Hierarchy

| Type | Name | Recognizer | Example |
|------|------|------------|---------|
| 3 | Regular | Finite automaton | `a*b` |
| 2 | Context-free | Pushdown automaton | Balanced parentheses |
| 1 | Context-sensitive | Linear bounded automaton | aⁿbⁿcⁿ |
| 0 | Unrestricted | Turing machine | Any computable |

### Applications

- **Programming language syntax**
- **Natural language parsing**
- **Generative models** (code generation, art)
- **Compiler construction**

## 9.4 Memoization and Dynamic Programming

### The Principle

**Memoization:** Cache function results to avoid redundant computation.

**Trade-off:** Memory for time.

### When to Use

✅ **Good candidates:**
- Function called repeatedly with same arguments
- Deterministic (same input → same output)
- No side effects
- Expensive computation

❌ **Bad candidates:**
- Arguments not hashable
- Random behavior
- Modifies external state

### Implementation
```python
import functools

@functools.lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### Dynamic Programming Connection

**Memoization** is top-down DP: solve problem recursively, cache subproblems.

**Tabulation** is bottom-up DP: solve subproblems first, build up to solution.

Both exploit **optimal substructure** (optimal solution contains optimal solutions to subproblems).

---

# 10. Code Reference

## Python Essentials

```python
# String operations
s.strip()                    # Remove whitespace
s.split(',')                 # Split by delimiter
','.join(list)               # Join list to string
s.replace('a', 'b')          # Replace substring
f"{var:.2f}"                 # Format string

# List operations
L.append(x)                  # Add to end
L.extend([1,2])              # Add multiple
L.insert(0, x)               # Insert at position
L.pop()                      # Remove last
sorted(L, key=func)          # Sort with key

# Dict operations
d.get(key, default)          # Get with default
d.keys(), d.values(), d.items()
d.update(other)              # Merge dicts
{**d1, **d2}                 # Merge (Python 3.5+)

# Comprehensions
[x**2 for x in range(10) if x % 2 == 0]
{k: v for k, v in items}
{x for x in items}

# File I/O
with open('file.txt', 'r') as f:
    content = f.read()

with open('file.txt', 'w') as f:
    f.write('text')
```

## NumPy Reference

```python
import numpy as np

# Creation
np.array([1, 2, 3])
np.zeros((3, 4)), np.ones((2, 3))
np.linspace(0, 1, 100), np.arange(0, 10, 0.5)
np.random.randn(3, 4)

# Properties
arr.shape, arr.dtype, arr.ndim

# Indexing
A[i, j], A[i, :], A[:, j], A[1:3, 0:2]
A[A > 5]                     # Boolean indexing

# Operations
A @ B                        # Matrix multiply
A * B                        # Element-wise
np.dot(a, b)                 # Dot product

# Statistics
np.mean(x), np.std(x), np.sum(x)
np.min(x), np.max(x), np.median(x)

# Reshaping
arr.reshape((2, 6)), arr.flatten(), arr.T
```

## Pandas Reference

```python
import pandas as pd

# I/O
df = pd.read_csv('data.csv')
df.to_csv('out.csv', index=False)

# Inspection
df.head(), df.info(), df.describe()
df.shape, df.columns, df.dtypes

# Selection
df['col'], df[['col1', 'col2']]
df.loc[row, col], df.iloc[i, j]
df[df['col'] > 5]

# Aggregation
df.groupby('cat').mean()
df['col'].value_counts()
df.pivot_table(values='val', index='row', columns='col')
```

## Scikit-Learn Reference

```python
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression())
])

# Train and evaluate
pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
pred = pipe.predict(X_new)

# Cross-validation
scores = cross_val_score(pipe, X, y, cv=5)

# Grid search
param_grid = {'clf__C': [0.1, 1, 10]}
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)
```

## Matplotlib Reference

```python
import matplotlib.pyplot as plt

# Basic plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'b-', label='Line')
ax.scatter(x, y, c='red', label='Points')

# Formatting
ax.set_xlabel('X'), ax.set_ylabel('Y'), ax.set_title('Title')
ax.legend(), ax.grid(True)

# Multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y)

# Save
plt.tight_layout()
plt.savefig('figure.pdf')
```

## NetworkX Reference

```python
import networkx as nx

# Create
G = nx.Graph()               # Undirected
D = nx.DiGraph()             # Directed

# Add
G.add_node(1)
G.add_edges_from([(1, 2), (2, 3)])

# Analysis
nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.pagerank(D)

# Algorithms
nx.shortest_path(G, source, target)
list(nx.topological_sort(D))
list(nx.bfs_edges(G, source))
```

## Regular Expressions

```python
import re

# Basic operations
re.match(r'pattern', string)     # Match at start
re.search(r'pattern', string)    # Search anywhere
re.findall(r'pattern', string)   # All matches
re.sub(r'pattern', repl, string) # Replace

# Common patterns
r'\d+'           # Digits
r'\w+'           # Word characters
r'\s+'           # Whitespace
r'^start'        # Start anchor
r'end$'          # End anchor
r'[a-z]+'        # Character class
r'(group)'       # Capture group
r'a|b'           # Alternation
```

## Memoization

```python
import functools

@functools.lru_cache(maxsize=1000)
def expensive_function(arg):
    # Computation
    return result

# Cache inspection
expensive_function.cache_info()
expensive_function.cache_clear()
```

---

*Consolidated Study Guide for CT5148 Programming Tools for AI*
