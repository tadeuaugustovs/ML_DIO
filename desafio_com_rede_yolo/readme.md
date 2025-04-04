# 🖼️ Desafio com Rede YOLO no Dataset COCO

Este projeto apresenta a implementação de um pipeline completo para detecção de objetos utilizando a rede **YOLOv3** no dataset **COCO**.

---

## 📌 Objetivo

Automatizar o processo de download, configuração, treinamento e teste do modelo YOLOv3 com o dataset COCO, proporcionando uma solução eficiente para detecção de objetos.

---

## 🚀 Tecnologias Utilizadas

- Python
- YOLOv3
- COCO Dataset
- OpenCV
- NumPy
- OS
- Subprocess

---

## 🧪 Metodologia

O script `desafio_yolo_coco.py` realiza as seguintes etapas:

1. **Download do Dataset COCO**:
   - Verifica se os arquivos de anotações e imagens já estão presentes.
   - Caso contrário, realiza o download e a extração dos arquivos necessários.
   - Cria as pastas `annotations`, `train2017` e `val2017` para armazenar os dados.

2. **Configuração do YOLOv3**:
   - Clona e compila o repositório do Darknet (implementação do YOLO).
   - Baixa os pesos pré-treinados do YOLOv3 para inicializar o modelo.

3. **Treinamento do Modelo**:
   - Treina o modelo YOLOv3 utilizando o conjunto de dados COCO.
   - Configura o treinamento para usar o arquivo de configuração `yolov3.cfg` e os pesos pré-treinados `yolov3.weights`.

4. **Teste do Modelo**:
   - Após o treinamento, testa o modelo em um conjunto de imagens de validação.
   - Seleciona aleatoriamente algumas imagens do diretório `val2017` e executa a detecção de objetos nelas.
   - Exibe as imagens com as detecções utilizando a função `imShow`.

---

## 📊 Resultados

- **Automatização**: O script automatiza todo o processo, desde o download dos dados até a visualização dos resultados.
- **Eficiência**: Utiliza o modelo YOLOv3, conhecido por sua rapidez e precisão na detecção de objetos.
- **Flexibilidade**: Pode ser adaptado para diferentes conjuntos de dados e configurações de modelo.

---

## 📂 Organização dos Arquivos

- `desafio_yolo_coco.py`: Script principal que executa todo o pipeline descrito.
- `readme.md`: Este arquivo, contendo a descrição do projeto.

---

## 📌 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/tadeuaugustovs/ML_DIO.git
   cd ML_DIO/desafio_com_rede_yolo
