from collections import deque

# Queue Question
queue = deque()
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")
print("Queue:", list(queue))
first_task = queue.popleft()
print("First task:", first_task)
print("Remaining:", list(queue))