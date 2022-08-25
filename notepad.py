import tkinter as tk

# Instanciando a janela
window = tk.Tk()

# Mudando o título

window.title('Notepad')

# Tamanho mínimo

window.minsize(width=780, height=520)

# Adicionando área de texto
text_area = tk.Text(window, font='Arial 20 bold')
text_area.pack()

# Menu

main_menu = tk.Menu(window)

file_menu = tk.Menu(main_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Save as ...')
file_menu.add_command(label='Save')
file_menu.add_command(label='Exit', command=window.quit)

main_menu.add_cascade(label='Menu', menu=file_menu)
window.config(menu=main_menu)

# Iniciando a janela
window.mainloop()
