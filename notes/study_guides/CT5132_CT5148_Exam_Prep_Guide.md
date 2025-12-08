# CT5132/CT5148 Programming and Tools for AI - Exam Prep Guide

## Exam Overview

| Aspect | Details |
|--------|---------|
| **Duration** | 2 hours |
| **Questions** | 3-4 questions (varies by year) |
| **Format** | Answer ALL questions, equal marks each |
| **Materials** | Non-programmable calculator allowed |
| **Release** | Exam released to venue (open book from 2023+) |

---

## Topic Frequency Analysis

Based on analysis of 4 exam papers (2021/22, 2022/23, 2023/24, 2024/25):

| Topic | Frequency | Priority |
|-------|-----------|----------|
| **Memoization** | 4/4 papers | 🔴 Critical |
| **Finite State Machines** | 4/4 papers | 🔴 Critical |
| **OOP & Dunder Methods** | 4/4 papers | 🔴 Critical |
| **Computational Complexity** | 4/4 papers | 🔴 Critical |
| **NumPy Vectorization** | 4/4 papers | 🔴 Critical |
| **Scikit-Learn API** | 4/4 papers | 🔴 Critical |
| **Graphs & Traversal** | 3/4 papers | 🟠 High |
| **Grammars (BNF)** | 3/4 papers | 🟠 High |
| **Generators** | 3/4 papers | 🟠 High |
| **R/dplyr (tidy data)** | 2/4 papers | 🟡 Medium |
| **Data Structures (dict, deque)** | 2/4 papers | 🟡 Medium |

---

## Topic 1: Memoization (Appears Every Year)

### Key Concepts

**What is memoization?**
- Caching technique that stores results of expensive function calls
- Returns cached result when same inputs occur again
- Trades memory for speed

### The List Argument Problem (Most Common Question!)

**Question pattern:** *"What happens if a function argument is a list?"*

**Model Answer:**
```
The cache is typically a dictionary where function arguments become keys.
Lists are MUTABLE, therefore NOT HASHABLE, so they cannot be dictionary keys.
This causes a crash (TypeError: unhashable type: 'list').

Solution: Convert lists to tuples (immutable) before caching, or use a 
custom implementation.
```

### Properties for Memoization

Functions suitable for memoization must be:
1. **Deterministic** - same input always produces same output
2. **Pure** - no side effects
3. **Have hashable arguments** - can be used as dictionary keys

### Implementation

```python
import functools

@functools.lru_cache(maxsize=None)
def expensive_function(n):
    # computation here
    return result

# Manual implementation
def memoize(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper
```

---

## Topic 2: Finite State Machines (Appears Every Year)

### Key Concepts

**Components of an FSM:**
1. **States** - discrete conditions (nodes)
2. **Transitions** - edges labeled with input symbols
3. **Start state** - initial state
4. **End states** - accepting/valid states

### Common Question Pattern

*"Draw an FSM to validate sequences matching pattern X"*

**Example from 2023/24:** Validate strings starting with `aaa`, then `b/c/d` repeated twice, then `a`.

### Model FSM Structure

```
        a       a       a      b,c,d    b,c,d     a
(start) → (1) → (2) → (3) → (4x) → (5) → (valid)
                             ↓
                             x → (invalid)
```

**Critical Points:**
- Every state must handle ALL possible inputs
- Unhandled inputs go to "invalid" state (implicit or explicit)
- FSM is NOT a flowchart - cannot use arbitrary program logic

### Python Representations

**Dictionary of transitions (most common):**
```python
FSM = {
    'start': {'a': '1'},
    '1': {'a': '2'},
    '2': {'a': '3'},
    '3': {'b': '4b', 'c': '4c', 'd': '4d'},
    '4b': {'b': '5'},
    '4c': {'c': '5'},
    '4d': {'d': '5'},
    '5': {'a': 'valid'}
}
start = 'start'
end_states = ['valid']
```

**List of edges:**
```python
G = [
    ('start', '1', 'a'),
    ('1', '2', 'a'),
    ('2', '3', 'a'),
    # etc.
]
```

### Tracing Examples (Always Required!)

**Valid string `aaabba`:**
```
start → 1 → 2 → 3 → 4b → 5 → valid
  a     a    a    b     b    a
Result: VALID (ends in accepting state)
```

**Invalid string `abba`:**
```
start → invalid (or start → 1 → invalid)
  a      b
Result: INVALID (no valid transition or ends in non-accepting state)
```

---

## Topic 3: Object-Oriented Programming

### Dunder Methods (Critical!)

| Expression | Translation | Purpose |
|------------|-------------|---------|
| `C(data)` | `C.__init__(self, data)` | Constructor |
| `len(c)` | `c.__len__()` | Length |
| `repr(c)` | `c.__repr__()` | Developer string |
| `str(c)` | `c.__str__()` | User string |
| `c < d` | `c.__lt__(d)` | Less than |
| `c <= d` | `c.__le__(d)` | Less than or equal |
| `c == d` | `c.__eq__(d)` | Equality |
| `c + d` | `c.__add__(d)` | Addition |

### Model Answer Pattern (2024/25 Question)

**Question:** Implement `c <= d` based on `len()`:

```python
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self):
        return self.x + self.y
    
    def __le__(self, other):
        return len(self) <= len(other)

# c <= d translates to c.__le__(d)
```

### Mixins (Frequently Asked)

**Definition:** A class designed to be inherited from in multiple inheritance, providing specific functionality.

**Scikit-Learn Example:**
```python
from sklearn.base import BaseEstimator, ClassifierMixin

class MyClassifier(BaseEstimator, ClassifierMixin):
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        return self
    
    def predict(self, X):
        return predictions

# ClassifierMixin provides score() for free
# BaseEstimator provides get_params(), set_params()
```

### Inheritance with super()

```python
class Vehicle:
    def __init__(self):
        self.wheels = 4

class Car(Vehicle):
    def __init__(self, colour):
        super().__init__()  # Call parent constructor
        self.colour = colour
```

---

## Topic 4: Computational Complexity

### Big O Notation

**Process:**
1. Count total operations as function of n
2. Keep only fastest-growing term
3. Drop coefficients
4. Express as O(...)

### Common Complexities

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | dict lookup, array access |
| O(log n) | Logarithmic | binary search |
| O(n) | Linear | single loop |
| O(n log n) | Log-linear | efficient sorting |
| O(n²) | Quadratic | nested loops |

### Python Data Structure Operations

```python
# Lists
L[i]           # O(1) - index access
L.append(x)    # O(1) - append
x in L         # O(n) - membership test
L.insert(0, x) # O(n) - insert at start

# Dictionaries/Sets
d[k]           # O(1) average - access
k in d         # O(1) average - membership
d.pop(k)       # O(1) average - delete
```

### Common Question Pattern (2024/25)

**Question:** Algorithm complexity for finding duplicates

**Model Answer:**
```
Algorithm: Use two sets - S for seen items, T for duplicates
For each item x:
    if x in S: add to T    # O(1) set lookup
    else: add to S         # O(1) set add

Time Complexity: O(n) where n = number of items
- Visit each item once: O(n)
- Set operations are O(1) each

Space Complexity: O(n) - proportional to unique items

Using generators (yield vs return):
- Time complexity: UNCHANGED
- Space complexity: UNCHANGED (still need both sets)
```

---

## Topic 5: NumPy Vectorization

### Key Principle

**Vectorization = operations on entire arrays at once, no Python loops**

### Common Question: Loop to Vectorized

**Original (2021/22):**
```python
s = 0
for i in range(len(L) - 1):
    if L[i] < L[i+1]:
        s += 1
```

**Vectorized Solution:**
```python
x = np.array(L)
s = (np.diff(x) > 0).sum()
# OR
s = (x[:-1] < x[1:]).sum()
```

**Common Mistakes:**
- List comprehensions are NOT vectorization
- For-loops over NumPy arrays are NOT vectorization
- Using indices like `x[i]` is NOT vectorized

### Vectorization Properties (2024/25 Question)

**Q: Does vectorization improve time complexity? Save memory?**

**A:** 
- Time complexity: **NO** - still O(n), but with better constants
- Memory: **YES** - NumPy uses less memory than Python lists

### Essential NumPy Operations

```python
# Creating arrays
np.linspace(0, 10, 101)                    # 101 evenly spaced values
np.linspace(0, 10, 100, endpoint=False)    # Exclude endpoint

# Numerical integration (area under curve)
w = (x[-1] - x[0]) / len(x)    # Rectangle width
result = (w * f(x)).sum()       # Sum of areas

# Boolean operations
z = x < y                       # Element-wise comparison
# Type: bool array, Shape: same as inputs
```

---

## Topic 6: Scikit-Learn API

### Five-Step Workflow

```python
# 1. Import
from sklearn.linear_model import LinearRegression

# 2. Instantiate
model = LinearRegression()

# 3. Fit
model.fit(X_train, y_train)

# 4. Evaluate
score = model.score(X_test, y_test)

# 5. Predict
predictions = model.predict(X_new)
```

### Common Exam Error (2024/25)

**Broken Code:**
```python
dt = DecisionTreeRegressor(X_train, y_train)  # WRONG!
dt.score(X_test, y_test)
```

**Problems:**
1. Data passed to constructor (should be empty or hyperparameters only)
2. Missing `.fit()` call

**Correct:**
```python
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
dt.score(X_test, y_test)
```

### Data Shape Requirements

```python
X.shape = (n_samples, n_features)  # 2D array, uppercase
y.shape = (n_samples,)              # 1D array, lowercase

# WRONG: Single feature as 1D
X = np.array([1, 2, 3])  # Shape (3,) - will fail

# CORRECT: Single feature as 2D
X = np.array([[1], [2], [3]])  # Shape (3, 1)
```

### Custom Estimator Template

```python
from sklearn.base import BaseEstimator, ClassifierMixin

class OneNearestNeighbour(BaseEstimator, ClassifierMixin):
    def fit(self, X, y):
        self.X_ = X
        self.y_ = y
        return self  # Must return self!
    
    def predict(self, X):
        predictions = []
        for query in X:
            idx = nearest_neighbour(query, self.X_)
            predictions.append(self.y_[idx])
        return np.array(predictions)
```

### One-Hot Encoding (2024/25)

```python
X = [['red'], ['orange'], ['green'], ['orange'], ['red']]

# OneHotEncoder output:
# [[1, 0, 0],   # red -> [green, orange, red]
#  [0, 1, 0],   # orange
#  [0, 0, 1],   # green (alphabetical order!)
#  [0, 1, 0],   # orange
#  [1, 0, 0]]   # red

# Actually: green=0, orange=1, red=2 (alphabetical)
```

---

## Topic 7: Graphs and Traversal

### Graph Representations

**Adjacency List (Dictionary):**
```python
G = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0],
    3: [0, 1],
    4: []
}
```

**Adjacency Matrix:**
```python
#   0 1 2 3 4
# 0 [0,1,1,1,0]
# 1 [1,0,0,1,0]
# ...
```

### BFS for Shortest Path (2024/25 Knight Problem)

```python
from collections import deque

def bfs_generative(start, target, moves):
    """BFS for infinite/large graphs using generator."""
    if start == target:
        return [start]
    
    back_pointers = {}
    queue = deque([start])
    
    while queue:
        n = queue.popleft()
        for m in moves(n):
            if m in back_pointers:
                continue  # Already visited
            back_pointers[m] = n
            queue.append(m)
            
            if m == target:
                # Reconstruct path
                path = [target]
                while path[-1] != start:
                    path.append(back_pointers[path[-1]])
                return path[::-1]
    
    return None  # No path found

# Knight moves
def knight_moves(pos):
    x, y = pos
    deltas = [(2,1), (2,-1), (-2,1), (-2,-1),
              (1,2), (1,-2), (-1,2), (-1,-2)]
    return [(x+dx, y+dy) for dx, dy in deltas]
```

### Topological Sort

**Only for DAGs (Directed Acyclic Graphs)**

**Algorithm:**
1. Find node with in-degree 0
2. If none exists → cycle detected → fail
3. Add to output, remove node and edges
4. Repeat until empty

**Question Pattern:** Given variable dependencies, draw graph, give topological order, identify cycles.

---

## Topic 8: Grammars (BNF)

### Grammar Components

- **Non-terminal:** `<expr>` - can be expanded
- **Terminal:** literal values - cannot be expanded
- **Production:** rewrite rule `<A> ::= <B> | <C>`

### Python Representation

```python
G = {
    "<expr>": [
        ["(", "<expr>", "<biop>", "<expr>", ")"],
        ["<uop>", "<expr>"],
        ["<var>"]
    ],
    "<biop>": [["and"], ["or"]],
    "<uop>": [["not"]],
    "<var>": [["x[0]"], ["x[1]"], ["x[2]"]]
}
```

### Random String Generation

```python
import random

def derive_random_str(G, symbol):
    if symbol in G:  # Non-terminal
        production = random.choice(G[symbol])
        return " ".join(derive_random_str(G, s) for s in production)
    else:  # Terminal
        return symbol

# Usage
expr = derive_random_str(G, "<expr>")
```

---

## Topic 9: Generators

### Key Concepts

- `yield` pauses function, returns value, remembers state
- `return` exits function completely
- Generators are memory-efficient for large data

### yield from

```python
# Rewrite yield from S:
for x in S:
    yield x

# Useful in recursive generators (e.g., tree traversal)
```

### Practical Application

```python
# Memory-efficient file processing
def process_file(filename):
    for line in open(filename):
        yield process_line(line)

# Versus loading entire file
def bad_process(filename):
    return [process_line(l) for l in open(filename).readlines()]
```

---

## Topic 10: R/dplyr (If Covered)

### dplyr Verbs

| Verb | Purpose |
|------|---------|
| `select` | Choose columns |
| `filter` | Choose rows by condition |
| `mutate` | Add/modify columns |
| `gather`/`pivot_longer` | Make data tidy |
| `inner_join` | Combine tables (matching rows) |
| `left_join` | Combine tables (keep all left rows) |

### Tidy Data Principles

**Not tidy:**
```
Country  Metric     2019  2020
Ireland  Population 5.1   5.2
Ireland  GDP        101   102
```

**Tidy:**
```
Country  Year  Population  GDP
Ireland  2019  5.1         101
Ireland  2020  5.2         102
```

**Rule:** Each column is ONE variable, each row is ONE observation.

### Pipe Operator

```r
# Before
select(mutate(D, a=0.4*a), year, a)

# After (with pipe)
D %>% mutate(a=0.4*a) %>% select(year, a)
```

---

## Common Mistakes from Marking Schemes

### 1. FSM Mistakes
- ❌ Using flowchart instead of FSM (nodes must be states, edges must be transitions)
- ❌ Not handling all possible inputs from each state
- ❌ Trying to "remember" values (FSMs are memoryless)

### 2. Vectorization Mistakes
- ❌ List comprehensions are NOT vectorization
- ❌ For-loops over NumPy arrays are NOT vectorization
- ❌ Using indices like `x[i]` - not vectorized

### 3. OOP Mistakes
- ❌ Forgetting `self` parameter
- ❌ Not returning `self` from `fit()`
- ❌ Missing trailing underscore on learned attributes

### 4. Complexity Mistakes
- ❌ Confusing time and space complexity
- ❌ Not defining what 'n' represents
- ❌ Forgetting that dict/set operations are O(1)

### 5. Scikit-Learn Mistakes
- ❌ Passing data to constructor instead of `fit()`
- ❌ Forgetting to call `fit()` before `predict()`
- ❌ Wrong data shapes (X must be 2D)

---

## Quick Reference Cheatsheet

### Complexity

```
O(1)       - dict/set lookup, array index
O(log n)   - binary search
O(n)       - single pass, list membership
O(n log n) - efficient sorting
O(n²)      - nested loops
```

### NumPy

```python
np.linspace(start, stop, num, endpoint=False)
np.diff(x)           # Differences between consecutive elements
x[:-1] < x[1:]       # Compare adjacent elements
(condition).sum()    # Count True values
```

### Scikit-Learn

```python
model = Model()              # Instantiate
model.fit(X, y)              # Train
model.score(X, y)            # Evaluate
model.predict(X)             # Predict
model.attribute_             # Learned parameter (trailing _)
```

### FSM Validation

```python
def validate(fsm, start, end_states, sequence):
    state = start
    for symbol in sequence:
        if symbol not in fsm.get(state, {}):
            return False
        state = fsm[state][symbol]
    return state in end_states
```

---

## Exam Strategy

1. **Read all questions first** - plan time allocation
2. **Start with strongest topic** - build confidence
3. **Show your working** - partial marks available
4. **Define your variables** - especially for complexity ("O(n) where n = ...")
5. **Draw diagrams** - especially for FSMs and graphs
6. **Trace examples** - show FSM processing step-by-step
7. **Use Python syntax** - even pseudocode should be Python-like
8. **Check for common mistakes** - especially Scikit-Learn workflow

---

## Final Checklist

Before the exam, ensure you can:

- [ ] Explain why memoization fails with list arguments
- [ ] Draw an FSM and trace string validation
- [ ] Implement dunder methods (`__le__`, `__repr__`, etc.)
- [ ] Analyze time/space complexity of algorithms
- [ ] Convert loops to vectorized NumPy code
- [ ] Implement a custom Scikit-Learn estimator
- [ ] Write BFS/DFS for graph problems
- [ ] Represent and use grammars in Python
- [ ] Explain generators and `yield from`
- [ ] Know dplyr verbs and tidy data principles

---

*Good luck with your exam!*
