from turtle import Screen
from snake import Snakes
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.title('Snake Game')
screen.bgcolor('indigo')
score=Score()
screen.tracer(0)
snake=Snakes()
food=Food()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<20:
        score.increase_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()
    
        
if game_is_on == False:
    screen.bgcolor('black') 
    score.color('red')      
        


screen.exitonclick()