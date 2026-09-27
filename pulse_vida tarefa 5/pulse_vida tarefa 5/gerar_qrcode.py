import os
import qrcode

# Garante que a pasta 'imagens' existe no diretório atual
os.makedirs("imagens", exist_ok=True)

# Link público completo para o GitHub Pages do Pulse Vida
url_projeto = "https://FerrazdeAndrade.github.io/pulse_vida/"

# Gera e salva o QR Code dentro da pasta imagens
img = qrcode.make(url_projeto)
img.save("imagens/qrcode_pulsevida.png")

print("Sucesso! O QR Code do Pulse Vida foi gerado na pasta 'imagens/qrcode_pulsevida.png'.")