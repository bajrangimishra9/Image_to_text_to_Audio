#Library inclusion
!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install Pillow==9.0.0
!pip install gtts
from PIL import Image
import pytesseract
from gtts import gTTS
import os

# Load the image using PIL
image_path = '/content/Screenshot 2024-01-20 153606.png'
image = Image.open(image_path)

# Perform OCR using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)

# Save the extracted text to an audio file
tts = gTTS(text)
audio_path = 'output.mp3'
tts.save(audio_path)

# Play the audio file
os.system(f'start {audio_path}')
