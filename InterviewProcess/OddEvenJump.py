"""
You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.
"""


def main():
    A = [5, 1, 3, 4, 2]
    print(oddEvenJumps(A))


def oddEvenJumps(A):
    N = len(A)

    def make(B):
        ans = [None] * N
        stack = []  # invariant: stack is decreasing
        for i in B:
            while stack and i > stack[-1]:
                ans[stack.pop()] = i
            stack.append(i)
        return ans

    B = sorted(range(N), key=lambda i: A[i])
    oddnext = make(B)
    B.sort(key=lambda i: -A[i])
    evennext = make(B)

    odd = [False] * N
    even = [False] * N
    odd[N-1] = even[N-1] = True

    for i in range(N-2, -1, -1):
        if oddnext[i] is not None:
            odd[i] = even[oddnext[i]]
        if evennext[i] is not None:
            even[i] = odd[evennext[i]]

    return sum(odd)


if __name__ == "__main__":
    main()
