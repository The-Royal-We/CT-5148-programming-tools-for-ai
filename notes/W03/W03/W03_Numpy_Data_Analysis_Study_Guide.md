# Week 3: Numpy, Data Analysis, and Numerical Computing - Study Guide

## Table of Contents
1. [Introduction to Scientific Computing Libraries](#introduction-to-scientific-computing-libraries)
2. [Pandas for Data Loading](#pandas-for-data-loading)
3. [Matplotlib for Visualization](#matplotlib-for-visualization)
4. [Numpy Arrays and Vectorization](#numpy-arrays-and-vectorization)
5. [Regression by Guessing](#regression-by-guessing)
6. [Signal Processing Example](#signal-processing-example)
7. [Floating Point Arithmetic](#floating-point-arithmetic)
8. [Quick Reference](#quick-reference)

---

## Introduction to Scientific Computing Libraries

### The Numpy Ecosystem

Python's scientific computing power comes from a set of core libraries:

| Library | Purpose | Key Objects |
|---------|---------|-------------|
| **Numpy** | Fast numerical arrays and functions | `array` |
| **Pandas** | Tabular data manipulation | `DataFrame`, `Series` |
| **Matplotlib** | Data visualization | `plot`, `scatter` |
| **Scipy** | Extended scientific computing | Various modules |

### Why Use These Libraries?

**Three Main Reasons:**

1. **Speed** - Numerical calculations are 10-100x faster than pure Python
2. **Abstraction** - Write mathematical notation instead of loops
3. **Library** - Common functions already implemented ("batteries included")

**Example - Sum of array:**

Pure Python (slow):
```python
L = [1, 2, 3, 4]
s = 0
for x in L:
    s += x
```

Numpy (fast):
```python
x = np.array(L)
s = x.sum()  # ~100x faster for large arrays
```

---

## Pandas for Data Loading

### Reading CSV Files

```python
import pandas as pd

df = pd.read_csv("data/cell_growth.csv")
```

### DataFrame Structure

A **DataFrame** is like a dictionary of columns - a table with named columns.

**Inspecting DataFrames:**
```python
df.head()        # View first 5 rows
df.head(10)      # View first 10 rows
df.shape         # (rows, columns) e.g., (100, 3)
df.columns       # Column names
```

### Accessing Columns

```python
# Access single column (returns a Series)
x = df['x']
y = df['y']

# Multiple columns
df[['x', 'y']]
```

### Pandas Series

Each column is a **Series** - a 1D array-like structure.

**Properties:**
```python
x.dtype          # Data type of elements
x.shape          # (length,)
x.values         # Convert to Numpy array
```

**Important:** Series and Numpy arrays are nearly interchangeable for most operations.

### Saving Data

```python
# Save DataFrame to CSV
results_df.to_csv("data/results.csv", index=False)

# Create DataFrame from data
results = []
for item in data:
    results.append((value1, value2, value3))

df = pd.DataFrame(results, columns=('col1', 'col2', 'col3'))
```

---

## Matplotlib for Visualization

### Basic Plotting

```python
import matplotlib.pyplot as plt

# Scatter plot
plt.scatter(x, y)
plt.show()

# Line plot
plt.plot(x, y)
plt.show()
```

**Note:** In Jupyter notebooks, use `;` to suppress output:
```python
plt.scatter(x, y);  # Semicolon prevents ugly return value
```

### Customizing Plots

**Axis labels and limits:**
```python
plt.scatter(x, y)
plt.xlim((0, 10))        # Set x-axis range
plt.ylim((0, 15))        # Set y-axis range
plt.xlabel(r"$x$")       # LaTeX with r-string
plt.ylabel(r"$\phi_{173}$")
plt.show()
```

**Colors and labels:**
```python
plt.scatter(x, y, label="Data", c="blue")
plt.plot(xgrid, ygrid, label="Model", c="orange")
plt.legend()  # Show legend
plt.show()
```

### Multiple Plots

```python
# Plot multiple functions
functions = [f1, f2, f3]
for func in functions:
    plt.plot(xgrid, func(xgrid), label=func.__name__)

plt.legend()
plt.show()
```

### Saving Figures

```python
plt.savefig("data/cell_growth.pdf")  # Use .pdf for papers
plt.close()  # Prevent over-plotting with multiple figures
```

**File formats:**
- **PDF** - Best for papers and publications (vector graphics)
- **PNG** - Good for web/presentations (raster graphics)
- Avoid **JPG** - lossy compression bad for plots

---

## Numpy Arrays and Vectorization

### Creating Arrays

```python
import numpy as np

# From Python lists
z = np.array([0.0, 1.0, 2.0])
M = np.array([[1, 2, 3], [4, 5, 6]])

# Evenly-spaced values
xgrid = np.linspace(0, 10, 101)  # 101 points from 0 to 10, inclusive
xgrid = np.linspace(0, 10, 101, endpoint=False)  # Exclude 10

# Other creation functions
np.zeros(10)           # Array of zeros
np.ones((3, 4))        # 3x4 array of ones
np.arange(0, 10, 0.5)  # Like range() for floats
```

### Array Properties

```python
arr = np.array([1.0, 2.0, 3.0])

arr.dtype    # dtype('float64')
arr.shape    # (3,) - tuple of dimensions
arr.size     # 3 - total number of elements
arr.ndim     # 1 - number of dimensions
```

### The Power of Vectorization

**Key Concept:** Functions work on entire arrays at once.

```python
def f_guess(x):
    return 3 * np.log(0.5 * x + 1)

# Works on single value
f_guess(4.3)  # Single float

# Works on entire array!
x = np.array([1, 2, 3, 4, 5])
f_guess(x)  # Returns array of results
```

**Why it's faster:**
- Loop executed in C/Fortran, not Python
- No type checking needed (array is homogeneous)
- Typical speedup: **10-100x** for large arrays

### Vectorized Operations

**Arithmetic operators:**
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

x + y       # [5, 7, 9]
x * y       # [4, 10, 18]
x ** 2      # [1, 4, 9]
(x - y)**2  # [9, 9, 9]
```

**Comparison operators:**
```python
x > 2       # [False, False, True]
x == y      # [False, False, False]
```

### Multidimensional Arrays

**Indexing with tuples:**
```python
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

A[2, 1]      # Row 2, column 1 → 8
A[0]         # Entire row 0 → [1, 2, 3]
A[:, 0]      # All rows, column 0 → [1, 4, 7]
A[0:2, 1:3]  # Rows 0-1, columns 1-2
```

**Flattening arrays:**
```python
x = np.array([[1, 2, 3]])  # Shape: (1, 3)
x = x.flatten()             # Shape: (3,)
```

### Common Numpy Functions

**Mathematical:**
```python
np.log(x)      # Natural logarithm
np.exp(x)      # e^x
np.sqrt(x)     # Square root
np.sin(x)      # Sine
np.cos(x)      # Cosine
```

**Statistical:**
```python
np.mean(x)     # Average
np.median(x)   # Median
np.std(x)      # Standard deviation
np.sum(x)      # Sum of all elements
np.min(x)      # Minimum
np.max(x)      # Maximum
```

**Array manipulation:**
```python
np.diff(x)               # Differences between adjacent elements
np.diff(x, prepend=x[0]) # Keep same length
np.corrcoef(x, y)        # Correlation matrix
```

---

## Regression by Guessing

### Problem Setup

**Goal:** Find a function that best fits experimental data.

**Approach:**
1. Try different mathematical functions
2. Measure how well each fits the data
3. Choose the best one

### Performance Metrics

#### Root Mean Squared Error (RMSE)

**Lower is better** - measures average magnitude of errors.

```python
def rmse(a, b):
    """Calculate RMSE between arrays a and b."""
    return np.sqrt(np.mean((a - b)**2))

# Example
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 1.9, 3.2, 3.8, 5.1])
rmse(y_true, y_pred)  # 0.14142...
```

**What it measures:**
- Penalizes large errors
- Same units as the original data
- Sensitive to outliers

#### Coefficient of Determination (R²)

**Higher is better** - measures how well the shape matches.

```python
def rsquared(a, b):
    """Calculate R² between arrays a and b."""
    M = np.corrcoef(a, b)
    R = M[0, 1]  # Extract correlation coefficient
    return R**2

rsquared(y_true, y_pred)  # Between 0 and 1
```

**What it measures:**
- 1.0 = perfect correlation
- 0.0 = no correlation
- Measures pattern matching, not magnitude

#### When to Use Each

| Metric | Use When | Pros | Cons |
|--------|----------|------|------|
| **RMSE** | Exact values matter | Penalizes large errors, intuitive units | Sensitive to scale |
| **R²** | Pattern matters more | Scale-invariant, measures correlation | Ignores magnitude |

### Automated Experimentation

**Don't copy-paste** - use loops!

**Bad approach:**
```python
# Manually test each function (tedious, error-prone)
plt.plot(x, f1(x))
plt.show()
plt.plot(x, f2(x))
plt.show()
# ...
```

**Good approach:**
```python
# Put functions in a list
guesses = [f_guess, f_guess2, xsq, xcub, logx1]

# Plot all at once
for guess in guesses:
    plt.plot(xgrid, guess(xgrid), label=guess.__name__)
plt.legend()
plt.show()
```

### Collecting Results

```python
results = []
for guess in guesses:
    guess_y = guess(x)
    result = (
        guess.__name__,
        rmse(y, guess_y),
        rsquared(y, guess_y)
    )
    results.append(result)

# Convert to DataFrame for easy viewing
results_df = pd.DataFrame(
    results,
    columns=('function', 'rmse', 'rsquared')
)

# Save results
results_df.to_csv("data/results.csv", index=False)
```

### Example Functions to Try

```python
def linear(x):
    return 2 * x + 3

def quadratic(x):
    return 0.5 * x**2

def logarithmic(x):
    return 3 * np.log(0.5 * x + 1)

def exponential(x):
    return 2 * np.exp(0.3 * x)

def sinusoidal(x):
    return 5 * np.sin(0.5 * x) + 5
```

---

## Signal Processing Example

### Heart Rate from ECG

**Problem:** Calculate heart rate (beats per minute) from electrocardiogram signal.

**Given:**
- Signal sampled at 360 Hz (360 measurements/second)
- 10 seconds of data
- Goal: Count heartbeats

### Loading Matlab Data

```python
import scipy.io as sio

m = sio.loadmat("data/ECG_MLII_1_NSR_100m_0.mat")
type(m)         # dict
list(m.keys())  # See available keys
x = m['val']    # Extract signal data
x = x.flatten() # Convert to 1D
```

### Signal Processing Pipeline

**Strategy:**
1. **Threshold** - convert to binary (0 or 1)
2. **Differentiate** - detect changes
3. **Filter** - keep only positive changes (rising edges)
4. **Count** - sum up the peaks

**Step 1: Thresholding**
```python
# Create binary signal: 1 where x > threshold, else 0
threshold = 1050
xt = (x > threshold).astype(int)
```

**Step 2: First Differences**
```python
# Detect where signal changes
xtd = np.diff(xt, prepend=xt[0])
# prepend ensures output has same length as input
```

**Step 3: Keep Positive Changes**
```python
# Keep only transitions from 0→1 (start of peak)
xtdp = xtd > 0
```

**Step 4: Calculate Heart Rate**
```python
L = 10  # Signal length in seconds
num_beats = np.sum(xtdp)
heart_rate = num_beats / L * 60  # Convert to beats per minute
```

### Visualization During Development

```python
fs = 360  # Sampling frequency
L = 10    # Length in seconds
t = np.linspace(0, L, fs * L)  # Time points

# Plot original signal
plt.plot(t, x)
plt.xlabel("time (s)")
plt.ylabel("energy")
plt.show()

# Plot after thresholding
plt.plot(t, xt)
plt.show()

# Zoom in to see detail
plt.plot(t[150:250], xt[150:250])
plt.show()
```

### Key Signal Processing Concepts

**Boolean masking:**
```python
x > threshold  # Returns boolean array
```

**Type conversion:**
```python
(x > threshold).astype(int)  # Convert True/False to 1/0
```

**Edge detection:**
- **Rising edge:** 0→1 transition (positive difference)
- **Falling edge:** 1→0 transition (negative difference)
- Each heartbeat creates exactly one rising edge

---

## Floating Point Arithmetic

### The Fundamental Problem

**Computers cannot represent real numbers exactly.**

- Real numbers have infinite possible values
- Computers have finite bits (64 bits for Python `float`)
- Between any two representable numbers are infinitely many unrepresentable ones

### IEEE 754 Standard

**Python's `float` type:**
- 64-bit double-precision floating point
- Same as `double` in C/C++
- Standard for scientific computing

### Inexactness

**Example:**
```python
2 / 3  # → 0.6666666666666666
# Not exact! Infinitely repeating decimal truncated
```

**Critical issue - equality comparisons:**
```python
import math

x = math.sqrt(2) ** 2
y = 2.0

x == y  # → False! (should be mathematically equal)
print(x)  # 2.0000000000000004
```

### Never Use `==` for Floats

**Solution 1: Manual epsilon comparison**
```python
eps = 10**-8  # Tolerance
abs(x - y) < eps  # → True
```

**Solution 2: Use `np.allclose()`**
```python
x = np.linspace(0.0, 1.0, 10, endpoint=False) / 3.0
y = np.linspace(0.0, 0.33333333, 10, endpoint=False)

np.allclose(x, y)  # → True
```

**Default tolerance:**
```python
np.allclose(x, y, rtol=1e-05, atol=1e-08)
# rtol: relative tolerance
# atol: absolute tolerance
```

### Overflow and Underflow

**Overflow - number too large:**
```python
(10.0**10.0)**10.0  # OK: 1e+100
10.0**(10.0**10.0)  # OverflowError: too large
```

**Underflow - number too small:**
```python
print(10 ** -10)   # Works: 1e-10
print(10 ** -350)  # → 0.0 (underflow, becomes zero)
```

**Machine epsilon:**
- Smallest representable non-zero magnitude
- Approximately `10**-324` in Python

### Special Values

**Three special IEEE 754 values:**

1. **Infinity** (`inf`)
2. **Negative Infinity** (`-inf`)
3. **Not a Number** (`nan`)

**Creating and using:**
```python
inf = float('inf')
neg_inf = -inf
nan = float('nan')

# Infinity comparisons
inf > 3          # → True
inf > 1000000    # → True
-inf < inf       # → True

# Infinity arithmetic
inf + 3          # → inf
inf * 2          # → inf
inf + (-inf)     # → nan (not zero!)

# NaN comparisons
nan < 3          # → False
nan == nan       # → False (!)
```

**Note:** In pure Python, division by zero raises error:
```python
15 / 0   # ZeroDivisionError
```

### Floating Point in Numpy

**Different error handling** - processing arrays means errors might occur for only some elements.

**Configuring behavior:**
```python
np.seterr(divide="warn")   # Warn but continue
np.seterr(divide="raise")  # Raise exception
np.seterr(divide="ignore") # Silently continue
```

**Examples:**
```python
x = 1.0
y = np.array([0.0, 1.0, 2.0])

x / y  # → [inf, 1.0, 0.5] with warning

x = 0.0
x / y  # → [nan, 0.0, 0.0] with warning
```

### Best Practices

1. **Never use `==` for float comparisons** - use `np.allclose()` or epsilon
2. **Be aware of overflow/underflow** - especially with exponentials
3. **Handle special values** - `inf` and `nan` propagate through calculations
4. **Use appropriate tolerance** - understand your data's required accuracy
5. **Configure error handling** - decide how Numpy should handle errors

### Understanding Your Precision Needs

**Questions to ask:**
- What precision does my application require?
- Are errors additive (accumulated over iterations)?
- Can I use relative vs absolute tolerance?
- Do I need to detect/handle `inf` or `nan`?

---

## Quick Reference

### Pandas Essentials

```python
import pandas as pd

# Loading data
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")

# Inspection
df.head()              # First 5 rows
df.shape               # (rows, columns)
df.columns             # Column names
df.dtypes              # Column data types

# Accessing data
df['column']           # Single column (Series)
df[['col1', 'col2']]   # Multiple columns

# Saving
df.to_csv("out.csv", index=False)
```

### Numpy Essentials

```python
import numpy as np

# Creation
np.array([1, 2, 3])
np.zeros(10)
np.ones((3, 4))
np.linspace(0, 10, 100)
np.arange(0, 10, 0.5)

# Properties
arr.shape    # Dimensions
arr.dtype    # Data type
arr.size     # Total elements
arr.ndim     # Number of dimensions

# Math functions
np.mean(), np.median(), np.std()
np.sum(), np.min(), np.max()
np.log(), np.exp(), np.sqrt()
np.sin(), np.cos(), np.tan()

# Array operations
np.diff(arr)              # Differences
np.corrcoef(x, y)         # Correlation
np.allclose(x, y)         # Fuzzy equality
arr.flatten()             # Convert to 1D
arr.astype(int)           # Type conversion
```

### Matplotlib Essentials

```python
import matplotlib.pyplot as plt

# Basic plots
plt.plot(x, y)          # Line plot
plt.scatter(x, y)       # Scatter plot

# Customization
plt.xlabel("label")
plt.ylabel("label")
plt.title("title")
plt.xlim((min, max))
plt.ylim((min, max))
plt.legend()
plt.grid()

# Multiple plots
plt.plot(x, y1, label="Data 1")
plt.plot(x, y2, label="Data 2")
plt.legend()

# Saving
plt.savefig("figure.pdf")
plt.close()

# In Jupyter
plt.plot(x, y);  # Semicolon suppresses output
```

### Common Patterns

**Load, process, visualize:**
```python
# Load
df = pd.read_csv("data.csv")
x, y = df['x'], df['y']

# Process
y_pred = my_function(x)
error = rmse(y, y_pred)

# Visualize
plt.scatter(x, y, label="Data")
plt.plot(x, y_pred, label="Model")
plt.legend()
plt.savefig("results.pdf")
```

**Automated experimentation:**
```python
functions = [f1, f2, f3]
results = []

for func in functions:
    y_pred = func(x)
    results.append({
        'name': func.__name__,
        'rmse': rmse(y, y_pred),
        'r2': rsquared(y, y_pred)
    })

pd.DataFrame(results).to_csv("results.csv")
```

**Signal processing pipeline:**
```python
# Threshold → Differentiate → Filter → Count
binary = (signal > threshold).astype(int)
changes = np.diff(binary, prepend=binary[0])
rising_edges = changes > 0
count = np.sum(rising_edges)
```

**Safe float comparison:**
```python
# Bad
if x == y:  # Don't do this!

# Good
if np.allclose(x, y):  # Use this
if abs(x - y) < 1e-8:  # Or this
```

### Performance Tips

1. **Use vectorization** - avoid Python loops over arrays
2. **Preallocate arrays** when size is known
3. **Use appropriate data types** - `int32` vs `int64`, `float32` vs `float64`
4. **Avoid repeated array creation** in loops
5. **Use Numpy's built-in functions** instead of writing your own

---

## Key Takeaways

### Scientific Computing Stack

- **Numpy** is the foundation - everything builds on arrays
- **Pandas** for structured data (tables, time series)
- **Matplotlib** for visualization
- **Scipy** extends Numpy with specialized functions

### Vectorization Philosophy

- Think in terms of entire arrays, not individual elements
- Mathematical notation becomes executable code
- Massive performance gains for large data
- Write `y = 3 * x + 5` instead of looping

### Data Analysis Workflow

1. **Load** - use Pandas
2. **Explore** - visualize with Matplotlib
3. **Process** - use Numpy vectorization
4. **Evaluate** - use metrics (RMSE, R²)
5. **Save** - preserve results programmatically

### Numerical Computing Awareness

- Floating point is approximate, not exact
- Never use `==` for floats
- Understand overflow, underflow, and special values
- Configure error handling appropriately
- Know your precision requirements

### Automation and Reproducibility

- Don't copy-paste - use loops
- Save all results programmatically
- Make plots publication-ready
- Document your process
- Use appropriate file formats

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 3*
