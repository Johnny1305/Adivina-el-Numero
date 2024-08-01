from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import Tk, Label, Button, Entry, Toplevel, messagebox, Frame, ttk, Text
from colorthief import ColorThief
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import random
import requests
from datetime import datetime
import time
import os
from io import BytesIO
import webbrowser
from PIL import UnidentifiedImageError

# ... Código del juego omitido ...

version_changes = [
    "🔰 Versión 1.0 (Fecha de lanzamiento: [21-07-2023]):\n- Implementación del juego 'Adivina el Número' con una interfaz gráfica simple.",
    "- El jugador debe adivinar un número secreto entre 1 y 100, con pistas sobre si el \nnúmero ingresado es demasiado alto o demasiado bajo.",
    "- El jugador tiene un total de 8 vidas para adivinar el número correcto.",
    "- Se incluye un menú de opciones con las siguientes funcionalidades:\n\t- Reiniciar el juego.\n\t- Acceder a redes sociales del desarrollador (LinkedIn, Twitter, Instagram).\n\t- Salir del juego.",
    "- Se incluye un menú de información con las siguientes funcionalidades:\n\t- Mostrar las instrucciones del juego.\n\t- Mostrar la versión actual del juego.",
    "- Se muestra un icono en la barra de título de la ventana, descargado desde una URL.",
    "- Se manejan errores al descargar la imagen del icono y al abrir imágenes no identificadas.",
    "- Se proporciona la versión y el nombre del desarrollador en el menú de información.",
    "- Se ofrece la opción de abrir enlaces de redes sociales desde el menú de opciones.\n\n"

    "🔰 Versión 1.1 (Fecha de lanzamiento: [NONE]):\n"
    "- Se agrega una barra de carga al iniciar el juego para una mejor experiencia visual.\n\n"
    "- Personalización del estilo de la ventana de inicio y la ventana de confirmación de salida.\n\n"
    "- Se implementa una confirmación de salida más minimalista y centrada en pantalla para \nevitar ventanas múltiples.\n\n"
    "- Mejora de la apariencia visual y la disposición de elementos en la ventana de inicio.\n\n"
    "- Se añade una imagen de fondo en la ventana de inicio para mejorar su aspecto estético.\n\n"
    "- Personalización del color de fondo de la ventana de inicio y la barra de carga.\n\n"
    "- La imagen de la ventana de inicio ahora tiene un efecto visual de zoom in/out al iniciar \nel juego.\n\n"
    "- Se actualiza la información de contacto del desarrollador en el menú de opciones.\n\n"
]

class JuegoAdivinarNumero:

    current_version = version_changes[-1].split(":")[0].strip()

    def show_version_changes(self):
        # Crear ventana emergente
        popup = Toplevel(self.ventana)
        popup.title("Cambios de versión")
        popup.geometry("750x300")
        popup.minsize(750, 300)
        popup.maxsize(750, 300)
        popup.resizable(False, False)
        
        # Widget de texto
        text_box = Text(popup)
        text_box.pack(fill="both", expand=True)

        # Agregar un scrollbar al widget Text
        scrollbar = Scrollbar(popup, command=text_box.yview)
        scrollbar.pack(side="right", fill="y")
        text_box.config(yscrollcommand=scrollbar.set)

        # Agregar los cambios de versión al widget Text
        text_box.insert("1.0", "HISTORIAL DE CAMBIOS:\n\n")
        for change in version_changes:
            text_box.insert("end", change + "\n\n")

        # Mostrar información adicional
        text_box.insert("end", "====================================================================\n")
        text_box.insert("end", "© " + datetime.now().strftime("%Y") + " - Adivina el Número\n")
        text_box.insert("end", "Developer: Johnny13\n")
        text_box.config(state="disabled")

    # Ventana emergente de versión
    def mostrar_version(self):
            global current_version

            # Personalizar el texto de la versión con colores
            about_window = Toplevel(self.ventana)
            about_window.title("Acerca de")
            about_window.geometry("600x200")
            about_window.resizable(False, False)

            # Personalizar el estilo de la ventana emergente
            about_window.configure(background="#D0D0D0")
            about_label = Label(about_window, text="Adivina el Número", font=("Helvetica", 12, "bold"),
                                bg="#D0D0D0", pady=10)
            about_label.pack()

            about_text = "Desarrollado por 'Johnny13'\n\n" \
                        "Descripción: El objetivo del juego es adivinar el número secreto.\n" \
                        "Contacto: jonathan.ramos.business@gmail.com\n\n" \
                        "Web: https://johnnyportfolio.x10.mx\n\n" \
                        f"© {datetime.now().strftime('%Y')}"

            about_info = Label(about_window, text=about_text, font=("Helvetica", 10), bg="#D0D0D0")
            about_info.pack()


    def mostrar_historia_principal(self):
        historia_principal = """
        ** Historia Principal **

En un rincón olvidado del mundo, un sombrío bosque se alza majestuosamente. 
Allí, en el corazón de la oscuridad,se encuentra la legendario Torre de los 
Números, un lugar temido y evitado por generaciones.

Cuentan las leyendas que la torre está protegida por un espíritu ancestral que ha atrapado un número demoníaco en su interior. Nadie sabe con certeza cómo es el número o cuál es su naturaleza, pero quien logre desafiarlo y 
adivinarlo será recompensado con un poder inimaginable.

Tú, valiente y audaz, has decidido enfrentar el desafío de la Torre de los Números. Emprenderás un viaje lleno de peligros y misterios para alcanzar 
la cima y desvelarel número demoníaco.

Pero cuidado, la torre no cederá fácilmente. Con cada intento, sentirás su presencia malévola y su risa burlona resonará en tu mente. Solo aquellos 
con determinación y astucia podrán enfrentar al número demoníaco y 
conquistar su poder.

¿Te atreves a adentrarte en la oscuridad y enfrentar el desafío de la 
Torre de los Números? 
Tu destino está en tus manos. 

¡Que comience la aventura!

        """
        popup_historia = Toplevel(self.ventana)
        popup_historia.title("Historia Principal")
        popup_historia.geometry("610x460")
        popup_historia.resizable(False, False)

        popup_historia.configure(background="#D0D0D0")
        historia_texto = Text(popup_historia)
        historia_texto.pack(fill="both", expand=True)
        historia_texto.insert("1.0", historia_principal)
        historia_texto.config(state="disabled")

        # Esperar a que se cierre la ventana emergente antes de continuar
        popup_historia.transient(self.ventana)
        popup_historia.grab_set()
        self.ventana.wait_window(popup_historia)

    def mostrar_historia_ganador(self, intentos):
        historia_ganador = f"""
            ** Historia Ganador **

El eco de tu último intento resonó en la tenebrosa torre mientras esperabas 
ansiosamente el resultado. La respuesta era inminente y sentías cómo el 
aire se volvía denso a tu alrededor.

El espíritu ancestral te miró fijamente a los ojos y pronunció una 
risa estruendosa.
"¡Correcto, intrépido aventurero! Has logrado desvelar el número demoníaco en {intentos} intentos."

En ese instante, una luz brillante llenó la habitación y la esencia del 
número demoníaco se liberó, concediéndote un poder inimaginable.

Con el número demoníaco en tu posesión, te convertiste en una leyenda viva, 
conocido en todo el reino como el valiente héroe que desafió la Torre de 
los Números y sobrevivió para contarlo.

La torre, ahora en paz, se hundió en la oscuridad, esperando a que otro 
valiente alma decidiera enfrentar su desafío en el futuro.

Tu nombre será recordado por siempre en los cuentos y canciones, y la 
leyenda de la Torre de los Números vivirá en la memoria de todos.

¡Enhorabuena, valiente aventurero, por tu triunfo en esta épica 
odisea numérica!

            """
        popup_historia_ganador = Toplevel()
        popup_historia_ganador.title("Historia Ganador")
        popup_historia_ganador.geometry("610x500")
        popup_historia_ganador.resizable(False, False)
            
        historia_texto_ganador = Text(popup_historia_ganador)
        historia_texto_ganador.pack(fill="both", expand=True)
        historia_texto_ganador.insert("1.0", historia_ganador)
        historia_texto_ganador.config(state="disabled")

    def mostrar_historia_perdedor(self):
        historia_perdedor = """
            ** Historia Perdedor **

Con cada intento fallido, la maldición de la Torre de los Números se hizo 
más fuerte.Sentías que el tiempo jugaba en tu contra mientras el número 
demoníaco se burlaba de tus esfuerzos.

Sin fuerzas para continuar, tus rodillas cedieron ante la oscuridad que 
rodeaba la torre. El espíritu ancestral emitió una risa malévola 
mientras tu valiente lucha llegaba a su fin.

Con lágrimas en los ojos y el corazón pesado, sabías que el número secreto 
permanecería oculto para siempre, y la maldición de la torre seguiría 
acechando a quienes osaran desafiarla.

Aunque tu valentía no fue recompensada con la victoria, tu nombre será 
recordado por aquellos que escuchen la trágica historia del valiente 
aventurero que se enfrentó a la Torre de los Números.

¡¡Que tu valiente espíritu descanse en paz, oh intrépido explorador!!.

            """
        popup_historia_perdedor = Toplevel()
        popup_historia_perdedor.title("Historia Perdedor")
        popup_historia_perdedor.geometry("610x360")
        popup_historia_perdedor.resizable(False, False)
            
        historia_texto_perdedor = Text(popup_historia_perdedor)
        historia_texto_perdedor.pack(fill="both", expand=True)
        historia_texto_perdedor.insert("1.0", historia_perdedor)
        historia_texto_perdedor.config(state="disabled")


    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = []
        self.numeros_ingresados = []
        self.vidas = 8
        
        self.ventana = tk.Tk()
        self.ventana.title("Adivina el Número || By Johnny13")
        self.ventana.configure(bg="#D0D0D0")
        self.current_version = version_changes[-1].split(":")[0].strip()
        # Ajustar el tamaño de la ventana
        self.ventana.geometry("500x450")
        self.ventana.resizable(False, False)  # Desactivar la redimensionabilidad de la ventana
        # Mostrar historia principal al iniciar el juego
        self.mostrar_historia_principal()
        # Descargar la imagen del icono desde la URL
        try:
            response = requests.get("https://i.imgur.com/jYH84kH.png")
            response.raise_for_status()  # Verificar si la descarga fue exitosa
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            self.icono = ImageTk.PhotoImage(image)
            self.ventana.iconphoto(True, self.icono)
        except requests.exceptions.RequestException as e:
            print("Error al descargar la imagen:", e)
        except UnidentifiedImageError as e:
            print("Error al abrir la imagen:", e)
        
        self.barra_herramientas = tk.Menu(self.ventana)
        self.ventana.config(menu=self.barra_herramientas)
        
        # Resto del código sin cambios...
        self.opciones_menu = tk.Menu(self.barra_herramientas, tearoff=0)
        self.barra_herramientas.add_cascade(label="Opciones", menu=self.opciones_menu)
        self.opciones_menu.add_command(label="🔄 Reiniciar juego", command=self.reiniciar_juego)
        self.opciones_menu.add_command(label="📋 Historia", command=self.mostrar_historia_principal)
        self.opciones_menu.add_separator()

        self.redes_sociales_menu = tk.Menu(self.opciones_menu, tearoff=0)
        self.opciones_menu.add_cascade(label="🌐 Redes Sociales", menu=self.redes_sociales_menu)
        self.redes_sociales_menu.add_command(label="LinkedIn", command=lambda: self.abrir_red_social("https://www.linkedin.com/in/johnny13/"))
        self.redes_sociales_menu.add_command(label="Twitter", command=lambda: self.abrir_red_social("https://twitter.com/Johnnyr1345"))
        self.redes_sociales_menu.add_command(label="Instagram", command=lambda: self.abrir_red_social("https://www.instagram.com/johnny13.htb"))

        self.opciones_menu.add_separator()
        self.opciones_menu.add_command(label="❌ Salir", command=self.confirmar_salida)
        

        self.info_menu = tk.Menu(self.barra_herramientas, tearoff=0)
        self.barra_herramientas.add_cascade(label="Info", menu=self.info_menu)
        self.info_menu.add_command(label="📋 Instrucciones", command=self.mostrar_instrucciones)
        self.info_menu.add_separator()
        self.info_menu.add_command(label="🔰 Historial Versiones", command=self.show_version_changes)
        self.info_menu.add_command(label="🔰 Acerca de", command=self.mostrar_version)

        


        self.titulo = tk.Label(self.ventana, text="Adivina el Número", font=("Arial", 24, "bold"), bg="#D0D0D0", fg="#2C3E50")
        self.titulo.pack(pady=20)
        
        self.etiqueta = tk.Label(self.ventana, text="Ingresa un número entre 1 y 100:", font=("Arial", 14), bg="#D0D0D0")
        self.etiqueta.pack(pady=10)
        
        self.entrada = tk.Entry(self.ventana, font=("Arial", 14), width=5)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.verificar_numero_enter)
        
        self.vidas_frame = tk.Frame(self.ventana, bg="#D0D0D0")
        self.vidas_frame.pack(pady=5)
        self.vidas_iconos = []
        self.font_awesome = font.Font(family="Arial", size=24)
        self.actualizar_vidas()

        self.boton = tk.Button(self.ventana, text="Adivinar", font=("Arial", 14), bg="#FF5722", fg="#FDFEFE", relief="raised", command=self.verificar_numero)
        self.boton.pack(pady=10)
        
        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 14), bg="#D0D0D0")
        self.resultado.pack(pady=10)
        
        self.numeros_label = tk.Label(self.ventana, text="Números ingresados:", font=("Arial", 14), bg="#D0D0D0")
        self.numeros_label.pack(pady=10)
        
        self.numeros_ingresados_label = tk.Label(self.ventana, text="", font=("Arial", 14), bg="#D0D0D0")
        self.numeros_ingresados_label.pack(pady=10)

        self.ventana.protocol("WM_DELETE_WINDOW", self.confirmar_salida)
        
    # Resto del código sin cambios...

    def verificar_numero(self):
        intento = self.entrada.get().strip()
        if intento:
            if intento.isdigit():
                intento = int(intento)
                if 1 <= intento <= 100:
                    self.verificar_numero_ingresado(intento)
                else:
                    self.resultado["text"] = "El número debe estar entre 1 y 100."
            else:
                self.resultado["text"] = "Debes ingresar un número válido."
        else:
            self.resultado["text"] = "Debes ingresar un número antes de adivinar."
        
    def verificar_numero_enter(self, event):
        self.verificar_numero()
        
    def verificar_numero_ingresado(self, intento):
        if intento in self.numeros_ingresados:
            self.resultado["text"] = "Ya ingresaste ese número. Intenta con otro."
            self.entrada.delete(0, "end")
        else:
            self.intentos.append(intento)
            self.numeros_ingresados.append(intento)
            
            if intento < self.numero_secreto:
                self.resultado["text"] = "Demasiado bajo. Intenta nuevamente."
                self.actualizar_vidas()
                self.entrada.delete(0, "end")
            elif intento > self.numero_secreto:
                self.resultado["text"] = "Demasiado alto. Intenta nuevamente."
                self.actualizar_vidas()
                self.entrada.delete(0, "end")
            else:
                self.resultado["text"] = f"¡Felicitaciones! ¡Adivinaste el número en {len(self.intentos)} intentos!"
                self.boton["state"] = "disabled"  # Desactivar el botón después de adivinar correctamente
                self.entrada["state"] = "disabled"  # Desactivar la entrada después de adivinar correctamente
                # Mostrar historia ganador
                self.mostrar_historia_ganador(len(self.intentos))
                # Añadir efecto de destello al resultado
                self.destello_resultado()
                # Añadir animación al mostrar el número secreto
                self.animacion_numero_secreto()
        
        self.actualizar_numeros_ingresados()
        
    def actualizar_numeros_ingresados(self):
        numeros_texto = ", ".join(map(str, self.numeros_ingresados))
        self.numeros_ingresados_label["text"] = numeros_texto
        
    def actualizar_vidas(self):
        if self.vidas > 0:
            self.vidas -= 1
            for icono in self.vidas_iconos:
                icono.destroy()
            self.vidas_iconos = []
            for _ in range(self.vidas):
                icono = tk.Label(self.vidas_frame, text="\u2764", font=self.font_awesome, bg="#D0D0D0", fg="#FF0000")
                icono.pack(side="left", padx=2)
                self.vidas_iconos.append(icono)
            
            if self.vidas == 0:
                self.boton["state"] = "disabled"
                self.entrada["state"] = "disabled"
                self.resultado["text"] = f"¡Perdiste! El número secreto era {self.numero_secreto}."
                self.mostrar_historia_perdedor()

    def animacion_numero_secreto(self):
        for _ in range(3):
            self.resultado.config(text=f"¡Número secreto: {self.numero_secreto}!", fg="#FF5722")
            self.ventana.update()
            self.ventana.after(800)
            self.resultado.config(text=f"¡Número secreto: {self.numero_secreto}!", fg="#2C3E50")
            self.ventana.update()
            self.ventana.after(800)
        self.resultado.config(text="", fg="#2C3E50")

    def destello_resultado(self):
        for _ in range(5):
            self.resultado.config(fg="green")
            self.ventana.update()
            self.ventana.after(100)
            self.resultado.config(fg="#2C3E50")
            self.ventana.update()
            self.ventana.after(100)


    def reiniciar_juego(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = []
        self.numeros_ingresados = []
        self.vidas = 8
        self.boton["state"] = "disabled"
        self.entrada["state"] = "disabled"
        self.resultado["text"] = ""
        self.numeros_ingresados_label["text"] = ""
        for icono in self.vidas_iconos:
            icono.destroy()
        self.vidas_iconos = []
        # Limpiar la entrada al reiniciar el juego
        self.entrada.delete(0, "end")
        self.actualizar_vidas()
        self.animacion_reinicio()
        self.boton["state"] = "normal"
        self.entrada["state"] = "normal"
        self.entrada.delete(0, "end")
        # Añadir efecto de parpadeo al botón "Adivinar" al reiniciar el juego
        self.efecto_parpadeo_boton()

    def efecto_parpadeo_boton(self):
        for _ in range(4):
            self.boton.config(fg="#FF5722")
            self.ventana.update()
            self.ventana.after(200)
            self.boton.config(fg="#FDFEFE")
            self.ventana.update()
            self.ventana.after(200)
        self.boton.config(fg="#FDFEFE")

    def animacion_reinicio(self):
        for _ in range(3):
            self.resultado.config(text="¡Reiniciando!", fg="#FF5722")
            self.ventana.update()
            self.ventana.after(500)
            self.resultado.config(text="¡Reiniciando!", fg="#2C3E50")
            self.ventana.update()
            self.ventana.after(500)
        self.resultado.config(text="", fg="#2C3E50")

    def mostrar_instrucciones(self):
        instrucciones = """
Bienvenido al Juego de Adivinar Número.

El objetivo del juego es adivinar el número secreto que se encuentra entre 1 y 100.

Después de cada intento, recibirás una pista para indicarte si el número es demasiado alto o demasiado bajo.

Tienes un total de 8 vidas para adivinar el número correcto.

Cada vez que te equivoques, perderás una vida.

Intenta adivinar el número en la menor cantidad de intentos posibles.


¡Buena suerte y diviértete!
"""
        messagebox.showinfo("Instrucciones", instrucciones)

    def abrir_red_social(self, url):
        webbrowser.open(url)

    def confirmar_salida(self):
        confirmar = messagebox.askokcancel("Confirmar Salida",
                                           "¿Estás seguro de que quieres salir del juego?",
                                           icon=messagebox.QUESTION,
                                           default=messagebox.CANCEL,
                                           parent=self.ventana,)

        if confirmar:
            self.ventana.destroy()
        
    def iniciar(self):
        self.ventana.mainloop()

class PantallaInicio:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Adivina el Número")
        self.parent.geometry("500x400")
        self.parent.resizable(False, False)

        # Color de fondo #D0D0D0
        self.color_fondo = "#D0D0D0"
        self.color_boton = "#FF5722"
        self.color_texto_titulo = "#2C3E50"
        self.color_texto_instrucciones = "#34495E"

        # Fuentes
        self.font_titulo = font.Font(family="Arial", size=20, weight="bold")
        self.font_instrucciones = font.Font(family="Arial", size=14)

        # Widgets
        self.titulo = Label(parent, text="Adivina el Número", font=self.font_titulo, fg=self.color_texto_titulo, bg=self.color_fondo)
        self.titulo.pack(pady=30)

        # Cargar el icono desde Internet
        try:
            response = requests.get("https://i.imgur.com/jYH84kH.png")  # Reemplaza esta URL con la URL de la imagen del icono
            response.raise_for_status()
            icono_data = response.content
            icono = Image.open(BytesIO(icono_data))
            self.icono = ImageTk.PhotoImage(icono)
            self.parent.iconphoto(False, self.icono)  # Establecer el icono de la ventana
        except requests.exceptions.RequestException as e:
            print("Error al descargar el icono:", e)
        except Exception as e:
            print("Error al cargar el icono:", e)

        # Cargar la imagen desde Internet y redimensionarla
        try:
            response = requests.get("https://i.imgur.com/jYH84kH.png")
            response.raise_for_status()
            imagen_data = response.content
            imagen = Image.open(BytesIO(imagen_data))
            imagen = imagen.resize((100, 100), Image.LANCZOS)
            self.imagen = ImageTk.PhotoImage(imagen)
            self.label_imagen = Label(parent, image=self.imagen, bg=self.color_fondo)
            self.label_imagen.pack(pady=20)
        except requests.exceptions.RequestException as e:
            print("Error al descargar la imagen:", e)
        except Exception as e:
            print("Error al cargar la imagen:", e)

        self.instrucciones = Label(parent, text="Haz clic en el botón para comenzar el juego", font=self.font_instrucciones, fg=self.color_texto_instrucciones, bg=self.color_fondo)
        self.instrucciones.pack(pady=10)

        self.boton_comenzar = Button(parent, text="Comenzar Juego", font=self.font_instrucciones, bg=self.color_boton, fg=self.color_fondo, relief="raised", bd=0, command=self.comenzar_juego)
        self.boton_comenzar.pack(pady=10, padx=20, ipadx=10, ipady=5)

        self.parent.protocol("WM_DELETE_WINDOW", self.confirmar_salida)


    def confirmar_salida(self):
        confirmar = messagebox.askokcancel("Confirmar Salida",
                                           "¿Estás seguro de que quieres salir del juego?",
                                           icon=messagebox.QUESTION,
                                           default=messagebox.CANCEL,
                                           parent=self.parent,)

        if confirmar:
            self.parent.destroy()

    def comenzar_juego(self):
        # Desactivar el botón para evitar múltiples clics durante la carga
        self.boton_comenzar.config(state="disabled")

        # Ocultar el botón y mostrar la barra de carga personalizada
        self.boton_comenzar.pack_forget()

        # Definir el estilo personalizado para la barra de carga
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Custom.Horizontal.TProgressbar", troughcolor=self.color_fondo, background="#FF0000", thickness=10)

        self.barra_carga = ttk.Progressbar(self.parent, length=200, mode="determinate", style="Custom.Horizontal.TProgressbar")
        self.barra_carga.pack(pady=30)

        # Simular la carga del juego con un bucle
        for i in range(10):
            time.sleep(0.5)
            self.parent.update()
            self.barra_carga['value'] = (i + 1) * 10
        time.sleep(3)

        # Eliminar la barra de carga
        self.barra_carga.pack_forget()

        # Volver a mostrar el botón
        self.boton_comenzar.pack(pady=10, padx=20, ipadx=10, ipady=5)
        self.boton_comenzar.config(state="normal")

        # Cerrar la pantalla de inicio
        self.parent.destroy()

        # Iniciar el juego principal
        juego = JuegoAdivinarNumero()
        juego.iniciar()

if __name__ == "__main__":
    ventana_inicio = Tk()
    ventana_inicio.configure(bg="#D0D0D0")  # Establecer el color de fondo de la ventana
    pantalla_inicio = PantallaInicio(ventana_inicio)
    ventana_inicio.mainloop()
