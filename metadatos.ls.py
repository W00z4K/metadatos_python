from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_metadata(image_path):
    """
    Extrae metadatos seleccionados de una imagen.
    :param image_path: Ruta de la imagen.
    :return: Diccionario con los metadatos deseados.
    """
    try:
        # Abre la imagen y extrae los datos EXIF
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if not exif_data:
            return "No EXIF data found."
        
        metadata = {}
        gps_data = {}
        
        # Mapea las etiquetas EXIF a nombres legibles
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            # Filtrar los campos necesarios
            if tag_name == "Make":
                metadata["Fabricante"] = value
            elif tag_name == "Model":
                metadata["Modelo"] = value
            elif tag_name == "Software":
                metadata["Software"] = value
            elif tag_name == "DateTime":
                metadata["Fecha y hora"] = value
            elif tag_name == "ExifImageWidth":
                metadata["Resolución Ancho"] = value
            elif tag_name == "ExifImageHeight":
                metadata["Resolución Alto"] = value
            elif tag_name == "GPSInfo":
                for gps_tag_id, gps_value in value.items():
                    gps_tag_name = GPSTAGS.get(gps_tag_id, gps_tag_id)
                    gps_data[gps_tag_name] = gps_value
        
        # Procesar la información GPS si está disponible
        if gps_data:
            def convert_to_degrees(value):
                d, m, s = value
                return d + (m / 60.0) + (s / 3600.0)
            
            if "GPSLatitude" in gps_data and "GPSLatitudeRef" in gps_data:
                lat = convert_to_degrees(gps_data["GPSLatitude"])
                if gps_data["GPSLatitudeRef"] != "N":
                    lat = -lat
                metadata["Latitud"] = lat
            
            if "GPSLongitude" in gps_data and "GPSLongitudeRef" in gps_data:
                lon = convert_to_degrees(gps_data["GPSLongitude"])
                if gps_data["GPSLongitudeRef"] != "E":
                    lon = -lon
                metadata["Longitud"] = lon
            
            if "Latitud" in metadata and "Longitud" in metadata:
                metadata["Google Maps Link"] = (
                    f"https://www.google.com/maps?q={metadata['Latitud']},{metadata['Longitud']}"
                )
        
        return metadata
    
    except FileNotFoundError:
        return "La ruta especificada no es válida o el archivo no existe."

# Pedir la ruta de la imagen al usuario
image_path = input("Por favor, ingresa la ruta completa de la imagen: ")

# Extraer y mostrar los metadatos
metadatos = extract_metadata(image_path)
if isinstance(metadatos, str):
    print(metadatos)
else:
    for clave, valor in metadatos.items():
        print(f"{clave}: {valor}")
