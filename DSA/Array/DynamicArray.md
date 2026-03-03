# Dynamic Array

## Video Summary
Source: https://youtu.be/nmViR9KtYyY
Title: `2.4 Dynamic Array Explained | Amortized Analysis | DSA in Python | Hindi` (Decode AiML)

This video explains why a dynamic array is needed, how insertion works when capacity is full, and why average insertion cost is still efficient.

### Key Points
- A dynamic array stores elements in contiguous memory like a normal array, but it can grow when full.
- When capacity is full, a new larger array is allocated (typically double size), old elements are copied, and then insertion continues.
- Most insertions are `O(1)` because they only place the new element at the end.
- Resize insertions are expensive (`O(n)`) because of copying.
- Amortized analysis shows that over many insertions, average cost per insertion is still `O(1)`.

### Amortized Intuition
- If capacity grows geometrically (for example, `1 -> 2 -> 4 -> 8 ...`), total copy work across `n` appends forms a geometric series.
- Total work over `n` appends becomes linear, so average per append is constant.
- So `append` in dynamic array is **amortized `O(1)`**, not worst-case `O(1)`.

### Python List Connection
- Python `list` behaves like a dynamic array internally.
- `append()` is usually constant time, but occasionally slower during resize.
- This is the reason Python lists perform well for append-heavy workloads.

### Complexity Summary
- Access by index: `O(1)`
- Update by index: `O(1)`
- Append: amortized `O(1)`, worst-case `O(n)` on resize
- Insert/Delete in middle: `O(n)` due to shifting

### Practical Takeaway
Dynamic arrays trade occasional expensive resizes for very fast average append performance, which is why they are one of the most useful core data structures in real systems and interview problems.
