from PIL import Image
import cv2
import numpy as np

def imread_unicode(path):
    """PIL로 열고 OpenCV로 변환 (유니코드 경로 지원)"""
    with Image.open(path) as img:
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def imwrite_unicode(path, image):
    """OpenCV 이미지를 PIL로 저장 (유니코드 경로 지원)"""
    if image.ndim == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(image)
    img_pil.save(path)
