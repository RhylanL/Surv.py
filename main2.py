import tkinter as tk #imports tkinter library
from tkinter.font import Font #imports tkinter font library - allows to use specific fonts
from PIL import ImageTk, Image #imports module which allows for me to use images off google/exterior sources
import sqlite3 #imports Sqlite databases for variables to be written to
from tkinter import messagebox #imports messagebox module which allows for pop up messages to appear




#=============================================== All defined functions and window/frame attributes ========================================================



def disable_event(): #prevents user from closing survey by pressing ALT+F4/closing via the X button
    pass

window = tk.Tk() #displays root window
window.protocol("WM_DELETE_WINDOW", disable_event) #prevents user from closing survey

window.attributes('-fullscreen', True) #automatically sets window to fullscreen
window.overrideredirect(True) #prevents user from closing survey

#sets row and column state for window
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)



def action(): #defines the process of answers from survey being put into sqlite database
    #sets variables for all string answers
    firstname = na.get()
    city = home.get()
    age = ag.get()
    gender = v.get()
    Q1 = v2.get()
    Q2 = v3.get()
    Q3 = v4.get()
    Q4 = v5.get()
    Q5 = v6.get()
    Q6 = v7.get()
    Q7 = manage.get()
    Q8 = v8.get()
    Q9 = v9.get()
    Q10 = learn.get()

    conn = sqlite3.connect("surveyanswers.db") #sets database form for data to be transferred to
    with conn:
        cursor=conn.cursor() #allows for data traversal
    cursor.execute('CREATE TABLE IF NOT EXISTS Answers (Firstname TEXT, City TEXT, Age INT, Gender TEXT, Q1 TEXT, Q2 TEXT, Q3 TEXT, Q4 TEXT, Q5 TEXT, Q6 TEXT, Q7 TEXT, Q8 TEXT, Q9 TEXT, Q10 TEXT)') #creates table on database with following titles
    cursor.execute('INSERT INTO Answers(Firstname, City, Age, Gender, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (firstname,city,age,gender,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10)) #uses the variables of the survey answers to put into table
    conn.commit() #makes the transaction occur
    conn.close() #closes the transaction after all data has been transferred



def show_frame(frame):
    frame.tkraise() #function which raises the frame to the top so that background images etc are not blocking the frames



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy() #if user wishes to quit, once quit button is pressed this message will pop up and if user wishes to leave the window will be destroyed and the survey will end



def validation():
    name = na.get() #variable for name answer
    msg = '' #msg has empty string this will be used to store the messages of condtions and it will be displayed in the end.

    if len(name) == 0:
        msg = 'name can\'t be empty' # If condition is started and lenght of name is checked. If the length is 0 that means there is no input in the entry box. In that case user will see a message ‘name can’t be empty’
    else: #In the else section, using exception handler try and Except if-else condition is used to check multiple parameters.
        try:
            if any(ch.isdigit() for ch in name):
                msg = 'Name can\'t have numbers' # any(ch.isdigit() for ch in name): This line of code checks for any number in the name. If found then error message will be displayed.
            elif len(name) <= 2:
                msg = 'name is too short.' # len(name) <= 2: If the total characters in the name is less than 3 than error message will be displayed.
            elif len(name) > 20:
                msg = 'name is too long.'# len(name) > 20 : name cannot be greater than 20 characters. The error message will then be shown
            else:
                show_frame(frame3)
                return True # this else statement means that if all elif and if statements above have been avoided then the next frame is able to be shown as it returns True

        except Exception as ep:
            messagebox.showerror('error', ep) #makes all of the attributes of the given Exception object accessible

    messagebox.showinfo('message', msg) # messagebox.showinfo('message', msg) This code displays the message in a pop up. Here ‘message’ is the title of message box promt and msg contains the message.



def validation2():  # =============== Same as defined function above ====================
    city = home.get()
    msg = ''

    if len(city) == 0:
        msg = 'City can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in city):
                msg = 'City can\'t have numbers'
            elif len(city) <= 2:
                msg = 'City is too short.'
            elif len(city) > 30:
                msg = 'City is too long.'
            else:
                show_frame(frame3)
                return True

        except Exception as ep:
            messagebox.showerror('error', ep)

    messagebox.showinfo('message', msg)



def validation3():  # =============== Same as defined function above ====================
    ip1 = manage.get()
    msg = ''

    if len(ip1) == 0:
        msg = 'Input can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in ip1):
                msg = 'Input can\'t have numbers'
            elif len(ip1) <= 5:
                msg = 'Input is too short.'
            elif len(ip1) > 1000:
                msg = 'Input is too long.'
            else:
                show_frame(frame10)
                return True

        except Exception as ep:
            messagebox.showerror('error', ep)

    messagebox.showinfo('message', msg)



def validation4():  # =============== Same as defined function above ====================
    ip2 = learn.get()
    msg = ''

    if len(ip2) == 0:
        msg = 'Input can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in ip2):
                msg = 'Input can\'t have numbers'
            elif len(ip2) <= 5:
                msg = 'Input is too short.'
            elif len(ip2) > 1000:
                msg = 'Input is too long.'
            else:
                show_frame(frame13)
                return True

        except Exception as ep:
            messagebox.showerror('error', ep)

    messagebox.showinfo('message', msg)



def correct(inp): #this function makes it so that only numbers (digits) can be entered in the input
   if inp.isdigit():
       return True #only digits return as True (only digits are able to be typed)
   elif inp is "":
       return True
   elif len(inp) == 0:
       return False #if input has zero characters it will return false
   elif len(inp) > 3:
       return False #if input has more than 3 characters it will return false
   else:
       return False #anything else entered will be false



#sets variables and colour for all 13 frames
frame1 = tk.Frame(window, bg="#dcdcdc")
frame2 = tk.Frame(window, bg="#dcdcdc")
frame3 = tk.Frame(window, bg="#dcdcdc")
frame4 = tk.Frame(window, bg="#dcdcdc")
frame5 = tk.Frame(window, bg="#dcdcdc")
frame6 = tk.Frame(window, bg="#dcdcdc")
frame7 = tk.Frame(window, bg="#dcdcdc")
frame8 = tk.Frame(window, bg="#dcdcdc")
frame9 = tk.Frame(window, bg="#dcdcdc")
frame10 = tk.Frame(window, bg="#dcdcdc")
frame11 = tk.Frame(window, bg="#dcdcdc")
frame12 = tk.Frame(window, bg="#dcdcdc")
frame13 = tk.Frame(window, bg="#dcdcdc")

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7,frame8, frame9, frame10,
              frame11, frame12, frame13):
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #sets the same sizing attributes to all frames



# sets variables for different fonts (different sizes, etc)
fonts = Font(family='Calibri', size=20, weight='bold')
fonts1 = Font(family='Calibri', size=40, weight='bold')



# sets canvas size (.pack() used to fill entire window)
canvas = tk.Canvas(window, height=900, width=900)
canvas.pack()



# sets background image
background_image = ImageTk.PhotoImage(Image.open("landscape.png")) #takes png image from folder
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1) #places background image as a lable



#===================Page1===========================



show_frame(frame1) #raises the frame to the top so that background images etc are not blocking the frames
button = tk.Button(frame1, text="Take Survey", command=lambda:show_frame(frame2), bg="#afeeee", height=3, width=20) #creates take survey button with set attributes, takes defined function from above (show_frame) to show next frame when button is clicked
button['font'] = fonts #uses font variable from above to set the button font
button.place(relx=0.5, rely=0.7) #button position

button2 = tk.Button(frame1, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20) #creates quit button with set attributes, takes defined fucntion from above (on_closing()) to show pop up message when quit button is clicked
button2['font'] = fonts #uses font variable from above to set the button font
button2.place(relx=0.25, rely=0.7) #button position

label = tk.Label(frame1, text="Waste Management Survey", bg="#dcdcdc") #create label which is used to hold text
label['font'] = fonts1 #uses font variable from above to set the label text font
label.place(relx=0.3, rely=0.1) #label position

label2 = tk.Label(frame1, text="Refuse what you do not need;\n reduce what you do need;\n reuse what you consume;\n recycle what you cannot refuse, reduce, or reuse;\n and rot the rest.", bg="#dcdcdc") #create label which is used to hold text
label2['font'] = fonts1 #uses font variable from above to set the label text font
label2.place(relx=0.12, rely=0.3) #label position



#===================Page2===========================



#variables set to strings which help manage the value of the following entry widgets
na = tk.StringVar()
home = tk.StringVar()
ag = tk.IntVar()

label3_text = tk.Label(frame2, text="Firstname", bg="#dcdcdc", font=("fonts1", 40)) #creates label which is used to hold text as well as defining the font
label3_text.place(relx=0.05, rely=0.15) #label position

f2label_entry = tk.Entry(frame2, textvariable=na,  width=25, font=("fonts1", 40)) # creates entry field next to corresponding label where user is able to type their preferred input, it is placed in frame2, has taken the String var from above, has a set width and has a font attribute which is active when user types
f2label_entry.place(relx=0.25, rely=0.15) # entry field position

label4_text = tk.Label(frame2, text="City", bg="#dcdcdc", font=("fonts1", 40)) #creates label which is used to hold text as well as defining the font
label4_text.place(relx=0.05, rely=0.25) #label position

f2label2_entry = tk.Entry(frame2, textvariable=home, width=25, font=("fonts1", 40)) # creates entry field next to corresponding label where user is able to type their preferred input, it is placed in frame2, has taken the String var from above, has a set width and has a font attribute which is active when user types
f2label2_entry.place(relx=0.25, rely=0.25) #entry field position

label5_text = tk.Label(frame2, text="Age", bg="#dcdcdc", font=("fonts1", 40)) #creates label which is used to hold text as well as defining the font
label5_text.place(relx=0.05, rely=0.35) #label position

f2label3_entry = tk.Entry(frame2, textvariable=ag, width=25, font=("fonts1", 40)) # creates entry field next to corresponding label where user is able to type their preferred input, it is placed in frame2, has taken the String var from above, has a set width and has a font attribute which is active when user types
f2label3_entry.place(relx=0.25, rely=0.35) #entry field positon
reg = window.register(correct) #takes defined function from above and registers it for the whole window
f2label3_entry.config (validate="key", validatecommand=(reg,'%P')) #specifies which type of event will trigger the validation. Checks if a data is valid within the entry

label6_text = tk.Label(frame2, text="Gender", bg="#dcdcdc", font=("fonts1", 40)) #creates label which is used to hold text as well as defining the font
label6_text.place(relx=0.05, rely=0.45) #label position

v = tk.IntVar() #radiobuttons variable set to a integer string (holds integers)
v.set(1) #makes it so that the first radiobutton is entered so that an answer is given even if user has not selected anything
radiobutton1 = tk.Radiobutton(frame2, variable=v, value=1, text="Male", font=("fonts1", 40)) #sets radiobutton and its attributes, each radiobutton has to have a different set value otherwise each radiobutton will be selected if they have the same value
radiobutton1.place(relx=0.35, rely=0.45) #radio button position
radiobutton2 = tk.Radiobutton(frame2, variable=v, value=2, text="Female", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)
radiobutton3 = tk.Radiobutton(frame2, variable=v, value=3, text="Other", font=("fonts1", 40))
radiobutton3.place(relx=0.65, rely=0.45)

button3 = tk.Button(frame2, text="Next -->", command=lambda:[validation(), validation2()], bg="#afeeee", height=3, width=20) #next button created in order to go to next frame, it carries two defined functions from above (validation and validation 2)
button3['font'] = fonts #uses font variable from above to set the button text font
button3.place(relx=0.65, rely=0.7) #button position

button4 = tk.Button(frame2, text="Quit", command=lambda: on_closing(), bg="#afeeee", height=3, width=20) #quit button aforementioned above
button4['font'] = fonts
button4.place(relx=0.4, rely=0.7)

button5 = tk.Button(frame2, text="<-- Back", command=lambda: show_frame(frame1), bg="#afeeee", height=3, width=20) #back button created in order for user to go back a frame
button5['font'] = fonts
button5.place(relx=0.15, rely=0.7)



#===================Page3 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame3, text="Are there public bins near your house?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.27, rely=0.25)

v2 = tk.IntVar()
v2.set(1)
radiobutton1 = tk.Radiobutton(frame3, variable=v2, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame3, variable=v2, value=2, text="Not Aware", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame3, text="Next -->", command=lambda:[validation, show_frame(frame4)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame3, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame3, text="<-- Back", command=lambda: show_frame(frame2), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page4 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame4, text="What category of waste is most significant in your household?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.15, rely=0.25)

v3 = tk.IntVar()
v3.set(1)
radiobutton1 = tk.Radiobutton(frame4, variable=v3, value=1, text="Food Waste", font=("fonts1", 40))
radiobutton1.place(relx=0.10, rely=0.45)
radiobutton2 = tk.Radiobutton(frame4, variable=v3, value=2, text="Plastic Waste", font=("fonts1", 40))
radiobutton2.place(relx=0.30, rely=0.45)
radiobutton3 = tk.Radiobutton(frame4, variable=v3, value=3, text="Paper Waste", font=("fonts1", 40))
radiobutton3.place(relx=0.50, rely=0.45)
radiobutton4 = tk.Radiobutton(frame4, variable=v3, value=4, text="Textile Waste", font=("fonts1", 40))
radiobutton4.place(relx=0.71, rely=0.45)

button6 = tk.Button(frame4, text="Next -->", command=lambda:[validation, show_frame(frame5)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame4, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame4, text="<-- Back", command=lambda: show_frame(frame3), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page5 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame5, text="Do you ever notice waste on the ground in your residential area?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.13, rely=0.25)

v4 = tk.IntVar()
v4.set(1)

radiobutton1 = tk.Radiobutton(frame5, variable=v4, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame5, variable=v4, value=2, text="Not Aware", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame5, text="Next -->", command=lambda:[validation, show_frame(frame6)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame5, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame5, text="<-- Back", command=lambda: show_frame(frame4), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page6 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame6, text="Do you use any waste management tools/processes?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.19, rely=0.25)

v5 = tk.IntVar()
v5.set(1)

radiobutton1 = tk.Radiobutton(frame6, variable=v5, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame6, variable=v5, value=2, text="Not Aware", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame6, text="Next -->", command=lambda:[validation, show_frame(frame7)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame6, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame6, text="<-- Back", command=lambda: show_frame(frame5), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page7 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame7, text="Do you know about the effects of poor waste management on the environment?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.05, rely=0.25)

v6 = tk.IntVar()
v6.set(1)

radiobutton1 = tk.Radiobutton(frame7, variable=v6, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame7, variable=v6, value=2, text="Not Aware", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame7, text="Next -->", command=lambda:[validation, show_frame(frame8)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame7, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame7, text="<-- Back", command=lambda: show_frame(frame6), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page8 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame8, text="Do you know about the impact of poor waste management on your health?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.08, rely=0.25)

v7 = tk.IntVar()
v7.set(1)

radiobutton1 = tk.Radiobutton(frame8, variable=v7, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame8, variable=v7, value=2, text="Not Aware", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame8, text="Next -->", command=lambda:[validation, show_frame(frame9)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame8, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame8, text="<-- Back", command=lambda: show_frame(frame7), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page9 Same code from previous page just with different variable names===========================



label5_text = tk.Label(frame9, text="How would you effectively manage waste?", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.24, rely=0.35)

manage = tk.StringVar()

f9label_entry = tk.Entry(frame9, textvariable=manage, width=40, font=("fonts1", 40))
f9label_entry.place(relx=0.20, rely=0.45)

button6 = tk.Button(frame9, text="Next -->", command=lambda: validation3(), bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame9, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame9, text="<-- Back", command=lambda: show_frame(frame8), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page10 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame10, text="In your opinion, do residents have an adequate opportunity \n to recycle and get rid of waste within the City?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.16, rely=0.25)

v8 = tk.IntVar()
v8.set(1)

radiobutton1 = tk.Radiobutton(frame10, variable=v8, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame10, variable=v8, value=2, text="Not Aware", font=("fonts1", 40))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame10, text="Next -->", command=lambda: show_frame(frame11), bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame10, text="Quit", command=lambda:on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame10, text="<-- Back", command=lambda: show_frame(frame9), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page11 Same code from previous page just with different variable names===========================



label7_text = tk.Label(frame11, text="Should more be done to educate the local community about \n waste/waste issues and ways to minimise waste to landfill?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.16, rely=0.25)

v9 = tk.IntVar()
v9.set(1)

radiobutton1 = tk.Radiobutton(frame11, variable=v9, value=1, text="Yes", font=("fonts1", 40))
radiobutton1.place(relx=0.4, rely=0.45)
radiobutton2 = tk.Radiobutton(frame11, variable=v9, value=2, text="No", font=("fonts1", 40))
radiobutton2.place(relx=0.55, rely=0.45)

button6 = tk.Button(frame11, text="Next -->", command=lambda: show_frame(frame12), bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame11, text="Quit", command=lambda: on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame11, text="<-- Back", command=lambda: show_frame(frame10), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page12 Same code from previous page just with different variable names===========================



label5_text = tk.Label(frame12, text="What would you like to learn about waste management?", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.18, rely=0.35)

learn = tk.StringVar()

f12label_entry = tk.Entry(frame12, textvariable=learn, width=40, font=("fonts1", 40))
f12label_entry.place(relx=0.21, rely=0.45)

button6 = tk.Button(frame12, text="Next -->", command=lambda: validation4(), bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame12, text="Quit", command=lambda: on_closing(), bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame12, text="<-- Back", command=lambda: show_frame(frame11), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)



#===================Page13 Same code from previous page just with different text and variable names===========================



label5_text = tk.Label(frame13, text="Thank you for participating and answering this survey. \n Please make sure you have answered all questions apporpriately and accurately.\n Your results will be collected anonymously and further used\n to provide our society with a cleaner and more efficient\n waste management system, thus benefiting both\n your health and the environment", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.03, rely=0.2)

button7 = tk.Button(frame13, text="Complete Survey", command=lambda: [action(),on_closing()], bg="#afeeee", height=3, width=20) #actives data collection for database (action())
button7['font'] = fonts
button7.place(relx=0.5, rely=0.7)

button8 = tk.Button(frame13, text="<-- Back", command=lambda: show_frame(frame12), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.33, rely=0.7)

window.mainloop() #executes application
