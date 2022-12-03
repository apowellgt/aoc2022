# Open the input file
with open('day3input.txt') as f:
  # Read the lines from the file
  lines = f.readlines()

  # Initialize a variable to store the sum of the priorities of the badge item types
  badge_priorities_sum = 0

  # Go through each group of three lines in the input
  for i in range(0, len(lines), 3):
    # Get the current group of lines
    group = lines[i:i + 3]

    group[0] = group[0].replace('\n', '')
    group[1] = group[1].replace('\n', '')
    group[2] = group[2].replace('\n', '')

    # Use the set intersection operator to find the letters that appear in all three lines
    common_item_type = set(group[0]) & set(group[1]) & set(group[2])

    # Get the first item type that is common to all three lines (there should only be one)
    badge_item_type = list(common_item_type)[0]

    # Calculate the priority of the badge item type
    if badge_item_type.islower():
      badge_priority = ord(badge_item_type) - 96
    else:
      badge_priority = ord(badge_item_type) - 38

    # Add the priority to the sum of the priorities of the badge item types
    badge_priorities_sum += badge_priority

  # Print the sum of the priorities of the badge item types
  print(badge_priorities_sum)
