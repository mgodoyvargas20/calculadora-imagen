#!/usr/bin/env python3
"""
Calculadora Gráfica con Imágenes
Usa tkinter para crear una interfaz gráfica con operaciones básicas representadas por imágenes
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class CalculadoraImagen:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora con Imágenes")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # Variables para la calculadora
        self.expresion = ""
        self.entrada_texto = tk.StringVar()
        
        # Crear la interfaz
        self.crear_display()
        self.crear_botones()
        
    def crear_display(self):
        """Crea el área de entrada para mostrar números y resultados"""
        frame_display = tk.Frame(self.root, bd=5, relief=tk.RIDGE)
        frame_display.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
        
        entrada = tk.Entry(
            frame_display,
            textvariable=self.entrada_texto,
            font=('Arial', 24, 'bold'),
            bd=10,
            insertwidth=4,
            width=14,
            justify='right',
            state='readonly',
            readonlybackground='white',
            fg='black'
        )
        entrada.pack(ipady=20)
        
    def crear_botones(self):
        """Crea todos los botones de la calculadora"""
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Cargar imágenes para las operaciones
        self.imagenes = self.cargar_imagenes()
        
        # Configuración de botones
        botones = [
            ['7', '8', '9', 'division'],
            ['4', '5', '6', 'multiplicacion'],
            ['1', '2', '3', 'resta'],
            ['C', '0', '=', 'suma']
        ]
        
        # Crear los botones
        for i, fila in enumerate(botones):
            for j, boton in enumerate(fila):
                if boton in ['suma', 'resta', 'multiplicacion', 'division']:
                    # Botón con imagen
                    btn = tk.Button(
                        frame_botones,
                        image=self.imagenes[boton],
                        bd=5,
                        relief=tk.RAISED,
                        command=lambda b=boton: self.click_operacion(b)
                    )
                elif boton == 'C':
                    # Botón borrar
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=('Arial', 18, 'bold'),
                        bd=5,
                        relief=tk.RAISED,
                        bg='#ff6b6b',
                        fg='white',
                        command=self.borrar
                    )
                elif boton == '=':
                    # Botón igual
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=('Arial', 18, 'bold'),
                        bd=5,
                        relief=tk.RAISED,
                        bg='#4CAF50',
                        fg='white',
                        command=self.calcular
                    )
                else:
                    # Botones de dígitos
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=('Arial', 18, 'bold'),
                        bd=5,
                        relief=tk.RAISED,
                        bg='#f0f0f0',
                        command=lambda b=boton: self.click_digito(b)
                    )
                
                btn.grid(row=i, column=j, sticky='nsew', padx=5, pady=5)
        
        # Configurar el peso de las filas y columnas para que se expandan uniformemente
        for i in range(4):
            frame_botones.grid_rowconfigure(i, weight=1)
            frame_botones.grid_columnconfigure(i, weight=1)
    
    def cargar_imagenes(self):
        """Carga las imágenes de las operaciones"""
        imagenes = {}
        operaciones = {
            'suma': 'suma.png',
            'resta': 'resta.png',
            'multiplicacion': 'multiplicacion.png',
            'division': 'division.png'
        }
        
        for operacion, archivo in operaciones.items():
            try:
                img = Image.open(archivo)
                img = img.resize((60, 60), Image.Resampling.LANCZOS)
                imagenes[operacion] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error cargando {archivo}: {e}")
                # Crear una imagen por defecto si falla
                imagenes[operacion] = None
        
        return imagenes
    
    def click_digito(self, digito):
        """Maneja el click en un botón de dígito"""
        self.expresion += str(digito)
        self.entrada_texto.set(self.expresion)
    
    def click_operacion(self, operacion):
        """Maneja el click en un botón de operación"""
        if self.expresion and self.expresion[-1] not in ['+', '-', '*', '/']:
            simbolos = {
                'suma': '+',
                'resta': '-',
                'multiplicacion': '*',
                'division': '/'
            }
            self.expresion += simbolos[operacion]
            self.entrada_texto.set(self.expresion)
    
    def borrar(self):
        """Borra toda la expresión"""
        self.expresion = ""
        self.entrada_texto.set("")
    
    def calcular(self):
        """Calcula el resultado de la expresión"""
        try:
            # Usar eval de forma segura, validando que solo contenga operadores permitidos
            # Solo permite números, operadores matemáticos básicos y espacios
            expresion_segura = self.expresion.strip()
            caracteres_permitidos = set('0123456789+-*/(). ')
            
            if not expresion_segura or not all(c in caracteres_permitidos for c in expresion_segura):
                raise ValueError("Expresión inválida")
            
            # Evaluar la expresión matemática
            resultado = str(eval(expresion_segura))
            self.entrada_texto.set(resultado)
            self.expresion = resultado
        except (ValueError, ZeroDivisionError, SyntaxError, NameError) as e:
            self.entrada_texto.set("Error")
            self.expresion = ""

def main():
    root = tk.Tk()
    calculadora = CalculadoraImagen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
