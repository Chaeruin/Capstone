import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service_secret_key.json'


# Imports the Google Cloud client library
from google.cloud import vision 
from google.cloud.vision_v1 import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(os.path.dirname(__file__),
                         'resources/test2.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations
