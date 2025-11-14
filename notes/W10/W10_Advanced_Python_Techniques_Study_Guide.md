# Week 10: Advanced Python Techniques - Study Guide

## Table of Contents
1. [`eval` and `exec`](#eval-and-exec)
2. [Grammars](#grammars)
3. [Regular Expressions](#regular-expressions)
4. [Memoization](#memoization)
5. [Quick Reference](#quick-reference)

---

## `eval` and `exec`

### What is `eval`?

**`eval`** takes a string containing a valid Python **expression** and evaluates it.

```python
# Basic usage
result = eval("2 + 3")
print(result)  # 5

# With variables
x = 10
result = eval("x * 2 + 5")
print(result)  # 25

# Complex expressions
s = "any((x > 3) for x in [0, 1, 2, 3, 4])"
result = eval(s)
print(result)  # True
```

**Returns:** The value of the expression

### Expression vs Statement

**Expression:** Has a single value
- Mathematical formulas: `2 + 3`
- Function calls: `len([1, 2, 3])`
- List comprehensions: `[x**2 for x in range(5)]`
- Object constructors: `LogisticRegression(C=1.5)`
- Lambda functions: `lambda x: x**2`

**Statement:** Does not have a single value
- Assignment: `x = 5`
- Conditionals: `if x > 3: ...`
- Loops: `for i in range(10): ...`
- Function definitions: `def f(x): ...`

**Cannot use in `eval`:**
```python
# These will fail:
eval("x = 5")           # SyntaxError
eval("if x > 3: x")     # SyntaxError
eval("for i in range(5): print(i)")  # SyntaxError
```

### What is `exec`?

**`exec`** executes arbitrary Python **code** (not just expressions).

```python
# Execute statements
exec("x = 5")
print(x)  # 5

# Execute multiple lines
code = """
def f(x):
    return x**2

for i in range(5):
    print(f(i))
"""
exec(code)
# Prints: 0, 1, 4, 9, 16
```

**Returns:** `None` (since arbitrary code doesn't have a single value)

### Practical Use Cases

#### 1. Recreating Objects from String Representation

```python
from sklearn.linear_model import LogisticRegression

# Create model
LR = LogisticRegression(C=1.5, fit_intercept=False, max_iter=200)

# Save as string
s = repr(LR)
print(s)  # "LogisticRegression(C=1.5, fit_intercept=False, max_iter=200)"

# Later, recreate the model
lr = eval(s)
```

#### 2. Python as JSON Alternative

```python
# Save data
data = {"a": [3, 4, 5], "b": [5, 6, 7]}
with open("data.txt", "w") as f:
    f.write(repr(data))

# Load data
with open("data.txt") as f:
    data = eval(f.read())

print(data)  # {"a": [3, 4, 5], "b": [5, 6, 7]}
```

**Advantages over JSON:**
- Can store Python-specific types (tuples, sets)
- Can include expressions

#### 3. Interactive Calculators

```python
while True:
    expr = input("Enter expression: ")
    if expr == "quit":
        break
    try:
        result = eval(expr)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
```

### Security Warning ⚠️

**Both `eval` and `exec` are dangerous with untrusted input!**

```python
# NEVER DO THIS with user input:
user_input = input("Enter code: ")
eval(user_input)  # User could enter: __import__('os').system('rm -rf /')
```

**Safe usage:**
- Only with trusted input
- Only with data you generated yourself
- Never from anonymous users over the internet
- Never from user-uploaded files

**Safer alternatives:**
- `ast.literal_eval()` - only evaluates Python literals (safe)
- `json.loads()` - for JSON data
- Custom parsers for specific use cases

---

## Grammars

### What is a Grammar?

A **context-free grammar (CFG)** is a computational device that can:
- **Generate** strings from a formal language
- **Parse** strings to verify they belong to a language

Written in **Backus-Naur Form (BNF)** notation.

### Grammar Components

**Rewrite rules:** `left-hand side ::= right-hand side`

**Non-terminal:** String in angle brackets (e.g., `<expr>`)
- Represents a category or concept
- Can be expanded using rules

**Terminal:** Any other string
- Literal values
- Cannot be expanded further

**Productions:** Alternative rewrites separated by `|`

**Start symbol:** The non-terminal of the first rule

### Example Grammar

**BNF notation:**
```
<expr> ::= (<expr> <biop> <expr>) 
         | <uop> <expr> 
         | <var> 
         | <const>
<biop> ::= and | or
<uop>  ::= not
<var>  ::= x[0] | x[1] | x[2]
<const> ::= True | False
```

**Python representation:**
```python
G = {
    "<expr>": [
        ["(", "<expr>", "<biop>", "<expr>", ")"],
        ["<uop>", "<expr>"],
        ["<var>"],
        ["<const>"]
    ],
    "<biop>": [["and"], ["or"]],
    "<uop>": [["not"]],
    "<var>": [["x[0]"], ["x[1]"], ["x[2]"]],
    "<const>": [["True"], ["False"]]
}
```

### Generating Strings from Grammars

**Algorithm:**
1. Start with the start symbol
2. Find leftmost non-terminal
3. Choose a random production to replace it
4. Repeat until no non-terminals remain

**Implementation:**

```python
import random

def derive_random_str(G, symbol):
    """Generate random string from grammar."""
    if symbol in G:  # Symbol is a non-terminal
        # Choose random production
        production = random.choice(G[symbol])
        # Recursively derive each part
        return " ".join(derive_random_str(G, s) for s in production)
    else:  # Symbol is a terminal
        return symbol

# Generate 10 random expressions
for i in range(10):
    print(derive_random_str(G, "<expr>"))
```

**Example output:**
```
( x[1] and ( not False or True ) )
not x[2]
( x[0] or x[1] )
True
( not ( x[2] and x[0] ) or False )
```

### Creating Executable Functions

**Combine grammar with `eval` to create random functions:**

```python
for i in range(10):
    s = derive_random_str(G, "<expr>")
    f = eval("lambda x: " + s)
    
    # Test the function
    x = (False, True, False)
    print(f"{s} : {f(x)}")
```

**Example output:**
```
( x[0] and x[1] ) : False
not x[2] : True
( x[1] or ( x[0] and True ) ) : True
```

### Applications

**1. Compiler Design**
- Programming language syntax definition
- Parsing source code

**2. Natural Language Generation**
- Generate sentences from grammar rules
- Chatbot responses

**3. Generative Art**
- Create random mathematical expressions
- Generate procedural content

**4. Testing**
- Generate random test cases
- Fuzz testing

**Quote:** *"I'd rather write programs that write programs than write programs"* - Richard Sites

---

## Regular Expressions

### What are Regular Expressions?

**Regular expressions (REs)** are patterns for matching strings.
- Written in a domain-specific language
- Equivalent to Finite State Machines
- For any RE, you can construct an equivalent FSM and vice versa

### Basic Syntax

| Pattern | Matches |
|---------|---------|
| `abc` | Literal string "abc" |
| `.` | Any single character |
| `^` | Start of string |
| `$` | End of string |
| `*` | 0 or more repetitions |
| `+` | 1 or more repetitions |
| `?` | 0 or 1 occurrence |
| `[abc]` | Any character in set |
| `[^abc]` | Any character NOT in set |
| `[a-z]` | Any lowercase letter |
| `\d` | Any digit (0-9) |
| `\w` | Any word character |
| `\s` | Any whitespace |
| `|` | Alternation (or) |
| `()` | Grouping |

### Python `re` Module

```python
import re

# Match from start
match = re.match(pattern, string)

# Search anywhere
match = re.search(pattern, string)

# Find all matches
matches = re.findall(pattern, string)

# Split by pattern
parts = re.split(pattern, string)

# Replace matches
new_string = re.sub(pattern, replacement, string)
```

### Common Examples

#### Matching HTML Tags

```python
import re

html = "<a href=test.com><font size=1>Some text</font></a>"
pattern = "<[^/].*?>"  # Non-closing tags

tags = re.findall(pattern, html)
print(tags)  # ['<a href=test.com>', '<font size=1>']
```

**Pattern breakdown:**
- `<` - literal `<`
- `[^/]` - any character except `/`
- `.*?` - any characters (non-greedy)
- `>` - literal `>`

#### Extracting Email Addresses

```python
text = "Contact us at support@example.com or sales@example.org"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(pattern, text)
print(emails)  # ['support@example.com', 'sales@example.org']
```

#### Validating Phone Numbers

```python
def is_valid_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None

print(is_valid_phone("123-456-7890"))  # True
print(is_valid_phone("123-45-6789"))   # False
```

#### Extracting Groups

```python
text = "Date: 2025-11-14"
pattern = r'(\d{4})-(\d{2})-(\d{2})'

match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
```

### Applications

1. **Input validation** - user IDs, credit cards, postcodes
2. **Text extraction** - emails, URLs, phone numbers
3. **Web scraping** - HTML tags, specific patterns
4. **Code analysis** - extract docstrings, function names
5. **Security** - blacklist URLs, detect patterns
6. **Syntax highlighting** - code editors
7. **Find and replace** - advanced text editing

### Learning Resources

**Interactive learning:**
- https://regex101.com/ - excellent testing and learning tool

**Python documentation:**
- https://docs.python.org/3/howto/regex.html - RE HOWTO
- https://docs.python.org/3/library/re.html - `re` module docs

---

## Memoization

### What is Memoization?

**Memoization** (not memo**R**ization) is an optimization technique:
- Store function results to avoid redundant calculations
- Trade memory for speed (RAM vs CPU)

### When to Use Memoization

**Good candidates:**
- ✓ Function called often with same arguments
- ✓ Function is **deterministic** (same input → same output)
- ✓ Function has **no side effects**
- ✓ Performance is a bottleneck

**Bad candidates:**
- ✗ Function rarely called with same arguments
- ✗ Function has random behavior
- ✗ Function modifies external state
- ✗ Arguments are unhashable (lists, dicts)

### The Fibonacci Problem

**Inefficient recursive implementation:**

```python
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(35)  # Very slow! Recalculates same values repeatedly
```

**Problem:** Exponential time complexity - `fibonacci(5)` is calculated many times.

### Solution 1: Manual Memoization

```python
cache = {0: 0, 1: 1}

def fibonacci_mem(n):
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci_mem(n - 1) + fibonacci_mem(n - 2)
    return cache[n]

fibonacci_mem(100)  # Much faster! Linear time complexity
```

### Solution 2: Higher-Order Function

**Create a general memoization wrapper:**

```python
def memoize(f):
    """Decorator to add memoization to any function."""
    cache = {}
    
    def mem_f(*args):
        if args in cache:  # Cache hit
            return cache[args]
        else:  # Cache miss
            cache[args] = f(*args)
            return cache[args]
    
    return mem_f

# Apply to fibonacci
fibonacci = memoize(fibonacci)
fibonacci(100)  # Fast!
```

**Key concept:** `mem_f` is a **closure** - it "closes over" the `cache` variable.

### Solution 3: Decorator Syntax

**Syntactic sugar for the above:**

```python
@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Equivalent to: fibonacci = memoize(fibonacci)
```

### Solution 4: Standard Library (Recommended)

**Use Python's built-in memoization:**

```python
import functools

@functools.lru_cache(maxsize=100)
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(100)  # Fast and clean!
```

**Parameters:**
- `maxsize`: Maximum cache size
- `maxsize=None`: Unlimited cache (use with caution)

### Understanding Closures

**A closure is a function + its environment:**

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # Uses 'factor' from enclosing scope
    return multiply

times_two = make_multiplier(2)
times_three = make_multiplier(3)

print(times_two(5))    # 10
print(times_three(5))  # 15
```

**Each closure has its own copy of the environment:**
- `times_two` has `factor=2`
- `times_three` has `factor=3`

### Cache Management

**LRU (Least Recently Used):**
- When cache is full, discard least recently used entry
- Good balance between hit rate and memory usage

**Other schemes:**
- **FIFO (First-In First-Out):** Discard oldest entry
- **LFU (Least Frequently Used):** Discard least used entry
- **Unlimited:** Never discard (dangerous for long-running programs)

**Trade-off:** Memory usage vs CPU usage

### Advanced: Cache Inspection

```python
@functools.lru_cache(maxsize=100)
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(20)

# Inspect cache statistics
print(fibonacci.cache_info())
# CacheInfo(hits=36, misses=21, maxsize=100, currsize=21)

# Clear cache
fibonacci.cache_clear()
```

### Important Constraints

**Arguments must be hashable:**

```python
@functools.lru_cache()
def process(data):
    # Do expensive computation
    return result

# This works:
process((1, 2, 3))  # Tuples are hashable

# This fails:
process([1, 2, 3])  # TypeError: unhashable type: 'list'
```

**Solution:** Convert to tuple if needed:
```python
result = process(tuple(my_list))
```

### Common Misconceptions

**Myth:** Memoization is only for recursive functions

**Truth:** Any deterministic function benefits from memoization if called repeatedly with same arguments.

```python
@functools.lru_cache(maxsize=1000)
def expensive_api_call(url):
    """Cache results of expensive operations."""
    return requests.get(url).json()

# First call: actually fetches
data1 = expensive_api_call("https://api.example.com/data")

# Second call: instant (from cache)
data2 = expensive_api_call("https://api.example.com/data")
```

---

## Quick Reference

### `eval` and `exec`

```python
# eval - evaluate expressions
result = eval("2 + 3")                    # 5
result = eval("len([1, 2, 3])")          # 3
result = eval("x * 2", {"x": 10})        # 20

# exec - execute code
exec("x = 5")
exec("def f(x): return x**2")

# Security: NEVER with untrusted input!
```

### Grammars

```python
# Define grammar
G = {
    "<start>": [["<symbol1>", "<symbol2>"], ["<symbol3>"]],
    "<symbol1>": [["a"], ["b"]],
    "<symbol2>": [["c"]],
    "<symbol3>": [["d"]]
}

# Generate random string
import random
def derive(G, sym):
    if sym in G:
        return " ".join(derive(G, s) for s in random.choice(G[sym]))
    return sym

print(derive(G, "<start>"))
```

### Regular Expressions

```python
import re

# Basic operations
re.match(pattern, string)      # Match from start
re.search(pattern, string)     # Search anywhere
re.findall(pattern, string)    # Find all
re.split(pattern, string)      # Split by pattern
re.sub(pattern, repl, string)  # Replace

# Common patterns
r'\d+'           # One or more digits
r'\w+'           # One or more word chars
r'\s+'           # One or more whitespace
r'^start'        # Start of string
r'end$'          # End of string
r'[a-z]+'        # Lowercase letters
r'[^0-9]'        # Not a digit
r'(group)'       # Capture group
r'a|b'           # a or b
r'a{3}'          # Exactly 3 a's
r'a{2,5}'        # 2 to 5 a's
r'.*?'           # Non-greedy any
```

### Memoization

```python
import functools

# Basic usage
@functools.lru_cache(maxsize=100)
def expensive_function(arg):
    # Expensive computation
    return result

# Unlimited cache
@functools.lru_cache(maxsize=None)
def another_function(arg):
    return result

# Manual memoization
def memoize(f):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrapper

# Cache inspection
func.cache_info()    # Statistics
func.cache_clear()   # Clear cache
```

---

## Key Takeaways

### `eval` and `exec`
1. **`eval` for expressions** - single value result
2. **`exec` for code** - arbitrary statements
3. **Useful for metaprogramming** - code that writes/runs code
4. **DANGEROUS with untrusted input** - never use with user data
5. **Use `ast.literal_eval()`** for safe evaluation of literals

### Grammars
1. **Define formal languages** - syntax rules
2. **Generate and parse** - create valid strings or verify them
3. **BNF notation** - standard way to write grammars
4. **Applications** - compilers, generative art, testing
5. **Equivalent to FSMs** - theoretical foundation

### Regular Expressions
1. **Pattern matching** - powerful text processing
2. **Domain-specific language** - learn the syntax
3. **Many applications** - validation, extraction, parsing
4. **Test interactively** - use regex101.com
5. **Equivalent to FSMs** - can be implemented as state machines

### Memoization
1. **Cache function results** - trade memory for speed
2. **Only for deterministic functions** - same input → same output
3. **Use `@functools.lru_cache()`** - standard library solution
4. **Arguments must be hashable** - tuples yes, lists no
5. **Not just for recursion** - any repeated computation benefits

### Metaprogramming
All these techniques are forms of **metaprogramming** - code that operates on code:
- `eval`/`exec`: Run code from strings
- Grammars: Generate/parse code
- Regular expressions: Pattern match in code/text
- Memoization: Modify function behavior

**Historical note:** Memoization was considered a machine learning technique when invented (learn from past computations).

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 10*
