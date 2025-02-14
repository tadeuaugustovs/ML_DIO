Projeto DIO Transfer learning / fine-tuning
Esta é a minha solução para o projeto da Dio, onde é aplicado Transfer Learning com o modelo VGG16, pré-treinado no ImageNet, para classificar imagens de gatos e cachorros. As primeiras camadas da rede foram congeladas para manter as características mais gerais, como bordas e texturas, enquanto as últimas foram ajustadas para as novas classes. Os dados foram divididos em 70% para treino, 15% para validação e 15% para teste, e o modelo foi treinado por 10 épocas, acompanhando a evolução com gráficos de perda e acurácia.

Esse método facilitou muito o treinamento, já que aproveitamos uma rede bem treinada, economizando tempo e melhorando a precisão do classificador. Comparado ao treinamento do zero, foi possível alcançar um desempenho superior com um número reduzido de imagens, entregando um modelo ajustado de forma eficiente para a tarefa proposta.

Link para baixar o dataset: https://www.microsoft.com/en-us/download/details.aspx?id=54765.
