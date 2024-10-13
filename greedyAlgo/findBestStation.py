states_needed = set(["mt", "wa", "or", "id", "nv", "ut",
"ca", "az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()
while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states & states_needed
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered
      # print(states_covered)
  print('before: ',states_needed)    
  states_needed -= states_covered
  print('after: ', states_needed)
  final_stations.add(best_station)
print(final_stations)
# for i, j in stations.items(): print('i: ', i,'\n', 'j: ', j)
