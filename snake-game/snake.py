from turtle import Turtle

MOVE_DISTANCE = 20
START_X = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Class to represent the snake"""

    def __init__(self):
        """Initialize snake object"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates 3 segment snake at starting position"""
        for num in range(START_X, 3):
            start_position = (START_X * num, 0)
            self.add_segment(start_position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        # add new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Move snake forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Set heading to North"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Set heading to South"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Set heading to West"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Set heading to East"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
