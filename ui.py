from cgitb import text
from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.win = Tk()
        self.win.title("Quiz By Liloz @")
        self.win.config(padx= 20,pady= 20,bg= THEME_COLOR)
        self.score = 0
        
        self.score_label = Label(text=f"score:{0}",highlightthickness=0,bg=THEME_COLOR)
        self.score_label.grid(row=0,column=2,padx=0,pady=40)

        self.canves = Canvas(width= 300, height= 250,bg="white")
        self.question_text = self.canves.create_text(150,125, font=("Arial",20,"italic"), text="question", fill= THEME_COLOR,width=288)
        self.canves.grid(row=2,column=1,columnspan=2)

        self.crros_image = PhotoImage(file="images/false.png")
        self.crros_butten = Button(image=self.crros_image,command= self.crros_return)
        self.crros_butten.grid(row=3,column=2,padx=0,pady=40)

        self.vey_image = PhotoImage(file="images/true.png")
        self.vey_butten = Button(image=self.vey_image, command= self.vey_return)
        self.vey_butten.grid(row=3,column=1,padx=0,pady=40)

        self.get_next_question()
       

        self.win.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canves.config(bg="white")
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canves.itemconfig(self.question_text,text= q_text)
        else:
            self.canves.config(bg="white")
            self.canves.itemconfig(self.question_text, text= "you've reached the end of the quiz")
            self.vey_butten.config(state= "disabled")
            self.crros_butten.config(state= "disabled")
    
    

    def vey_return(self):
        self.give_feedback(self.quiz.check_answer("true"))



    def crros_return(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,is_right):
        if is_right:
            self.canves.config(bg="green")
        else:
            self.canves.config(bg="red")

        self.win.after(1000,self.get_next_question)

        
        
