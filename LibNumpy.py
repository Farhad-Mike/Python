import numpy

# Может делать арифметические вычисления последовательно с каждым элементов списка
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_height = numpy.array(height)
np_weight = numpy.array(weight)
bmi = np_weight / np_height ** 2

# Compare and convert to boolean every element
bmi > 23

# Print only those observations above 23
bmi[bmi > 23]