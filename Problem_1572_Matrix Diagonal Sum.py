'''
Calculating the Diagonal Sum of nxn matrix

To calculate the sum of the matrix:
* Always add [0,0], [0,n], [n,0], and [n,n] elements
* Consider [row_number_index, row_number_index] element always
* Remaining all elements in a row can be accessed while iterating using [n - row_number_index - 1]
* Ignore adding the same element to the sum by writing a if condition.
  For Example, in a 3x3 matrix, [1, 1] will be already considered as per the above procedure. So, avoid the same by adding a condition
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """ For returning the sum of the diagonal elements of a square matrix """
        mat_shape = len(mat)  # To get the shape of the matrix such as 3x3, 4x4, 5x5 etc.
        diagonal_total = 0  # Intial Diagonal Sum value of the matrix
        

        # A for loop to iterate over all the rows of the matrix
        
        for row_num in range(mat_shape):
            diagonal_total += mat[row_num][row_num]
            
            # To check whether the [row_number_index, row_number_index] element is already added into the sum or not
            
            if row_num != mat_shape - row_num - 1:
                diagonal_total += mat[row_num][mat_shape - row_num - 1]
        return diagonal_total
