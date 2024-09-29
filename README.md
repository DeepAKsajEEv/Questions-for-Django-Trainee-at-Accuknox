# Topic 1: Django Signals
### Question 1: Are Django signals executed synchronously or asynchronously by default?

Answer: By default, Django signals are executed synchronously. This means the signal handler runs in the same flow as the event that triggered the signal, causing it to block the execution until it completes.

### Question 2: Do Django signals run in the same thread as the caller?
Answer: Yes, Django signals run in the same thread as the caller. When a signal is triggered, the signal handler executes in the same thread as the code that fired the signal.

### Question 3: Do Django signals run in the same database transaction as the caller?
Answer: By default, Django signals run in the same database transaction as the caller. This means that if a transaction is open, the signal handler will be part of the same transaction. If the transaction rolls back, the signal’s side effects will be rolled back as well.

# Topic 2: Custom Classes in Python
### Task: Implement a Rectangle class that allows iteration over its dimensions.

Requirement:
An instance of the Rectangle class requires length and width to be initialized.
We can iterate over an instance of the Rectangle class.
When iterated, the instance yields its length in the format {'length': <VALUE_OF_LENGTH>} followed by its width in the format {'width': <VALUE_OF_WIDTH>}.
