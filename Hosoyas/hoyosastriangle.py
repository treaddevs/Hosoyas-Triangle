# Template by Lindsay Jamieson
# Project 6: Hosoya's Triangle
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

''' This function will print a left justified copy of Hosoya's triangle.
    Input: triangle - the values to be printed, levels - the height of the triangle
    Output: NONE'''

# Main function starts flow of control, prompting user to enter a desired "n" number of levels (aka rows)
# User must enter a positive integer, otherwise returns False
# Prints triangle on seperate lines to display triangle shape
def main():
    n = int(input("Enter number of levels as integer: "))
    if n <= 0:
        print("Must enter a positive integer")
    triangle = computeTriangle(n)
    printTriangle(triangle, n)
main()

''' This is the main control function for the program.
    You should ask the user how many levels and then compute the triangle
    recursively. Then you should print the triangle.'''

