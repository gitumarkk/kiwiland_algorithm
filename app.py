import os
from copy import copy


class Graph(object):
    def __init__(self, data_file='data/train_route.txt', data_string=None):
        """Initializes the object by getting the input data and
            generating the graph

        Args:
            data_file (str): The file path to be opened.
                Assumes the content of the file is in the format;
                Graph: AB5, BC4, CD8, DC8
            data_string

        """
        if data_string:
            processed_data = self.parse_input_data(data_string)
        else:
            processed_data = self.get_input_data(data_file)

        self.graph = self.generate_graph(processed_data)

    def parse_input_data(self, content):
        """Get's an input string of the graph and produces a string for further formatting

        Args:
            content (str): The content to read in the format 'Graph: AB5, BC4, CD8, DC8'

        Returns:
            str: Of the preprocessed input data in the form of 'B5, BC4, CD8, DC8'

        """
        return content.split(":")[-1].strip()

    def get_input_data(self, data_file):
        """Open's a file provided in the key word and reads the data from it

        Args:
            data_file (str): The file path to be opened.
                Assumes the content of the file is in the format;
                Graph: AB5, BC4, CD8, DC8

        Returns:
            str: The processed string from the file

        """
        with open(data_file) as input_file:
            content = input_file.read()
        return self.parse_input_data(content)

    def process_node_string(self, data_string):
        """Recieves a string and returns the individual characters in the string after validation

        Args:
            data_string (char): The data string to be taken e.g. AB1,
                should be <char><char><int>

        Returns:
            tuple: A tuple in the format (str, str, int)

        Raises:
            Exception: If the lenght of the data_string != 3
            ValueError: If last string cannot be cast into an integer.

        Example:
            >> self.process_node_string('AB1')
            ('A', 'B', 1)

        """
        if len(data_string) != 3:
            raise Exception(
                "The %s entry is in the wrong format, should be <start><stop><distance>" %
                data_string
            )

        start = data_string[0]
        stop = data_string[1]
        distance = int(data_string[2])
        return start, stop, distance

    def generate_graph(self, data_string):
        """Recieves a string and generates a dict representing an adjancency list between the keys and
            nodes the key has a route and the distance between them

        Args:
            data_string (str): A string containing all possible routes.

        Returns:
            dict: A graph representation as a dict of all the possible routes

        Example:
            >> self.generate_graph('AB5, BC4, AD8')
            {'A': {'B': {'distance': 5}, 'D': {'distance': 8}}, 'B': {'C': {'distance': 4}}

        """
        graph = {}
        for item in data_string.split(","):
            start, stop, distance = self.process_node_string(item.strip())
            if not graph.get(start):
                graph[start] = {}
            graph[start][stop] = {
                'distance': distance
            }
        return graph

    def get_route_distance(self, route, total_distance=0):
        """Is a recursive function that recieves a route and get's the distance
            between the routes by traversing the graph

        Args:
            route (str): A route to traverse
            total_distance (int): The total distance already traversed

        Returns;
            int: If a path from the start to the end node has been found.
            str: If a path from the start to the end node has not been found.
            func: If a the start path leads to another node with routes still in it.

        Example:
            >> self.get_route_distance('ABC', total_distance=0)
            8
        """
        start = route[0]
        stop = route[1]

        if not self.graph.get(start) or not self.graph[start].get(stop):
            return 'NO SUCH ROUTE'

        total_distance += self.graph[start][stop]['distance']

        if len(route) == 2:
            return total_distance
        return self.get_route_distance(route[1:], total_distance)

    def get_route_combinations(self, start, stop, route="", current_depth=0, max_depth=None):
        """A recursive function that returns all possible route combinations leading
            to a destination. Modifies the global self.visited paths array populating it
            with all possible routes

        Args:
            start (str): A single character string representing the starting node
            stop (str): A single character string representing the ending node
            route (str): A string that's built up recursively and represents the route traversed.
            current_depth (int): An int that is recursively accumulated and represents the number of
                recursions in the current iteration
            max_depth (int): The maximum number of recursions the function should perform in order
                to prevent an infinite loop if path doesn't exist

        Returns:
            None: If current_depth exceeds max depth due to no route existing or max_depth
                value passed in by user

        Example:
            >> self.get_route_combination('A', 'B', route='', current_depth=0, max_depth=4)
        """
        route += start
        graph = self.graph

        if current_depth > max_depth:
            return

        elif start == stop and (len(route) > 1):
            self.visited.append(route)

            if len(route) >= max_depth:
                return

        for new_start in graph[start].keys():
            self.get_route_combinations(
                new_start,
                stop,
                route=route,
                current_depth=current_depth + 1,
                max_depth=max_depth
            )

    def get_trip_info(self, start, stop, key=None, value=None):
        """Attempts to get the route between a starting and ending node that fulfills
            the conditions specified by the `key` and `value` parameters

        Args:
            start (str): A single character string representing the starting node
            stop (str): A single character string representing the ending node
            key (str): Represents what conditions the route should fulfill and is used
                in a conditional statement where transformations is applied ot the data
            value (int): Represents the value of the condition each data transformation
                should fulfill

        Returns:
            int: The outcome of traversing the path as defined by the data transformation

        Example:
        >> self.get_trip_info('A', 'B', key='max_stops', value=3)
        5

        """
        self.visited = []

        if key == 'max_stops':
            self.get_route_combinations(start, stop, max_depth=value)
            return len(set(self.visited))

        elif key == 'exact_stops':
            self.get_route_combinations(start, stop, max_depth=value + 1)
            return len(filter(lambda route: len(route) == value + 1, set(self.visited)))

        elif key == 'shortest_route':
            self.get_route_combinations(start, stop, max_depth=len(self.graph.keys()))
            return min([self.get_route_distance(route) for route in set(self.visited)])

        elif key == 'max_distance':
            self.get_route_combinations(start, stop, max_depth=len(self.graph.keys()) + 4)
            return len([route for route in set(self.visited) if self.get_route_distance(route) < 30])


def run_graph_to_check_distance(data_string=None, item={}):
    """This is a helper function to provide the distance for traversing a route

        Args:
            data_string (str?): If provided builds the graph based on the initial data_string
            item (dict): Should contain the input item to test in the format
                {"route": ""}

        Return:
            int: Returns the result for the given input item
    """

    graph_obj = Graph(data_string=data_string)

    result = graph_obj.get_route_distance(item['route'])
    print("For the route {route}, the distance is: {result} ".format(route=item['route'], result=result))
    return result


def run_graph_for_start_to_stop_path(data_string=None, item={}):
    """This is a helper function to provide the result between the start and stop
        routes based on the specified key and value.

        Args:
            data_string (str?): If provided builds the graph based on the initial data_string
            item (dict): Should contain the input item to test in the format
                {"start": "", "stop": "", "key": "", "value": ""}

        Return:
            int: Returns the result for the given input item
    """
    graph_obj = Graph(data_string=data_string)

    result = graph_obj.get_trip_info(item['start'], item['stop'], key=item['key'], value=item['value'])
    print("For the path {start} to {stop}, with {key}={value}, the result is: {result}".
        format(start=item['start'], stop=item['stop'], key=item['key'],  value=item['value'], result=result))
    return result

if __name__ == "__main__":
    graph_input_string = "Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

    print('Calculating the distance along a path: ')
    distance_list_to_test = [
        {"route": "ABC"},
        {"route": "AD"},
        {"route": "ADC"},
        {"route": "AEBCD"},
        {"route": "AED"}
    ]

    for item in distance_list_to_test:
        run_graph_to_check_distance(data_string=graph_input_string, item=item)

    print('\nChecking the result between a start and stop node based on a key criteria:')
    path_list_to_test = [
        {"start": "C", "stop": "C", "key": "max_stops", "value": 3},
        {"start": "A", "stop": "C", "key": "exact_stops", "value": 4},
        {"start": "A", "stop": "C", "key": "shortest_route", "value": None},
        {"start": "B", "stop": "B", "key": "shortest_route", "value": None,},
        {"start": "C", "stop": "C", "key": "max_distance", "value": 30},
    ]
    for item in path_list_to_test:
        run_graph_for_start_to_stop_path(data_string=graph_input_string, item=item)

