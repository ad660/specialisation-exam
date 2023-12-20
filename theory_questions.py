'''

1. The deque module is part of which python library?
answer: Collections

2. What are 2 differences that distinguish a tree from a graph?
So a tree is acyclic (does not contain any cycles or loops) whereas a graph can contain both.
Furthermore, as a tree is a type of graph that is connected in between paths of nodes while a graph can be connected
or disconnected because it does not have to have a root node.


3. Give the definitions of time complexity and space complexity
Time complexity - The calculation of the amount of run time needed and how many fundamental operations it needs to
perform.

Space complexity - describes how much memory or space an algorithm requires as a function of
input size in order to carry out its functions.

4. Describe the buble sort algorithm and its complexity. What is guaranteed at the end of the first pass?
Bubble sort iteratively steps through the list, compares neighbouring elements, and swaps them if they are out of order.
Until no swaps are required—a sign that the list is sorted—the trip through the list is repeated.
The steps for bubble swap are as follows:

1. Begin at the top of the list (also known as the leftmost element).
2. Analyse the first two components in comparison. Swap them if they are not in the correct order,
e.g. when the current element is bigger than the subsequent element in ascending order.
3. In the list, go one item to the right until you get to the end of the list
4. then start from the top of the list again and once more, analyse the first two components in comparison.
The biggest element in the list's unsorted section has now "bubbled up" to the end of the list.

In terms of complexity its time complexity differs depending on if the list is in reverse order as opposed to sort.
Bubble Sort performs n*(n-1)/2 comparisons and swaps when the list is in reverse order but in general,
bubble sort has a time complexity of O(n^2).
Bubble Sort doesn't require more memory other than the original input list therefore it's space complexity is O(1).

5. Explain what LIFO and FIDO are and how each works in practice with a named data structure

First-In-First-Out (FIFO) and Last-In-First-Out (LIFO) specify which elements can be added to and removed from
the data structure in what order. Let's examine each idea and their practical application to named data structures:
One named data structure that makes use of FIFO is called a "queue." within the collections' module.

enqueue: Appends a piece of data to the end (back) of the queue.
Dequeue: Takes an element out of the front (head) of the queue and puts it back.

6. What is a Balanced Binary Tree and what would be the best root? Walk through how you would search using this feature.

A balanced binary tree makes sure that each node's left and right subtrees differ in depth by no more than one.
It keeps search, insert, and remove operations in data structures like Red-Black trees and AVL efficient.
Optimal Root Choice:

A balanced structure with nearly equal numbers of nodes on the left and right subtrees is the goal of the
optimal root selection.

In order to look for items in a balanced binary tree you have to do the following:

Start with the root then compare with the node that is currently in use.
When there's a match, the search ends.
Proceed left if less, and right if greater.
Until the value is located or a leaf node is reached, repeat steps 2-4.
Because of the logarithmic depth (O(log n)), efficient.
'''
