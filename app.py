import os
from copy import copy

class Graph(object):
	def __init__(self):
		"""

		# """
		processed_data = self.get_input_data()
		self.graph = self.generate_graph(processed_data)
		self.graph_slim = self.generate_graph_slim()

	def generate_graph_slim(self):
		return { k: v.keys() for k,v in self.graph.items() }

	def get_input_data(self, data_file='data/train_route.txt'):
		"""

		"""
		with open(data_file) as input_file:
			content = input_file.read()
		return content.split(":")[-1].strip()

	def process_node_string(self, data_string):
		"""

		"""
		if len(data_string) != 3:
			raise Exception("The %s entry is in the wrong format, should be <start><stop><distance>" % data_string)

		start = data_string[0]
		stop = data_string[1]
		distance = int(data_string[2])
		return start, stop, distance

	def generate_graph(self, data):
		"""

		"""
		graph = {}
		for item in data.split(","):
			start, stop, distance = self.process_node_string(item.strip())
			if not graph.get(start):
				graph[start] = {}
			graph[start][stop] = {
				'distance': distance
			}
		return graph


	def get_route_distance(self, route, total_distance=0):
		"""

		"""
		start = route[0]
		stop = route[1]

		if not self.graph.get(start) or not self.graph[start].get(stop):
			return 'NO SUCH ROUTE'

		total_distance += self.graph[start][stop]['distance']


		if len(route) == 2:
			return total_distance
		return self.get_route_distance(route[1:], total_distance)


   # def find_all_paths(graph, start, end, path=[]):
   #      path = path + [start]
   #      if start == end:
   #          return [path]
   #      if not graph.has_key(start):
   #          return []
   #      paths = []
   #      for node in graph[start]:
   #          if node not in path:
   #              newpaths = find_all_paths(graph, node, end, path)
   #              for newpath in newpaths:
   #                  paths.append(newpath)
   #      return paths

	# def get_route_combinations(self, start, stop, path=[], visited=[]):
	# 	path = path + [start]
	# 	graph = self.graph_slim
	# 	print "start: %s\nstop: %s\ngraph: %s\npath: %s\n" % (start, stop, graph[start], path)

	# 	print len(path)
	# 	if start == stop:
	# 		return [path]

	# 	if not graph.has_key(start):
	# 		return []

	# 	paths = []
	# 	visited.append(start)
	# 	for route_next in graph[start]:
	# 		if route_next not in path:
	# 			new_paths = self.get_route_combinations(route_next, stop, path, visited)
	# 			for new_path in new_paths:
	# 				paths.append(new_path)
	# 	return paths


	def get_route_combinations(self, start, stop, route="", current_depth=0, max_depth=None):
		# route.append(start)
		route += start
		graph = self.graph
		if max_depth == None:
			max_depth = 5 # Prevent infinite recursion, otherwise keep going
		# print "start: %s\nstop: %s\ngraph: %s\nroute: %s\n" % (start, stop, graph[start], route)
		print route, self.visited, max_depth, current_depth
		if current_depth > max_depth:
			return

		if start == stop and (len(route) > 1):
			self.visited.append(route)
			# route = route[0:len(route)-1]
			return
		else:
			for new_start in graph[start].keys():
				self.get_route_combinations(new_start, stop, route=route, current_depth=current_depth + 1, max_depth=max_depth)

	def get_trip_info(self, start, stop, key=None, value=None):
		self.visited = []

		if key == 'max_stops':
			self.get_route_combinations(start, stop)
			return len([route for route in self.visited if (len(route) - 1) <= value])

		elif key == 'exact_stops':
			self.get_route_combinations(start, stop)
			return self.visited

		elif key == 'shortest_route':
			self.get_route_combinations(start, stop)
			print self.visited
			return min([self.get_route_distance(route) for route in self.visited])




