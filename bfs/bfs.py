from collections import deque

def bfs():
  graph = {}
  graph["me"] = ["alice", "bob", "claire"]
  
  graph[graph["me"][0]] = ["a", "b", "c"] 
  graph[graph["me"][1]] = ["d", "e", "f"] 
  graph[graph["me"][2]] = ["g", "h", "i"] 
  print(graph)
  search_queue = deque()
  searched = []
  search_queue += graph["me"]

  def is_target(person):
    if person == "claire": 
      return True
    return False

  while search_queue:
    person = search_queue.popleft()
    if not person in searched: 
      if is_target(person):
        print(search_queue)
        return person, searched
      else:
        search_queue += graph[person]
        searched.append(person)

  return "Target is not here", searched

print(bfs())

# graph = {}
# graph["me"] = ["alice", "bob", "claire"]

# def is_target(person):
#   if person == "claire": 
#     return True
#   return False

# def search(name):
#   search_queue = deque()
#   search_queue += graph[name]
#   searched = []
#   while search_queue:
#     person = search_queue.popleft()
#     if not person in searched:
#       if is_target(person):
#         print(person + ' is a mango seller!')
#         return True
#       else:
#         search_queue += graph[person]
#         searched.append(person)
#   return False

# search("me")