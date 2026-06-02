import qrcode, os
os.makedirs('qr', exist_ok=True)

BASE = "https://rmt1965-cloud.github.io/cantabrana-jotas/?jota="

jotas = [
    "Alboradas--01","Cecilio_Jose_Diaz_Linaje--09","Cecilio_Jose_Diaz_Linaje--10",
    "Elena_Diaz_Linaje--39","Gregorio_Ojeda_Pena_y_Julian_Ojeda_Ojeda--02",
    "Grupal_himno_Cantabrana--27","julian-Ojeda-Ojeda--18","Julian-Ojeda-Ojeda--20",
    "Julian-Ojeda-Ojeda--22","Julian-Ojeda-Ojeda--23",
    "Julian-Ojeda-Ojeda-y-Gregorio-Ojeda-Pena--11","Julian_Ojeda_Ojeda--04",
    "Julian_Ojeda_Ojeda--05","Julian_Ojeda_Ojeda--08","Julian_Ojeda_Ojeda--14",
    "Julian_Ojeda_Ojeda--15","Julian_Ojeda_Ojeda--16","Julian_Ojeda_Ojeda--17",
    "Julian_Ojeda_Ojeda--19","Julian_Ojeda_Ojeda--21","Julian_Ojeda_Ojeda--24",
    "Julian_Ojeda_Ojeda--25","Julian_Ojeda_Ojeda--26","Julian_Ojeda_Ojeda--28",
    "Julian_Ojeda_Ojeda--30","Julian_Ojeda_Ojeda--31",
    "Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--03",
    "Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--06",
    "Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--13",
    "Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--34",
    "Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--35",
    "Julian_Ojeda_Ojeda_y_Gregorio_Ojeda_Pena--36",
    "Lucia_Ojeda_Pena_y_Julian_Ojeda_Ojeda--29","Pedro-Felix-Garcia-Linaje--38",
    "Pedro-Felix-Garcia-Linaje-07","Pedro_Felix_Garcia_Linaje--12",
    "Pedro_Felix_Garcia_Linaje--32","Pedro_Felix_Garcia_Linaje--33","Salve--37"
]

for j in jotas:
    qr = qrcode.make(BASE + j)
    qr.save(f"qr/QR_{j}.png")
    print(f"OK: {j}")

print(f"\nTotal: {len(jotas)} QR generados en carpeta qr/")