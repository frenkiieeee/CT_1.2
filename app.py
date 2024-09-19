import tkinter as tk
from tkinter import font as tkfont
import compresor_tk
import mp4_to_mp3_tk
import photo_convert_tk
import remove_png_tk
import yt_tk

# Animaciones para los botones del menu
def on_enter(e):
    e.widget.config(bg='#ffffff')
    e.widget.config(padx=3, pady=3)
    e.widget.config(fg="#7e3bb7")

def on_leave(e):
    e.widget.config(bg='#7e3bb7')
    e.widget.config(padx=0, pady=0)
    e.widget.config(fg="white")

# Animaciones para el boton de cerrar
def on_enter_close(e):
    e.widget.config(bg='#ff0000')
    e.widget.config(padx=3, pady=3)
    e.widget.config(fg="white")

def on_leave_close(e):
    e.widget.config(bg='#7e3bb7')
    e.widget.config(padx=0, pady=0)
    e.widget.config(fg="white")

# Menu principal
def show_menu():
    def open_app_1():   # Funcion para abrir YouTube
        root.destroy()
        yt_tk.show_menu_yt_tk()
        show_menu()

    def open_app_2():   # Funcion para abrir Photo Converter
        root.destroy()
        photo_convert_tk.show_menu()
        show_menu()

    def open_app_3():   # Funcion para abrir MP3 to MP4
        root.destroy()
        mp4_to_mp3_tk.show_menu()
        show_menu()

    def open_app_4():   # Funcion para abrir Compress File
        root.destroy()
        compresor_tk.compress_file()
        show_menu()

    def open_app_5():   # Funcion para abrir Remove Background  
        root.destroy()
        remove_png_tk.show_menu()
        show_menu()

    def close_program(): # Funcion para cerrar el programa
        root.destroy()

    # Interfaz Menu principal
    root = tk.Tk()
    root.title("Creators Tools")
    root.geometry("400x375")
    root.resizable(False, False)
    root.configure(bg="#222222")
    root.iconbitmap("CT.ico")

    # Fuente en negrita
    bold_font = tkfont.Font(size=18, weight="bold")

    # Botones 
    title_label = tk.Label(root, text="CREATORS TOOLS",font=bold_font ,fg="white", bg="#7e3bb7", width=35)
    title_label.pack(pady=17)

    app1_button = tk.Button(root, text="YouTube Downloader", command=open_app_1, fg="white", bg="#7e3bb7", width=20)
    app1_button.pack(pady=10)
    app1_button.bind('<Enter>', on_enter)
    app1_button.bind('<Leave>', on_leave)

    app2_button = tk.Button(root, text="Photo Convert", command=open_app_2, fg="white", bg="#7e3bb7", width=20)
    app2_button.pack(pady=10)
    app2_button.bind('<Enter>', on_enter)
    app2_button.bind('<Leave>', on_leave)

    app3_button = tk.Button(root, text="MP4 to MP3", command=open_app_3, fg="white", bg="#7e3bb7", width=20)
    app3_button.pack(pady=10)
    app3_button.bind('<Enter>', on_enter)
    app3_button.bind('<Leave>', on_leave)

    app4_button = tk.Button(root, text="Photo/Video Compresor", command=open_app_4, fg="white", bg="#7e3bb7", width=20)
    app4_button.pack(pady=10)
    app4_button.bind('<Enter>', on_enter)
    app4_button.bind('<Leave>', on_leave)

    app5_button = tk.Button(root, text="Remove Background (beta)", command=open_app_5, fg="white", bg="#7e3bb7", width=20)
    app5_button.pack(pady=10)
    app5_button.bind('<Enter>', on_enter)
    app5_button.bind('<Leave>', on_leave)

    close_button = tk.Button(root, text="Cerrar", command=close_program, fg="white", bg="#7e3bb7", width=14)
    close_button.pack(pady=10)
    close_button.bind('<Enter>', on_enter_close)
    close_button.bind('<Leave>', on_leave_close)

    root.mainloop()

show_menu()