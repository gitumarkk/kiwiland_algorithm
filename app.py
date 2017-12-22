import os


class Graph(object):
	def __init__(self):
		"""

		"""
		processed_data = self.get_input_data()
		self.graph = self.generate_graph(processed_data)


	def get_input_data(self, data_file='data/train_route.txt'):
		"""

		"""
		with open(data_file) as input_file:
			content = input_file.read()
		return content.split(":")[-1].strip()

	def validate_data(self, data):
		pass

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


