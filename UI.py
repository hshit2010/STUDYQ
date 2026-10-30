import tkinter as tk
from main import main_question

the_box = tk.Tk()
the_box.title("STUDYQ")
the_box.geometry("1987x2000")

name_label = tk.Label(the_box,
                      text = "please enter your name")
name_label.pack()
name_input_box = tk.Entry(the_box)
name_input_box.pack()
print(name_input_box)

def submit_name():
    # .get() extracts the text from the UI box!
    typed_name = name_input_box.get() 
    print(f"The UI grabbed: {typed_name}")
    typed_label = tk.Label(the_box , text = typed_name)
    typed_label.pack()
    main_question(typed_name)
    
    # This is where we will eventually run main_question!

submit_btn = tk.Button(the_box, text="Submit Name", command=submit_name)
submit_btn.pack()
the_box.mainloop()