import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()


def correct(inp):
   if inp.isdigit():
       return True
   elif inp is "":
       return True
   elif len(inp) == 0:
       return False
   elif len(inp) > 100:
       return False
   else:
       return False

def validation(event):
    if event.isalpha():
        return True
    elif len(event) == 0:
        return False
    elif len(event) > 20:
        return False
    elif len(event) <= 2:
        return False
    else:
        return False

def disable_event():
    pass

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", disable_event)
window.state('zoomed')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


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
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


fonts = Font(family='Calibri', size=20, weight='bold')
fonts1 = Font(family='Calibri', size=40, weight='bold')

canvas = tk.Canvas(window, height=900, width=900)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("landscape.png"))
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

#===================Page1===========================

show_frame(frame1)
button = tk.Button(frame1, text="Take Survey", command=lambda:show_frame(frame2), bg="#afeeee", height=3, width=20)
button['font'] = fonts
button.place(relx=0.5, rely=0.7)

button2 = tk.Button(frame1, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button2['font'] = fonts
button2.place(relx=0.33, rely=0.7)

label = tk.Label(frame1, text="Waste Management Survey", bg="#dcdcdc")
label['font'] = fonts1
label.place(relx=0.34, rely=0.1)

label2 = tk.Label(frame1, text="Refuse what you do not need;\n reduce what you do need;\n reuse what you consume;\n recycle what you cannot refuse, reduce, or reuse;\n and rot the rest.", bg="#dcdcdc")
label2['font'] = fonts1
label2.place(relx=0.22, rely=0.3)

#===================Page2===========================

label3_text = tk.Label(frame2, text="Firstname", bg="#dcdcdc", font=("fonts1", 40))
label3_text.place(relx=0.15, rely=0.15)
label3_entry = tk.Entry(frame2, width=40, font=("fonts1", 40))
label3_entry.place(relx=0.30, rely=0.15)
reg = window.register(validation)
label3_entry.config (validate="key", validatecommand=(reg,'%P'))

label4_text = tk.Label(frame2, text="City", bg="#dcdcdc", font=("fonts1", 40))
label4_text.place(relx=0.15, rely=0.25)
label4_entry = tk.Entry(frame2, width=40, font=("fonts1", 40))
label4_entry.place(relx=0.30, rely=0.25)
reg = window.register(validation)
label4_entry.config (validate="key", validatecommand=(reg,'%P'))

label5_text = tk.Label(frame2, text="Age", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.15, rely=0.35)
label5_entry = tk.Entry(frame2, width=40, font=("fonts1", 40))
label5_entry.place(relx=0.30, rely=0.35)
reg = window.register(correct)
label5_entry.config (validate="key", validatecommand=(reg,'%P'))

label6_text = tk.Label(frame2, text="Gender", bg="#dcdcdc", font=("fonts1", 40))
label6_text.place(relx=0.15, rely=0.45)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame2, variable=v, value=1, text="Male", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame2, variable=v, value=2, text="Female", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)
radiobutton3 = tk.Radiobutton(frame2, variable=v, value=3, text="Other", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton3.place(relx=0.65, rely=0.45)

button3 = tk.Button(frame2, text="Next -->", command=lambda:[validation, correct, show_frame(frame3)], bg="#afeeee", height=3, width=20)
button3['font'] = fonts
button3.place(relx=0.65, rely=0.7)

button4 = tk.Button(frame2, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button4['font'] = fonts
button4.place(relx=0.43, rely=0.7)

button5 = tk.Button(frame2, text="<-- Back", command=lambda: show_frame(frame1), bg="#afeeee", height=3, width=20)
button5['font'] = fonts
button5.place(relx=0.20, rely=0.7)

#===================Page3===========================

label7_text = tk.Label(frame3, text="Are there public bins near your house?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.27, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame3, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame3, variable=v, value=2, text="Not Aware", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame3, text="Next -->", command=lambda:[validation, correct, show_frame(frame4)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame3, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame3, text="<-- Back", command=lambda: show_frame(frame2), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page4===========================

label7_text = tk.Label(frame4, text="What category of waste is most significant in your household?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.15, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame4, variable=v, value=1, text="Food Waste", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.10, rely=0.45)
radiobutton2 = tk.Radiobutton(frame4, variable=v, value=2, text="Plastic Waste", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.30, rely=0.45)
radiobutton3 = tk.Radiobutton(frame4, variable=v, value=3, text="Paper Waste", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton3.place(relx=0.50, rely=0.45)
radiobutton4 = tk.Radiobutton(frame4, variable=v, value=4, text="Textile Waste", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton4.place(relx=0.71, rely=0.45)

button6 = tk.Button(frame4, text="Next -->", command=lambda:[validation, correct, show_frame(frame5)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame4, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame4, text="<-- Back", command=lambda: show_frame(frame3), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page5===========================

label7_text = tk.Label(frame5, text="Do you ever notice waste on the ground in your residential area?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.13, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame5, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame5, variable=v, value=2, text="Not Aware", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame5, text="Next -->", command=lambda:[validation, correct, show_frame(frame6)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame5, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame5, text="<-- Back", command=lambda: show_frame(frame4), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page6===========================

label7_text = tk.Label(frame6, text="Do you use any waste management tools/processes?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.19, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame6, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame6, variable=v, value=2, text="Not Aware", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame6, text="Next -->", command=lambda:[validation, correct, show_frame(frame7)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame6, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame6, text="<-- Back", command=lambda: show_frame(frame5), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page7===========================

label7_text = tk.Label(frame7, text="Do you know about the effects of poor waste management on the environment?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.05, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame7, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame7, variable=v, value=2, text="Not Aware", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame7, text="Next -->", command=lambda:[validation, correct, show_frame(frame8)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame7, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame7, text="<-- Back", command=lambda: show_frame(frame6), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page8===========================

label7_text = tk.Label(frame8, text="Do you know about the impact of poor waste management on your health?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.08, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame8, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame8, variable=v, value=2, text="Not Aware", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame8, text="Next -->", command=lambda:[validation, correct, show_frame(frame9)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame8, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame8, text="<-- Back", command=lambda: show_frame(frame7), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page9===========================

label5_text = tk.Label(frame9, text="How would you effectively manage waste?", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.24, rely=0.35)

label5_entry = tk.Entry(frame9, width=40, font=("fonts1", 40))
label5_entry.place(relx=0.20, rely=0.45)

button6 = tk.Button(frame9, text="Next -->", command=lambda:[validation, correct, show_frame(frame10)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame9, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame9, text="<-- Back", command=lambda: show_frame(frame8), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page10===========================

label7_text = tk.Label(frame10, text="In your opinion, do residents have an adequate opportunity \n to recycle and get rid of waste within the City?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.16, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame10, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.35, rely=0.45)
radiobutton2 = tk.Radiobutton(frame10, variable=v, value=2, text="Not Aware", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.485, rely=0.45)

button6 = tk.Button(frame10, text="Next -->", command=lambda:[validation, correct, show_frame(frame11)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame10, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame10, text="<-- Back", command=lambda: show_frame(frame9), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page11===========================

label7_text = tk.Label(frame11, text="Should more be done to educate the local community about \n waste/waste issues and ways to minimise waste to landfill?", bg="#dcdcdc", font=("fonts1", 40))
label7_text.place(relx=0.16, rely=0.25)

v = tk.IntVar()
radiobutton1 = tk.Radiobutton(frame11, variable=v, value=1, text="Yes", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton1.place(relx=0.4, rely=0.45)
radiobutton2 = tk.Radiobutton(frame11, variable=v, value=2, text="No", font=("fonts1", 40),  command=lambda: print(v.get()))
radiobutton2.place(relx=0.55, rely=0.45)

button6 = tk.Button(frame11, text="Next -->", command=lambda:[validation, correct, show_frame(frame12)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame11, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame11, text="<-- Back", command=lambda: show_frame(frame10), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page12===========================

label5_text = tk.Label(frame12, text="What would you like to learn about waste management?", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.18, rely=0.35)

label5_entry = tk.Entry(frame12, width=40, font=("fonts1", 40))
label5_entry.place(relx=0.21, rely=0.45)

button6 = tk.Button(frame12, text="Next -->", command=lambda:[validation, correct, show_frame(frame13)], bg="#afeeee", height=3, width=20)
button6['font'] = fonts
button6.place(relx=0.65, rely=0.7)

button7 = tk.Button(frame12, text="Quit", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.43, rely=0.7)

button8 = tk.Button(frame12, text="<-- Back", command=lambda: show_frame(frame11), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.20, rely=0.7)

#===================Page13===========================

label5_text = tk.Label(frame13, text="Thank you for participating and answering this survey. \n Please make sure you have answered all questions apporpriately and accurately.\n Your results will be collected anonymously and further used\n to provide our society with a cleaner and more efficient\n waste management system, thus benefiting both\n your health and the environment", bg="#dcdcdc", font=("fonts1", 40))
label5_text.place(relx=0.03, rely=0.2)

button7 = tk.Button(frame13, text="Complete Survey", command=window.destroy, bg="#afeeee", height=3, width=20)
button7['font'] = fonts
button7.place(relx=0.5, rely=0.7)

button8 = tk.Button(frame13, text="<-- Back", command=lambda: show_frame(frame12), bg="#afeeee", height=3, width=20)
button8['font'] = fonts
button8.place(relx=0.33, rely=0.7)

window.mainloop()