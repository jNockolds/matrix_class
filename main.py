import math


class Matrix:

  def __init__(self, matrix: list[list]) -> None:
    self.matrix = matrix
    self.rows = len(matrix)
    self.columns = len(matrix[0])

  def get_highest_valued_cell(self):
    highest = -math.inf
    for i in range(self.rows):
      for j in range(self.columns):
        if highest < self.matrix[i][j]:
          highest = self.matrix[i][j]
    return highest

  def __str__(self):
    cell_width = len(str(self.get_highest_valued_cell()))

    output = ""
    for i in range(self.rows):
      for j in range(self.columns):
        if j == 0:
          output += '[ '

        output += str(self.matrix[i][j])  # cell value

        output += ' ' * (cell_width - len(str(self.matrix[i][j])) + 1
                         )  # spacing

        if j >= self.columns - 1:
          output += ']'

      if i < self.rows - 1:
        output += '\n'

    return output

  def get_determinant(self):
    if self.columns != self.rows:
      raise ValueError("Determinant can only be computed for square matrices")

    if self.columns == 1:
      return self.matrix[0][0]
    if self.columns == 2:
      return (self.matrix[0][0] * self.matrix[1][1]) - (self.matrix[0][1] *
                                                        self.matrix[1][0])

    cofactors = []
    for column in range(self.columns):
      matrix = []
      for row in range(1, self.rows):
        local_row = []
        for i in range(self.columns):
          if i != column:
            local_row.append(self.matrix[row][i])
        matrix.append(local_row)
      matrix = Matrix(matrix)
      cofactors.append(matrix)

    determinant = 0
    for column in range(self.columns):
      if column % 2 == 0:  # if even
        determinant += self.matrix[0][column] * cofactors[
            column].get_determinant()
      else:  # if odd
        determinant -= self.matrix[0][column] * cofactors[
            column].get_determinant()

    return determinant


test_matrix = Matrix([[1, 6, 7], [2, 5, 8], [3, 4, 5]])

print(test_matrix)

print(test_matrix.get_determinant())
