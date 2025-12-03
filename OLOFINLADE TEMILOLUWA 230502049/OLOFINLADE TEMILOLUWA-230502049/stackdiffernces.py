

# 1. Points of Access:
# Stack;

# Only one end is used for inserting (push) and removing (pop) items.

# Queue;

# Uses two ends:
# Front → removal (dequeue)
# Rear → insertion (enqueue)

# 2. Typical Operations:
# Stack;

# push(), pop(), peek() (view top element)

# Queue;

# enqueue(), dequeue(), front(), rear()

# . Real-World Uses:
# Stack;

# Function call management in programming languages
# Undo/redo systems in text editors
# Syntax parsing or backtracking (e.g., DFS in graphs)

# Queue;

# Managing tasks in operating systems (job scheduling)
# Network buffering and packet processing
# Breadth-first search (BFS) in algorithms

# 4. Memory Behavior:
# Stack;

# Works well for backtracking (store previous states).
# Often implemented using dynamic arrays or linked lists.

# Queue;

# Works well for scheduling and sequential processing.
# Implemented using arrays, linked lists, or circular arrays for efficiency.


# 5. Conceptual Difference:
# Stack;

# Best for scenarios where the most recent action must be reversed first.

# Queue;

# Best for scenarios requiring fairness, where the first request should be served first.


# Q2. Time Complexity of Stack and Queue?

# Answer;
# 1. Stack Time Complexity;
# | Operation                | Description                              | Time Complexity |
# | ------------------------ | ---------------------------------------- | --------------- |
# | push()                   | Insert an element on top of the stack    | O(1)            |
# | pop()                    | Remove the top element                   | O(1)            |
# | peek()/top()             | View the top element without removing it | O(1)            |
# | isEmpty()                | Check if stack is empty                  | O(1)            |
# | Search (rarely used)     | Finding an element in the stack          | O(n)            |

# Why?

# All core stack operations happen at one end only, so no traversal is needed.
# Therefore, each core operation executes in constant time.

# 2. Queue Time Complexity;
# | Operation               | Description                      | Time Complexity |
# | ----------------------- | -------------------------------- | --------------- |
# |   enqueue()             | Insert an element at the rear    |   O(1)          |
# |   dequeue()             | Remove an element from the front |   O(1)          |
# |   isEmpty()             | Check if queue is empty          |   O(1)          |
# |   Search (not common)   | Finding an element               |   O(n)          |

# Why?

# A queue works with two ends (front and rear), so inserting or removing does not require shifting or traversing.
# With a proper structure (linked list or circular buffer), all main operations are constant time.