import os
from PIL import Image

def remove_metadata_from_folder(folder_path):
    """
    Elimina los metadatos de las imágenes de una carpeta y guarda las copias en una nueva carpeta.
    :param folder_path: Ruta de la carpeta original con las imágenes.
    """
    try:
        # Verificar si la carpeta existe
        if not os.path.exists(folder_path):
            print("La carpeta especificada no existe.")
            return

        # Crear la carpeta de salida
        folder_name = os.path.basename(folder_path)
        output_folder = os.path.join(
            os.path.dirname(folder_path),
            f"sin metadatos {folder_name}"
        )
        os.makedirs(output_folder, exist_ok=True)

        # Procesar cada archivo en la carpeta
        for filename in os.listdir(folder_path):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)

            # Procesar solo archivos de imagen
            try:
                with Image.open(input_path) as img:
                    # Crear una copia sin metadatos
                    data = img.getdata()
                    clean_img = Image.new(img.mode, img.size)
                    clean_img.putdata(data)
                    clean_img.save(output_path)
                    print(f"Procesada: {filename}")
            except Exception as e:
                print(f"Error al procesar {filename}: {e}")

        print(f"Todas las imágenes procesadas. Las copias sin metadatos están en: {output_folder}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Pedir la ruta de la carpeta original
folder_path = input("Por favor, ingresa la ruta completa de la carpeta con las imágenes: ")

# Llamar a la función para procesar la carpeta
remove_metadata_from_folder(folder_path)
