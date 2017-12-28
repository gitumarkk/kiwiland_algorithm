# KIWILAND TRAIN ALGORITHM
The repository contains the solution to the kiwiland train traversal problem statement. To test the project,
simply run `python tests.py`.

## DEPENDENCIES
There are no hard dependencies other than having a local version of python running. 

### DEV DEPENDENCIES
However, the soft dependencies are defined in `requirements.txt` and include:
* `pycodestyle` which is used for pep8 linting, in order to focus on best conventions.

## IMPLEMENTATION DETAILS
The codebase is made up of 2 main files, the `app.py` file which contains the graph algorithm and the `tests.py` file which contains the unittests to test the funcionality. The implemantion of the graph traversal algorithm has a big emphasis on the *DRY* concept i.e. Don't Repeat Yourself, for both the graph implementation and testing. This means there is significant reuse of functions for the general use case, with slight modifications for specific cases. The functions in `app.py` contains python docstrings that highlights the functions implemantation.

### `app.py`

The codebase implementation is done using python classes, the specific function implemantions have been highlighted using docstrings in the `app.py` file and won't be repeated in this `README.md` section. This section contains reasoning behind the algorithm implementation.

#### `def get_trip_info(self, start, stop, key=None, value=None):`
The function forms the base of the algorithm and provides a general case for the graph traversal. It calls the `get_route_combinations(self, start, stop, route="", current_depth=0, max_depth=None)` function with different defaults, and according to the specified defaults, different algorithm end states are reached. This means that only one function is required for all the cases specified in the problem statement i.e. *DRY*. 

For example, in order to test for `max_stops=3`, the following function call needs to be made `self.get_trip_info(self, 'C', 'C', key='max_stops', value=3)`

#### `get_route_combinations(self, start, stop, route="", current_depth=0, max_depth=None)`
The function is recursive and depends on the initial defaults to arrive at specific end cases. It modifies a global `self.visited` array with the possible route combinations where the recursion is terminated when the a maximum number of recursions have been made as specified in the function run. 


## CUSTOM TESTING
In order to run a simulation of the functions, the `def run_graph_to_check_distance` and the  `def run_graph_for_start_to_stop_path` methods have been provided which take in custom arguments. The arguments can be modified in the `__name__ == "__main__"` section. A sample of the expected input data has been provided for testing.

## PROBLEM STATEMENT - TRAINS:

Problem:  The local commuter railroad services a number of towns in Kiwiland.  Because of monetary concerns, all of the tracks are 'one-way.' That is, a route from Kaitaia to Invercargill does not imply the existence of a route from Invercargill to Kaitaia.  In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance!

The purpose of this problem is to help the railroad provide its customers with information about the routes.  In particular, you will compute the distance along a certain route, the number of different routes between two
towns, and the shortest route between two towns.

Input:  A directed graph where a node represents a town and an edge represents a route between two towns.  The weighting of the edge represents the distance between the two towns.  A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

Output: For test input 1 through 5, if no such route exists, output 'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra stops!  For example, the first problem means to start at city A, then 
travel directly to city B (a distance of 5), then directly to city C (a distance of 4).

1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3
stops.  In the sample data below, there are two such trips: C-D-C (2
stops). and C-E-B-C (3 stops).
7. The number of trips starting at A and ending at C with exactly 4 stops.
In the sample data below, there are three such trips: A to C (via B,C,D); A
to C (via D,C,D); and A to C (via D,E,B).
8. The length of the shortest route (in terms of distance to travel) from A
to C.
9. The length of the shortest route (in terms of distance to travel) from B
to B.
10. The number of different routes from C to C with a distance of less than 30.
In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC,
CEBCEBC, CEBCEBCEBC.