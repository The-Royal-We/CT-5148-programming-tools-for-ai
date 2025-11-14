# Week 5: Scikit-Learn Machine Learning - Study Guide

## Table of Contents
1. [Scikit-Learn Introduction](#scikit-learn-introduction)
2. [The Standard Workflow](#the-standard-workflow)
3. [Hyperparameter Tuning](#hyperparameter-tuning)
4. [Cross-Validation](#cross-validation)
5. [Feature Selection](#feature-selection)
6. [Feature Engineering](#feature-engineering)
7. [Analyzing Errors](#analyzing-errors)
8. [Quick Reference](#quick-reference)

---

## Scikit-Learn Introduction

### The Five-Step Workflow

Every supervised learning task in Scikit-Learn follows this pattern:

1. **Import** - Import the model class
2. **Instantiate** - Create an instance of the model
3. **Fit** - Train on training data
4. **Evaluate** - Test performance on test data
5. **Predict** - Make predictions on new data

### Data Shape Conventions

**Critical rules:**
- **Independent variables `X`**: shape `(n_samples, n_features)`
  - Even with 1 feature: use `(n_samples, 1)`, NOT `(n_samples,)`
- **Dependent variable `y`**: shape `(n_samples,)`
- **Naming convention**: Uppercase `X` for multiple features, lowercase `y` for target

```python
import numpy as np

# Correct shapes
X = np.array([[1, 2], [3, 4], [5, 6]])  # (3, 2)
y = np.array([10, 20, 30])               # (3,)

# Wrong! Single feature must still be 2D
# X = np.array([1, 3, 5])  # (3,) - WRONG

# Correct single feature
X = np.array([[1], [3], [5]])  # (3, 1)
```

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)
# Default: 75% train, 25% test, random shuffle
```

**⚠️ Order matters!** Result order: `X_train, X_test, y_train, y_test`

**Custom split:**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3,      # 30% for testing
    random_state=42     # Reproducible split
)
```

---

## The Standard Workflow

### Linear Regression Example

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 2. Import and instantiate
lr = LinearRegression()

# 3. Fit (train)
lr.fit(X_train, y_train)

# 4. Evaluate
score = lr.score(X_test, y_test)  # Returns R² for regression
print(f"R² score: {score:.3f}")

# 5. Predict
X_query = np.array([[83., 4000.0]])
prediction = lr.predict(X_query)
print(f"Prediction: {prediction}")
```

### Inspecting Model Parameters

```python
# Intercept (a in y = a + b₀x₀ + b₁x₁ + ...)
a = lr.intercept_

# Coefficients (b_i values)
B = lr.coef_

print(f"Model: y = {a:.2f} + {B[0]:.2f}*x₀ + {B[1]:.2f}*x₁")
```

### Classification Example

```python
from sklearn.linear_model import LogisticRegression

# Same workflow
clf = LogisticRegression()
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)  # Returns accuracy for classification

# Predict classes
y_pred = clf.predict(X_test)

# Predict probabilities
probs = clf.predict_proba(X_test)
```

### Pandas Integration

**Can use DataFrames instead of NumPy arrays:**

```python
import pandas as pd

df = pd.read_csv("data.csv")
X = df[['feature1', 'feature2']]
y = df['target']

# Works the same!
lr = LinearRegression()
lr.fit(X, y)
```

**⚠️ Important:** Be consistent - don't mix NumPy and Pandas.

---

## Hyperparameter Tuning

### Three Approaches to Improvement

1. **Different models** (e.g., Linear Regression vs Random Forest)
2. **Hyperparameter tuning** (model selection) ← This section
3. **Feature engineering** (covered next)

### Comparing Multiple Models

**Use duck typing for flexible model comparison:**

```python
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

models = [
    LinearRegression(),
    RandomForestRegressor(max_depth=3),
    RandomForestRegressor(max_depth=10),
    RandomForestRegressor(max_depth=20)
]

for model in models:
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{repr(model)}: {score:.2f}")
```

### Manual Grid Search

**Test all combinations of hyperparameters:**

```python
import itertools

n_estimators_list = [1, 10, 100]
max_depth_list = [2, 4, 8, 16, None]

for n_est, max_d in itertools.product(n_estimators_list, max_depth_list):
    rf = RandomForestRegressor(n_estimators=n_est, max_depth=max_d)
    rf.fit(X_train, y_train)
    score = rf.score(X_test, y_test)
    print(f"n_estimators={n_est}, max_depth={max_d}: {score:.3f}")
```

---

## Cross-Validation

### Why Cross-Validation?

**Problems with single train-test split:**
- Vulnerable to random variation in the split
- Some data never used for training

**Cross-validation solution:**
- Splits data into k folds (typically 5 or 10)
- Trains k times, each time on (k-1)/k of data
- Validates on remaining 1/k
- Returns k scores (average them for overall performance)

### Using Cross-Validation

```python
from sklearn.model_selection import cross_val_score

rf = RandomForestRegressor(n_estimators=50, max_depth=8)

# Perform 5-fold cross-validation
scores = cross_val_score(rf, X_train, y_train, cv=5)

print(f"Scores: {scores}")
print(f"Mean: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

**Parameters:**
- `cv=5`: Number of folds (default: 5)
- Returns array of k scores

### Grid Search with Cross-Validation

**Automate hyperparameter search with CV:**

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [1, 10, 100],
    'max_depth': [2, 4, 8, 16, None]
}

# Create grid search object
grid = GridSearchCV(
    RandomForestRegressor(), 
    param_grid, 
    cv=5,
    verbose=1  # Show progress
)

# Fit performs all combinations with cross-validation
grid.fit(X_train, y_train)

# Get best parameters
print(f"Best params: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.3f}")

# Score on test data
test_score = grid.score(X_test, y_test)
print(f"Test score: {test_score:.3f}")
```

**⚠️ Important:** Don't call `fit()` on the underlying model - `GridSearchCV` handles that!

### Advanced CV Options

```python
from sklearn.model_selection import LeaveOneOut, StratifiedKFold

# Leave-one-out (for small datasets)
loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo)

# Stratified K-fold (for imbalanced datasets)
skf = StratifiedKFold(n_splits=5)
scores = cross_val_score(model, X, y, cv=skf)
```

---

## Feature Selection

### Why Feature Selection?

**Benefits:**
- Reduce overfitting
- Improve training speed
- Improve model interpretability
- Reduce data collection costs

### Transformer Pattern

Both feature selection and engineering use **transformers**:

```python
# Basic transformer interface
transformer.fit(X)             # Learn from training data
X_new = transformer.transform(X)  # Apply transformation
# OR
X_new = transformer.fit_transform(X)  # Shortcut
```

### Filter Approach

**Calculate statistics per feature, keep those above threshold.**

#### Variance Threshold

Remove features with low variance (little information):

```python
from sklearn.feature_selection import VarianceThreshold

# Remove zero-variance features
sel = VarianceThreshold()
X_new = sel.fit_transform(X)

# Custom threshold
sel = VarianceThreshold(threshold=0.01)
X_new = sel.fit_transform(X)

print(f"Original features: {X.shape[1]}")
print(f"Selected features: {X_new.shape[1]}")
```

#### SelectKBest

Select k best features based on statistical tests:

```python
from sklearn.feature_selection import SelectKBest, chi2, f_classif

# For classification: chi-squared test
sel = SelectKBest(chi2, k=2)
X_new = sel.fit_transform(X, y)

# For regression: f-statistic
sel = SelectKBest(f_classif, k=5)
X_new = sel.fit_transform(X, y)

# See feature scores
print("Feature scores:", sel.scores_)
```

### Wrapper Approach

**Try different feature subsets and evaluate model performance.**

**Types:**
- **Forward selection**: Start empty, add best features
- **Backward elimination**: Start full, remove worst features
- **Metaheuristic**: Use optimization algorithms

#### Recursive Feature Elimination (RFE)

```python
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression

# RFE with cross-validation
selector = RFECV(LinearRegression(), cv=5)
X_new = selector.fit_transform(X_train, y_train)

# Apply to test set
X_test_new = selector.transform(X_test)

print(f"Optimal number of features: {selector.n_features_}")
print(f"Selected features: {selector.support_}")
```

---

## Feature Engineering

### Scaling

**Why:** Many ML algorithms work better with normalized features.

#### StandardScaler

Standardize features: zero mean, unit variance.

Formula: $(X - \bar{X}) / \sigma(X)$

```python
from sklearn.preprocessing import StandardScaler

# Fit on training data only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Apply same transformation to test data
X_test_scaled = scaler.transform(X_test)  # Don't refit!
```

**⚠️ Data Leakage Warning:**
- Calculate mean/std from **training set only**
- Apply same transformation to test set
- **Never** use test set statistics for training

#### Other Scalers

```python
from sklearn.preprocessing import MinMaxScaler, RobustScaler

# Scale to [0, 1] range
minmax = MinMaxScaler()
X_scaled = minmax.fit_transform(X_train)

# Robust to outliers (uses median and IQR)
robust = RobustScaler()
X_scaled = robust.fit_transform(X_train)
```

### Handling Missing Values

#### Imputation

```python
from sklearn.impute import SimpleImputer

# Impute with mean
imp = SimpleImputer(strategy='mean')
X_filled = imp.fit_transform(X)

# Other strategies
imp = SimpleImputer(strategy='median')
imp = SimpleImputer(strategy='most_frequent')
imp = SimpleImputer(strategy='constant', fill_value=0)
```

#### Dropping Missing Values

```python
import pandas as pd
import numpy as np

# With Pandas
df_clean = df.dropna()

# With NumPy (drop rows with any NaN)
mask = ~np.isnan(X).any(axis=1)
X_clean = X[mask]
y_clean = y[mask]  # Drop same rows from y!
```

### Polynomial Features

**Create polynomial features for nonlinear relationships:**

```python
from sklearn.preprocessing import PolynomialFeatures

# Create polynomial features up to degree 3
poly = PolynomialFeatures(degree=3, include_bias=False)
X_poly = poly.fit_transform(X)

# Example: [x] → [x, x², x³]
# Example: [x₀, x₁] → [x₀, x₁, x₀², x₀x₁, x₁², x₀³, x₀²x₁, x₀x₁², x₁³]
```

**Use with linear regression for polynomial regression:**

```python
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

lr = LinearRegression()
lr.fit(X_poly, y)
```

### One-Hot Encoding

**Convert categorical variables to binary features:**

```python
from sklearn.preprocessing import OneHotEncoder

# Example data
X = np.array([['a'], ['b'], ['c'], ['a'], ['b']])

# Fit on training data
ohe = OneHotEncoder(sparse=False)
ohe.fit(X_train)

# Transform both sets with same encoder
X_train_enc = ohe.transform(X_train)
X_test_enc = ohe.transform(X_test)

# Result: 'a' → [1, 0, 0], 'b' → [0, 1, 0], 'c' → [0, 0, 1]
```

**⚠️ Important:** Don't refit on test set - categories might differ!

### Pipelines

**Chain transformers and models together:**

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Create pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# Use like any other model
pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
predictions = pipe.predict(X_new)
```

**Benefits:**
- Prevents data leakage
- Cleaner code
- Works with GridSearchCV
- Ensures same preprocessing for training and testing

---

## Analyzing Errors

### Confusion Matrix

```python
from sklearn.metrics import confusion_matrix, classification_report

y_pred = clf.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
#       Predicted
#         0    1
# Actual 0  TN  FP
#        1  FN  TP

# Classification report
print(classification_report(y_test, y_pred))
```

### Visualizing Decision Boundaries

**For 2D data, visualize where the model makes decisions:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a grid
g = np.linspace(-5, 5, 101)
xg, yg = np.meshgrid(g, g)
xg = xg.flatten()
yg = yg.flatten()
Xg = np.array([xg, yg]).T

# Step 2: Predict probabilities on grid
probs = clf.predict_proba(Xg)
probs = probs[:, 1]  # P(y=1)
probs = probs.reshape(101, 101)

# Step 3: Plot contours with test data
fig, ax = plt.subplots(figsize=(8, 6))

# Contour plot of probabilities
contour = ax.contourf(g, g, probs, 25, cmap="RdBu", 
                       vmin=0, vmax=1)

# Add colorbar
ax_c = fig.colorbar(contour)
ax_c.set_label("$P(y = 1)$")

# Overlay test points
ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, 
           s=50, cmap="RdBu", vmin=-0.2, vmax=1.2,
           edgecolor="white", linewidth=1)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
```

**Requirements:**
- Model must have `predict_proba()` method
- For SVC: use `SVC(probability=True)`

**What it reveals:**
- Decision boundary (where $P(y=1) = 0.5$)
- Individual errors (points colored wrong for their region)
- Model confidence (color intensity)
- Linear vs nonlinear boundaries

### ROC Curve

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Get predicted probabilities
y_probs = clf.predict_proba(X_test)[:, 1]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
auc = roc_auc_score(y_test, y_probs)

# Plot
plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

## Quick Reference

### Standard Workflow

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Instantiate
model = LinearRegression()

# Fit
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)

# Predict
predictions = model.predict(X_new)
```

### Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'param1': [value1, value2],
    'param2': [value3, value4]
}

grid = GridSearchCV(Model(), param_grid, cv=5)
grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
```

### Feature Selection

```python
from sklearn.feature_selection import VarianceThreshold, SelectKBest

# Variance threshold
sel = VarianceThreshold(threshold=0.01)
X_new = sel.fit_transform(X)

# Select k best
sel = SelectKBest(chi2, k=10)
sel.fit(X_train, y_train)
X_train_new = sel.transform(X_train)
X_test_new = sel.transform(X_test)
```

### Feature Engineering

```python
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# One-hot encoding
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
X_encoded = ohe.fit_transform(X)
```

### Pipelines

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', LinearRegression())
])

pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
```

### Common Models

```python
# Regression
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
```

---

## Key Takeaways

### Workflow
1. **Always split data** before any processing
2. **Use consistent shapes** - X is 2D, y is 1D
3. **Follow the five steps** - Import, Instantiate, Fit, Evaluate, Predict
4. **Don't call fit() on GridSearchCV's underlying model**

### Data Hygiene
1. **Fit transformers on training data only**
2. **Apply same transformation to test data**
3. **Never use test set information during training**
4. **Use pipelines to prevent leakage**

### Hyperparameter Tuning
1. **Use cross-validation** - more reliable than single split
2. **Use GridSearchCV** - automates the process
3. **Start with wide ranges** - narrow down iteratively
4. **Monitor overfitting** - compare training vs test scores

### Feature Engineering
1. **Scaling often helps** - especially for distance-based methods
2. **Handle missing data** - impute or drop
3. **Create polynomial features** - for nonlinear relationships
4. **One-hot encode categoricals** - most models need numeric input

### Model Evaluation
1. **Use appropriate metrics** - accuracy, R², ROC-AUC, etc.
2. **Visualize errors** - decision boundaries, confusion matrices
3. **Check for overfitting** - compare train vs test scores
4. **Consider business context** - false positives vs false negatives

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 5*
