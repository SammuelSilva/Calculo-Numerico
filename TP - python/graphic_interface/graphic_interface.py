
# Width – Largura do widget;
# Height – Altura do widget;
# Text – Texto a ser exibido no widget;
# Font – Família da fonte do texto;
# Fg – Cor do texto do widget;
# Bg – Cor de fundo do widget;
# Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).
# Frame(master) - Janela de aplicação

from tkinter import *
from math import *
#defines

HEIGHT  = 700
WIDTH   = 800
aux     = -1;

#end

#functions

def get_equations(entry):
    x = A.get()
    var_answer.set(eval(entry))
    answer()

def answer():  
    label_answer = Label(answer_frame, text = "For the lower limit equals to: "+ str (A.get()), bg = '#031636', font = "system 16 bold", fg = 'white')
    label_answer.place(relx = 0.5, rely = 0.2, relwidth = 0.4, relheight = 0.2, anchor = 'n')
    label_answer = Label(answer_frame, text = "For the upper limit equals to: "+ str (B.get()), bg = '#031636', font = "system 16 bold", fg = 'white')
    label_answer.place(relx = 0.5, rely = 0.35, relwidth = 0.4, relheight = 0.2, anchor = 'n')
    label_answer = Label(answer_frame, text = "And the number of iterations equals to: "+ str (M.get()), bg = '#031636', font = "system 16 bold", fg = 'white')
    label_answer.place(relx = 0.5, rely = 0.5, relwidth = 0.4, relheight = 0.2, anchor = 'n')
    label_answer = Label(answer_frame, text = "The answer is: "+ str (var_answer.get()), bg = '#031636', font = "system 16 bold", fg = 'white')
    label_answer.place(relx = 0.5, rely = 0.65, relwidth = 0.4, relheight = 0.2, anchor = 'n')
    if option.get() == 0:
        label_answer = Label(answer_frame, text = "Using the: Trapezium rule", bg = '#031636', font = "system 16 bold", fg = 'white')
    elif option.get() == 1:
        label_answer = Label(answer_frame, text = "Using the: Simpson's first rule", bg = '#031636', font = "system 16 bold", fg = 'white')
    else:
        label_answer = Label(answer_frame, text = "Using the: Simpson's second rule", bg = '#031636', font = "system 16 bold", fg = 'white')
    label_answer.place(relx = 0.5, rely = 0.8, relwidth = 0.4, relheight = 0.2, anchor = 'n')


def insert_data(entryA, entryB, entryM):
    A.set(entryA.get())
    B.set(entryB.get()) 
    M.set(entryM.get())

#end functions

root = Tk()
 
A          = DoubleVar()
B          = DoubleVar()
M          = DoubleVar()
var_answer = DoubleVar()

#Canvas layer and Background

canvas = Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = PhotoImage(file = 'bckgd.png' )
background_label = Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

#end


#set of buttons

    #Set of functions buttons

buttons__math_frame = Frame(root, bg = '#CCB2B2')
buttons__math_frame.place(relx = 0.5, rely = 0.08, relwidth = 0.90, relheight = 0.35, anchor = 'n')
    
    #end

    #Radio Buttons
option  = IntVar()

r_t = Radiobutton(root, text =  "Trapezium rule               ", variable = option, value = 0, bg = '#031636', font = "system 16 bold", fg = 'white')
r_t.place(relx = 0.27, rely = 0.47, anchor = 'n')
r_sf = Radiobutton(root, text = "Simpson's first rule" , variable = option, value = 1, bg = '#031636', font = "system 16 bold", fg = 'white')
r_sf.place(relx = 0.5, rely = 0.47, anchor = 'n')
r_ss = Radiobutton(root, text = "Simpson's second rule", variable = option, value = 2,  bg = '#031636', font = "system 16 bold", fg = 'white')
r_ss.place(relx = 0.72, rely = 0.47, anchor = 'n')
   
    #end
  
    #Set of Buttons add: A, B and M

      #Frame buttons

buttons_var_frame = Frame(root, bg = '#031636')
buttons_var_frame.place(relx = 0.5, rely = 0.55, relwidth = 0.90, relheight = 0.08, anchor = 'n')

            #Label Buttons for lower limit

label_buttonsA = Label(buttons_var_frame, text =  "Lower Limit", bg = '#031636', font = "system 16 bold", fg = 'white')
label_buttonsA.place(relx = 0.15, rely = 0.5, relwidth = 0.15, relheight = 0.35, anchor = 'e')

                #Lower limit input

entry_lower = Entry(buttons_var_frame, text = "Lower", bg = '#031636', font = "system 16 bold", fg = 'white', justify = CENTER)
entry_lower.place(relx = 0.29, rely = 0.5, relwidth = 0.15, relheight = 0.5, anchor = 'e')

                #End lower limit input
            #End Label Buttons for lower limit
            
            #Label Buttons for upper limit

label_buttonsB = Label(buttons_var_frame, text =  "Upper Limit", bg = '#031636', font = "system 16 bold", fg = 'white')
label_buttonsB.place(relx = 0.45, rely = 0.5, relwidth = 0.15, relheight = 0.35, anchor = 'e')
               
                #Upper limit input

entry_upper = Entry(buttons_var_frame, text = "Upper", bg = '#031636', font = "system 16 bold", fg = 'white', justify = CENTER)
entry_upper.place(relx = 0.585, rely = 0.5, relwidth = 0.15, relheight = 0.5, anchor = 'e')

                #End upper limit input
             #End Label Buttons for upper limit

             #Label Buttons for iterations
               
label_buttonsM = Label(buttons_var_frame, text =  "Iterations", bg = '#031636', font = "system 16 bold", fg = 'white')
label_buttonsM.place(relx = 0.75, rely = 0.5, relwidth = 0.15, relheight = 0.35, anchor = 'e')
                #Iterations input

entry_iterations = Entry(buttons_var_frame, text = "iterations", bg = '#031636', font = "system 16 bold", fg = 'white', justify = CENTER)
entry_iterations.place(relx = 0.88, rely = 0.5, relwidth = 0.15, relheight = 0.5, anchor = 'e')
              
                #End iterations input
             #End Label Buttons for iterations

            #push button 

f_button = Button(buttons_var_frame, text = "Insert", command = lambda:(insert_data(entry_lower, entry_upper, entry_iterations)))
f_button.place(relx = 0.975, rely = 0.5, relwidth = 0.08 , relheight = 0.5, anchor = 'e')

            #end push button

        #end_Frame_buttons
    #end Set Buttons

    #Equation Frame and Button

equation_frame = Frame(root, bg = '#031636')
equation_frame.place(relx = 0.5, rely = 0.65, relwidth = 0.90, relheight = 0.08, anchor = 'n')

            #Label Buttons for lower limit

label_equation = Label(equation_frame, text =  "Input Equation", bg = '#031636', font = "system 16 bold", fg = 'white')
label_equation.place(relx = 0.167, rely = 0.5, relwidth = 0.15, relheight = 0.35, anchor = 'e')

                #Lower limit input

entry_eq = Entry(equation_frame, text = "equation", bg = '#031636', font = "system 16 bold", fg = 'white', justify = CENTER)
entry_eq.place(relx = 0.875, rely = 0.5, relwidth = 0.7, relheight = 0.5, anchor = 'e')

                #End lower limit input
            #End Label Buttons for lower limit

              #push button 

eq_button = Button(equation_frame, text = "Solve", command = lambda:(get_equations(entry_eq.get())))
eq_button.place(relx = 0.975, rely = 0.5, relwidth = 0.08 , relheight = 0.5, anchor = 'e')

            #end push button

    #End of Equation Frame and Button

    #Answer Frame
answer_frame = Frame(root, bg = '#031636')
answer_frame.place(relx = 0.5, rely = 0.75, relwidth = 0.90, relheight = 0.2, anchor = 'n')
        #answer Label
label_answer = Label(answer_frame, text = "ANSWER", bg = '#031636', font = "system 16 bold", fg = 'white')
label_answer.place(relx = 0.5, rely = 0.01, relwidth = 0.2, relheight = 0.2, anchor = 'n')
        #end Label
    #end Frame

root.mainloop()


