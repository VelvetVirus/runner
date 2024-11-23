"""
Created on Tue Nov 12 16:20:23 2024
"""

__author__ = "Son Hoang"
__copyright__ = "Copyright (c) 2024, University of Southampton"
__credits__ = ["Son Hoang"]
__licence__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Son Hoang"
__email__ = "T.S.Hoang@soton.ac.uk"
__status__ = "Prototype"

# from maze import Maze


def test_constructor_get_dimensions() -> None:
    """A Unit test for :py:func:`~maze.__init__` and
    accessing the width and height properties.

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Assert the width (11) and height (5) of the newly created maze.
    created runner.
    """
    maze = Maze(11, 5)
    assert maze.width == 11
    assert maze.height == 5


def test_constructor_get_walls() -> None:
    """A Unit test for :py:func:`~Maze.__init__` and
    :py:func:`~Maze.get_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Assert that there are no walls at the (4, 2)-coordinate.
    """
    maze = Maze(11, 5)
    assert maze.get_walls(4, 2) == (False, False, False, False)


def test_add_horizontal_wall() -> None:
    """A Unit test for :py:func:`~Maze.add_horizontal_wall` and
    :py:func:`~Maze.get_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a horizontal wall at (5, 2).

    4. Assert that there are no walls at the (5, 2)-coordinate, except the South.
    """
    maze = Maze(11, 5)
    maze.add_horizontal_wall(5, 2)

    assert maze.get_walls(5, 2) == (False, False, True, False)


def test_add_vertical_wall() -> None:
    """A Unit test for :py:func:`~Maze.add_vertical_wall` and
    :py:func:`~Maze.get_walls`

    Below is the test sequence:

    1. Create a maze of size (11, 5).

    2. Add a vertical wall at (2, 4).

    3. Assert that there are no walls at the (4, 2)-coordinate, except the West.
    """
    maze = Maze(11, 5)
    maze.add_vertical_wall(2, 4)
    assert maze.get_walls(4, 2) == (False, False, False, True)
