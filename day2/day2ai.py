# Load the strategy guide from a file.
with open("day2input.txt") as f:
  strategy_guide = f.readlines()

# Initialize the total score to 0.
total_score = 0

# Iterate over each line of the strategy guide.
for line in strategy_guide:
  # Split the line into two columns (opponent's move and our move).
  opponent_move, our_move = line.strip().split()

  # Calculate the score for our move (1 for Rock, 2 for Paper, 3 for Scissors).
  our_score = 0
  if our_move == "X":
    our_score = 1
  elif our_move == "Y":
    our_score = 2
  elif our_move == "Z":
    our_score = 3

  # Calculate the outcome of the round.
  outcome = 0
  if (opponent_move == "A" and our_move == "X") or (opponent_move == "B" and our_move == "Y") or (opponent_move == "C" and our_move == "Z"):
    # If both players choose the same shape, the round is a draw.
    outcome = 3
  elif (opponent_move == "A" and our_move == "Y") or (opponent_move == "B" and our_move == "Z") or (opponent_move == "C" and our_move == "X"):
    # If we win, add 6 to the score.
    outcome = 6

  # Add the score for the round to the total score.
  total_score += our_score + outcome

# Print the total score.
print(total_score)