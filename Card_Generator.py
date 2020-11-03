from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk,ImageGrab
import pyautogui



canvas=0

def save_as_png(canvas,fileName):
    # save postscipt image 
    #time.sleep(3)
    #img= ImageGrab.grab(bbox=canvas) #(0,0,380,195))
    #canvas.postscript(file = fileName + '.eps') 
    # use PIL to convert to PNG 
    #img = Image.open(fileName + '.eps') 
    img = pyautogui.screenshot()
    img.save(fileName + '.png', 'png') 
top=0
def getter(widget,fileName):
    global top
    x=top.winfo_rootx()+widget.winfo_x()-5
    print(x)
    y=top.winfo_rooty()+widget.winfo_y()-5
    print(y)
    x1=x+395
    print(x1)
    y1=y+210
    print(y1)
    ImageGrab.grab().crop((x,y,x1,y1)).save(fileName + '.png')

def card_gen():
    global canvas,name,top
    top = Toplevel(root)
    top.title("Card")
    top.geometry("405x255")
    top.resizable(False, False)
    canvas = Canvas(top)
    
    bg_col="#8df74f"
    rely_var1=0.1
    lb11 = Label(canvas,text=name.get(), bg="white",fg="black",font=('Helvetica',18,'bold'))
    lb11.place(relx=0.75-0.02*len(name.get()),rely=0.055, relheight=0.15)
    
    photo = PhotoImage(file = "python2.png")
#photo = photo.resize((250, 250), Image. ANTIALIAS)
    photoimage= photo.subsample(1, 1)
    
    
    lb12=Label(canvas,image = photoimage,borderwidth=0, highlightthickness=0)
    lb12.place(relx=0.01,rely=0.23)

    distance=0.12
    fg_color_text="black"
    starting=0.85
    lb13 = Label(canvas,text=high_edu.get(), bg=bg_col,fg=fg_color_text,font=('Helvetica',12))
    lb13.place(relx=starting-0.02*len(high_edu.get()),rely=rely_var1+distance, relheight=0.09)

    lb14 = Label(canvas,text=contact.get(), bg=bg_col,fg=fg_color_text,font=('Helvetica',12))
    lb14.place(relx=starting-0.02*len(contact.get()),rely=rely_var1+2*distance, relheight=0.09)

    lb15 = Label(canvas,text=Email.get(), bg=bg_col,fg=fg_color_text,font=('Helvetica',12))
    lb15.place(relx=starting-0.02*len(Email.get()),rely=rely_var1+3*distance, relheight=0.10)

    lb16 = Label(canvas,text=Position.get(), bg=bg_col,fg=fg_color_text,font=('Helvetica',12))
    lb16.place(relx=starting-0.02*len(Position.get()),rely=rely_var1+4*distance, relheight=0.09)

    lb17 = Label(canvas,text="Skill "+str(Language_Skill_Scale.get()), bg=bg_col,fg=fg_color_text,font=('Helvetica',12,"bold"))
    lb17.place(relx=0.18-0.01*len("Skill "+str(Language_Skill_Scale.get())),rely=rely_var1+4*distance+0.03, relheight=0.09)
    
    my_rectangle = round_rectangle(5, 5, 380, 195, 20,canvas, fill=bg_col)
   
    my_rectangle2 = round_rectangle(15, 15, 365, 55, 20,canvas, fill="white")
    canvas.place(x=10,y=10)
    
    # new_im = Image.fromarray(top)
    # new_im.save("Card.png")
    savebtn = Button(top,text="Save",bg='#d1ccc0', fg='black', command= lambda: getter(canvas,name.get()+"'s Card" )  )
    savebtn.place(x=195,y=215)
   
    top.mainloop()
   
    



def round_rectangle(x1, y1, x2, y2, radius,can, **kwargs):
    global canvas
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return can.create_polygon(points, **kwargs, smooth=True)


    



    

    
global bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

root = Tk()
root.title("Card Generator")
root.minsize(width=400,height=400)
root.geometry("600x700")

headingLabel = Label(root, text="Add Details", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.08)

bg_color='#d1ccc0'
fg_color='black'
rely_var=0.1
rel_change_h=0.10
lb1 = Label(root,text="Name : ", fg=fg_color,font=(15))
lb1.place(relx=0.05,rely=rely_var, relheight=0.05)
    
name = Entry(root)
name.place(relx=0.3,rely=rely_var, relwidth=0.62, relheight=0.05)
    

lb2 = Label(text="Highest\t  \nEducation : ", fg=fg_color,font=(1))
lb2.place(relx=0.05,rely=rely_var+rel_change_h, relheight=0.06)
    
high_edu= Entry(root)
high_edu.place(relx=0.3,rely=rely_var+rel_change_h, relwidth=0.62, relheight=0.05)
   
lb3 = Label(root,text="Contact No : ",  fg=fg_color,font=(15))
lb3.place(relx=0.05,rely=rely_var+2*rel_change_h, relheight=0.05)
    
contact = Entry(root)
contact.place(relx=0.3,rely=rely_var+2*rel_change_h, relwidth=0.62, relheight=0.05)
    

lb4 = Label(root,text="Email : ",  fg=fg_color,font=(15))
lb4.place(relx=0.05,rely=rely_var+3*rel_change_h, relheight=0.05)
    
Email = Entry(root)
Email.place(relx=0.3,rely=rely_var+3*rel_change_h, relwidth=0.62, relheight=0.05)

lb5 = Label(root,text="Position : ", fg=fg_color,font=(15))
lb5.place(relx=0.05,rely=rely_var+4*rel_change_h, relheight=0.05)
    
Position = Entry(root)
Position.place(relx=0.3,rely=rely_var+4*rel_change_h, relwidth=0.62, relheight=0.05)


lb5 = Label(root,text="Working : ", fg=fg_color,font=(15))
lb5.place(relx=0.05,rely=rely_var+5*rel_change_h, relheight=0.05)

CheckVar1 = IntVar()

Working = Checkbutton(root, text = "Working", variable = CheckVar1,onvalue = 1, offvalue = 0,)    

Working.place(relx=0.3,rely=rely_var+5*rel_change_h, relwidth=0.62, relheight=0.05)

Language_Skill = Label(root,text="Language Skill : ", fg=fg_color,font=(12))
Language_Skill.place(relx=0.05,rely=rely_var+6*rel_change_h, relheight=0.05)

Language_Skill_Scale = Scale(root, from_=0,to=100,orient=HORIZONTAL)
Language_Skill_Scale.place(relx=0.3,rely=rely_var+6*rel_change_h, relwidth=0.62, relheight=0.05)

def hello():
 messagebox.showinfo("Creator", "Marvin Raval")
B1 = Button(root, text = "Creator", command = hello)
B1.place(relx=0.70,rely=rely_var+7*rel_change_h, relwidth=0.18,relheight=0.05)

#Submit Button
SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', command=card_gen)
SubmitBtn.place(relx=0.28,rely=rely_var+8*rel_change_h, relwidth=0.18,relheight=0.05)

quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',command=root.destroy)
quitBtn.place(relx=0.53,rely=rely_var+8*rel_change_h, relwidth=0.18,relheight=0.05)

root.mainloop()

