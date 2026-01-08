#!/usr/bin/env python3
"""Script para crear las imágenes de las operaciones matemáticas"""
from PIL import Image, ImageDraw, ImageFont

def crear_imagen_operacion(texto, nombre_archivo, color_fondo=(255, 200, 100)):
    """Crea una imagen simple con el símbolo de la operación"""
    # Crear imagen de 60x60 píxeles
    img = Image.new('RGB', (60, 60), color_fondo)
    draw = ImageDraw.Draw(img)
    
    # Intentar usar una fuente grande, si no está disponible usar la predeterminada
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Calcular posición para centrar el texto
    bbox = draw.textbbox((0, 0), texto, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((60 - text_width) / 2, (60 - text_height) / 2 - 5)
    
    # Dibujar el texto
    draw.text(position, texto, fill=(0, 0, 0), font=font)
    
    # Guardar la imagen
    img.save(nombre_archivo)
    print(f"Imagen creada: {nombre_archivo}")

if __name__ == "__main__":
    # Crear las imágenes para cada operación
    crear_imagen_operacion("+", "suma.png", (144, 238, 144))  # Verde claro
    crear_imagen_operacion("-", "resta.png", (255, 182, 193))  # Rosa claro
    crear_imagen_operacion("×", "multiplicacion.png", (173, 216, 230))  # Azul claro
    crear_imagen_operacion("÷", "division.png", (255, 218, 185))  # Melocotón
    print("¡Todas las imágenes han sido creadas!")
