graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

graph = {'A': ['B', 'E', 'D'], 'C': ['E', 'D'], 'B': ['C'], 'E': ['B'], 'D': ['C', 'E']}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


print find_all_paths(graph, 'A', 'D')



def find_paths_recursion(graph, current, goal, current_depth, max_depth, num_paths, current_path, paths_found)
  current_path.append(current)

  if current_depth > max_depth:
    return

  if current == goal:
    if len(paths_found) <= number_of_paths_to_find:
      paths_found.append(copy(current_path))

    current_path.pop()
    return

  else:
    for successor in graph[current]:
    self.find_paths_recursion(graph, successor, goal, current_depth + 1, max_depth, num_paths, current_path, paths_found)

  current_path.pop()


  def find_paths[s, t, d, k]:
  paths_found = [] # PASSING THIS BY REFERENCE
  find_paths_recursion(s, t, 0, d, k, [], paths_found)
