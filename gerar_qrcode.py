import os
import qrcode

# Garante que a pasta 'imagens' existe
os.makedirs("imagens", exist_ok=True)

# Link público completo para o GitHub Pages
url_projeto = "https://ferrazdeandrade.github.io/pulse_vida/"

# Gera e salva o QR Code dentro da pasta imagens
img = qrcode.make(url_projeto)
img.save("imagens/qrcode_pulsevida.png")

print("Sucesso! O QR Code atualizado foi gerado na pasta 'imagens/'.")