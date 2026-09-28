import qrcode

# URL do seu repositório ou página do projeto
url_repositorio = "https://github.com/FerrazdeAndrade/pulse-vida-tarefa-5.git"

# Configurações do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

# Adiciona os dados (URL)
qr.add_data(url_repositorio)
qr.make(fit=True)

# Cria a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem na pasta do projeto
nome_arquivo = "qrcode_pulse_vida.png"
img.save(nome_arquivo)

print(f"Sucesso! QR Code gerado e salvo como '{nome_arquivo}'.")
