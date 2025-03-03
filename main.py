import tkinter as tk
from tkinter import filedialog, messagebox
from buscador_palabra_word import *
from formulario_datos import VentanaFormulario
import datos_centrales


def ejecutar_cambios():
    """
    Función intermedia que pasa los argumentos necesarios desde datos_centrales
    a buscar_y_reemplazar_en_word.
    """
    # Verifica que se haya seleccionado un archivo y creado un diccionario
    import datos_centrales
    print("Contenido de datos_centrales antes de ejecutar cambios:")
    print("Archivo Word:", datos_centrales.archivo_word)
    print("Diccionario:", datos_centrales.diccionario_completo)

    if not datos_centrales.archivo_word:
        print("Error: No se ha seleccionado un archivo Word.")
        messagebox.showinfo("INFORMACIÓN",
                            "No se ha realizado ningún cambio por")
        return

    if not datos_centrales.diccionario_completo:
        print("Error: El diccionario está vacío.")
        messagebox.showinfo("INFORMACIÓN",
                            "No se ha realizado ningún cambio")
        return

    # Llama a la función con los datos desde datos_centrales
    buscar_y_reemplazar_en_word(
        datos_centrales.archivo_word, datos_centrales.diccionario_completo)


def crear_interfaz():
    """
    Crea una interfaz gráfica básica para coordinar las funciones de los módulos.
    """
    ventana = tk.Tk()
    ventana.title("Gestor de Reemplazo en Word")
    ventana.geometry("400x400")

    # Etiqueta de bienvenida
    label_bienvenida = tk.Label(
        ventana, text="Bienvenido al Gestor de Reemplazo en Word", font=("Arial", 12))
    label_bienvenida.pack(pady=10)

    def seleccionar_word():
        archivo_seleccionado = filedialog.askopenfilename(
            title="Seleccionar archivo Word",
            filetypes=[("Archivos Word", "*.docx")]
        )

        if archivo_seleccionado:
            datos_centrales.archivo_word = archivo_seleccionado
            print(f"Archivo seleccionado: {datos_centrales.archivo_word}")
            tk.messagebox.showinfo(
                "Éxito", "El archivo ha sido seleccionado correctamente.")
        else:
            print("No se seleccionó ningún archivo.")
            tk.messagebox.showinfo(
                "Fracaso", "El archivo no ha sido seleccionado MAMAHUEVO.")

    # Botón para elegir el archivo word (donde vamos aplicar los cambios)
    boton_elegir_word = tk.Button(ventana, text="Elegir el archivo Word", font=(
        "Arial", 10), command=seleccionar_word)
    boton_elegir_word.pack(pady=20)

    # Botón para crear el diccionario (vamos a colocar las palabras que queremos sustituir)
    boton_crear_diccionario = tk.Button(ventana, text="Crear Diccionario", font=(
        "Arial", 10), command=VentanaFormulario)
    boton_crear_diccionario.pack(pady=20)

    # Botón para aplicar el diccionario creado en el word seleccionado
    boton_aplicar_cambios = tk.Button(ventana, text="Ejecutar cambios", font=(
        "Arial", 10), command=ejecutar_cambios)
    boton_aplicar_cambios.pack(pady=20)

    # Botón para salir
    boton_salir = tk.Button(ventana, text="Salir", font=(
        "Arial", 10), command=ventana.destroy)
    boton_salir.pack(pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    crear_interfaz()
