from PIL import Image

# Função para converter a imagem para escala de cinza e binário (preto e branco)
def converter_para_cinza_e_binario(nome_arquivo_entrada, nome_arquivo_saida_cinza, nome_arquivo_saida_binario):
    # Abrir a imagem original
    imagem = Image.open(nome_arquivo_entrada)
    largura, altura = imagem.size
    
    # Obter os dados dos pixels
    pixels = imagem.load()

    # Criar uma nova imagem para a versão em escala de cinza
    imagem_cinza = Image.new("RGB", (largura, altura))
    # Criar uma nova imagem para a versão binária (preto e branco)
    imagem_binaria = Image.new("1", (largura, altura))

    # Converter para escala de cinza e binário
    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            # Calcular a média para converter para cinza
            cinza = int((r + g + b) / 3)
            # Definir o novo valor do pixel para a imagem em tons de cinza
            imagem_cinza.putpixel((x, y), (cinza, cinza, cinza))
            
            # Para a imagem binária, considerar o valor de cinza
            if cinza > 128:
                imagem_binaria.putpixel((x, y), 255)  # Branco
            else:
                imagem_binaria.putpixel((x, y), 0)  # Preto

    # Salvar as novas imagens
    imagem_cinza.save(nome_arquivo_saida_cinza, format="PNG")
    imagem_binaria.save(nome_arquivo_saida_binario, format="PNG")

    # Imprimir mensagem de sucesso
    print("A imagem foi convertida para tons de cinza e binário (preto e branco)")

# Exemplo de uso: converter "Lenna_test_image.jpg" para "Lenna_test_image_gray.png" e "Lenna_test_image_binary.png"
converter_para_cinza_e_binario('Lenna_test_image.png', 'Lenna_test_image_gray.png', 'Lenna_test_image_binary.png')
