import cv2
import numpy as np
import requests
from io import BytesIO
from PIL import Image
import os

# URL da imagem - Você pode alterar a URL para outra imagem
url = "https://heltonmaia.com/computervision/_images/cover.jpeg"

# Baixando a imagem
response = requests.get(url)
img_array = np.array(Image.open(BytesIO(response.content)))

# Convertendo para BGR (OpenCV usa BGR, não RGB)
image_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

# Convertendo para escala de cinza
gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

# Adicionando texto
cv2.putText(
    gray,
    "OpenCV Challenge",
    (50, 50),  # posição (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,
    1.0,        # escala
    255,        # cor (branco)
    2           # espessura
)

# Exibindo a imagem processada
cv2.imshow("Imagem em escala de cinza", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Criando pasta para salvar a imagem
output_dir = "atividade_1_resultado"
os.makedirs(output_dir, exist_ok=True)

# Salvando a imagem
output_path = os.path.join(output_dir, "imagem_processada.jpg")
cv2.imwrite(output_path, gray)

print(f"Imagem salva em: {output_path}")
