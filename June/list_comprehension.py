def vector_combinations(x, y, z, n):
    vector_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(vector_list)

vector_combinations(2, 2, 2, 2)

