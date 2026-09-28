import qrcode

url_repositorio = "https://github.com/FerrazdeAndrade/pulse-vida-tarefa-5.git"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(url_repositorio)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

caminho = "pulse_vida-tarefa-5-2-main/pulse_vida tarefa 5/pulse_vida tarefa 5/imagens/qrcode_pulse_vida.png"
img.save(caminho)
print("QR Code gerado com sucesso!")
