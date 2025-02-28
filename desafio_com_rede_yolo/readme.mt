Descrição do Projeto
O script realiza as seguintes etapas:

Download do Dataset COCO:

O script verifica se os arquivos do COCO (anotações e imagens) já estão baixados. Caso contrário, ele faz o download e descompacta os arquivos necessários.

As pastas annotations, train2017, e val2017 são criadas para armazenar os dados.

Configuração do YOLOv3:

O repositório do Darknet (implementação do YOLO) é clonado e compilado.

Os pesos pré-treinados do YOLOv3 são baixados para inicializar o modelo.

Treinamento do Modelo:

O modelo YOLOv3 é treinado utilizando o conjunto de dados COCO.

O treinamento é configurado para usar o arquivo de configuração yolov3.cfg e os pesos pré-treinados yolov3.weights.

Teste do Modelo:

Após o treinamento, o modelo é testado em um conjunto de imagens de validação.

O script seleciona aleatoriamente algumas imagens do diretório val2017 e executa a detecção de objetos nelas.

As imagens com as detecções são exibidas utilizando a função imShow.

Visualização dos Resultados:

As imagens com as detecções são salvas como predictions.jpg e exibidas para análise.
