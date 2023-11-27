import os
import fitz

def convert_pdf_to_png(pdf_directory, output_directory):
    # Recorrer todos los archivos en el directorio dado
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            doc = fitz.open(os.path.join(pdf_directory, filename))
            for i in range(len(doc)):
                page = doc.load_page(i)  # Cargar cada página
                pix = page.get_pixmap()  # Obtener una imagen de la página
                output = os.path.join(output_directory, filename[:-4] + '_page_' + str(i) + '.png')
                pix.save(output)  # Guardar la imagen como PNG

# Directorio de entrada y salida
input_directory = '../../ruta'
output_directory = '../../ruta'

# Uso de la función
convert_pdf_to_png(input_directory, output_directory)
