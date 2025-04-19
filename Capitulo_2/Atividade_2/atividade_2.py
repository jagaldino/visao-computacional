import cv2
import numpy as np

# 1. Carregar vídeo (pode usar '0' para webcam também)
cap = cv2.VideoCapture('video.mp4')

# Verifica se o vídeo foi carregado corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo!")
    exit()

# 2. Obter propriedades do vídeo (largura, altura e FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Novo tamanho: largura dobrada (lado a lado)
output_size = (width * 2, height)

# 3. Criar o objeto de escrita do novo vídeo (colorido agora!)
output = cv2.VideoWriter('video_lado_a_lado.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'),
                         fps,
                         output_size,
                         isColor=True)

# 4. Processar frame a frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Processar: converter para cinza e equalizar histograma
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray_frame)

    # Converter o frame equalizado de volta para BGR para juntar lado a lado
    equalized_bgr = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

    # Concatenar lado a lado: [original | processado]
    lado_a_lado = np.hstack((frame, equalized_bgr))

    # Escrever no vídeo de saída
    output.write(lado_a_lado)

# 5. Liberar recursos
cap.release()
output.release()
# cv2.destroyAllWindows()

print("✅ Vídeo salvo como 'video_lado_a_lado.mp4' com comparativo lado a lado!")