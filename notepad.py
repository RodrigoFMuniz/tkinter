import tkinter as tk


# Instanciando a janela
window = tk.Tk()


# Mudando o título


window.title('Notepad')

# Tamanho mínimo

window.minsize(width=780, height=520)

# Adicionando área de texto
text_area = tk.Text(window, font='Arial 20 bold', width=780, height=520)
text_area.pack()


def NewFile():
    text_area.delete(1.0, "end")


def Save():
    print('Save ...')


def Save_As():
    print('Save as ...')


def quit():
    print('tchau')
    window.quit()


# Menu

main_menu = tk.Menu(window)

file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New', command=NewFile)
file_menu.add_command(label='Save as ...', command=Save_As)
file_menu.add_command(label='Save', command=Save)
file_menu.add_command(label='Exit', command=quit)

main_menu.add_cascade(label='Menu', menu=file_menu)
window.config(menu=main_menu,)


# Iniciando a janela
window.mainloop()
