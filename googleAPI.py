import io, os
from google.cloud import vision
from google.cloud.vision_v1 import types
credential_path = "./auth.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

#한국어만 인식 Image to Korean+English
def orc_kor_eng(image_file):
    content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    labels = response.text_annotations
    res = labels[0].description
    # for  label in labels:
    #     res += label.description + '\n'
    # print(labels)
    return res

client = vision.ImageAnnotatorClient()






