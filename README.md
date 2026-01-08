# Calculadora Gráfica con Imágenes

Una calculadora gráfica desarrollada en Python usando tkinter, que utiliza imágenes personalizadas para representar las operaciones matemáticas básicas.

## Características

- **Interfaz gráfica intuitiva**: Diseño limpio y fácil de usar con tkinter
- **Área de entrada**: Muestra los números y el resultado de las operaciones
- **Botones numéricos**: Dígitos del 0 al 9
- **Operaciones con imágenes**: 
  - Suma (+) - Icono verde
  - Resta (-) - Icono rosa
  - Multiplicación (×) - Icono azul
  - División (÷) - Icono naranja
- **Botón C**: Limpia toda la expresión (color rojo)
- **Botón =**: Calcula el resultado (color verde)

## Requisitos

- Python 3.x
- tkinter (generalmente viene instalado con Python)
- Pillow (PIL) para manejar las imágenes

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/mgodoyvargas20/calculadora-imagen.git
cd calculadora-imagen
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```
O manualmente:
```bash
pip install Pillow
```

3. (Opcional) Generar las imágenes de las operaciones:
```bash
python3 crear_imagenes.py
```
*Nota: Las imágenes ya están incluidas en el repositorio*

## Uso

Ejecutar la calculadora:
```bash
python3 calculadora.py
```

### Cómo usar la calculadora:

1. Haz clic en los números para ingresarlos
2. Haz clic en una imagen de operación (+, -, ×, ÷)
3. Ingresa otro número
4. Presiona el botón "=" para ver el resultado
5. Usa el botón "C" para borrar y empezar de nuevo

## Estructura del Proyecto

```
calculadora-imagen/
├── .gitignore             # Archivos a excluir del control de versiones
├── calculadora.py          # Aplicación principal de la calculadora
├── crear_imagenes.py       # Script para generar las imágenes de operaciones
├── suma.png               # Imagen del botón de suma
├── resta.png              # Imagen del botón de resta
├── multiplicacion.png     # Imagen del botón de multiplicación
├── division.png           # Imagen del botón de división
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```

## Capturas de Pantalla

![Calculadora en funcionamiento](https://github.com/user-attachments/assets/6b5ddbd0-8957-454a-a1d6-8d3d9ac9795f)

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.