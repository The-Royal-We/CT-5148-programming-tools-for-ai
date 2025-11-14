# Week 6: Object-Oriented Programming & Scikit-Learn API - Study Guide

## Table of Contents
1. [Object-Oriented Programming Basics](#object-oriented-programming-basics)
2. [Special Methods (Dunder Methods)](#special-methods-dunder-methods)
3. [Inheritance](#inheritance)
4. [Advanced OOP Concepts](#advanced-oop-concepts)
5. [The Iterator Protocol](#the-iterator-protocol)
6. [Scikit-Learn Estimator API](#scikit-learn-estimator-api)
7. [Creating Custom Estimators](#creating-custom-estimators)
8. [Scikit-Learn API Overview](#scikit-learn-api-overview)
9. [Quick Reference](#quick-reference)

---

## Object-Oriented Programming Basics

### Defining Classes

```python
class C:
    def __init__(self, data=17):
        self.data = data
```

**Key concepts:**
- `self` is the first argument of all methods (like `this` in other languages)
- `__init__` is the constructor
- No access restrictions - all fields are public and mutable
- Classes have their own namespace

### Creating and Using Objects

```python
# Create instances
c1 = C()        # Uses default: data=17
c2 = C(42)      # Custom value: data=42

# Access attributes
print(c1.data)  # 17
print(c2.data)  # 42

# Modify attributes
c1.data = 100
print(c1.data)  # 100
```

### Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def have_birthday(self):
        self.age += 1

# Usage
p = Person("Alice", 30)
print(p.greet())      # "Hello, I'm Alice"
p.have_birthday()
print(p.age)          # 31
```

---

## Special Methods (Dunder Methods)

### Common Dunder Methods

**"Dunder" = Double UNDERscore** (e.g., `__init__`)

| Python Call | Translation |
|-------------|-------------|
| `C(data)` | `C.__init__(self, data)` |
| `len(c)` | `c.__len__()` |
| `repr(c)` | `c.__repr__()` |
| `str(c)` | `c.__str__()` |
| `c < d` | `c.__lt__(d)` |
| `c == d` | `c.__eq__(d)` |
| `c + d` | `c.__add__(d)` |

### `__repr__` vs `__str__`

**`__repr__()` - Representation for developers:**
- Should return code that could recreate the object
- Used by `repr()` and in interactive shell
- Goal: unambiguous, complete information

**`__str__()` - String for end users:**
- Human-readable format
- Used by `print()` and `str()`
- Goal: readable, user-friendly

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))  # Point(3, 4)
print(str(p))   # (3, 4)
print(p)        # (3, 4) - uses __str__ if available
```

**Best practice:** Always implement at least `__repr__()`. If `__str__()` isn't defined, Python falls back to `__repr__()`.

### Comparison Operators

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __eq__(self, other):
        return self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1 < p2)   # False
print(p1 > p2)   # True (automatically from __lt__ by symmetry)
print(p1 == p2)  # False
```

**"Free Lunch" Principle:** Implementing `__lt__` automatically enables `>` due to symmetry.

### Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2      # Vector(4, 6)
v4 = v1 * 3       # Vector(3, 6)
```

---

## Inheritance

### Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.name)    # "Buddy" (inherited attribute)
print(dog.speak()) # "Woof!" (overridden method)
```

### Using `super()`

Call parent class methods:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent's __init__
        self.department = department

m = Manager("Alice", 100000, "Engineering")
print(m.name)       # "Alice"
print(m.salary)     # 100000
print(m.department) # "Engineering"
```

### Method Resolution Order (MRO)

Python searches for methods in this order:
1. Instance's class
2. Parent classes (left to right in inheritance list)
3. Grandparent classes, etc.

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    pass

class D(B, C):
    pass

d = D()
print(d.method())  # "B" (B comes before C in D's parent list)
print(D.__mro__)   # Shows: D -> B -> C -> A -> object
```

---

## Advanced OOP Concepts

### Multiple Inheritance

```python
class Flyer:
    def fly(self):
        return "Flying!"

class Swimmer:
    def swim(self):
        return "Swimming!"

class Duck(Flyer, Swimmer):  # Inherits from both
    def quack(self):
        return "Quack!"

d = Duck()
print(d.fly())    # "Flying!"
print(d.swim())   # "Swimming!"
print(d.quack())  # "Quack!"
```

### Mixins

A **mixin** is a class designed specifically for multiple inheritance to add functionality:

```python
class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class Calculator(LoggingMixin):
    def add(self, a, b):
        result = a + b
        self.log(f"Adding {a} + {b} = {result}")
        return result

calc = Calculator()
calc.add(5, 3)  # [Calculator] Adding 5 + 3 = 8
```

### Functions as Objects

**Everything in Python is an object**, including functions:

```python
def square(x):
    return x**2

def cube(x):
    return x**3

# Functions have attributes
print(square.__name__)  # 'square'

# Can add custom attributes
square.inverse = lambda x: x**0.5
cube.inverse = lambda x: x**(1/3)

# Use the custom attribute
print(square.inverse(16))  # 4.0
```

### Duck Typing

"If it looks like a duck, walks like a duck, and quacks like a duck, treat it like a duck."

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    # Doesn't check type - just needs speak() method
    print(animal.speak())

make_animal_speak(Dog())  # Works!
make_animal_speak(Cat())  # Also works!
```

---

## The Iterator Protocol

### Requirements

An iterator must have:
- `__iter__()`: Returns the iterator object (often `self`)
- `__next__()`: Returns the next item or raises `StopIteration`

### Example: Countdown

```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

# Usage
for i in Countdown(5):
    print(i)  # Prints: 4, 3, 2, 1, 0
```

### Example: Reverse Count

```python
class ReverseCount:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n

for x in ReverseCount(5):
    print(x)  # Prints: 4, 3, 2, 1, 0
```

**Note:** Generators (using `yield`) are often easier than implementing the iterator protocol manually.

---

## Scikit-Learn Estimator API

### Why Mimic the API?

**Benefits:**
- **Uniform interface** across all models
- **Polymorphism** - swap algorithms easily
- Works with Scikit-Learn tools (pipelines, cross-validation, GridSearchCV)

### Example: Polymorphic Code

```python
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

clfs = [LogisticRegression(), SVC()]

for clf in clfs:
    clf.fit(X_train, y_train)
    print(f"{clf.__class__.__name__}: {clf.score(X_test, y_test):.3f}")
```

### Three Essential Methods

1. **`fit(X, y)`** - Train the model
2. **`predict(X)`** - Make predictions
3. **`score(X, y)`** - Evaluate performance

---

## Creating Custom Estimators

### Simple Implementation (1-Nearest Neighbor)

```python
import numpy as np
import scipy.spatial.distance

class OneNN:
    def fit(self, X, y):
        """Store training data."""
        self.X = X
        self.y = y
        return self  # Important!
    
    def predict(self, X):
        """Predict using nearest neighbor."""
        # Calculate distances
        D = scipy.spatial.distance.cdist(self.X, X)
        # Find nearest neighbor for each query
        nearest = np.argmin(D, axis=0)
        return self.y[nearest]
    
    def score(self, X, y):
        """Calculate accuracy."""
        predictions = self.predict(X)
        return np.mean(predictions == y)

# Usage
clf = OneNN()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.3f}")
```

### Inheriting from Base Classes

**Better approach:** Inherit from Scikit-Learn base classes.

```python
from sklearn.base import BaseEstimator, ClassifierMixin

class OneNN(BaseEstimator, ClassifierMixin):
    def fit(self, X, y):
        self.X = X
        self.y = y
        return self
    
    def predict(self, X):
        D = scipy.spatial.distance.cdist(self.X, X)
        nearest = np.argmin(D, axis=0)
        return self.y[nearest]
    
    # score() method provided by ClassifierMixin!
```

**Benefits of inheritance:**
- `BaseEstimator`: Provides `get_params()`, `set_params()`
- `ClassifierMixin`: Provides standard `score()` method (accuracy)
- `RegressorMixin`: Provides standard `score()` method (R²)

### API Rules and Best Practices

#### Constructor Rules

```python
class MyModel(BaseEstimator):
    def __init__(self, param1=default1, param2=default2):
        # All parameters should be keyword arguments with defaults
        self.param1 = param1
        self.param2 = param2
        # Don't perform computation here - save for fit()
```

**Rules:**
- Arguments should have defaults
- `MyModel()` with no arguments should work
- Don't perform heavy computation in `__init__`

#### `fit()` Method

```python
def fit(self, X, y=None):
    # Even unsupervised should accept y=None
    # Perform training here
    # ...
    return self  # Always return self!
```

**Rules:**
- Must return `self` (enables chaining: `model.fit(X, y).predict(Z)`)
- Accept `y=None` for unsupervised (pipeline compatibility)
- Subsequent calls overwrite previous training

#### Naming Conventions

**Learned attributes** (created during `fit()`) should have **trailing underscore**:

```python
class MyLinearRegression(BaseEstimator, RegressorMixin):
    def fit(self, X, y):
        # Compute coefficients
        self.coef_ = np.linalg.lstsq(X, y)[0]  # Note the trailing _
        self.intercept_ = 0.0
        return self
```

**Examples from Scikit-Learn:**
- `coef_` - coefficients
- `support_vectors_` - support vectors
- `n_iter_` - number of iterations performed

---

## Scikit-Learn API Overview

### API Categories (Duck Typing)

**Estimator:**
- Has `fit(X)` or `fit(X, y)` method
- Learns from data
- Base type for all Scikit-Learn objects

**Predictor:**
- Estimator with `predict(X)` method
- May also have:
  - `predict_proba(X)` - probability estimates
  - `decision_function(X)` - decision scores

**Transformer:**
- Estimator with `transform(X)` method
- Often has `fit_transform(X)` shortcut
- Used for preprocessing and feature engineering
- **Not the same as deep learning transformers!**

**Model:**
- Has `score(X)` or `score(X, y)` method
- Evaluates performance
- Higher score is always better

### Common Patterns by Problem Type

| Problem | Technique | Create | Fit | Evaluate | Use |
|---------|-----------|--------|-----|----------|-----|
| **Unsupervised** |
| Clustering | k-means | `km = KMeans(n_clusters=2)` | `km.fit(X)` | `km.score(X)` | `km.labels_` |
| Density | KDE | `kde = KernelDensity()` | `kde.fit(X)` | - | `kde.score_samples(X)` |
| Representation | MDS | `mds = MDS()` | `mds.fit(X)` | - | `mds.embedding_` |
| **Supervised** |
| Regression | Linear | `lr = LinearRegression()` | `lr.fit(X, y)` | `lr.score(X, y)` | `lr.predict(X)` |
| Classification | SVM | `svm = SVC()` | `svm.fit(X, y)` | `svm.score(X, y)` | `svm.predict(X)` |

### Example: Clustering

```python
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3)
km.fit(X)

# Get cluster assignments
labels = km.labels_

# Get cluster centers
centers = km.cluster_centers_

# Predict cluster for new data
new_labels = km.predict(X_new)
```

### Example: Transformer

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X_train)

# Transform data to 2D
X_train_2d = pca.transform(X_train)
X_test_2d = pca.transform(X_test)

# Or use fit_transform shortcut on training data
X_train_2d = pca.fit_transform(X_train)
```

---

## Quick Reference

### OOP Basics

```python
class MyClass:
    def __init__(self, param):
        self.param = param
    
    def method(self):
        return self.param * 2

obj = MyClass(5)
print(obj.method())  # 10
```

### Special Methods

```python
class MyClass:
    def __repr__(self):
        return "MyClass(...)"
    
    def __str__(self):
        return "friendly string"
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
```

### Inheritance

```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
```

### Iterator Protocol

```python
class MyIterator:
    def __iter__(self):
        return self
    
    def __next__(self):
        if condition:
            raise StopIteration
        return value
```

### Custom Estimator

```python
from sklearn.base import BaseEstimator, ClassifierMixin

class MyClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, param=default):
        self.param = param
    
    def fit(self, X, y):
        # Training logic
        self.learned_param_ = ...
        return self
    
    def predict(self, X):
        # Prediction logic
        return predictions
```

### Using Estimators

```python
# Create
model = MyEstimator(param=value)

# Train
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)

# Predict
predictions = model.predict(X_new)

# Get learned parameters (note trailing _)
params = model.learned_param_
```

---

## Key Takeaways

### OOP in Python
1. **`self` is explicit** - always first parameter of methods
2. **No access control** - all attributes are public
3. **Duck typing** - focus on behavior, not type
4. **Dunder methods** - customize how objects behave with operators

### Inheritance
1. **Use `super()`** to call parent methods
2. **Multiple inheritance** enables mixins
3. **MRO determines** which method is called
4. **Mixins add functionality** without full inheritance

### Scikit-Learn API
1. **Three essential methods**: `fit()`, `predict()`, `score()`
2. **Return `self` from `fit()`** - enables chaining
3. **Trailing underscore** for learned attributes
4. **Inherit from base classes** - get functionality for free
5. **Uniform interface** enables polymorphism

### Best Practices
1. **Always implement `__repr__()`** for debugging
2. **Use `BaseEstimator` and mixins** for custom models
3. **Follow naming conventions** - trailing `_` for learned parameters
4. **Accept `y=None`** even in unsupervised (pipeline compatibility)
5. **Test with GridSearchCV** - validates your API implementation

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 6*
