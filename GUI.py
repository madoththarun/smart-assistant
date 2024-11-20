from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
# Create the main window
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# ask function 

def ask():
    ask_val = speech_to_text.speech_to_text()
    
    
    if ask_val:
        bot_val = action.Action(ask_val)
        text.insert(END, 'User---> ' + ask_val + "\n")

        if bot_val is not None:
            text.insert(END, "BOT <--- " + str(bot_val) + "\n")

        if bot_val == "ok sir":
            root.destroy()
    else:
        text.insert(END, "BOT <--- Sorry, I couldn't understand that.\n")



# send fun

def send():
    send=entry.get()
    bot=action.Action(send)
    text.insert(END,'User--->'+send+"\n")
    if bot!=None:
        text.insert(END,"BOT <---"+str(bot)+"\n")
    if bot =="ok sir":
        root.destroy()
    
# delete func

def del_text():
    text.delete("1.0", "end")
    
# Frame for the content
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief='raised')
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text label for the title
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image resizing and adding to label
img = Image.open("assistant.png")
img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

image = ImageTk.PhotoImage(img)
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Adding a Text widget below the image
text = Text(root, font=('Courier', 10, 'bold'), bg="#356696")
text.place(x=100, y=375, width=375, height=100)

# entry widget

entry= Entry(root, justify=CENTER)
entry.place(x=100 , y=500, width=350 , height=30)

# Button 1: ASK
Button1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# Button 2: SEND
Button2 = Button(root, text="SEND", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# Button 3: DELETE
Button3 = Button(root, text="DELETE", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)



# Main loop
root.mainloop()
