from day1input import today

calories = 0
max_calories = 0
elf = 0
all_calories = []

for line in today.splitlines():
  if line == "":
    all_calories.append(calories)
    elf = elf+1
    calories = 0
  else:
    calories += int(line)
    if calories > max_calories:
      max_calories = calories

all_calories.sort(reverse=True)

print(max_calories)
print(all_calories[0] + all_calories[1] + all_calories[2])