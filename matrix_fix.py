def input_matrix(rows, cols):
  matrix = []
  print("Masukkan elemen-elemen matriks:")
  for i in range(rows):
      row = []
      for j in range(cols):
          element = float(input(f"Masukkan elemen baris {i+1} kolom {j+1}: "))
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
      print("\nOperasi penjumlahan tidak dapat dilakukan karena ukuran matriks tidak sama.")
      return None

  result = []
  for i in range(len(matrix1)):
      row = []
      for j in range(len(matrix1[0])):
          row.append(matrix1[i][j] + matrix2[i][j])
      result.append(row)

  print("\nHasil penjumlahan matriks:")
  print_matrix(result)
  return result

def subtract_matrices(matrix1, matrix2):
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
      print("\nOperasi pengurangan tidak dapat dilakukan karena ukuran matriks tidak sama.")
      return None

  result = []
  for i in range(len(matrix1)):
      row = []
      for j in range(len(matrix1[0])):
          row.append(matrix1[i][j] - matrix2[i][j])
      result.append(row)

  print("\nHasil pengurangan matriks:")
  print_matrix(result)
  return result

def multiply_matrices(matrix1, matrix2):
  if len(matrix1[0]) != len(matrix2):
      print("\nOperasi perkalian tidak dapat dilakukan karena jumlah kolom matriks pertama tidak sama dengan jumlah baris matriks kedua.")
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

  print("\nHasil perkalian matriks:")
  print_matrix(result)
  return result

def transpose_matrix(matrix):
  result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
  print("\nHasil transpose matriks:")
  print_matrix(result)
  return result

def determinant_matrix(matrix):
  if len(matrix) != len(matrix[0]):
      print("\nDeterminan hanya dapat dihitung untuk matriks persegi.")
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
  print(f"\nDeterminan matriks: {det}")
  return det

def inverse_matrix(matrix):
  if len(matrix) != len(matrix[0]):
      print("\nMatriks invers hanya dapat dihitung untuk matriks persegi.")
      return None

  det = determinant_matrix(matrix)
  if det == 0:
      print("\nMatriks tidak memiliki invers.")
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

  print("\nMatriks invers:")
  print_matrix(inv)
  return inv

def main():
  while True:
      print("\nPilih operasi matriks:")
      print("1. Penjumlahan, pengurangan, perkalian matriks")
      print("2. Transpose matriks")
      print("3. Mencari Determinan matriks")
      print("4. Mencari Invers matriks")
      choice = input("Masukkan pilihan (1/2/3/4): ")

      if choice == '1':
          rows1 = int(input("Masukkan jumlah baris matriks pertama: "))
          cols1 = int(input("Masukkan jumlah kolom matriks pertama: "))
          matrix1 = input_matrix(rows1, cols1)

          rows2 = int(input("Masukkan jumlah baris matriks kedua: "))
          cols2 = int(input("Masukkan jumlah kolom matriks kedua: "))
          matrix2 = input_matrix(rows2, cols2)

          add_matrices(matrix1, matrix2)
          subtract_matrices(matrix1, matrix2)
          multiply_matrices(matrix1, matrix2)

      elif choice == '2':
          rows = int(input("Masukkan jumlah baris matriks: "))
          cols = int(input("Masukkan jumlah kolom matriks: "))
          matrix = input_matrix(rows, cols)
          transpose_matrix(matrix)

      elif choice == '3':
          rows = int(input("Masukkan jumlah baris matriks: "))
          cols = int(input("Masukkan jumlah kolom matriks: "))
          matrix = input_matrix(rows, cols)
          determinant_matrix(matrix)

      elif choice == '4':
          rows = int(input("Masukkan jumlah baris matriks: "))
          cols = int(input("Masukkan jumlah kolom matriks: "))
          matrix = input_matrix(rows, cols)
          inverse_matrix(matrix)

      else:
          print("\nPilihan tidak valid.")

      repeat = input("\nApakah Anda ingin melakukan operasi matriks lainnya? (ya/tidak): ")
      if repeat.lower() != 'ya':
          break

  print("Terimakasih! Good luck.")

if __name__ == "__main__":
  main()