import os
from uncompyle6.main import decompile_file

def descompilar_pyc(pyc_file):
    # Verifica se o arquivo existe
    if not os.path.isfile(pyc_file):
        print(f"Arquivo {pyc_file} não encontrado.")
        return

    # Obtém o nome base do arquivo sem a extensão
    file_name = os.path.splitext(os.path.basename(pyc_file))[0]

    # Define o caminho do arquivo descompilado em C:\temp
    output_file = os.path.join('C:\\Projeto\\GT_Pessoal\\Scripts_Python\\Descompilador', f"{file_name}.py")

    # Descompila e salva o arquivo
    try:
        with open(output_file, 'w') as f:
            decompile_file(pyc_file, f)
        print(f"Arquivo descompilado com sucesso: {output_file}")
    except Exception as e:
        print(f"Erro ao descompilar o arquivo: {e}")

if __name__ == "__main__":
    pyc_file = input("Insira o caminho do arquivo .pyc: ")
    descompilar_pyc(pyc_file)
