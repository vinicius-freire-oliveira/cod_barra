# Importa a classe EAN13 do módulo barcode, que permite criar códigos de barras no formato EAN-13.
from barcode import EAN13

# Importa a classe ImageWriter do módulo barcode.writer, que permite salvar códigos de barras como imagens.
from barcode.writer import ImageWriter

# Importa o módulo Image da biblioteca PIL (Python Imaging Library), que permite abrir, manipular e salvar muitos formatos de arquivo de imagem diferentes.
from PIL import Image

# Importa o módulo os, que fornece uma forma de usar funcionalidades dependentes do sistema operacional como manipulação de arquivos e diretórios.
import os


def generate_barcode(number, filename):
    """
    Gera um código de barras EAN-13 e salva como uma imagem PNG.
    
    :param number: Número de 12 dígitos para o código de barras.
    :param filename: Nome do arquivo de saída sem extensão.
    """
    try:
        # Verifica se o número tem 12 dígitos
        if len(number) != 12 or not number.isdigit():
            raise ValueError("O número deve ter 12 dígitos.")
        
        # Cria o código de barras EAN-13 com a opção de escritor de imagem
        ean = EAN13(number, writer=ImageWriter())
        
        # Salva a imagem do código de barras
        full_filename = ean.save(filename)
        
        print(f"Código de barras salvo como {full_filename}")
        return full_filename
    except Exception as e:
        print(f"Erro ao gerar código de barras: {e}")
        return None

def main():
    # Solicita ao usuário um número de 12 dígitos
    number = input("Digite um número de 12 dígitos para o código de barras EAN-13: ")
    
    # Nome do arquivo de saída (sem extensão)
    filename = "barcode"
    
    # Gera o código de barras
    full_filename = generate_barcode(number, filename)
    
    if full_filename:
        # Tenta exibir a imagem gerada
        try:
            img = Image.open(full_filename)
            img.show()
        except Exception as e:
            print(f"Erro ao abrir a imagem do código de barras: {e}")
            print(f"Por favor, abra a imagem manualmente no caminho: {os.path.abspath(full_filename)}")

if __name__ == "__main__":
    main()
