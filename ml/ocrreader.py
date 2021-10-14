try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string(Image.open('test.png')))

# List of available languages
print(pytesseract.get_languages(config=''))

# French text image to string
print(pytesseract.image_to_string(Image.open('ocrimages/hindi1.png'), lang='hin'))
img=Image.open('ocrimages/test.png')
Image._show(img)