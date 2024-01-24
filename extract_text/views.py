from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract

def extract_text(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = 'any.png'
    text = pytesseract.image_to_string(image_path)
    img = Image.open("any.png")
    text = pytesseract.image_to_string(img)
    return HttpResponse(text)




