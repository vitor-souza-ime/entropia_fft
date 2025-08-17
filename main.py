import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
from scipy.stats import entropy

# URLs das imagens sugeridas (domínio público)
urls = [
    'https://upload.wikimedia.org/wikipedia/commons/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg',  # Renascimento
    'https://upload.wikimedia.org/wikipedia/commons/9/99/Las_Meninas_01.jpg',  # Barroco
    'https://upload.wikimedia.org/wikipedia/commons/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg',  # Romantismo
    'https://upload.wikimedia.org/wikipedia/commons/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg'  # Impressionismo
]

titles = ['Renascimento: Mona Lisa(Leonardo da Vinci)', 'Barroco: As Meninas (Velázquez) ', 'Romantismo: O Andarilho (C.D. Friedrich)', 'Impressionismo: Impressão (Claude Monet)']

def download_image(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Erro ao baixar {url}")
            return None
        img = Image.open(BytesIO(response.content)).convert('RGB')
        img = img.resize((256, 256))  # Redimensiona para padronização
        return np.array(img)
    except Exception as e:
        print(f"Erro: {e}")
        return None

def calculate_entropy(image):
    entropies = []
    for channel in range(3):
        hist, _ = np.histogram(image[:, :, channel], bins=256, range=(0, 256), density=True)
        hist = hist[hist > 0]
        ent = entropy(hist, base=2)
        entropies.append(ent)
    return entropies

def apply_fft(image):
    gray_image = np.mean(image, axis=2).astype(np.uint8)
    fft_result = np.fft.fft2(gray_image)
    fft_shift = np.fft.fftshift(fft_result)
    magnitude_spectrum = 20 * np.log(np.abs(fft_shift) + 1)  # Melhor normalização em dB
    return magnitude_spectrum

# Configura plotagem
fig, axs = plt.subplots(2, len(urls), figsize=(15, 6))

for i, url in enumerate(urls):
    img_array = download_image(url)
    if img_array is None:
        continue

    # Entropia
    entropies = calculate_entropy(img_array)
    print(f"{titles[i]} - Entropia (R, G, B): {entropies[0]:.2f}, {entropies[1]:.2f}, {entropies[2]:.2f} bits")

    # Imagem original
    axs[0, i].imshow(img_array)
    axs[0, i].set_title(titles[i])
    axs[0, i].axis('off')

    # Espectro FFT com melhorias
    fft_spectrum = apply_fft(img_array)
    im = axs[1, i].imshow(fft_spectrum, cmap='hot', vmin=np.min(fft_spectrum), vmax=np.max(fft_spectrum))  # Colormap 'hot' para contraste
    axs[1, i].set_title(f'FFT {titles[i].split(":")[0]}')
    axs[1, i].axis('off')
    fig.colorbar(im, ax=axs[1, i], fraction=0.046, pad=0.04)  # Adiciona colorbar

plt.tight_layout()
plt.show()
