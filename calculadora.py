#!/usr/bin/env python3
"""
Calculadora Gráfica con Imágenes
Usa tkinter para crear una interfaz gráfica con operaciones básicas representadas por imágenes
"""
import tkinter as tk
from PIL import Image, ImageTk
import ast
import operator

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
            except (FileNotFoundError, OSError) as e:
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
        """Calcula el resultado de la expresión de forma segura"""
        try:
            # Validar que solo contenga caracteres permitidos
            expresion_segura = self.expresion.strip()
            caracteres_permitidos = set('0123456789+-*/(). ')
            
            if not expresion_segura or not all(c in caracteres_permitidos for c in expresion_segura):
                raise ValueError("Expresión inválida")
            
            # Usar ast para evaluar de forma segura
            # ast.literal_eval no funciona para expresiones matemáticas, 
            # pero podemos usar eval con un entorno restringido
            resultado = self._evaluar_expresion_segura(expresion_segura)
            self.entrada_texto.set(str(resultado))
            self.expresion = str(resultado)
        except (ValueError, ZeroDivisionError, SyntaxError, NameError, TypeError) as e:
            self.entrada_texto.set("Error")
            self.expresion = ""
    
    def _evaluar_expresion_segura(self, expresion):
        """Evalúa una expresión matemática de forma segura"""
        # Permitir solo operaciones matemáticas básicas
        operadores_permitidos = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg,
        }
        
        def evaluar_nodo(nodo):
            if isinstance(nodo, ast.Constant):  # Número (Python 3.8+)
                return nodo.value
            elif isinstance(nodo, ast.Num):  # Número (compatibilidad con Python 3.7 y anterior)
                return nodo.n
            elif isinstance(nodo, ast.BinOp):  # Operación binaria
                op_func = operadores_permitidos.get(type(nodo.op))
                if op_func is None:
                    raise ValueError("Operador no permitido")
                return op_func(evaluar_nodo(nodo.left), evaluar_nodo(nodo.right))
            elif isinstance(nodo, ast.UnaryOp):  # Operación unaria
                op_func = operadores_permitidos.get(type(nodo.op))
                if op_func is None:
                    raise ValueError("Operador no permitido")
                return op_func(evaluar_nodo(nodo.operand))
            else:
                raise ValueError("Tipo de nodo no permitido")
        
        arbol = ast.parse(expresion, mode='eval')
        return evaluar_nodo(arbol.body)

def main():
    root = tk.Tk()
    calculadora = CalculadoraImagen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
