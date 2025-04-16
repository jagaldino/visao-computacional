import gradio as gr
import cv2
import numpy as np

def processar_imagem(imagem, dx, dy, angulo, escala, cor, contraste, gamma):
    # Converte imagem PIL para numpy (BGR)
    img = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)
    h, w = img.shape[:2]

    # Translação
    M_trans = np.float32([[1, 0, dx], [0, 1, dy]])
    img = cv2.warpAffine(img, M_trans, (w, h))

    # Rotação
    centro = (w // 2, h // 2)
    M_rot = cv2.getRotationMatrix2D(centro, angulo, escala)
    img = cv2.warpAffine(img, M_rot, (w, h))

    # Conversão de espaço de cor
    if cor == "Grayscale":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif cor == "HSV":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif cor == "RGB":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Contraste
    img = cv2.convertScaleAbs(img, alpha=contraste, beta=0)

    # Correção Gamma
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in np.arange(256)]).astype("uint8")
    img = cv2.LUT(img, table)

    # Converte para formato que o Gradio entende (RGB ou Grayscale)
    if len(img.shape) == 2:  # imagem em escala de cinza
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    return img

# Interface Gradio
interface = gr.Interface(
    fn=processar_imagem,
    inputs=[
        gr.Image(type="pil"),
        gr.Slider(-200, 200, value=0, label="Translação X"),
        gr.Slider(-200, 200, value=0, label="Translação Y"),
        gr.Slider(0, 360, value=0, label="Rotação (graus)"),
        gr.Slider(0.1, 3.0, value=1.0, label="Escala"),
        gr.Radio(["RGB", "Grayscale", "HSV"], label="Espaço de cor", value="RGB"),
        gr.Slider(0.1, 3.0, value=1.0, label="Contraste"),
        gr.Slider(0.1, 3.0, value=1.0, label="Gamma")
    ],
    outputs=gr.Image(type="numpy"),
    title="Editor de Imagem com OpenCV + Gradio",
    allow_flagging="never"
)

interface.launch()
