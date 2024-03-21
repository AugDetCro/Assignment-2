import numpy as num_py

if __name__ == '__main__':
    # A: Use NumPy to create a random vector and apply changes
    print("A: Use NumPy to create a random vector and apply changes")

    # Creating the vector
    vector = num_py.random.random(15)
    vector = (vector * 19) + 1

    # Reshaping the vector
    reshapedVector = vector.reshape(3, 5)

    # Printing shape of vector
    print(reshapedVector.shape, "\n")

    # Replace max of each row with 0
    reshapedVector[num_py.arange(len(reshapedVector)), reshapedVector.argmax(1)] = 0
    print(reshapedVector, "\n")

    # Create a 2-dimensional array
    two_dimensional_array = num_py.zeros((4, 3), dtype = num_py.int32)

    # Print 2-dimensional array shape, type, and datatype
    print("Shape: ", two_dimensional_array.shape)
    print("Type: ", type(two_dimensional_array))
    print("Datatype: ", two_dimensional_array.dtype)

    # B: Compute eigenvalues and right eigenvectors of a given array
    print("===========================\nB: Compute eigenvalues and right eigenvectors of a given array")

    # Initialize the array
    computeArray = num_py.array([[3, -2], [1, 0]])

    # Compute the eigenvalues and right eigenvectors
    eigenValues, eigenVectors = num_py.linalg.eig(computeArray)

    # Print results
    print("Computed eigenvalues:", eigenValues)
    print("Computed eigenvectors:\n", eigenVectors)

    # C: Compute the sum of the diagonal element of an array
    print("===========================\nC: Compute the sum of the diagonal element of an array")

    # Initialize the array
    diagonalArray = num_py.array([[0, 1, 2], [3, 4, 5]])

    # Print array (for visual clarity)
    print("Given array:\n", diagonalArray)

    # Find the sum of the diagonal elements and print the results
    print("Sum of array: ", num_py.trace(diagonalArray))

    # D: Reshape an array without changing data
    print("===========================\nD: Reshape an array without changing data")

    # Initialize the array
    reshapeArray = num_py.array([[1, 2], [3, 4], [5, 6]])

    # Print the array before the reshaping (for visual clarity)
    print("Array before reshape:\n", reshapeArray)

    # Print the array after the reshaping
    print("Array after reshape:\n", reshapeArray.reshape(2, 3))