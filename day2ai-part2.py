# Load the strategy guide from a file.
with open("day2input.txt") as f:
  strategy_guide = f.readlines()

# Initialize the total score to 0.
total_score = 0

# Iterate over each line of the strategy guide.
for line in strategy_guide:
  # Split the line into two columns (opponent's move and the desired outcome).
  opponent_move, desired_outcome = line.strip().split()

  # Choose the shape that will result in the desired outcome.
  our_move = None
  if desired_outcome == "X":
    if opponent_move == "A":
      our_move = "C"
    elif opponent_move == "B":
      our_move = "A"
    elif opponent_move == "C":
      our_move = "B"
  elif desired_outcome == "Y":
    our_move = opponent_move
  elif desired_outcome == "Z":
    if opponent_move == "A":
      our_move = "B"
    elif opponent_move == "B":
      our_move = "C"
    elif opponent_move == "C":
      our_move = "A"

  # Calculate the score for our move (1 for Rock, 2 for Paper, 3 for Scissors).
  our_score = 0
  if our_move == "A":
    our_score = 1
  elif our_move == "B":
    our_score = 2
  elif our_move == "C":
    our_score = 3

  # Calculate the outcome of the round.
  outcome = 0
  if opponent_move == our_move:
    # If both players choose the same shape, the round is a draw.
    outcome = 3
  elif (opponent_move == "A" and our_move == "B") or (opponent_move == "B" and our_move == "C") or (opponent_move == "C" and our_move == "A"):
    # If we win, add 6 to the score.
    outcome = 6

  # Add the score for the round to the total score.
  total_score += our_score + outcome

# Print the total score.
print(total_score)