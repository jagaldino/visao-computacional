import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem colorida
img_color = plt.imread('dog.png')

# Normaliza para 0–255 se necessário
if img_color.max() <= 1.0: img_color = img_color * 255

# Converte para inteiros
img_color = img_color.astype(np.uint8)

# Calcula os histogramas dos canais e armazena os máximos
colors = ('red', 'green', 'blue')
hist_list = []
max_freq = 0

for i in range(3):
    canal = img_color[..., i].ravel() # equivalente a img_color[:, :, i].ravel()
    hist, bins = np.histogram(canal, bins=256, range=(0, 256))
    hist_list.append((hist, bins))
    max_freq = max(max_freq, hist.max())  # Atualiza o maior valor de frequência

# Plotagem
plt.figure(figsize=(15, 5))

# Imagem original
plt.subplot(141)
plt.imshow(img_color)
plt.axis('off')
plt.title('Imagem Colorida')

# Histogramas dos canais com mesma escala no eixo Y
for i, color in enumerate(colors):
    hist, bins = hist_list[i]
    plt.subplot(142 + i)
    plt.plot(bins[:-1], hist, color=color)
    plt.ylim(0, max_freq * 1.05)  # Limite ajustado com margem de 5%
    plt.title(f'Canal {color.title()}')
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')

plt.tight_layout()
plt.show()
