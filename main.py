from tkinter import *

import random

global questions_answers
names = []
asked = []
score=0

questions_answers={
    1:["Which teacher code does Ms Chen have?",'HUL','BNT','CHA','MKN',3],
    2:["Which teacher code does Ms Maka have?",'MKN','MOR','CDA','SKE',1],
    3:["Which teacher code does Mr Singh have?",'SKE','SNR','TUL','RDK',2],
    4:["Which teacher code does Mr Johsnson have?",'JNR','EBM','YAN','DSR',1],
    5:["Which teacher code does Ms Ranchhodiji have?",'YAN','BNT','SNR','RDK',4],
    6:["Which teacher code does Mrs Wright have?",'HPL','WRS','LYN','KAN',2],
    7:["Which teacher code does Mr Coker have?",'CDA','SBV','CRJ','KAN',3],
    8:["Which teacher code does Ms Yang have?",'YAN','DSR','LYN','WRS',1],
    9:["Which teacher code does Ms Katira have?",'JNR','KAN','BNT','TUL',2],
    10:["Which teacher code does Mrs Lynch have?",'SBV','SKE','BNT','LYN',4],
    
    }

 
def randomiser():
    global qnum # The number given to the question from the dictionary above.
    qnum = random.randint(1,10) # Order of the questions is randomised
    if qnum not in asked: # presented is the list in which the numbers are added and checked everytime before a question is presented
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

 
class Main:
    def __init__(self, parent): # Constructor, The __init__() function is called automatically every time the class is being used to create a new object.
        background_color="RoyalBlue" #To set it as background color for the main page for my quiz.

        # Frame set up for my main page for the quiz.
        self.main_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady how many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.main_frame.grid() #This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        # The main name label heading widget 
        self.caption_label=Label(self.main_frame, text="MATHS TEACHER CODE QUIZ", font=("Tw Cen MT","50","bold"),bg="#ce0018",)
        self.caption_label.grid(row=0, padx=20) 

        #The label for username to input the username by the users.
        self.usernamez_label=Label(self.main_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg="#ce0018")
        self.usernamez_label.grid(row=1, padx=20, pady=20)

        #The space given to enter the username
        self.entry_box=Entry(self.main_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #The label for age to input  by the users.
        self.age_label=Label(self.main_frame, text="Please enter your age below: ", font=("Tw Cen MT","16"),bg="#ce0018")
        self.age_label.grid(row=4, padx=20, pady=20) 

        #The space given to enter the age
        self.entry_box=Entry(self.main_frame)
        self.entry_box.grid(row=5,padx=20, pady=20)

        #The Continue button
        self.continue_button = Button(self.main_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="Red", command=self.name_collection)
        self.continue_button.grid(row=6,  padx=20, pady=20)

        
        #The exit button
        self.quit_button = Button(self.main_frame, text="Exit", font=("Helvetica", "15", "bold"), bg="Red", command=self.endScreen)
        self.quit_button.grid(row=8, sticky=E,padx=35, pady=35)

       

# the coding for the exit button on the home page and will lead to a pop screen saying Please try again next time giving users an option of wanting to quit before the quiz even starts.
    def endScreen(self):
        root.withdraw()
        open_endscrn=End()

class End:
    def __init__(self):
        background="Oldlace"
        self.end.box= Toplevel(root)
        self.end_box.title("End Box")

        self.end_frame = Frame (self.end.box, width=1000, height=1000, bg=background)
        self.end_frame.grid()

        end_heading = Label (self.end_frame, text='Please try again next time', font=('Tw Cen MT',22, 'bold'), bg=background, pady=15)
        end_hearing.grid(row=0)

        exit_button= Button(self.end_frame, text='Exit', width=10, bg="IndianRed1", font=('Tw Cen MT',12,'bold'), command=self.close_end)
        exit_button.grid(row=4, pady=20)

        
    def close_end(self):
        self.end_box.destory()
        root.withdraw()
                

                       
            

    
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        #self.quiz_frame.destory()
        self.main_frame.grid_forget()
        Quiz(root)
      
       
class Quiz:
    def __init__(self,parent):
        background_color="OldLace"
        self.quiz_frame= Frame(parent, bg= background_color, padx=100, pady=100)
        self.quiz_frame.grid()
     
#questions for the quiz
        self.question_label = Label(self.quiz_frame, text= questions_answers[qnum][0], font=("Tw,Cen,Mt","16"), bg=background_color)
        self.question_label.grid(row=1, padx=10, pady=10)
  
        #Holds the value of the radio buttons
        self.var1=IntVar()
  
        #radio button 1
        self.rb1= Radiobutton(self.quiz_frame, text=questions_answers[qnum][1],font=("Helvetica","12"), bg=background_color,value=1,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "light blue")
        self.rb1.grid(row=2,sticky=W)
  
        #radio button 2
        self.rb2= Radiobutton(self.quiz_frame, text=questions_answers[qnum][2],font=("Helvetica","12"), bg=background_color,value=2,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "light blue")
        self.rb2.grid(row=3,sticky=W)
      
        #radio button 3
        self.rb3= Radiobutton(self.quiz_frame, text=questions_answers[qnum][3],font=("Helvetica","12"), bg=background_color,value=3,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "light blue")
        self.rb3.grid(row=4,sticky=W)
  
        #radio button 4
        self.rb4= Radiobutton(self.quiz_frame, text=questions_answers[qnum][4],font=("Helvetica","12"), bg=background_color,value=4,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "light blue")
        self.rb4.grid(row=5,sticky=W)
  
        #Confrim Button
        self.quizery_instance= Button(self.quiz_frame, text="Confirm", font=("Helevetica","13","bold"),bg="Gold", command=self.test_progress)
        self.quizery_instance.grid(row=7, padx=5, pady=5)
  
        #score label
        self.score_label=Label(self.quiz_frame,text="SCORE", font=("Tw Cen Mt","16"),bg=background_color,)
        self.score_label.grid(row=8,padx=10,pady=1)




   
    # Editing the question label and radio buttons to show the next questions data
    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])

    
    #Method that will invoke the confirm button, to take care of the progress 
    def test_progress(self): 
        global score 
        scr_label=self.score_label
        choice = self.var1.get()
        if len(asked)>9: # if the question is last 
            if choice==questions_answers[qnum][5]: #if last question is right answer
                score +=1
                scr_label.configure(text=score)
                self.quizery_instance.config(text="confirm")
            else:
                score+=0
                scr_label.configure(text="THE CORRECT ANSWER was "+ questions_answers[qnum][5])
                self.quizery_instance.config(text="Confirm")
        else:
            if choice == 0: # checks if he user has made a choice
                self.quizery_instance.config(text="TRY AGAIN plz you didn't select anything")
                choice=self.var1.get()
            else: # if they made a choice and it's not last question
                if choice==questions_answers[qnum][5]: # if their choice is right
                    score+=1 
                    scr_label.configure(text=score)
                    self.quizery_instance(text="Confirm")
                    self.questions_setup() # run this method to move to next question
                else: #if the choice was wrong
                    score+=0
                    scr_label.configure(text="The correct answer was:"+ questions_answers[qnum][5])
                    self.quizery_instance.configure(text="Confirm")
                    self.questions.setup()


# The exit button that will appear on the question page which will lead to a pop screen which will say Well Done and soon wil have a scoreboard.
    
def endScreen(self):
    root.withdraw()
    open_endscrn=End()

class End:
    def __init__(self):
        background="Oldlace"
        self.end.box= Toplevel(root)
        self.end_box.title("End Box")

        self.end_frame = Frame (self.end.box, width=1000, height=1000, bg=background)
        self.end_frame.grid()

        end_heading = Label (self.end_frame, text='Well Done', font=('Tw Cen MT',22, 'bold'), bg=background, pady=15)
        end_hearing.grid(row=0)

        exit_button= Button(self.end_frame, text='Exit', width=10, bg="IndianRed1", font=('Tw Cen MT',12,'bold'), command=self.close_end)
        exit_button.grid(row=4, pady=20)

        
def close_end(self):
    self.end_box.destory()
    root.withdraw()


    
          
#starting point of my quiz           
randomiser ()


if __name__ == "__main__":
    root = Tk()
    root.title("MATHS TEACHER CODE QUIZ")  
    quiz_instance_object = Main(root) #instantiation, making an instance of the class Main
    root.mainloop()#so the frame doesnt dissapear
