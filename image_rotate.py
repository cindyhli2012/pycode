class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ls = 0
        le = n-1
        while (ls < le):
            # operate the layer with boundary ls and le for row and col
            # row = ls, le (with col :ls to le)
            # col = ls, le (with row: ls to le)
            # move row ls to col le, col le to row le, row le to col ls, col ls to row ls: clockwise
            j = ls # for row ls
            while j < le:
                tmp = matrix[ls][j] # start with first of row ls
                # rotate the relevant values for row ls, col j
                matrix[ls][j] = matrix[le+ls-j][ls]
                matrix[le+ls-j][ls] = matrix[le][le+ls-j]
                matrix[le][le+ls-j] = matrix[j][le]
                matrix[j][le] = tmp
                j += 1
            ls += 1
            le -= 1
