# Selection sort

Selectin Sort is a naive sorting algorithm which involves finding the minimum element in one pass through the array and then swapping it with the first position of the unsorted part of the array. Time complexity of selection sort is O(n^2) in all cases.

Selection sort is one of the slowest algorithms and can fall behind bubble sort. But slow doesn’t always mean its bad in all potential cases, often being the last to finish sorting for large arrays. However, it does work very well on small lists.

Selection sort can be good at checking if everything is already sorted. It is also good to use when memory space is limited. This is because unlike other sorting algorithms, selection sort doesn’t go around swapping things until the very end, resulting in less temporary storage space used.
