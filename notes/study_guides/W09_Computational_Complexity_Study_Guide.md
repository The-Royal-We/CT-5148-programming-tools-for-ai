# Week 9: Computational Complexity - Study Guide

## Table of Contents
1. [Introduction to Computational Complexity](#introduction-to-computational-complexity)
2. [Big O Notation](#big-o-notation)
3. [Common Complexity Classes](#common-complexity-classes)
4. [Python Data Structures & Time Complexity](#python-data-structures--time-complexity)
5. [Measuring Object Complexity](#measuring-object-complexity)
6. [Practice Exercises](#practice-exercises)
7. [Quick Reference](#quick-reference)

---

## Introduction to Computational Complexity

### Why Computational Complexity Matters

Computational efficiency is crucial in programming. The efficiency of an algorithm isn't well-measured by "wall clock time" because:
- You can reduce runtime by buying faster hardware
- Different languages execute at different speeds
- Small inputs make even inefficient algorithms appear fast

**Computational complexity** is defined as: **how quickly the runtime increases as input gets arbitrarily large**.

### Key Assumptions

A program consists of idealized "instructions":
- Different instruction types (e.g., multiplication, equality checks) may vary in speed
- Speed differences are by a **constant factor** only
- If one instruction is slower by a factor that **depends on input size**, it's not an instruction—it's composed of multiple instructions

With these assumptions, runtime = number of instructions (a formula in *n*, the input size).

### Worst-Case Analysis

In computational complexity, when the number of instructions could vary for fixed input size, we consider the **worst-case**. This accounts for situations where algorithms can exit early for special cases or errors.

(Note: Average-case analysis is sometimes considered as well.)

### Asymptotic Runtime

"Asymptotic behavior" means behavior for arbitrarily large values. In computational complexity, we only care about the number of instructions executed for large *n*.

For large *n*, only the **fastest-growing term** matters.

**Why?** Even multiplying by 1000× or adding 100,000 constant operations becomes negligible compared to the growth of the dominant term as *n* increases.

---

## Big O Notation

### Definition

"Big O" notation expresses the order of complexity:

1. Write total instructions as a function of *n* (e.g., 2n² + n + 2)
2. Drop all but the fastest-growing term
3. Drop its coefficient
4. Write in Big O notation: **O(n²)**

### Example Calculation: Row Sum of Matrix

```python
def row_sum(M):
    R = []
    for L in M:
        R.append(sum(L))
    return R
```

For an n×n matrix:
- Create empty list: 1
- Loop n times:
  - Each `sum(L)` requires n lookups + n additions = 2n
  - Plus 1 append = 2n + 1 per loop
  - Loop total: n(2n + 1)
- **Total: 2n² + n + 1 → O(n²)**

### Important Notes

- Always define *n* clearly (e.g., "O(n²) with respect to n, the number of rows")
- For multiple inputs (n and m), you may need O() expressions in both (e.g., O(nm))

---

## Common Complexity Classes

From slowest to fastest-growing:

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Array access, hash table lookup |
| O(log n) | Logarithmic | Binary search, tree traversal to root |
| O(n) | Linear | Simple iteration, checking element exists |
| O(n log n) | Log-linear/Quasi-linear | Efficient sorting (merge sort, quicksort) |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci (naive) |
| O(n!) | Factorial | Generating all permutations |

### Visualization

Even for small *n*, the differences are dramatic:

```python
ns = range(2, 21)
growths = {
    "constant": lambda n: 1,
    "logarithmic": lambda n: math.log(n),
    "linear": lambda n: n,
    "log-linear": lambda n: n * math.log(n),
    "quadratic": lambda n: n ** 2
}
```

**Key Insight:** Quadratic algorithms are far worse than linear, even when linear has a 1000× coefficient or 100,000 constant setup cost.

### Rules of Thumb

1. **Every for-loop multiplies by a factor of n**
   ```python
   for i in range(n):
       for j in range(n):
           for k in range(n):
               # do something  # This is O(n³)
   ```

2. **Reading input can usually be ignored**
   - Reading is typically O(n)
   - Processing won't be sub-linear
   - Processing time dominates

3. **Logarithmic complexity (O(log n))** often appears with:
   - Tree structures (tree of n nodes has log n levels)
   - Binary search algorithms
   - Dividing input in half repeatedly

4. **Log-linear complexity (O(n log n))** often appears when:
   - Putting data into a tree structure (each of n elements takes log n)
   - Efficient sorting algorithms

### When Complexity Doesn't Matter

- Small, fixed input sizes (e.g., n < 7)
- Webserver handling uniform small requests
- For small *n*, setup time and coefficients matter more than asymptotic behavior

---

## Python Data Structures & Time Complexity

### Fundamental Fact

Given a **known location in memory**, we can read from or write to it in **constant time O(1)**.

### Lists

**Internal representation:** Contiguous array in memory

```
[0][1][2][3][4][5][6][7]
                    ^^^
```

**Complexity:**
- **O(1):** append, get item (`L[i]`), set item (`L[i] = x`), `len(L)`
- **O(n):** insert item, delete item, iterate, `min(L)`, `x in L`

**Characteristics:**
- Fast for changes at the end
- Slow for changes near the beginning (all items must "move")
- Stores pointer to end (fast append)
- Remembers length (no iteration needed for `len`)

### Tuple

Similar to list for allowed operations (but immutable).

### Double-Ended Queue (deque)

**Use case:** When you need fast operations at both ends

```python
from collections import deque
```

**Complexity:**
- **O(1):** append, appendleft, pop, popleft, `len`
- **O(n):** get, set, or remove element in the middle

**Implementation:** Doubly-linked list

**Example:** Breadth-first search needs queue behavior ("first-in, first-out"). Using a list is slow; use `deque` instead.

### Dictionaries

**Key technology:** Hash functions

A hash function maps objects to integers, uniformly distributed over a wide range.

```python
hash(2)           # hashable
hash('abc')       # hashable
hash([5, 6, 7])   # NOT hashable (lists are mutable)
```

#### How Dictionaries Work (Simplified)

1. Create a list `L` of fixed size (e.g., 5)
2. To add key `k` with value `v`:
   ```python
   i = hash(k) % 5
   L[i] = (k, v)
   ```
3. To retrieve value for key `k`:
   ```python
   i = hash(k) % 5
   return L[i]  # second element is v
   ```

**Performance:**
- Calculating `hash` and looking up list element: both O(1)
- Trade-off: Uses extra memory for speed

#### Hash Collisions

When two keys get the same index:
```python
hash(2) % 5          # might equal
hash('abcdefghi') % 5  # this one
```

**Solution:** Linear probing - check `L[i+1]`, `L[i+2]`, etc. until finding empty space

**Re-hashing:** When dictionary gets full:
1. Create much larger list
2. Recalculate all indices with new size
3. Copy elements to new locations

This is **O(n)** but happens **rarely**.

#### Amortized Analysis

- Typically adding entry: **O(1)**
- Rarely: **O(n)** (when re-hashing)
- Average across many additions: **practically constant-time**

Since we typically add to a dict many times, we use average-case instead of worst-case.

**Dictionary Complexity:**
- **O(1) average:** `x in d`, add item, retrieve item, delete item, `len`
- **O(n):** iterate over items

### Sets

**Implementation:** Similar to dictionaries (keys with dummy values)

**Complexity:**
- **O(1):** `x in s`, add item, delete item, `len`
- **O(n):** iterate over items

> "The performance of dictionaries is one of the minor miracles of computer science." - Downey, *Think Complexity*

### Summary Table

| Operation | List | Deque | Dict | Set |
|-----------|------|-------|------|-----|
| Get/Set item | O(1) | O(n) | O(1)* | N/A |
| Add item | O(1)** | O(1) | O(1)* | O(1)* |
| Delete item | O(n) | O(1)*** | O(1)* | O(1)* |
| Search (`in`) | O(n) | O(n) | O(1)* | O(1)* |
| Iterate | O(n) | O(n) | O(n) | O(n) |
| `len` | O(1) | O(1) | O(1) | O(1) |

\* Average case (amortized)  
\*\* At end only  
\*\*\* At ends only (appendleft, append, popleft, pop)

---

## Measuring Object Complexity

### What is Object Complexity?

Object complexity measures **how much information** is contained in an object (different from computational complexity).

Focus on **strings** because any computational object can be converted to a string.

### Examples

```python
s1 = 'aaaaaaaaaaaaaaaaaaaaaaaa'  # Lowest complexity
s2 = 'abcdabcdabcdabcdabcdabcd'  # Medium complexity
s3 = 'abaabddbcbabdbabcccadacc'  # Highest complexity
```

`s1` has an obvious pattern (least information), `s2` has a repeating pattern (medium), `s3` has no obvious pattern (most information).

### Method 1: Distinct N-grams

**Idea:** If there are few distinct n-grams, there must be lots of repetition (low complexity). Many distinct n-grams means less repetition (higher complexity).

```python
def count_distinct_ngrams(s, n):
    ngrams = [s[i:i+n] for i in range(len(s) - n + 1)]
    return len(set(ngrams))  # count distinct ones

# Example with 4-grams:
s1 = 'aaaaaaaaaaaaaaaaaaaaaaaa'  # Result: 1
s2 = 'abcdabcdabcdabcdabcdabcd'  # Result: 4
s3 = 'abaabddbcbabdbabcccadacc'  # Result: 19
```

### Method 2: Kolmogorov Complexity

**Definition:** The length of the shortest program which would output the string.

**Example:**
```python
s2 = 'abcdabcdabcdabcdabcdabcd'

# Can be compressed to:
'abcd' * 6  # Shorter! Shows there's a pattern
```

For complex patterns:
```python
s4 = '112123123412345123456123456712345678'
# High n-gram count, but compressible with a short program
```

**Problem:** Finding the shortest program is **uncomputable** - no algorithm can guarantee to find it!

### Practical Methods

In practice, we use simpler approximations:
- Counting distinct n-grams
- Entropy (are all symbols equally common?)
- Conditional entropy (are all n-grams equally common?)
- LZW-compression (related to zip compression)
- Assembly index (how many "joins" needed?)

**Field:** Algorithmic Information Theory studies these concepts.

---

## Practice Exercises

### Exercise 1: Binary Search Complexity

```python
def binary_search(L, value):
    low = 0
    high = len(L) - 1
    while low <= high: 
        mid = (low + high) // 2
        if L[mid] > value: high = mid - 1
        elif L[mid] < value: low = mid + 1
        else: return mid
    return -1
```

**Question:** What is the time complexity?

<details>
<summary>Answer</summary>

**O(log n)** where n is the length of list L.

Binary search divides the list in two at every step, so it only needs to check log₂(n) elements in the worst case.

</details>

---

### Exercise 2: Subset Check Complexity

```python
def subset(S, T):
    '''
    Return True if S is a subset of T.
    Both S and T are lists. T might not be sorted, so we sort it.
    '''
    T.sort()
    return all((binary_search(T, x) >= 0) for x in S)
```

**Question:** What is the computational complexity?

<details>
<summary>Answer</summary>

Let n = size of S, m = size of T.

1. **Sorting T:** O(m log m)
2. **Binary search in T:** O(log m) per search
3. **Searches:** n times (once for each element in S)
4. **Total for searches:** O(n log m)

**Combined:** O(m log m) + O(n log m)

If we assume n ≤ m (reasonable for subset checking):
**O(m log m)**

The sorting dominates the complexity.

</details>

---

### Exercise 3: Pairwise Distance Space Complexity

In `scipy.spatial.distance.pdist`, we calculate pairwise distance between every pair of points, storing only the upper triangle:

```
0 5 4 9 2
5 0 1 6 3
4 1 0 3 2
9 6 3 0 7
2 3 2 7 0
```

Stored as: `[5, 4, 9, 2, 1, 6, 4, 3, 2, 7]` (length 10)

**Question:** What is the space complexity?

<details>
<summary>Answer</summary>

**O(n²)** with respect to n (number of points).

The upper triangle has: (n-1) + (n-2) + ... + 1 elements

This is a triangular number = n(n-1)/2

Dropping constants: **O(n²)**

**Note:** If each point is a vector of m elements, and we consider m as variable, the complexity becomes O(n²m).

</details>

---

### Exercise 4: Finite State Machine

Create an FSM for language L where:
- Words consist of chunks of length 3
- Every chunk starts with `aa` and can end with any of {a, b, c}

Examples:
- `aaa` ✓ in L
- `aabaacaab` ✓ in L
- `aa` ✗ not in L
- `aba` ✗ not in L

**Question:** Draw the FSM and write it in Python.

<details>
<summary>Answer</summary>

**FSM Diagram:**
```
    a        a      a,b,c
(start) → (a1) → (a2) → (start)
  ↑_________________________↑
```

(start) is both start state and only accepting state.

**Python representation:**
```python
FSM = {
    'start': {'a': 'a1'},
    'a1': {'a': 'a2'},
    'a2': {'a': 'start', 'b': 'start', 'c': 'start'}
}
```

**Time complexity of running FSM:** O(n) where n is the length of input (single pass through input).

</details>

---

### Exercise 5: Machine Learning Algorithm Complexity

**Question:** What is the complexity of linear regression for:
1. **Prediction** phase?
2. **Training** phase (using gradient descent)?

<details>
<summary>Answer</summary>

**Prediction:**
- Input: vector x with n variables
- Calculation: ŷ = a + b₁x₁ + b₂x₂ + ... + bₙxₙ
- Complexity: **O(n)** where n = number of variables

**Training:**
- Dataset: n variables, m examples
- Iterations: s steps of gradient descent
- Each step: must process all m examples and all n variables
- Complexity: **O(nms)** where:
  - n = number of variables
  - m = number of training examples
  - s = number of iterations

Can simplify to O(m) if treating n and s as fixed constants.

</details>

---

## Quick Reference

### Complexity Cheat Sheet

#### Common Growth Rates (Fastest to Slowest)
1. **O(1)** - Constant
2. **O(log n)** - Logarithmic
3. **O(n)** - Linear
4. **O(n log n)** - Log-linear
5. **O(n²)** - Quadratic
6. **O(2ⁿ)** - Exponential
7. **O(n!)** - Factorial

#### Python Data Structure Operations

**Lists:**
```python
L[i]          # O(1) - get/set by index
L.append(x)   # O(1) - add at end
x in L        # O(n) - search
L.insert(0,x) # O(n) - insert at beginning
```

**Dictionaries:**
```python
d[k]          # O(1) average - get/set
k in d        # O(1) average - check membership
d.pop(k)      # O(1) average - delete
for k in d    # O(n) - iterate
```

**Sets:**
```python
x in s        # O(1) average - membership
s.add(x)      # O(1) average - add element
s.remove(x)   # O(1) average - remove element
```

#### Common Patterns to Recognize

**O(log n):**
- Binary search
- Tree traversal to root
- Halving input each step

**O(n log n):**
- Efficient sorting algorithms
- Building tree structures from data

**O(n):**
- Single pass through data
- Reading input
- Simple iteration

**O(n²):**
- Nested loops over same data
- Comparing all pairs
- Bubble sort

**Accidental Quadratic:**
Watch for O(n) operations inside O(n) loops!

```python
# AVOID THIS - O(n²)
for item in list1:
    if item in list2:  # O(n) operation in O(n) loop
        # ...

# BETTER - O(n)
set2 = set(list2)      # O(n) once
for item in list1:     # O(n) loop
    if item in set2:   # O(1) operation
        # ...
```

#### Key Takeaways

1. **Focus on the dominant term** for large n
2. **Constants don't matter** in Big O
3. **Choose the right data structure** for your operations
4. **Dictionary/Set lookups are "magic"** - use them!
5. **Always specify what n represents**
6. **Worst-case vs. average-case** - know which you're using

---

## Additional Resources

### Recommended Reading
- Downey, *Think Python*, Appendix B
- Downey, *Think Complexity*, Chapter 3
- https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
- https://wiki.python.org/moin/TimeComplexity

### Websites
- Accidentally Quadratic: http://accidentallyquadratic.tumblr.com
- Complexity vs AI: https://www.gwern.net/Complexity-vs-AI

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 9*
