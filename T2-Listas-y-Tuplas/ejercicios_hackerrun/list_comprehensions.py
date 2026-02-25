"""
List Comprehensions
-------------------
You are given three integers x, y, z representing the dimensions of a cuboid
along with an integer n. Print a list of all possible coordinates [i, j, k]
on a 3D grid where:
    - 0 <= i <= x
    - 0 <= j <= y
    - 0 <= k <= z
    - i + j + k != n

Print the list in lexicographic increasing order using list comprehensions.

Input Format:
    Four integers x, y, z and n, each on a separate line.

Sample Input 0:        Sample Output 0:
    1                      [[0, 0, 0], [0, 0, 1], [0, 1, 0],
    1                       [1, 0, 0], [1, 1, 1]]
    1
    2

Sample Input 1:        Sample Output 1:
    2                      [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2],
    2                       [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2],
    2                       [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1],
    2                       [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0],
                            [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1],
                            [2, 2, 2]]
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]

    print(result)
