# PLP Python Week 7 Assignment: Shopping List Manager

## File Descriptions
* **list_warmup.py**: Demonstrates basic Python list operations (indexing, appending, removing, and length tracking).
* **shopping_list.py**: Interactive shopping list manager with robust state tracking and error-preventing conditional checks.
* **list_report.py**: Analyzes data arrays via loops, index mapping, string length evaluation, and comparison.
* **README.md**: Repository documentation and prompt concept explanation.

## Conceptual Question Explanation
**Why is it safer to check `in` before calling `.remove()`?**
Checking membership with the `in` operator before attempting to remove an element prevents Python from throwing an unhandled `ValueError` when an item does not exist. It allows the program to gracefully catch missing elements and show a helpful user message instead of crashing.
