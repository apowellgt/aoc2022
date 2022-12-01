# Import the numbers from day1input.txt, and then sum up each group of numbers.
# Tell me the sum of the largest group and the sum of the three largest groups.
# The file is like this:
# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# Open the file in read-only mode
with open("day1input.txt", "r") as file:
  # Read the lines of the file into a list
  lines = file.readlines()

# Close the file
file.close()

# Initialize a list to store the sums
sums = []

# Initialize a variable to track the current sum
current_sum = 0

# Loop over the lines in the list
for line in lines:
  # Check if the line is empty
  if line.strip() == "":
    # If the line is empty, append the current sum to the list of sums
    sums.append(current_sum)
    # Reset the current sum to 0
    current_sum = 0
  else:
    # If the line is not empty, add the number on the line to the current sum
    current_sum += int(line)

# After looping through all the lines, append the final sum to the list of sums
sums.append(current_sum)

# Sort the list of sums in descending order
sums.sort(reverse=True)

# Print the sum of the largest group
print("Sum of largest group:", sums[0])

# Print the sum of the three largest groups
print("Sum of three largest groups:", sums[0] + sums[1] + sums[2])
