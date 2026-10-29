class Matrix:
    def __init__(self,rows):
        if rows and any(len(row) != len(rows[0]) for row in rows):
            raise ValueError("All rows must have same length")
        self.rows =[row[:] for row in rows]
    def __str__(self):
        if not self.rows:
            return "[]"
        cols=len(self.rows[0])
        widths=[
            max(len(str(row[j])) for row in self.rows)
            for j in range(cols)
        ]
        lines=[]
        for row in self.rows:
            values=" ".join(
                str(value).rjust(widths[j])
                for j,value in enumerate(row)
            )
            lines.append(f"| {values} |")
        return "\n".join(lines)
    def __repr__(self):
        return f"Matrix({self.rows!r})"    
    def __eq__(self, value):
        if not isinstance(value,Matrix):
            return NotImplemented
        return self.rows == value.rows
    def __add__(self, other):
        if not isinstance(other,Matrix):
            return NotImplemented
        if self.dimensions() != other.dimensions():
            raise ValueError("Matrices must have same dimenstions")
        result=[
            [a + b for a,b in zip(row_a ,row_b)]
            for row_a, row_b in zip(self.rows ,other.rows)
        ]
        return Matrix(result)
    def __mul__(self, other):
        if not isinstance(other,Matrix):
            return NotImplemented
        rows_a,cols_a=self.dimensions()
        rows_b,cols_b=other.dimensions()
        if cols_a != rows_b:
            raise ValueError("Inner dimenstions must match for Matrix multiplication")
        result=[
            [
            sum(self.rows[i][k] * other.rows[k][j] for k in range(cols_a))
                for j in range(cols_b)]
            for i in range(rows_a)
        ]
        return Matrix(result)
    def __getitem__(self, index):
        return self.rows[index]
    def __len__(self):
        return len(self.rows)
    def dimensions(self):
        rows=len(self.rows)
        cols=len(self.rows[0]) if rows > 0 else 0
        return (rows,cols)
    def transpose(self):
        return Matrix([
            list(column)
            for column in zip(*self.rows)
        ])
A= Matrix([[1,2,3],
         [4,5,6]])
B= Matrix([[7,8,9],
         [10,11,12]])
print("Matrix A (2x3):")
print(A)
print("\nMatrix B (2x3):")
print(B)
print("\nA + B")
print(A + B)
C=Matrix([[1,2],
         [3,4],
         [5,6]])
print("\nMatrix C (3x2):")
print(C)
print("\nA * C")
print(A * C)
print("\nA[0][2]=",A[0][2])
print("A[0]=",A[0])
print("len(A)=",len(A))
print("dimensions:",A.dimensions())
print("\nTranspose of A:")
print(A.transpose())
try:
    print(A + C)
except ValueError as e:
    print("\nAdding matrices with different dimensions:")
    print(f"ValueError: {e}")
print("\nA == B:", A == B)
try:
    invalid = Matrix([[1, 2], [3]])
except ValueError as e:
    print("Invalid matrix:", e)
        
""" Matrix Class
You'll practice 
Arithmetic operators, indexing, and equality for a 2D data structure
Create a Matrix class for 2D matrices.

Constructor: Takes a list of lists (rows). Validates that all rows have the same length.

Dunder methods:
- __str__ — pretty prints the matrix with aligned columns
- __repr__ — returns "Matrix([[1, 2], [3, 4]])"
- __eq__ — matrices are equal if all elements match
- __add__ — matrix addition (must be same dimensions — raise ValueError if not)
- __mul__ — matrix multiplication (inner dimensions must match — raise ValueError if not). Note: this is proper matrix multiplication, not element-wise.
- __getitem__ — m[0] returns row 0 as a list. m[0][1] returns element at row 0, col 1.
- __len__ — returns number of rows

Regular methods:
- dimensions() — returns tuple (rows, cols)
- transpose() — returns a new Matrix that is the transpose

Demonstrate with at least two matrices:
1. Print both matrices formatted
2. Add them
3. Multiply them (use compatible dimensions)
4. Access specific elements with indexing
5. Print len and dimensions
6. Print the transpose
7. Try adding matrices with different dimensions — show error

Example output:

Matrix A (2x3):
| 1  2  3 |
| 4  5  6 |

Matrix B (2x3):
| 7  8  9 |
| 10 11 12 |

A + B:
| 8  10 12 |
| 14 16 18 |

A[0][2] = 3
len(A) = 2
dimensions: (2, 3)

Transpose of A:
| 1  4 |
| 2  5 |
| 3  6 |
 """
    