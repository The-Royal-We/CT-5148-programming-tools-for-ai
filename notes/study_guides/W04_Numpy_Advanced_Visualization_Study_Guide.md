# Week 4: NumPy Advanced Arrays and Data Visualization - Study Guide

## Table of Contents
1. [Multidimensional Arrays](#multidimensional-arrays)
2. [Fancy Indexing](#fancy-indexing)
3. [Array Reshaping and Transposing](#array-reshaping-and-transposing)
4. [Image Data Representation](#image-data-representation)
5. [Broadcasting](#broadcasting)
6. [Matrix Operations](#matrix-operations)
7. [Advanced Matplotlib](#advanced-matplotlib)
8. [Seaborn Statistical Visualization](#seaborn-statistical-visualization)
9. [Quick Reference](#quick-reference)

---

## Multidimensional Arrays

### Array Shapes

**Key Concept:** Arrays have a **shape** (tuple of integers) rather than just a length.

```python
import numpy as np

# Creating arrays with specific shapes
M = np.ones((3, 3))  # 3x3 array of ones
print(M.shape)       # (3, 3)

# From list of lists
X = [[1.0, 2.0], 
     [3.0, 4.0]]
X = np.array(X)
print(X.shape)       # (2, 2)
```

### Array Properties

```python
X = np.array([[1, 2, 3], [4, 5, 6]])

X.shape    # (2, 3) - rows, columns
X.ndim     # 2 - number of dimensions
X.size     # 6 - total number of elements
X.dtype    # dtype('int64') - data type
```

### Element-wise Operations

All arithmetic operations work element-by-element:

```python
X = np.array([[1.0, 2.0], 
              [3.0, 4.0]])

X + 10     # Add 10 to every element
X * 2      # Multiply every element by 2
X ** 2     # Square every element
```

---

## Fancy Indexing

### Indexing Comparison

| Operation | Python List | NumPy Array |
|-----------|-------------|-------------|
| Index     | `L[int]`    | `a[tuple]`  |
| Shape     | `len(L)`    | `a.shape`   |

### Single Element Access

```python
X = np.array([[1.0, 2.0], 
              [3.0, 4.0]])

# Using tuple indexing
X[0, 1]    # Row 0, column 1 → 2.0
X[(0, 1)]  # Equivalent

# First row, second column
X[0, 1]    # 2.0
```

### Extracting Rows and Columns

**The `:` operator means "all elements" in that dimension:**

```python
X = np.array([[1.0, 2.0, 3.0], 
              [4.0, 5.0, 6.0]])

# Extract entire row 0
X[0, :]    # array([1., 2., 3.])

# Extract entire column 0
X[:, 0]    # array([1., 4.])

# All elements
X[:, :]    # Same as entire array
```

### Slicing Multidimensional Arrays

```python
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# First 2 rows, first 2 columns
A[0:2, 0:2]
# array([[1, 2],
#        [5, 6]])

# All rows, columns 1-2
A[:, 1:3]
# array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])
```

---

## Array Reshaping and Transposing

### Reshaping

**Key Rule:** Total number of elements must remain the same.

```python
X = np.array(range(10))  # [0, 1, 2, ..., 9]
print(X.shape)           # (10,)

# Various reshapes
X.reshape((5, 2))   # 5 rows, 2 columns
X.reshape((2, 5))   # 2 rows, 5 columns
X.reshape((10, 1))  # Column vector
X.reshape((1, 10))  # Row vector

# Original array is not modified
print(X.shape)      # Still (10,)
```

### Transposing

**Swaps rows and columns:**

```python
X = np.array([[1.0, 2.0, 3.0], 
              [4.0, 5.0, 6.0]])
print(X.shape)  # (2, 3)

Y = X.T
print(Y.shape)  # (3, 2)
print(Y)
# [[1. 4.]
#  [2. 5.]
#  [3. 6.]]
```

**Note:** Transpose creates a **view**, not a copy. Original is not modified.

---

## Image Data Representation

### Grayscale Images

**2D arrays** where each element is a pixel intensity:

```python
import matplotlib.pyplot as plt

# Load grayscale image
x = np.load("data/penguin_grey.npy")
print(x.shape)  # e.g., (400, 300) - height × width

# Display
plt.imshow(x, cmap="gray")
plt.show()
```

### Color Images

**3D arrays** with shape (height, width, channels):

```python
# Load color image
x = plt.imread("img/penguin.jpg")
print(x.shape)  # e.g., (400, 300, 3)

# Channels
# x[:, :, 0]  # Red channel
# x[:, :, 1]  # Green channel
# x[:, :, 2]  # Blue channel

# Display
plt.imshow(x)
plt.show()
```

**Channel options:**
- **RGB:** 3 channels (Red, Green, Blue)
- **RGBA:** 4 channels (+ Alpha for transparency)

### Data Types for Images

```python
# Common image data types
x = np.array([0, 128, 255], dtype='uint8')   # 0-255
x = np.array([0, 128, 255], dtype='int8')    # -128 to 127
x = np.array([0.0, 0.5, 1.0], dtype='float32')  # 0.0-1.0
```

**`uint8`**: Unsigned 8-bit integer, range [0, 255] - most common for images

### Higher-Dimensional Arrays

**Applications:**
- **2D:** Matrices, grayscale images
- **3D:** Color images, time series data
- **4D:** Batch of images (e.g., 1000 images: shape `(1000, 100, 100, 3)`)
- **5D+:** Video batches, medical imaging volumes

---

## Broadcasting

### Element-wise Operations Recap

When arrays have the **same shape**, operations work element-by-element:

```python
X = np.array([[1.0, 2.0, 3.0], 
              [4.0, 5.0, 6.0]])

Y = np.array([[0.01, 0.1, 1.0], 
              [10.0, 100.0, 1000.0]])

X * Y  # Element-wise multiplication (Hadamard product)
# array([[0.01, 0.2, 3.0],
#        [40.0, 500.0, 6000.0]])
```

### Broadcasting Rules

**Broadcasting** allows operations between arrays of different shapes if they're compatible.

**Rules (align shapes from the right):**
1. Dimensions must be equal, OR
2. One dimension must be 1, OR
3. One dimension is missing

### Valid Broadcasting Examples

**Example 1: Adding a 1D array to each row**

```
A (2d):  2 x 4
B (1d):      4
Result:  2 x 4
```

```python
A = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8]])    # shape: (2, 4)

B = np.array([10, 11, 12, 13])  # shape: (4,)

C = A + B  # B is broadcast to each row
# [[11, 13, 15, 17],
#  [15, 17, 19, 21]]
```

**Example 2: Multi-dimensional broadcasting**

```
A (4d):  8 x 1 x 6 x 1
B (3d):      7 x 1 x 5
Result:  8 x 7 x 6 x 5
```

### Invalid Broadcasting

**Incompatible dimensions:**

```
A (2d):  2 x 4
B (1d):      2
Result:  incompatible (2 ≠ 4)
```

```python
A = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8]])  # shape: (2, 4)

B = np.array([10, 11])        # shape: (2,)

# A + B  # ValueError! Shapes incompatible
```

### Fixing Shape Incompatibility

**Use `reshape()` to make shapes compatible:**

```python
A = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8]])        # shape: (2, 4)

B = np.array([10, 11])              # shape: (2,)
B = B.reshape(2, 1)                 # shape: (2, 1)

C = A + B  # Now it works!
# [[11, 12, 13, 14],
#  [16, 17, 18, 19]]
```

---

## Matrix Operations

### Element-wise vs Matrix Multiplication

**Element-wise multiplication** (Hadamard product): Uses `*`
```python
X = np.array([[1, 2], 
              [3, 4]])
Y = np.array([[5, 6], 
              [7, 8]])

X * Y  # Element-wise
# [[5, 12],
#  [21, 32]]
```

**Matrix multiplication**: Uses `@`
```python
X @ Y  # Matrix multiplication
# [[19, 22],
#  [43, 50]]
```

### Matrix Multiplication Requirements

**Shape compatibility:** Inner dimensions must match.

```
(m × n) @ (n × p) = (m × p)
```

```python
X = np.array([[1.0, 2.0], 
              [3.0, 4.0], 
              [5.0, 6.0]])  # 3×2

Y = np.array([[1.0, 1.0, 1.0, 1.0], 
              [10.0, 10.0, 10.0, 10.0]])  # 2×4

C = X @ Y  # Result shape: (3, 4)
# [[21., 21., 21., 21.],
#  [43., 43., 43., 43.],
#  [65., 65., 65., 65.]]
```

---

## Advanced Matplotlib

### Object-Oriented Interface

**Two interfaces in Matplotlib:**
1. **Pyplot stateful interface:** `plt.plot()`, `plt.xlabel()`
2. **Object-oriented interface:** `fig, ax = plt.subplots()`

**OO interface is preferred for complex plots:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plot on specific axes
ax.plot(x, y, color='blue', label='Data')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('My Plot')
ax.legend()

plt.show()
```

### Creating Multiple Subplots

```python
# Create 2×2 grid of subplots
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# Access individual subplots
ax[0, 0].plot(x, y1)
ax[0, 1].plot(x, y2)
ax[1, 0].scatter(x, y3)
ax[1, 1].hist(data)

# Set titles
ax[0, 0].set_title('Plot 1')
ax[0, 1].set_title('Plot 2')

plt.tight_layout()  # Prevent overlapping
plt.show()
```

### Plot Types and Customization

```python
fig, ax = plt.subplots(2, 2, figsize=(9, 6))

# Different plot types
ax[0, 0].plot(x, y, "s", color="g", alpha=0.5, 
              markersize=10, markeredgewidth=0)
ax[0, 1].stem(x, y)
ax[1, 0].plot(x, y, linestyle="--")
ax[1, 1].errorbar(x, y, yerr=errors)
```

**Common customization options:**
- `"s"`: square markers, `"o"`: circles, `"^"`: triangles
- `alpha`: transparency (0-1)
- `markersize`: size of markers
- `markeredgewidth`: border thickness
- `linestyle`: `"--"`, `"-."`, `":"`, `"-"`
- `color`: color specification

### Histograms

```python
fig, ax = plt.subplots(1, 4, figsize=(12, 3))
bins = [5, 10, 20, 40]

for i, b in enumerate(bins):
    ax[i].hist(data, bins=b)
    ax[i].set_xlabel('Value')
    if i == 0:
        ax[i].set_ylabel('Frequency')
    ax[i].set_title(f'{b} bins')

plt.show()
```

### Pandas Integration

**Pass DataFrame directly to plotting functions:**

```python
import pandas as pd

df = pd.read_csv("data/cell_growth.csv")

# Cleaner syntax with column names
plt.scatter("x", "y", data=df, label="Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
```

---

## Seaborn Statistical Visualization

### Introduction

**Seaborn** is built on Matplotlib with:
- Nicer default styles
- Higher-level statistical plots
- Excellent Pandas integration
- Focus on exploratory data analysis

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Pairplot

**Visualize all pairwise relationships in a dataset:**

```python
# Load example dataset
df = sns.load_dataset("penguins")

# Create pairplot
sns.pairplot(df, hue="species")
plt.show()
```

**What it shows:**
- Scatterplot for every pair of numeric variables
- Diagonal shows **kernel density estimation** (smoothed histogram)
- `hue` parameter separates categories by color

**Use case:** Quickly explore relationships in multivariate data

### Boxplot

**Show distribution and compare groups:**

```python
tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill",
            hue="smoker", 
            palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)
plt.show()
```

**Boxplot components:**
- **Box:** Inter-quartile range (IQR) - 25th to 75th percentile
- **Line in box:** Median (50th percentile)
- **Whiskers:** Extend to data within 1.5×IQR from box
- **Points:** Outliers beyond whiskers

**Parameters:**
- `x`: Categorical variable for x-axis groups
- `y`: Numeric variable to show distribution
- `hue`: Additional categorical variable for nested groups
- `palette`: Color scheme

### Joint Plot (Kernel Density)

**2D density estimation with marginal distributions:**

```python
# Generate correlated data
import numpy as np

data = np.random.multivariate_normal(
    [50, 20],           # means
    [[5, 2], [2, 2]],   # covariance matrix
    size=2000
)

df = pd.DataFrame(data, columns=["salary", "spending"])

sns.jointplot(x="salary", y="spending", 
              data=df, kind="kde")
plt.show()
```

**What it shows:**
- Center: 2D kernel density (contour plot)
- Top: Distribution of x variable
- Right: Distribution of y variable

**Key insight:** Reveals dependencies not visible in 1D distributions. Both variables might look normally distributed individually, but joint plot shows correlation.

### Other Useful Seaborn Plots

| Plot Type | Function | Purpose |
|-----------|----------|---------|
| Violin plot | `sns.violinplot()` | Distribution with density info |
| Strip plot | `sns.stripplot()` | Individual points with categories |
| Swarm plot | `sns.swarmplot()` | Non-overlapping points |
| Heatmap | `sns.heatmap()` | Matrix visualization |
| Count plot | `sns.countplot()` | Categorical frequency |

---

## Quick Reference

### NumPy Array Basics

```python
import numpy as np

# Creation
np.ones((3, 3))           # 3×3 array of ones
np.zeros((2, 4))          # 2×4 array of zeros
np.array([[1, 2], [3, 4]])  # From nested lists
np.linspace(0, 10, 100)   # 100 evenly-spaced points
np.arange(0, 10, 0.5)     # Like range() for floats

# Properties
arr.shape    # Tuple of dimensions
arr.ndim     # Number of dimensions
arr.size     # Total elements
arr.dtype    # Data type

# Reshaping
arr.reshape((rows, cols))
arr.flatten()   # Convert to 1D
arr.T           # Transpose
```

### Indexing and Slicing

```python
# 2D array indexing
A[row, col]        # Single element
A[row, :]          # Entire row
A[:, col]          # Entire column
A[r1:r2, c1:c2]    # Slice

# 3D array (e.g., color image)
img[:, :, 0]       # Red channel
img[:, :, 1]       # Green channel
img[:, :, 2]       # Blue channel
```

### Broadcasting Rules

```python
# Shapes align from the right
# Each dimension must be:
# - Equal, OR
# - One is 1, OR
# - One is missing

# Fix incompatible shapes
B = B.reshape(new_shape)
```

### Matrix Operations

```python
A * B    # Element-wise multiplication
A @ B    # Matrix multiplication
A.T      # Transpose
```

### Matplotlib OO Interface

```python
# Single plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Title')
ax.legend()

# Multiple subplots
fig, ax = plt.subplots(nrows, ncols, figsize=(w, h))
ax[row, col].plot(x, y)

# Saving
plt.savefig("figure.pdf")
plt.close()
```

### Seaborn Quick Reference

```python
import seaborn as sns

# Pairplot
sns.pairplot(df, hue="category")

# Boxplot
sns.boxplot(x="category", y="value", data=df)

# Joint plot
sns.jointplot(x="var1", y="var2", data=df, kind="kde")

# Styling
sns.despine()              # Remove top/right spines
sns.set_style("whitegrid") # Set style
```

---

## Key Takeaways

### NumPy Arrays
1. **Shape matters** - always check with `.shape`
2. **Indexing uses tuples** for multidimensional arrays
3. **Reshape doesn't modify** original data
4. **Images are just arrays** (2D grayscale, 3D color)
5. **Higher dimensions** enable batch processing

### Broadcasting
1. **Enables operations on different shapes** - powerful but can be confusing
2. **Align shapes from the right** - check compatibility
3. **Use `reshape()`** to fix incompatible shapes
4. **Element-wise `*` ≠ Matrix multiplication `@`**

### Visualization
1. **Matplotlib OO interface** - more control than pyplot
2. **Seaborn for statistics** - better defaults, easier exploration
3. **Always explore visually** before analysis
4. **Experiment with parameters** (bins, colors, plot types)
5. **Use appropriate plot types** - boxplots for distributions, scatter for relationships

### Best Practices
- **Pandas integration** - pass DataFrames directly to plotting functions
- **Subplot grids** - compare multiple views systematically
- **Save as PDF** - vector graphics for publications
- **Tight layout** - prevent overlapping labels
- **Choose colormaps carefully** - consider colorblind accessibility

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 4*
