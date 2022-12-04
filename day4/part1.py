# Define a function that takes two range pairs (e.g. "2-4" and "3-5")
# and returns True if the first range fully contains the second, and
# False otherwise.
def range_contains(range1, range2):
  # Convert the range strings to tuples of integers.
  range1 = tuple(map(int, range1.split("-")))
  range2 = tuple(map(int, range2.split("-")))

  # Check if the start and end of the second range are both within
  # the first range.
  return range1[0] <= range2[0] and range1[1] >= range2[1]


# Open the input file and read the lines.
with open("input.txt") as f:
  lines = f.readlines()

# Split each line into range pairs.
pairs = [line.strip().split(",") for line in lines]

# Count the number of pairs where one range fully contains the other.
counter = 0
for pair in pairs:
  if range_contains(pair[0], pair[1]) or range_contains(pair[1], pair[0]):
    counter += 1

# Print the result.
print(counter)
