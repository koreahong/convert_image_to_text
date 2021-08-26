import io, os
from google.cloud import vision
from google.cloud.vision_v1 import types
from typing import List

#API KEY Path 설정
credential_path = "./auth.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

def convert_image(image_file) -> str:
    """
    google API를 통해서 텍스트 이미지를 텍스트로 전환하기
    """
    content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    labels: List[List[str]]= response.text_annotations
    res: str = labels[0].description
    return res


client = vision.ImageAnnotatorClient()
