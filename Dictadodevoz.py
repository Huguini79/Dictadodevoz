import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import speech_recognition as sr
import pyautogui
import time

root = tk.Tk()
root.configure(bg='yellow')
root.geometry('660x550')
root.title('Dictado de voz')
root.iconbitmap('microfono.ico')

def activar_dictado_de_voz():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as fuente:
            messagebox.showinfo('Mensaje', 'Cuando presiones OK, habla para activar el dictado de voz.')
            
            audio = r.listen(fuente)
            messagebox.showinfo('Mensaje', 'Ok, cuando le des click al mensaje, tendrás que esperar tres segundos para que el programa pueda escribir el texto de la voz.')
            
            texto_de_audio = r.recognize_google(audio, language="es-ES")  # Idioma español
            time.sleep(3)
            pyautogui.write(texto_de_audio)  # Escribe el texto detectado
            
    except sr.UnknownValueError:
        messagebox.showerror('Error', 'No se pudo entender el audio.')
    except sr.RequestError as e:
        messagebox.showerror('Error', f'Error de conexión al servicio: {e}')
    except Exception as e:
        messagebox.showerror('Error', f'Ocurrió un error inesperado: {e}')

img = Image.open('microfono.png')
img = img.resize((123, 80))
img = ImageTk.PhotoImage(img)
tk.Label(root, text='Dictado de voz', wraplength=200, bg='yellow').grid(row=0, column=0, padx=10, pady=10)
botón_micrófono = tk.Button(root, image=img, command=activar_dictado_de_voz)
botón_micrófono.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()