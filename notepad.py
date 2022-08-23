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


# Iniciando a janela
window.mainloop()
