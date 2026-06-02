import qrcode, os
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://rmt1965-cloud.github.io/cantabrana-jotas/"
QR_DIR = "qr"
os.makedirs(QR_DIR, exist_ok=True)

JOTAS = [
    ("Alboradas--01.mp3", "Alboradas"),
    ("Cecilio_Jose_Diaz_Linaje--09.mp3", "Cecilio José Díaz Linaje 09"),
    ("Cecilio_Jose_Diaz_Linaje--10.mp3", "Cecilio José Díaz Linaje 10"),
    ("Elena_Diaz_Linaje--39.mp3", "Elena Díaz Linaje"),
    ("Gregorio_Ojeda_Pena_y_Julian_Ojeda_Ojeda--02.mp3", "Gregorio y Julián Ojeda 02"),
    ("Grupal_himno_Cantabrana--27.mp3", "Himno de Cantabrana"),
    ("julian-Ojeda-Ojeda--18.mp3", "Julián Ojeda 18"),
    ("Julian-Ojeda-Ojeda--20.mp3", "Julián Ojeda 20"),
    ("Julian-Ojeda-Ojeda--22.mp3", "Julián Ojeda 22"),
    ("Julian-Ojeda-Ojeda--23.mp3", "Julián Ojeda 23"),
    ("Julian-Ojeda-Ojeda-y-Gregorio-Ojeda-Pena--11.mp3", "Julián y Gregorio Ojeda 11"),
    ("Julian_Ojeda_Ojeda--04.mp3", "Julián Ojeda 04"),
    ("Julian_Ojeda_Ojeda--05.mp3", "Julián Ojeda 05"),
    ("Julian_Ojeda_Ojeda--08.mp3", "Julián Ojeda 08"),
    ("Julian_Ojeda_Ojeda--14.mp3", "Julián Ojeda 14"),
    ("Julian_Ojeda_Ojeda--15.mp3", "Julián Ojeda 15"),
    ("Julian_Ojeda_Ojeda--16.mp3", "Julián Ojeda 16"),
    ("Julian_Ojeda_Ojeda--17.mp3", "Julián Ojeda 17"),
    ("Julian_Ojeda_Ojeda--19.mp3", "Julián Ojeda 19"),
    ("Julian_Ojeda_Ojeda--21.mp3", "Julián Ojeda 21"),
    ("Julian_Ojeda_Ojeda--24.mp3", "Julián Ojeda 24"),
    ("Julian_Ojeda_Ojeda--25.mp3", "Julián Ojeda 25"),
    ("Julian_Ojeda_Ojeda--26.mp3", "Julián Ojeda 26"),
    ("Julian_Ojeda_Ojeda--28.mp3", "Julián Ojeda 28"),
    ("Julian_Ojeda_Ojeda--30.mp3", "Julián Ojeda 30"),
    ("Julian_Ojeda_Ojeda--31.mp3", "Julián Ojeda 31"),
    ("Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--03.mp3", "Julián y Gregorio Ojeda 03"),
    ("Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--06.mp3", "Julián y Gregorio Ojeda 06"),
    ("Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--13.mp3", "Julián y Gregorio Ojeda 13"),
    ("Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--34.mp3", "Julián y Gregorio Ojeda 34"),
    ("Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--35.mp3", "Julián y Gregorio Ojeda 35"),
    ("Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--36.mp3", "Julián y Gregorio Ojeda 36"),
    ("Lucia_Ojeda_Pena_y_Julian_Ojeda_Ojeda--29.mp3", "Lucía y Julián Ojeda 29"),
    ("Pedro-Felix-Garcia-Linaje--38.mp3", "Pedro Félix García 38"),
    ("Pedro-Felix-Garcia-Linaje-07.mp3", "Pedro Félix García 07"),
    ("Pedro_Felix_Garcia_Linaje--12.mp3", "Pedro Félix García 12"),
    ("Pedro_Felix_Garcia_Linaje--32.mp3", "Pedro Félix García 32"),
    ("Pedro_Felix_Garcia_Linaje--33.mp3", "Pedro Félix García 33"),
    ("Salve--37.mp3", "Salve Cantabrana"),
]

def generar_qr(url, nombre, archivo):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    # Añadir texto debajo
    w, h = img.size
    nuevo = Image.new('RGB', (w, h + 50), 'white')
    nuevo.paste(img, (0, 0))
    draw = ImageDraw.Draw(nuevo)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0,0), nombre, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, h + 10), nombre, fill='black', font=font)
    nuevo.save(os.path.join(QR_DIR, archivo))

# QR