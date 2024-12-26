from PIL import Image

def remove_metadata(image_path, output_path):
    """
    Elimina los metadatos de una imagen y guarda una copia sin metadatos.
    :param image_path: Ruta de la imagen original.
    :param output_path: Ruta donde se guardará la nueva imagen.
    """
    try:
        # Abrir la imagen
        with Image.open(image_path) as img:
            # Crear una copia sin metadatos
            data = img.getdata()
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(data)
            
            # Guardar la nueva imagen sin metadatos
            clean_img.save(output_path)
            print(f"Imagen sin metadatos guardada en: {output_path}")
    except FileNotFoundError:
        print("La ruta especificada no es válida o el archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Pedir al usuario las rutas de la imagen original y el archivo de salida
image_path = input("Por favor, ingresa la ruta completa de la imagen original: ")
output_path = input("Por favor, ingresa la ruta completa para guardar la nueva imagen: ")

# Llamar a la función para eliminar los metadatos
remove_metadata(image_path, output_path)
