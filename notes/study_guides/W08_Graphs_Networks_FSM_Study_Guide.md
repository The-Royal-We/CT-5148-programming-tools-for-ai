# Week 8: Graphs, Networks, and State Machines - Study Guide

## Table of Contents
1. [Introduction to Graphs](#introduction-to-graphs)
2. [NetworkX Library](#networkx-library)
3. [Centrality Measures](#centrality-measures)
4. [Topological Sort](#topological-sort)
5. [Finite State Machines](#finite-state-machines)
6. [Graph Traversal](#graph-traversal)
7. [Shortest Path Problems](#shortest-path-problems)
8. [Quick Reference](#quick-reference)

---

## Introduction to Graphs

### What is a Graph?

A **graph** is a collection of objects (nodes/vertices) with connections (edges/arcs) among them.

**Terminology:**
- **Nodes** (vertices, points): The objects
- **Edges** (arcs, lines): The connections
- **Order**: Number of nodes
- **Size**: Number of edges

### Types of Graphs

**Directed vs Undirected:**
- **Undirected**: Edges have no direction (friendship, co-authorship)
- **Directed**: Edges have direction (Twitter follows, web links)

**Weighted vs Unweighted:**
- **Unweighted**: All edges are equal
- **Weighted**: Edges have values (distances, costs, capacities)

### Key Properties

**Cycles:**
- **Cycle**: Path starting and ending at same node
- **Directed cycle**: Path following edge directions
- **Acyclic**: No cycles (e.g., trees)

**Degree:**
- **Degree**: Number of neighbors
- **In-degree**: Incoming edges (directed graphs)
- **Out-degree**: Outgoing edges (directed graphs)

**Trees:**
- Graph with no cycles
- Examples: File systems, family trees, abstract syntax trees

### Real-World Applications

**1. Seven Bridges of Königsberg**
- Can you walk across all bridges without re-crossing?
- Founding problem of graph theory (Euler, 1736)

**2. Navigation Systems**
- Shortest path through road networks
- Dijkstra's algorithm

**3. Social Networks**
- Finding influential people
- Six degrees of separation
- Community detection

**4. The Web**
- Pages as nodes, hyperlinks as directed edges
- PageRank algorithm: a page is trusted if trusted pages link to it

**5. Collaboration Graphs**
- Authors/actors as nodes
- Co-authorship/co-starring as edges

**6. Infrastructure Networks**
- Power grids, water systems
- Capacity constraints

**7. Abstract Syntax Trees (AST)**
- Code represented as tree structure
- Used by interpreters/compilers

---

## Graph Representations

### 1. Adjacency Matrix

**n × n matrix** for n nodes:
- `0` = no edge
- `1` = edge exists
- For weighted graphs, use weight instead of 1

```
  | 0 1 2 3 4
--+----------
0 | 0 1 1 1 0
1 | 1 0 0 1 0
2 | 1 0 0 0 0
3 | 1 1 0 0 0
4 | 0 0 0 0 0
```

**Advantages:**
- Fast edge lookup: O(1)
- Good for dense graphs

**Disadvantages:**
- Memory: O(n²)
- Slow to find all neighbors

### 2. Adjacency Lists

**Dictionary mapping each node to its neighbors:**

```python
G = {
    0: [1, 2, 3], 
    1: [0, 3], 
    2: [0], 
    3: [0, 1], 
    4: []
}
```

**Advantages:**
- Memory: O(n + m) where m = edges
- Fast neighbor lookup
- Good for sparse graphs

### 3. List of Edges

**Simple list of tuples:**

```python
G = [(0, 1), (0, 2), (0, 3), (1, 3)]
```

**Use case:** Simple, compact representation

---

## NetworkX Library

### Creating Graphs

```python
import networkx as nx

# Undirected graph
G = nx.Graph()

# Add nodes
G.add_node(0)
G.add_nodes_from([1, 2, 3, 4])
G.add_nodes_from(range(5))

# Add edges
G.add_edge(0, 1)
G.add_edge(0, 2, weight=0.5)  # With properties

# Add multiple edges
G.add_edges_from([(1, 3), (0, 3)])
```

### Directed Graphs

```python
# Directed graph
D = nx.DiGraph()
D.add_edge(0, 1)  # 0 → 1
D.add_edge(1, 0)  # 1 → 0 (different edge!)
```

### NetworkX Representation

**Dict-of-dicts-of-dicts:**

```python
G = {
    0: {1: {"weight": 0.5}, 2: {"weight": 0.1}},
    1: {0: {"weight": 0.5}, 3: {"weight": 0.3}},
    2: {0: {"weight": 0.1}},
    3: {1: {"weight": 0.3}},
}
```

### Reading Graphs from Files

```python
import networkx as nx

G = nx.Graph()

# Read from CSV
with open("data/edges.csv") as f:
    for line in f:
        n1, n2 = line.strip().split(",")
        G.add_edge(n1, n2)
```

### Visualization

```python
import matplotlib.pyplot as plt

nx.draw_spring(G, with_labels=True)
plt.savefig("graph.pdf")
plt.show()
```

**Layout options:**
- `nx.draw_spring()` - force-directed layout
- `nx.draw_circular()` - circular arrangement
- `nx.draw_random()` - random positions
- `nx.draw_shell()` - concentric circles

---

## Centrality Measures

### 1. Degree Centrality

**Counts connections:**

```python
centrality = nx.degree_centrality(G)
# Returns: {node: degree/max_possible_degree}
```

**Interpretation:**
- Higher value = more connections
- Normalized by maximum possible degree

### 2. Betweenness Centrality

**Measures "betweenness":**

```python
centrality = nx.betweenness_centrality(G)
```

**Interpretation:**
- How often a node appears on shortest paths
- High values = "broker" or "bridge" positions
- Important for controlling information flow

**Example:** Medici family in Florence had high betweenness - they connected different groups.

### 3. Eigenvector Centrality (PageRank)

**A node is important if connected to important nodes:**

```python
centrality = nx.eigenvector_centrality(G)
# Or for directed graphs:
pagerank = nx.pagerank(G)
```

**Interpretation:**
- Circular definition that converges
- Same principle as Google's PageRank
- Connection to important nodes > connection to many nodes

### Comparing Centrality Measures

```python
import pandas as pd

df = pd.DataFrame({
    'degree': nx.degree_centrality(G),
    'betweenness': nx.betweenness_centrality(G),
    'eigenvector': nx.eigenvector_centrality(G)
})

print(df.sort_values('betweenness', ascending=False))
```

---

## Topological Sort

### Definition

**Topological sort** orders nodes in a directed graph so all edges point "forward":
- For every edge (i, j), node j appears after node i

**Only exists for Directed Acyclic Graphs (DAGs)**
- If cycles exist, topological sort is impossible

### Applications

**1. Project Planning**
- Tasks with dependencies
- Provides valid execution order
- Identifies parallel tasks

```python
# Building a house
D = nx.DiGraph()
D.add_edge("buy bricks", "build walls")
D.add_edge("buy wood", "build roof")
D.add_edge("build walls", "build roof")
D.add_edge("build walls", "install door")
D.add_edge("buy door", "install door")
```

**2. Data-Flow Graphs**
- Excel formulas
- Cell dependencies
- Update order

**3. Package Management**
- Library dependencies
- Installation order

**4. Build Systems**
- Compilation dependencies
- Make, Ant, Maven

### Algorithm

```
1. Find node n with in-degree 0
2. If none exist → cycle detected → fail
3. Add n to output, remove n and its edges
4. Repeat until graph is empty
```

### Implementation

```python
def topological_sort(D):
    """Return topological ordering of nodes."""
    output = []
    D = D.copy()  # Don't modify original
    
    while D.order():  # While nodes remain
        # Find node with in-degree 0
        remove_node = None
        for n in D:
            if D.in_degree(n) == 0:
                remove_node = n
                break
        
        if remove_node is not None:
            output.append(remove_node)
            D.remove_node(remove_node)  # Removes edges too
        else:
            raise ValueError("Cycle detected!")
    
    return output
```

### Using NetworkX

```python
# NetworkX provides built-in topological sort
order = list(nx.topological_sort(D))
```

**Note:** Topological sort is not unique - multiple valid orderings may exist.

---

## Finite State Machines

### What is an FSM?

**Components:**
1. **States** - Discrete conditions
2. **Edges** - Transitions between states (labeled with inputs)
3. **Start state** - Initial state
4. **End states** - Validation/accepting states (optional)

**Execution:**
- At each step, receive an input
- Follow edge matching that input
- Optionally execute action
- Move to new state

### Applications

**1. Communication Protocols**
- HTTP states and transitions
- Network protocol validation

**2. Game AI**
- NPC behavior (DOOM: Standing, Walking, Chasing, Attacking, Dying)
- State transitions based on player proximity, damage

**3. Parsing**
- Compiler design
- Input validation

**4. User Interfaces**
- Application states
- Button enabled/disabled logic

### Key Insight

**All FSMs share the same code structure** - they differ only in their data (transition table).

### Implementation

```python
class ValidationFSM:
    def __init__(self, transition_table, initial_state, end_states):
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.end_states = end_states
    
    def validate_sequence(self, sequence):
        """Check if sequence is valid."""
        self.state = self.initial_state
        
        for symbol in sequence:
            try:
                # Follow transition for this symbol
                self.state = self.transition_table[self.state][symbol]
            except KeyError:
                return False  # No valid transition
        
        # Check if we ended in an acceptable state
        return self.state in self.end_states
```

### Example Usage

```python
# Define transition table
transition_table = {
    0: {'a': 1},
    1: {'a': 2},
    2: {'a': 3},
    3: {'a': 7, 'b': 4, 'c': 5, 'd': 6},
    4: {'b': 3},
    5: {'c': 3},
    6: {'d': 3},
    7: {'a': 7}  # Can stay in end state
}

fsm = ValidationFSM(transition_table, 
                    initial_state=0, 
                    end_states=[7])

print(fsm.validate_sequence('aaabba'))    # True
print(fsm.validate_sequence('aaaccaaa'))  # True
print(fsm.validate_sequence('aaabca'))    # False
```

### FSM ⟷ Regular Expressions

**FSMs and regular expressions are equivalent:**
- Any FSM can be converted to a regex
- Any regex can be converted to an FSM
- RegEx implementations use FSMs internally

---

## Graph Traversal

### Depth-First Traversal

**Explore as deep as possible before backtracking.**

#### Depth-First Preorder

Visit node before children:

```python
def depth_first_preorder(G, n):
    """Traverse tree in preorder."""
    yield n  # Visit node first
    for m in G[n]:
        yield from depth_first_preorder(G, m)

# Result: a, b, d, e, c
```

#### Depth-First Postorder

Visit node after children:

```python
def depth_first_postorder(G, n):
    """Traverse tree in postorder."""
    for m in G[n]:
        yield from depth_first_postorder(G, m)
    yield n  # Visit node last

# Result: d, e, b, c, a
```

### Handling Cycles

**Problem:** In graphs (not trees), must avoid revisiting nodes.

**Solution:** Track visited nodes.

```python
def depth_first_graph(G, n):
    """DFS for graphs with cycles."""
    visited = set()
    
    def _helper(n):
        if n in visited:
            return  # Don't revisit
        yield n
        visited.add(n)
        for m in G[n]:
            yield from _helper(m)
    
    yield from _helper(n)
```

### Breadth-First Search (BFS)

**Explore level by level (outward from start).**

```python
from collections import deque

def breadth_first(G, n):
    """BFS traversal."""
    queue = deque([n])
    visited = set([n])
    
    while queue:
        n = queue.popleft()
        yield n
        for m in G[n]:
            if m not in visited:
                visited.add(m)
                queue.append(m)

# Result: a, b, c, d, e
```

**Key difference from DFS:**
- Uses **queue** (FIFO) instead of recursion (stack/LIFO)
- Finds **shortest path** in unweighted graphs

### DFS vs BFS

| Property | DFS | BFS |
|----------|-----|-----|
| Data structure | Stack (recursion) | Queue |
| Memory | O(h) height | O(w) width |
| Shortest path | No | Yes (unweighted) |
| Use case | Explore all paths | Find nearest solution |

---

## Shortest Path Problems

### Dijkstra's Algorithm

**Generalization of BFS for weighted graphs:**

**Algorithm:**
1. Maintain distances to all nodes (initially ∞)
2. Start with source node (distance 0)
3. Repeatedly:
   - Visit unvisited node with smallest distance
   - Update distances to its neighbors
4. Stop when target is visited

### Using NetworkX

```python
# Shortest path
path = nx.shortest_path(G, source=0, target=4, weight='weight')
print(path)  # [0, 1, 3, 4]

# Path length
length = nx.shortest_path_length(G, source=0, target=4, weight='weight')
print(length)  # Total weight

# All shortest paths from one source
paths = nx.single_source_shortest_path(G, source=0)
lengths = nx.single_source_shortest_path_length(G, source=0)
```

### Searching Infinite Graphs

**Problem:** "Calculator with 3 buttons: ×3, +2, -2. Get from 0 to 100 with minimum presses."

**Solution:** Generate graph during BFS.

```python
from collections import deque

def bfs_generative(start, target, moves):
    """BFS for infinite/large graphs.
    
    Args:
        start: Starting state
        target: Goal state
        moves: Function that returns possible next states
    """
    if start == target:
        return [start]
    
    back_pointers = {}  # Track how we got here
    queue = deque([start])
    
    while queue:
        n = queue.popleft()
        for m in moves(n):
            if m in back_pointers:
                continue  # Already visited
            
            queue.append(m)
            back_pointers[m] = n
            
            if m == target:
                return reconstruct_path(back_pointers, start, target)
    
    return None  # No path found

def reconstruct_path(back_pointers, start, target):
    """Build path from start to target."""
    path = [target]
    while target != start:
        target = back_pointers[target]
        path.append(target)
    path.reverse()
    return path
```

**Usage:**

```python
start = 0
target = 100
moves = lambda x: (x*3, x+2, x-2)

path = bfs_generative(start, target, moves)
print(path)  # Optimal sequence
```

**Other applications:**
- Farmer, wolf, goat, cabbage puzzle
- Sliding tile puzzles
- Rubik's cube solving
- Any state-space search problem

---

## Quick Reference

### NetworkX Basics

```python
import networkx as nx

# Create graphs
G = nx.Graph()           # Undirected
D = nx.DiGraph()         # Directed

# Add nodes/edges
G.add_node(0)
G.add_nodes_from([1, 2, 3])
G.add_edge(0, 1, weight=5)
G.add_edges_from([(1, 2), (2, 3)])

# Properties
G.order()               # Number of nodes
G.size()                # Number of edges
G.degree(node)          # Node degree
D.in_degree(node)       # Incoming edges
D.out_degree(node)      # Outgoing edges

# Visualization
nx.draw_spring(G, with_labels=True)
```

### Centrality Measures

```python
nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.eigenvector_centrality(G)
nx.pagerank(D)  # For directed graphs
```

### Algorithms

```python
# Topological sort (DAG only)
order = list(nx.topological_sort(D))

# Shortest paths
path = nx.shortest_path(G, source, target, weight='weight')
length = nx.shortest_path_length(G, source, target)

# All paths from source
paths = nx.single_source_shortest_path(G, source)

# Check for cycles
nx.is_directed_acyclic_graph(D)

# Connected components
nx.connected_components(G)
nx.strongly_connected_components(D)
```

### Traversal Patterns

```python
# DFS
def dfs(G, start):
    visited = set()
    def _dfs(n):
        if n in visited:
            return
        visited.add(n)
        yield n
        for neighbor in G[n]:
            yield from _dfs(neighbor)
    yield from _dfs(start)

# BFS
from collections import deque
def bfs(G, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        n = queue.popleft()
        yield n
        for neighbor in G[n]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## Key Takeaways

### Graphs are Everywhere
1. **Social networks, infrastructure, the web** - graphs model connections
2. **Multiple representations** - choose based on the problem
3. **NetworkX provides** most graph algorithms

### Centrality Matters
1. **Degree** - raw number of connections
2. **Betweenness** - broker positions, information flow
3. **Eigenvector/PageRank** - connected to important nodes

### Topological Sort
1. **Only for DAGs** - directed acyclic graphs
2. **Essential for dependencies** - package management, build systems
3. **Not unique** - multiple valid orderings possible

### Finite State Machines
1. **States + transitions** - simple, elegant model
2. **All FSMs share structure** - differ only in data
3. **Equivalent to regexes** - theoretical foundation of parsing

### Traversal Strategies
1. **DFS** - explore deeply, good for finding any solution
2. **BFS** - explore broadly, finds shortest path
3. **Handle cycles** - track visited nodes
4. **Generate on-the-fly** - for large/infinite graphs

### Practical Applications
1. **Navigation** - shortest paths
2. **Dependency management** - topological sort
3. **Influence analysis** - centrality measures
4. **State machines** - protocols, game AI, parsers
5. **Puzzle solving** - state-space search

---

*Study Guide created for CT-5148 Programming Tools for AI - Week 8*
