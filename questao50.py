# Crie uma calculadora com INTERFACE GRÁFICA de soma, subtração, multiplicação e divisão mostrando
# na tela e salvando em ARQUIVO cada resultado. Basicamente, o usuário digita o valor do primeiro
# número e do segundo número nos campos da tela, depois ele clica em uma das operações: soma, subtração,
# multiplicação ou divisão, então o programa processa o resultado da operação escolhida pelo usuário com os
# números que digitados e apresenta a saída na tela no lugar do texto "resultado".

from tkinter import *

win = Tk()
win.geometry("380x324")
win.resizable(0, 0)
win.title("Calculadora")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""

input_text = StringVar()


input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)


input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)


btns_frame = Frame(win, width=312, height=272.5, bg="grey")

btns_frame.pack()


limpa = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#fff",
               command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)


botao_7 = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

botao_8 = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

botao_9 = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiplica = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)


botao_4 = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

botao_5 = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

botao_6 = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

subtrai = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

botao_1 = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

botao_2 = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

botao_3 = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

soma = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)


botao_0 = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

ponto = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

iguala = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()

