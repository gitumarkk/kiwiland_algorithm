# Python
import unittest

# App
from app import Graph


class TestGraph(unittest.TestCase):
	def setUp(self):
		self.graph_obj = Graph()


	def test_get_input_file_should_success(self):
		self.assertEqual(
			self.graph_obj.get_input_data(),
			"AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
		)

	def test_process_node_string_with_invalid_towns_should_fail(self):
		node_string = "ABB5"
		with self.assertRaises(Exception) as context:
			self.graph_obj.process_node_string(node_string)
		self.assertEqual(
			context.exception.message,
			'The %s entry is in the wrong format, should be <start><stop><distance>' % node_string
		)

	def test_process_node_string_with_invalid_distance_should_fail(self):
		node_string = "ABB"
		with self.assertRaises(Exception) as context:
			self.graph_obj.process_node_string(node_string)
		self.assertEqual(
			context.exception.message,
			"invalid literal for int() with base 10: 'B'"
		)

	def test_process_node_string_with_valid_strin_succes(self):
		node_string = "AB1"
		self.assertEqual(
			self.graph_obj.process_node_string(node_string),
			("A", "B", 1)
		)

	def test_graph_generated_on_initialization_success(self):
		self.assertEqual(
			self.graph_obj.graph,
			{
				'A': {'B': {'distance': 5}, 'E': {'distance': 7}, 'D': {'distance': 5}},
				'C': {'E': {'distance': 2}, 'D': {'distance': 8}},
				'B': {'C': {'distance': 4}},
				'E': {'B': {'distance': 3}},
				'D': {'C': {'distance': 8}, 'E': {'distance': 6}}
			}
		)

	def test_distance_success(self):
		input_list = [
			{ "input": "ABC", "expected": 9 },
			{ "input": "AD", "expected": 5 },
			{ "input": "ADC", "expected": 13 },
			{ "input": "AEBCD", "expected": 22 },
			{ "input": "AED", "expected": 'NO SUCH ROUTE' }
		]

		for item in input_list:
			self.assertEqual(
				self.graph_obj.get_route_distance(item['input']),
				item['expected']
			)


if __name__ == '__main__':
	unittest.main()