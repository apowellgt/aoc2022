# Read the input from day3input.txt and store it in a list of strings
with open("day3input.txt") as f:
  rucksacks = f.read().splitlines()

# Split each rucksack string in half to obtain the items in the first and second compartment
first_compartment = [s[:len(s) // 2] for s in rucksacks]
second_compartment = [s[len(s) // 2:] for s in rucksacks]

# Loop through each rucksack and store the count of each item type in a dictionary
common_item_types = []
for i in range(len(rucksacks)):
  count = {}
  for item in first_compartment[i]:
    if count.get(item, 0) == 0:
      count[item] = count.get(item, 0) + 1

  for item in second_compartment[i]:
    if count.get(item, 0) == 1:
      count[item] = count.get(item, 0) + 1

  # Find the item type that appears in both compartments of the rucksack by checking
  # which item type has a count equal to 2
  common_item_type = None
  for item, item_count in count.items():
    if item_count == 2:
      common_item_type = item
      break

  # Calculate the priority of the common item type by converting it to its ASCII code
  # and subtracting 96 if it is lowercase or 64 if it is uppercase
  priority = ord(common_item_type) - (96 if common_item_type.islower() else 38)
  common_item_types.append(priority)

# Print the sum of the priorities of the common item types
print(sum(common_item_types))
