import io
import os
from pathlib import Path
import pymysql

credential_path = os.path.join(Path(__file__).resolve().parent.parent, 'staticfiles', 'service_key.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Imports the Google Cloud client library
from google.cloud import vision_v1p4beta1 as vision
from google.cloud.vision_v1p4beta1 import types

# Instantiates a client
client = vision.ImageAnnotatorClient()


BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR,'media')

# 폴더 내 모든 파일 가져오기
files = os.listdir(path)

# 파일의 수정 시간을 기준으로 정렬
files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))

# 최신 파일 선택
latest_file = files[-1]

latest_file_path = os.path.join(path, latest_file)

with io.open(latest_file_path, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
