# 🔍 Sistema de Recomendação por Similaridade de Imagens

Este projeto implementa um sistema de recomendação baseado na **aparência visual de imagens**, utilizando **Deep Learning** para extrair características e **FAISS** para busca eficiente por similaridade.

---

## 🧠 Objetivo

Dado um produto ou objeto representado por uma imagem (ex: mouse, laptop, roteador), o sistema encontra **outros itens visualmente semelhantes**, sem considerar nome, marca ou descrição textual.

---

## 🗂️ Dataset

O dataset utilizado é o [Electronic Object Detection Dataset](https://www.kaggle.com/datasets/ksenia5/electronic-object-detection), contendo imagens organizadas por categoria:

- Mouse
- Teclado
- Laptop
- Celular
- Roteador
- Server Rack
- USB Stick
- Entre outros...

As imagens foram organizadas em pastas (uma por classe), e o upload é feito diretamente no Google Colab.

---

## ⚙️ Tecnologias e Bibliotecas

- Python 3
- TensorFlow / Keras
- ResNet50 (modelo pré-treinado)
- FAISS (Facebook AI Similarity Search)
- Gradio (Interface web interativa)
- Matplotlib (visualização no notebook)

---

## 🚀 Etapas do Projeto

1. **Upload e descompactação do dataset** (.zip)
2. **Pré-processamento** das imagens
3. **Extração de vetores** (embeddings) com ResNet50
4. **Indexação com FAISS**
5. **Busca por similaridade** entre imagens
6. **Demonstração visual** com Matplotlib
7. *(Opcional)* Interface com **Gradio** para recomendações visuais

---

## 🖼️ Exemplo de Uso

```python
show_similar_images(query_index=10)
```

Exibe a imagem de entrada e suas 5 mais semelhantes com base nos vetores extraídos.

---

## 🌐 Interface com Gradio

Uma interface interativa que permite ao usuário enviar uma imagem e receber sugestões semelhantes diretamente no navegador.

---

## 📁 Estrutura esperada do dataset

```
electronic-object-detection/
├── computer mouse/
│   ├── mouse1.jpg
│   ├── mouse2.jpg
├── laptop/
│   ├── laptop1.jpg
│   ├── laptop2.jpg
...
```

---

## 📌 Observações

- O modelo pode ser substituído por outros como `EfficientNetB0`, `MobileNet`, etc.
- Para acelerar a busca em datasets grandes, é possível aplicar **PCA**.
- FAISS é ideal para produção com muitos dados.

---

## 👨‍💻 Autor

Projeto desenvolvido por **Tadeu Augusto Vilela da Silva**  
Com apoio do ChatGPT (OpenAI)  
Faculdade Multivix Serra · Engenharia da Computação

---

## 📄 Licença

Este projeto é open-source para fins educacionais. Sinta-se à vontade para adaptar e expandir.
