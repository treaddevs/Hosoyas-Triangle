# Template by Lindsay Jamieson
# Project 6: Hosoya's Triangle TESTING
# Sam Treadwell
# CS 5001
# 11/09/2022    

# Computes first three levels (aka rows) of triangle
def computeTriangle(levels):
    if levels == 1:
        return [[1]]
    elif levels == 2:
        result = computeTriangle(levels - 1)
        current = [1, 1]
        result.append(current)
        return result
    elif levels == 3:
        result = computeTriangle(levels - 1)
        current = [2, 1, 2]
        result.append(current)
        return result
    else:
        # Calculate the total/net result of accumulated levels
        # For example: [[1], [1, 1], [2, 1 ,2], [3, 2, 2, 3]]
        result = computeTriangle(levels - 1) 

        # Calculate the previous levels result:
        previous_row = result[-1] # [3, 2, 2, 3] level = 3
        prev_prev = result[-2] # [2 , 1, 2] level = 2

        # Empty list = current = []
        current = []

        # Separates triangle in two halves, uses different formulas for each half:
        for i in range(levels):
            if i < levels//2:  # For indices = 0, 1, 2 (left half)
                current_num = previous_row[i] + prev_prev[i]
                current.append(current_num)
            else: # For indices = 3, 4 (right half)
                current_num = previous_row[i - levels] + prev_prev[i - levels]
                current.append(current_num)
        # Append the result to update list
        result.append(current)
        return result
#computeTriangle()

# This is a test for positive 4 levels:
levels = 4
actual_values = computeTriangle(levels)
expected_values = [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3]]
print("Test computeTriangle")
print("Levels: ", levels)
print("Expected values: ", expected_values)
print("Actual values: ", actual_values)

# This is a test for negative 1 levels:
levels = -1
actual_values = computeTriangle(levels)
expected_values = ("Must enter a positive integer")
print("Test computeTriangle")
print("Levels: ", levels)
print("Expected values: ", expected_values)
print("Actual values: ", actual_values)

''' This function is recursive.  It will compute the levels of Hosoya's 
    triangle.
    It does NOT print Hosoya's triangle.  Remember that each location in the
    triangle is the sum of the two diagonally above it with the top two rows being:
    1
    1 1
    Input: The number of rows to generate
    Output: The triangle as a list of lists.'''

# Prints the indicies for the triangle in "list of lists" format
def printTriangle(triangle, levels):
    triangle = computeTriangle(levels)
    for i in range(levels):
        print(triangle[i])
#printTriangle()

# This is a test for positive 4 levels:
levels = 4
actual_values = printTriangle(levels)
expected_values = [1]
''                [1, 1]  
''                [2, 1, 2]
''                [3, 2, 2, 3]
print("Test computeTriangle")
print("Levels: ", levels)
print("Expected values: ", expected_values)
print("Actual values: ", actual_values)

# This is a test for negative 1 levels:
levels = -1
actual_values = computeTriangle(levels)
expected_values = ("Must enter a positive integer")
print("Test computeTriangle")
print("Levels: ", levels)
print("Expected values: ", expected_values)
print("Actual values: ", actual_values)