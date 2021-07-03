from tkinter import *
from tkinter import ttk, filedialog
from fpdf import FPDF
import os
root = Tk()
root.title("Convert text to pdf")
root.geometry('650x320')
# create frame 
frame = LabelFrame(root, text="File Converter", font=('ariel 15 bold'),bd=5,fg='red',labelanchor='n',relief=GROOVE)
frame.place(x=50,y=35)
# create labels
open_file = Label(frame, text="Open File:", font=('ariel 15 bold'))
open_file.grid(row=0,column=0,padx=15,pady=15,sticky='e')
format_label = Label(frame, text="Format:", font=('ariel 15 bold'))
format_label.grid(row=1,column=0,padx=15,pady=15,sticky='e')
info_label = Label(frame, font=('ariel 15 bold'))
info_label.grid(row=2,column=1,pady=15)
# create entry
file = StringVar()
file_entry = Entry(frame, textvariable=file,font=('ariel 11 bold'), bd=2, relief=RIDGE)
file_entry.grid(row=0,column=1,padx=15,pady=15)
file_path = " "
def browse():
    # open only text files
    file_path = filedialog.askopenfilename(initialdir = os.getcwd(),title= "select file",filetypes = (("Text file","*.txt"),("All files","*.*")))
    # set the path of text file into entry
    file.set(file_path)
def convert():
    global file_path, file
                
    # create object of FPDF class
    pdf = FPDF() 
    # create or add a page in pdf
    pdf.add_page() 
    # set font style and size for text 
    pdf.set_font("arial", size = 10) 
    # open file with read mode
    text_file = open(file.get(), "r") 
    # use for loop to access the text
    # from text_file and insert it into pdf cell 
    for text in text_file: 
            pdf.cell(200, 10, txt = text, ln=1,align='L')
    # get the name of file to save
    name=file.get().split('/')[-1]
    # save the converted file with name of original file 
    pdf.output(f"{name.split('.')[0]}.{format1.get()}")        
    info_label.config(text=f"{name} converted to {name.split('.')[0]}.{format1.get()}")
# create button
browse_file = Button(frame, text="Browse File", font=('ariel 15 bold'),bd=2, relief=RIDGE,bg='green3', command=browse)
browse_file.grid(row=0,column=2,padx=15,pady=15)
convert_file = Button(frame, text="Convert File", font=('ariel 15 bold'),bd=2, relief=RIDGE,bg='green3', command=convert)
convert_file.grid(row=1,column=2,padx=15,pady=15)
# create disabled combobox with default value as pdf
format1 = StringVar()
file_formats = ['pdf']
format_combo = ttk.Combobox(frame, textvariable=format1, font=('ariel 15 bold'),width=12,state=DISABLED)
format_combo['values']=file_formats
# set the default value as pdf
format_combo.current(0)
format_combo.grid(row=1,column=1,padx=15,pady=15)
root.mainloop()