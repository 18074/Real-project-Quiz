from tkinter import *
from PIL import Image, ImageTk
import random
import tkfont



# The dictionary for my questions and answers
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

 # The function randomiser which gives a random question each time.
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
        self.main_frame= Frame (parent, bg = background_color, padx=100, pady=100)
        #padx, pady how many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.main_frame.grid() #This geometry manager organizes widgets in a table-like structure in the parent widget.

        # The code to add image in my home page
        self.bg_image= Image.open("21.png")
        self.bg_image= self.bg_image.resize((300,250), Image.ANTIALIAS )
        self.bg_image= ImageTk.PhotoImage(self.bg_image)

        self.main_frame = Frame (parent, bg= background_color)
        self.main_frame.grid()

        self.image_label = Label (self.main_frame, image=self.bg_image)
        self.image_label.place(x=100, y=100, relheight=1)

      
        # The main name label heading widget 
        self.caption_label = Label (self.main_frame, text="MATHS TEACHER CODE QUIZ", font=("Tw Cen MT","50","bold"),bg="#ce0018",)
        self.caption_label.grid(row=0, padx=20) 

        #The label for username to input the username by the users.
        self.usernamez_label = Label (self.main_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg="#ce0018")
        self.usernamez_label.grid(row=1, padx=20, pady=20)

        #The space given to enter the username
        self.entry_box = Entry (self.main_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #The label for age to input  by the users.
        self.age_label = Label (self.main_frame, text="Please enter your age below: ", font=("Tw Cen MT","16"),bg="#ce0018")
        self.age_label.grid(row=4, padx=20, pady=20) 

        #The space given to enter the age
        self.entry_box = Entry (self.main_frame)
        self.entry_box.grid(row=5,padx=20, pady=20)

        #The Continue button
        self.continue_button = Button (self.main_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="Red", command=self.name_collection)
        self.continue_button.grid(row=6,  padx=20, pady=20)

        
        #The exit button
        self.quit_button = Button (self.main_frame, text="Exit", font=("Helvetica", "15", "bold"), bg="Red", command=self.firstScreen)
        self.quit_button.grid(row=8)

            
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        #self.quiz_frame.destory()
        self.main_frame.grid_forget()
        Quiz(root)
        



       

# the coding for the exit button on the home page and will lead to a pop screen saying Please try again next time giving users an option of wanting to quit before the quiz even starts.


    def firstScreen(self):
        root.withdraw()
        open_firstscrn=First()

class First:
    def __init__(self):
        background="Oldlace"
        self.first_box= Toplevel(root)
        self.first_box.title("End Box")

        self.first_frame = Frame (self.first_box, width=1000, height=1000, bg=background)
        self.first_frame.grid()

        first_heading = Label (self.first_frame, text='Thank You', font=('Tw Cen MT',22, 'bold'), bg=background, pady=15)
        first_heading.grid(row=0)

        exit_button = Button (self.first_frame, text='Exit', width=10, bg="IndianRed1", font=('Tw Cen MT',12,'bold'), command=self.close_first)
        exit_button.grid(row=4, pady=20)

        
    def close_first(self):
        self.first_box.destory()
        root.withdraw()



                      
      
       
class Quiz:
    def __init__(self,parent):
        background_color="#3399ff"
        self.quiz_frame = Frame (parent, bg= background_color, padx=100, pady=100)
        self.quiz_frame.grid()
     
#questions for the quiz
        self.question_label = Label (self.quiz_frame, text= questions_answers[qnum][0], font=("Tw,Cen,Mt","16"), bg=background_color)
        self.question_label.grid(row=1, padx=10, pady=10)
  
        #Holds the value of the radio buttons
        self.var1=IntVar()
  
        #radio button 1
        self.rb1 = Radiobutton (self.quiz_frame, text=questions_answers[qnum][1],font=("Helvetica","12"), bg=background_color,value=1,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "#ff5050")
        self.rb1.grid(row=2,sticky=W, padx=10, pady=10)
  
        #radio button 2
        self.rb2 = Radiobutton (self.quiz_frame, text=questions_answers[qnum][2],font=("Helvetica","12"), bg=background_color,value=2,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "#ff5050")
        self.rb2.grid(row=3,sticky=W, padx=10, pady=10,)
      
        #radio button 3
        self.rb3 = Radiobutton (self.quiz_frame, text=questions_answers[qnum][3],font=("Helvetica","12"), bg=background_color,value=3,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "#ff5050")
        self.rb3.grid(row=4,sticky=W, padx=10, pady=10)
  
        #radio button 4
        self.rb4 = Radiobutton (self.quiz_frame, text=questions_answers[qnum][4],font=("Helvetica","12"), bg=background_color,value=4,padx=10,pady=10,
                  variable=self.var1, indicator = 0, background = "#ff5050")
        self.rb4.grid(row=5,sticky=W, padx=10, pady=10)
  
        #Confrim Button
        self.quizery_instance = Button (self.quiz_frame, text="Confirm", font=("Helevetica","13","bold"),bg="Gold", command=self.test_progress)
        self.quizery_instance.grid(row=6, padx=5, pady=5)
  
        #score label
        self.score_label = Label (self.quiz_frame,text="SCORE", font=("Tw Cen Mt","16"),bg=background_color,)
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
                    self.quizery_instance.config(text="Confirm")
                    self.questions_setup() # run this method to move to next question
                else: #if the choice was wrong
                    score+=0
                    self.quizery_instance.configure(text="Confirm")
                    self.questions_setup()


# The exit button that will appear on the question page which will lead to a pop screen which will say Well Done and soon wil have a scoreboard.
    
#The exit button
        self.quit1_button = Button (self.quiz_frame, text="Exit", font=("Helvetica", "15", "bold"), bg="Red", command=self.lastScreen)
        self.quit1_button.grid(row=8)

      
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        #self.quiz_frame.destory()
        self.quiz_frame.grid_forget()
        Quiz(root)



    def lastScreen(self):
        root.withdraw()
        open_lastscrn=Last()

class Last:
    def __init__(self):
        background="Oldlace"
        self.last_box= Toplevel(root)
        self.last_box.title("End Box")

        self.last_frame = Frame (self.last_box, width=1000, height=1000, bg=background)
        self.last_frame.grid()

        last_heading = Label (self.last_frame, text='Thank You', font=('Tw Cen MT',22, 'bold'), bg=background, pady=15)
        last_heading.grid(row=0)

        exit_button = Button (self.last_frame, text='Exit', width=10, bg="IndianRed1", font=('Tw Cen MT',12,'bold'), command=self.close_last)
        exit_button.grid(row=4, pady=20)

      
    def close_last(self):
        self.last_box.destory()
        root.withdraw()



    
# The coding for the leadboard from the exit page for the exit button on the question page
    def lastscreen(self):
        root.withdraw()
        name=names[0]
        file=open("leaderboard.txt","a")
        file.write(str(score))
        file.write("-")
        file.write(name+"/n")
        file.close()

        inputFile = open("leaderboard.txt",'r')
        lineList= inputFile.readlines()
        lineList.sort()
        top=[]
        top5=(lineList[-5:])
        for line in top5:
            point=line.split("-")
            top.append((int(point[0]),point[1]))
        file.close()
        top.sort()
        top.reverse()
        return_string= ""
        for line in range(len(top)):
            return_string += "{} - {}\n".format(top[i][0], top[i][1])
        print(return_string)

        open_lastscreen=End()
        open.lastscreen.listLabel.config(text=return_string)


  # The label to run lastscreen class for the leadearboard page
        self.listLabel = Label (self.last_frame, text="1st place available", font=("Tw CEN Mt ",18), width=40, bg=background, padx=10, pady=10)
        self.listLabel.grid(column=0,row=2)   







#starting point of my quiz           
randomiser ()


if __name__ == "__main__":
    root = Tk()
    root.title("MATHS TEACHER CODE QUIZ")  
    quiz_instance_object = Main(root) #instantiation, making an instance of the class Main
    root.mainloop()#so the frame doesnt dissapear
