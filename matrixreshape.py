import random
def matrixReshape(matrix, r, c):
    all_elements = []
    for i in range(0, len(matrix)):
        all_elements = all_elements+matrix[i]

    new_matrix = []
    print(all_elements)
    for i in range(0, c):
        new_matrix.append(all_elements[0:r])
        all_elements = all_elements[r:]
        print(all_elements)
    print("Reshaped matrix")
    print(*new_matrix, sep="\n")
    print("New r ", r)
    print("New c ", c)
        
        

matrix = []
r = random.randint(1, 10)
c = random.randint(1, 10)
for i in range(0, r):
    matrix.append(random.sample(range(1,100), c))
print("Original matrix")
print(*matrix, sep="\n")
print("Initial r ", r)
print("Initial c ", c)

#Get factors
number_of_elements = r*c
factors = []
for i in range(2, number_of_elements+1):
    if number_of_elements%i == 0:
        factors.append(i)

print("Length of factors", len(factors))
new_r = factors[random.randint(0, len(factors)-1)]
new_c = number_of_elements//new_r

matrixReshape(matrix, new_r, new_c)
