ef input_matrix(rows, cols):
  matrix = []
  print("Enter the elements of the matrix:")
  for i in range(rows):
      row = []
      for j in range(cols):
          element = float(input(f"Enter element at row {i+1} column {j+1}: "))
          row.append(element)
      matrix.append(row)
  return matrix

def print_matrix(matrix):
  for row in matrix:
      print("(", end="")
      for element in row:
          print(f"{element:<7.2f}", end="")
      print(")")

def add_matrices(matrix1, matrix2):
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
      print("\nAddition operation cannot be performed because the sizes of the matrices are not the same.")
      return None

  result = []
  for i in range(len(matrix1)):
      row = []
      for j in range(len(matrix1[0])):
          row.append(matrix1[i][j] + matrix2[i][j])
      result.append(row)

  print("\nResult of matrix addition:")
  print_matrix(result)
  return result

def subtract_matrices(matrix1, matrix2):
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
      print("\nSubtraction operation cannot be performed because the sizes of the matrices are not the same.")
      return None

  result = []
  for i in range(len(matrix1)):
      row = []
      for j in range(len(matrix1[0])):
          row.append(matrix1[i][j] - matrix2[i][j])
      result.append(row)

  print("\nResult of matrix subtraction:")
  print_matrix(result)
  return result

def multiply_matrices(matrix1, matrix2):
  if len(matrix1[0]) != len(matrix2):
      print("\nMultiplication operation cannot be performed because the number of columns in the first matrix is not equal to the number of rows in the second matrix.")
      return None

  result = []
  for i in range(len(matrix1)):
      row = []
      for j in range(len(matrix2[0])):
          total = 0
          for k in range(len(matrix2)):
              total += matrix1[i][k] * matrix2[k][j]
          row.append(total)
      result.append(row)

  print("\nResult of matrix multiplication:")
  print_matrix(result)
  return result

def transpose_matrix(matrix):
  result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
  print("\nResult of matrix transpose:")
  print_matrix(result)
  return result

def determinant_matrix(matrix):
  if len(matrix) != len(matrix[0]):
      print("\nDeterminant can only be calculated for square matrices.")
      return None

  def recursive_determinant(matrix):
      if len(matrix) == 1:
          return matrix[0][0]
      elif len(matrix) == 2:
          return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
      else:
          det = 0
          for i in range(len(matrix)):
              minor = [row[:i] + row[i+1:] for row in matrix[1:]]
              det += (-1)**i * matrix[0][i] * recursive_determinant(minor)
          return det

  det = recursive_determinant(matrix)
  print(f"\nDeterminant of the matrix: {det}")
  return det

def inverse_matrix(matrix):
  if len(matrix) != len(matrix[0]):
      print("\nInverse matrix can only be calculated for square matrices.")
      return None

  det = determinant_matrix(matrix)
  if det == 0:
      print("\nThe matrix does not have an inverse.")
      return None

  def cofactor(matrix, i, j):
      minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
      return (-1)**(i+j) * determinant_matrix(minor)

  inv = []
  for i in range(len(matrix)):
      row = []
      for j in range(len(matrix[0])):
          row.append(cofactor(matrix, i, j) / det)
      inv.append(row)

  print("\nInverse matrix:")
  print_matrix(inv)
  return inv

def main():
  while True:
      print("\nChoose matrix operation:")
      print("1. Addition, subtraction, multiplication of matrices")
      print("2. Transpose of matrix")
      print("3. Calculate determinant of matrix")
      print("4. Calculate inverse of matrix")
      choice = input("Enter choice (1/2/3/4): ")

      if choice == '1':
          rows1 = int(input("Enter the number of rows of the first matrix: "))
          cols1 = int(input("Enter the number of columns of the first matrix: "))
          matrix1 = input_matrix(rows1, cols1)

          rows2 = int(input("Enter the number of rows of the second matrix: "))
          cols2 = int(input("Enter the number of columns of the second matrix: "))
          matrix2 = input_matrix(rows2, cols2)

          add_matrices(matrix1, matrix2)
          subtract_matrices(matrix1, matrix2)
          multiply_matrices(matrix1, matrix2)

      elif choice == '2':
          rows = int(input("Enter the number of rows of the matrix: "))
          cols = int(input("Enter the number of columns of the matrix: "))
          matrix = input_matrix(rows, cols)
          transpose_matrix(matrix)

      elif choice == '3':
          rows = int(input("Enter the number of rows of the matrix: "))
          cols = int(input("Enter the number of columns of the matrix: "))
          matrix = input_matrix(rows, cols)
          determinant_matrix(matrix)

      elif choice == '4':
          rows = int(input("Enter the number of rows of the matrix: "))
          cols = int(input("Enter the number of columns of the matrix: "))
          matrix = input_matrix(rows, cols)
          inverse_matrix(matrix)

      else:
          print("\nInvalid choice.")

      repeat = input("\nDo you want to perform another matrix operation? (yes/no): ")
      if repeat.lower() != 'yes':
          break

  print("Thank you! Good luck.")

if __name__ == "__main__":
  main()
