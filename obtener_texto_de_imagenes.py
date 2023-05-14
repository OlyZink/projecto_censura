#Para utilizar Google Vision API tenemos que crear una cuenta de Google Cloud
# y habilitar la API de Vision; y descargar e instalar el CLI de Google Cloud 

#Antes de ejecutar este código, es necesario ejecutar el CLI de Google y hacer
# login con él, abriendo la consola (símbolo del sistema, terminal, como se llame)
#  y mediante la línea:
#  gcloud auth application-default login

#Una vez hecho el login con el CLI, este código cogerá las credenciales y se
# ejecutará él solito.

# El texto completo aparece en el campo fullTextAnnotattion, en "text".

import os
from os import listdir

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
        #print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    return texts

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



path="data"
#resultado = detect_text(path)

imagespath=os.path.join(path,"images")
#código guardar
for imageName in listdir(imagespath):
    image=os.path.join(imagespath,imageName)
    texts = detect_text(image)
    try:
        with open(os.path.join(path,"texts",imageName.replace("jpg", "txt")),"w", encoding='utf-8') as file:
            file.write(texts[0].description)          
            #pag = texts[0].description
            #file.write(pag)
            file.close()
    except Exception as error:
        print(error)



