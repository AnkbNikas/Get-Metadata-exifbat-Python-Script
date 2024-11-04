import subprocess
import os

def get_metadata(file_path):
    """
    Extrae los metadatos del archivo especificado utilizando exiftool.

    :param file_path: Ruta del archivo del cual se extraerán los metadatos.
    :return: Salida de exiftool con los metadatos del archivo.
    """
    exiftool_path = "C:\\Path\\To\\exiftool.exe"  # Ajusta según tu instalación

    # Ejecutar exiftool y capturar la salida
    result = subprocess.run([exiftool_path, file_path], capture_output=True, text=True)
    return result.stdout

def show_formatted_output(output):
    """
    Muestra la salida formateada utilizando bat.

    :param output: Salida de exiftool con los metadatos del archivo.
    """
    # Guardar la salida en un archivo temporal
    with open("temp_output.txt", "w") as temp_file:
        temp_file.write(output)

    # Usar bat para mostrar la salida formateada
    subprocess.run(["bat", "temp_output.txt"])

    # Eliminar el archivo temporal
    os.remove("temp_output.txt")

def main():
    """
    Punto de entrada del script. Solicita al usuario la ruta del archivo,
    extrae los metadatos y muestra la salida formateada.
    """
    file_path = input("Ingresa la ruta del archivo (foto o documento): ")

    # Obtener los metadatos
    metadata = get_metadata(file_path)

    # Mostrar la salida formateada
    show_formatted_output(metadata)

if __name__ == "__main__":
    main()
