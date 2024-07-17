import PyPDF2
import os

def unir_pdfs():
    # Solicitar la cantidad de archivos
    try:
        num_archivos = int(input("¿Cuántos archivos PDF desea unir? "))
        if num_archivos < 1:
            print("El número de archivos debe ser al menos 1.")
            return
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    # Ruta predefinida
    ruta_base = "C:\\Users\\raton\\Downloads\\"

    # Lista para almacenar las rutas completas de los archivos
    archivos = []

    # Solicitar los nombres de los archivos
    # test i = -1
    for i in range(num_archivos):
        nombre_archivo = input(f"Ingrese el nombre del archivo {i + 1} (sin la extensión .pdf): ")
        archivos.append(os.path.join(ruta_base, nombre_archivo + ".pdf"))

    # Crear un objeto de escritura de PDF
    pdf_writer = PyPDF2.PdfWriter()

    # Leer y agregar cada archivo PDF
    for archivo in archivos:
        try:
            with open(archivo, "rb") as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for pagina in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[pagina])
        except FileNotFoundError:
            print(f"No se encontró el archivo: {archivo}")
            return

    # Guardar el archivo PDF combinado
    nombre_salida = input("Ingrese el nombre del archivo de salida (sin la extensión .pdf): ")
    ruta_salida = os.path.join(ruta_base, nombre_salida + ".pdf")

    with open(ruta_salida, "wb") as f_salida:
        pdf_writer.write(f_salida)

    print(f"Archivo PDF combinado guardado en: {ruta_salida}")

if __name__ == "__main__":
    unir_pdfs()
