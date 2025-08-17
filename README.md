# Análise Quantitativa da Complexidade Visual em Períodos Artísticos

Este repositório contém um script Python que realiza uma análise digital de obras de arte representativas de quatro períodos artísticos ocidentais (Renascimento, Barroco, Romantismo e Impressionismo) usando técnicas de processamento de imagens. O código calcula a entropia de Shannon para os canais RGB das imagens e aplica a Transformada Rápida de Fourier (FFT) para analisar os padrões espaciais, oferecendo uma abordagem quantitativa complementar à crítica tradicional de arte.

## Repositório
- **URL**: [https://github.com/vitor-souza-ime/entropia_fft](https://github.com/vitor-souza-ime/entropia_fft)
- **Arquivo principal**: `main.py`

## Descrição
O script `main.py` baixa imagens de domínio público de obras icônicas, como a *Mona Lisa* (Renascimento), *Las Meninas* (Barroco), *Wanderer above the Sea of Fog* (Romantismo) e *Impression, Sunrise* (Impressionismo), processa-as e gera visualizações que comparam a complexidade visual entre os períodos. A entropia mede a diversidade de intensidades de pixel, enquanto a FFT revela os espectros de frequência espacial, destacando diferenças estilísticas (ex.: gradientes suaves vs. bordas nítidas).

## Requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
- `requests` (para download de imagens)
- `numpy` (para manipulação de arrays)
- `Pillow` (para processamento de imagens)
- `matplotlib` (para visualização)
- `scipy` (para cálculo de entropia)

Instale as dependências com:
```bash
pip install requests numpy Pillow matplotlib scipy
```

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/vitor-souza-ime/entropia_fft.git
   cd entropia_fft
   ```
2. Execute o script:
   ```bash
   python main.py
   ```
3. O script exibirá:
   - Imagens originais redimensionadas (256x256 pixels).
   - Espectros FFT com barras de cor para melhor interpretação.
   - Valores de entropia (em bits) para os canais RGB no console.

## Saída
- **Console**: Exibe a entropia por canal (R, G, B) para cada obra, ex.: "Renascimento: Mona Lisa - Entropia (R, G, B): 7.60, 7.39, 6.32 bits".
- **Gráfico**: Uma figura com duas linhas:
  - Linha superior: Imagens originais.
  - Linha inferior: Espectros FFT, com colormap 'hot' e colorbar.

## Estrutura do Código
- **URLs**: Listadas no início, apontando para imagens de domínio público no Wikimedia Commons.
- **Funções**:
  - `download_image`: Baixa e redimensiona as imagens.
  - `calculate_entropy`: Calcula a entropia de Shannon por canal RGB.
  - `apply_fft`: Aplica a FFT e normaliza o espectro em dB.
- **Visualização**: Usa `matplotlib` para plotar os resultados.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:
- Adicionar mais períodos artísticos ou obras.
- Melhorar a visualização (ex.: ajustar colormaps ou adicionar métricas).
- Otimizar o código para desempenho.

Por favor, abra uma issue ou envie um pull request com suas sugestões.

## Licença
Este projeto está sob a [MIT License](LICENSE) (ou especifique outra licença, se aplicável). As imagens usadas são de domínio público, conforme disponíveis no Wikimedia Commons.


