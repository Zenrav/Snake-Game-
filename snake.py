from turtle import Turtle
starting_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
class Snakes(Turtle):    
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.hideturtle()
        self.createsnake()
        self.head=self.segments[0]
        
    def createsnake(self):
        for i in starting_position:
            self.add_segment(i)
    
    def add_segment(self,i):
        new_part=Turtle('square')
        new_part.color('cyan')
        new_part.penup()
        new_part.goto(i)
        new_part.speed('fastest')
        self.segments.append(new_part)        
    
    def extend(self):
       self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].fd(move_distance)
   
    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def right(self):
        self.segments[0].setheading(0)
    def left(self):
        self.segments[0].setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head=self.segments[0]
    