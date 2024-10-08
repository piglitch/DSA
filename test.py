def typing_distance(word):
  """Calculates the total distance traveled by a robot typing a given word on a keyboard.

  Args:
    word: A string containing only uppercase letters.

  Returns:
    The total distance traveled by the robot.
  """

  keyboard = {
      'Q': (0, 0), 'W': (1, 0), 'E': (2, 0), 'R': (3, 0), 'T': (4, 0), 'Y': (5, 0), 'U': (6, 0), 'I': (7, 0), 'O': (8, 0), 'P': (9, 0),
      'A': (0, 1), 'S': (1, 1), 'D': (2, 1), 'F': (3, 1), 'G': (4, 1), 'H': (5, 1), 'J': (6, 1), 'K': (7, 1), 'L': (8, 1),
      'Z': (0, 2), 'X': (1, 2), 'C': (2, 2), 'V': (3, 2), 'B': (4, 2), 'N': (5, 2), 'M': (6, 2)
  }

  current_pos = keyboard['Q']
  total_distance = 0

  for letter in word:
    new_pos = keyboard[letter]
    total_distance += abs(new_pos[0] - current_pos[0]) + abs(new_pos[1] - current_pos[1])
    current_pos = new_pos

  return total_distance

# Example usage
word = "QA"
distance = typing_distance(word)
  # Output: 3

graph = {}

graph["start"] = {}

graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['b'] = {}

graph['a']['fin'] = 1
graph['b']['fin'] = 5
graph['b']['a'] = 3

graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = ['start']
parents['b'] = ['start'] 
parents['fin'] = None

processed = []

x = graph['b']
parents['a'] = 'l'
print(parents)