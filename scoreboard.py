from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as file:
            current_hs=file.read()
            self.high_score=int(current_hs)
        self.color('orange')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"SCORE: {self.score} HIGHSCORE: {self.high_score}",align='center',font=('Courier',18,'italic'))

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}  HIGHSCORE: {self.high_score}",align='center',font=('Courier',18,'italic'))
        
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER",align='center',font=('Courier',30,'italic'))
        
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('data.txt',mode ='w') as file:
                file.write(f"{self.high_score}")


        self.score=0
        self.update_scoreboard()
        
