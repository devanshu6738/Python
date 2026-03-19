🧠 Problem: Concurrent Array Sum Using Threads

You are given a large array of integers. Your task is to compute the total sum of the array using multithreading to improve performance.

📌 Requirements

Divide the array into N equal (or near-equal) parts.

Create N threads, where each thread:

Computes the sum of its assigned subarray.

Combine the partial sums from all threads to produce the final total sum.

🔧 Input

An integer array arr of size M

An integer N representing the number of threads

🎯 Output

A single integer representing the total sum of the array

⚠️ Constraints

1 ≤ M ≤ 10^7

1 ≤ N ≤ 100

Threads should not overlap in processing indices

Handle cases where M % N ≠ 0

🧩 Example

Input:

arr = [1, 2, 3, 4, 5, 6, 7, 8]
N = 3

Possible Division:

Thread 1 → [1, 2, 3]

Thread 2 → [4, 5, 6]

Thread 3 → [7, 8]

Output:

36
🚀 Bonus Challenges

🔒 Ensure thread-safe accumulation (use mutex/lock or atomic variables)

⚡ Compare performance with single-threaded solution

🧪 Handle extremely large arrays efficiently

🔄 Use thread pools instead of manually creating threads