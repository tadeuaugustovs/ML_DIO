# 🧠 Projeto DIO - Classificação de Imagens com Transfer Learning

Este projeto é uma solução prática para um desafio da [DIO](https://www.dio.me/), utilizando **Transfer Learning com o modelo VGG16** (pré-treinado no ImageNet) para classificar imagens de **gatos e cachorros**.

---

## 📌 Objetivo

Demonstrar como aplicar fine-tuning em redes neurais convolucionais para reaproveitar conhecimento de modelos já treinados e adaptá-los a um novo conjunto de dados.

---

## 🚀 Tecnologias Utilizadas

- Python
- TensorFlow / Keras
- VGG16 (pré-treinado no ImageNet)
- Pandas / Numpy / Matplotlib

---

## 🧪 Metodologia

- As **camadas iniciais da VGG16 foram congeladas**, mantendo as extrações de bordas e texturas.
- As **camadas finais foram ajustadas** para a nova tarefa (gatos vs. cachorros).
- Divisão dos dados:
  - 70% treino
  - 15% validação
  - 15% teste
- O modelo foi treinado por **10 épocas**, com acompanhamento da **acurácia** e da **função de perda** por meio de gráficos.

---

## 📊 Resultados

- **Economia de tempo** com treinamento rápido e eficiente
- **Alta acurácia** mesmo com poucas épocas
- Visualização dos gráficos de desempenho durante o treinamento

---

## 📂 Organização dos Arquivos

- `Transfer_Learning_VGG16.ipynb`: notebook com todo o pipeline do projeto.
- `dataset/`: pasta de imagens de gatos e cachorros divididas em treino, validação e teste.

---

## 📌 Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/tadeuaugustovs/ML_DIO.git
   cd ML_DIO/Deep\ Learning/Projeto\ DIO
