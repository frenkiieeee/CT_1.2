# Con el uso de la libreria "pytubefix" deja descargar videos a una calidad maxima de 360p
# ( Es la libreria que no ha dado problemas a la hora de descargar videos, ya que otras estan generando errores)

import tkinter as tk
from tkinter import filedialog, messagebox, font as tkfont
from pytubefix import YouTube
from moviepy.editor import *
import os
import urllib.request
from PIL import Image, ImageTk

# Animaciones para los botones del menu
def on_enter(e):
    e.widget.config(bg='#ffffff')
    e.widget.config(padx=3, pady=3)
    e.widget.config(fg="#7e3bb7")

def on_leave(e):
    e.widget.config(bg='#7e3bb7')
    e.widget.config(padx=0, pady=0)
    e.widget.config(fg="white")

# Funciones para el menu de descarga del video
def show_menu_yt_tk():
    def download_video_with_url(url):
        def select_folder():
            folder_selected = filedialog.askdirectory()
            return folder_selected

        def show_download_complete():
            messagebox.showinfo("Descarga completa", "El archivo ha sido descargado")

        def download_selected_video():
            selected_quality_index = variable.get()
            selected_video_stream = yt_quality[selected_quality_index]
            folder_path = select_folder()
            if folder_path:
                selected_video_stream.download(output_path=folder_path)
                show_download_complete()
                root.destroy()
                show_menu_yt_tk()

        def download_selected_audio():
            selected_audio_stream = yt_audio[variable.get() - len(yt_quality)]
            folder_path = select_folder()
            if folder_path:
                audio_path = selected_audio_stream.download(folder_path)
                mp3_path = os.path.splitext(audio_path)[0] + ".mp3"
                audio = AudioFileClip(audio_path)
                audio.write_audiofile(mp3_path)
                os.remove(audio_path)
                show_download_complete()
                root.destroy()
                show_menu_yt_tk()

        yt = YouTube(url)
        yt_title = yt.title
        yt_thumbnail = yt.thumbnail_url
        yt_streams = yt.streams

        # Filtrar las calidades de video específicas
        desired_qualities = ["144p", "240p", "360p", "480p", "720p", "1080p"]
        yt_quality = [stream for stream in yt_streams.filter(progressive=True) if stream.resolution in desired_qualities]

        # Filtrar las mejores dos opciones de audio
        yt_audio = yt_streams.filter(only_audio=True).order_by("abr")[-2:]

        # Menu de descarga
        root = tk.Tk()
        root.title("Creators Tools")
        root.configure(bg="#222222")
        root.geometry("420x330")
        root.resizable(False, False)
        root.iconbitmap("CT.ico")

        # Miniatura del video
        urllib.request.urlretrieve(yt_thumbnail, "thumbnail.png")
        thumbnail_image = Image.open("thumbnail.png")
        thumbnail_image = thumbnail_image.resize((185, 110), Image.ANTIALIAS)
        thumbnail_image = ImageTk.PhotoImage(thumbnail_image)

        thumbnail_label = tk.Label(root, image=thumbnail_image, bg="#7e3bb7", border=2)
        thumbnail_label.grid(row=0, column=0, padx=10, pady=25, rowspan=2)

        # Titulo del video
        title_label = tk.Label(root, text=yt_title, fg="white", bg="#7e3bb7", wraplength=150, justify="center")
        title_label.grid(row=2, column=0, padx=10, pady=10)

        quality_label = tk.Label(root, text="Seleccione la calidad:", fg="white", bg="#7e3bb7", border=10)
        quality_label.grid(row=1, column=3, padx=20)

        yt_streams = yt_quality + yt_audio
        variable = tk.IntVar()

        # Bucle para generar los formatos de descarga
        row_counter = 2
        for i, stream in enumerate(yt_quality):
            text = f"{stream.resolution} / mp4"
            radio_button = tk.Radiobutton(root, text=text, variable=variable, value=i, fg="white", bg="#222222", selectcolor="#7e3bb7")
            radio_button.grid(row=row_counter, column=3, sticky="w", padx=50)
            row_counter += 1

        for i, stream in enumerate(yt_audio):
            text = f"{stream.abr} / mp3"
            radio_button = tk.Radiobutton(root, text=text, variable=variable, value=len(yt_quality) + i, fg="white", bg="#222222", selectcolor="#7e3bb7")
            radio_button.grid(row=row_counter, column=3, sticky="w", padx=50)
            row_counter += 1

        # Funcion para la descarga del archivo
        def download_selected():
            if variable.get() < len(yt_quality):
                download_selected_video()
            else:
                download_selected_audio()

        download_button = tk.Button(root, text="Descargar", command=download_selected, fg="white", bg="#7e3bb7", width=20)
        download_button.grid(row=4, column=0)
        download_button.bind('<Enter>', on_enter)
        download_button.bind('<Leave>', on_leave)

        root.mainloop()

    # Funcion para buscar el enlace
    def download_video():
        url = url_entry.get()
        if not is_valid_url(url):
            messagebox.showerror("Error", "El enlace que has introducido no es válido")
            url_entry.delete(0, tk.END)
            return
        root.destroy()
        download_video_with_url(url)

    def paste_from_clipboard():
        clipboard_content = root.clipboard_get()
        url_entry.insert(tk.END, clipboard_content)

    def is_valid_url(url):
        try:
            yt = YouTube(url)
            yt.check_availability()
            return True
        except Exception as e:
            print(f"Error de validación de URL con pytubefix: {e}")
            return False

    # Menu principal
    root = tk.Tk()
    root.title("Creators Tools")
    root.configure(bg="#222222")
    root.geometry("300x150")
    root.resizable(False, False)
    root.iconbitmap("CT.ico")


    title_label = tk.Label(root, text="Ingresa la URL del video de YouTube:", fg="white", bg="#7e3bb7", width=50, height=1)
    title_label.pack(pady=10)

    url_entry = tk.Entry(root, width=40)
    url_entry.pack(pady=10)

    paste_button = tk.Button(root, text="Pegar URL", command=paste_from_clipboard, fg="white", bg="#7e3bb7", width=10)
    paste_button.pack(pady=20, padx=26, side="left")
    paste_button.bind('<Leave>', on_leave)
    paste_button.bind('<Enter>', on_enter)

    download_button = tk.Button(root, text="Descargar", command=download_video, fg="white", bg="#7e3bb7", width=10)
    download_button.pack(pady=20, padx=26, side="right")
    download_button.bind('<Enter>', on_enter)
    download_button.bind('<Leave>', on_leave)

    root.mainloop()
    
show_menu_yt_tk()