from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

mensaje = MIMEMultipart()
mensaje["from"] = "Manu Torres"
mensaje["to"] = "mail@gmail.com"
mensaje["subject"] = "Email de prueba"
mensaje.attach(MIMEText("Cuerpo del mensaje", "plain"))
mensaje.attach(MIMEImage(Path("imagen.png").read_bytes()))

# Habilitar autenticacion de 2 pasos en Gmail y App Password
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mail@gmail.com", "****")
    smtp.send_message(mensaje)
    print("Mensaje enviado")
