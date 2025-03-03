import tkinter as tk
from tkinter import messagebox
import datos_centrales


class VentanaFormulario:
    def __init__(self):
        # este diccionario lo hemos creado ahora, no confundir con diccionario de datos centrales.
        self.diccionario = {}

        self.crear_ventana()

    def guardar_datos(self):
        """
        Recoge los datos ingresados en los widgets y los guarda en un diccionario.
        Luego cierra la ventana.
        """

        """En self.diccionario también debemos hacer las modificaciones necesarias si queremos cambiar
        las palabras a sustiuir en el word"""

        self.diccionario = {
            "(FECHA_ACCIDENTE)": self.entrada_fecha_accidente.get(),
            "(FECHA_NACIMIENTO)": self.entrada_fecha_nacimiento.get(),
            "(DNI_TABLA)": self.entrada_dni_tabla.get(),
            "(NOMBRE1)": self.entrada_nombre1.get(),
            "(EDAD_TABLA)": self.entrada_edad_tabla.get(),
            "(PROFESION_TABLA)": self.entrada_profesion_tabla.get(),
            "(NUM_FICHA)": self.entrada_num_ficha.get(),
            "(NOMBRE2)": self.entrada_nombre2.get(),
            "(PERDIDA_CALIDAD_VIDA)": self.entrada_perdida_calidad_vida.get(),
            "(DIAS_BAJA_TOTAL)": self.entrada_dias_baja_total.get(),
            "(DIAS_BAJA_MODERADA)": self.entrada_dias_baja_moderada.get(),
            "(DIAS_BAJA_BASICA)": self.entrada_dias_baja_basica.get(),
            "(FECHA_INFORME)": self.entrada_fecha_informe.get()}

        # Validar campos vacíos
        campos_vacios = [k for k, v in self.diccionario.items() if not v]
        if campos_vacios:
            messagebox.showwarning("Advertencia", f"Por favor, rellena los siguientes campos: {
                                   ', '.join(campos_vacios)}")
            return

        # Guardar el diccionario en datos_centrales
        datos_centrales.diccionario_completo = self.diccionario

        # Imprimir el diccionario y cerrar la ventana
        print(f"Datos guardados en diccionario: {self.diccionario}")
        self.ventana.destroy()  # Cierra la ventana

    def crear_ventana(self):
        """
        Crea la ventana de entrada de datos con todos los widgets.
        (Aquí se pueden hacer las modificaciones para cambiar las palabras que queremos buscar y 
        sustituir para luego crear el diccionario de búsqueda)
        """
        self.ventana = tk.Tk()
        self.ventana.title("Ingresar Datos")

        # Configurar widgets
        tk.Label(self.ventana, text="Fecha de Nacimiento (dd/mm/yyyy):").grid(row=0,
                                                                              column=0, padx=10, pady=5)
        self.entrada_fecha_nacimiento = tk.Entry(self.ventana, width=30)
        self.entrada_fecha_nacimiento.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Fecha de Accidente (dd/mm/yyyy):").grid(row=1,
                                                                             column=0, padx=10, pady=5)
        self.entrada_fecha_accidente = tk.Entry(self.ventana, width=30)
        self.entrada_fecha_accidente.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="DNI Tabla:").grid(
            row=2, column=0, padx=10, pady=5)
        self.entrada_dni_tabla = tk.Entry(self.ventana, width=30)
        self.entrada_dni_tabla.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Nombre 1:").grid(
            row=3, column=0, padx=10, pady=5)
        self.entrada_nombre1 = tk.Entry(self.ventana, width=30)
        self.entrada_nombre1.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Edad Tabla:").grid(
            row=4, column=0, padx=10, pady=5)
        self.entrada_edad_tabla = tk.Entry(self.ventana, width=30)
        self.entrada_edad_tabla.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Profesión Tabla:").grid(
            row=5, column=0, padx=10, pady=5)
        self.entrada_profesion_tabla = tk.Entry(self.ventana, width=30)
        self.entrada_profesion_tabla.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Número de Ficha:").grid(
            row=6, column=0, padx=10, pady=5)
        self.entrada_num_ficha = tk.Entry(self.ventana, width=30)
        self.entrada_num_ficha.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Nombre 2:").grid(
            row=7, column=0, padx=10, pady=5)
        self.entrada_nombre2 = tk.Entry(self.ventana, width=30)
        self.entrada_nombre2.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Pérdida de Calidad de Vida:").grid(
            row=8, column=0, padx=10, pady=5)
        self.entrada_perdida_calidad_vida = tk.Entry(self.ventana, width=30)
        self.entrada_perdida_calidad_vida.grid(
            row=8, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Días Baja Total:").grid(
            row=9, column=0, padx=10, pady=5)
        self.entrada_dias_baja_total = tk.Entry(self.ventana, width=30)
        self.entrada_dias_baja_total.grid(row=9, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Días Baja Moderada:").grid(
            row=10, column=0, padx=10, pady=5)
        self.entrada_dias_baja_moderada = tk.Entry(self.ventana, width=30)
        self.entrada_dias_baja_moderada.grid(row=10, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Días Baja Básica:").grid(
            row=11, column=0, padx=10, pady=5)
        self.entrada_dias_baja_basica = tk.Entry(self.ventana, width=30)
        self.entrada_dias_baja_basica.grid(row=11, column=1, padx=10, pady=5)

        tk.Label(self.ventana, text="Fecha de Informe (dd/mm/yyyy):").grid(row=12,
                                                                           column=0, padx=10, pady=5)
        self.entrada_fecha_informe = tk.Entry(self.ventana, width=30)
        self.entrada_fecha_informe.grid(row=12, column=1, padx=10, pady=5)

        # Botón para guardar
        tk.Button(self.ventana, text="Guardar", command=self.guardar_datos).grid(
            row=13, column=0, columnspan=2, padx=10, pady=10)

        # Ejecutar la ventana
        self.ventana.mainloop()


# Crear y ejecutar la ventana
if __name__ == "__main__":
    formulario = VentanaFormulario()
    print("Diccionario final:", formulario.diccionario)
