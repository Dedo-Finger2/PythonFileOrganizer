import os
import shutil
from typing import List, Set, Dict
from pseudo_database import file_extension_folder_name, white_listed_directories


def get_all_files(root_path: str) -> List[str]:
    """
    Retorna todos os arquivos de um diretório de origem

    Essa função recebe um caminho para um diretório orignal e retorna os arquiovs encontrados nesse diretório

    :param root_path: Caminho do diretório de origem
    :type root_path: str
    :return: Uma lista com todos os arquivos encontrados no diretório de origem
    :rtype: list of str
    """
    # Loop passando por todos os items da pasta no caminho de origem
    for file in os.listdir(root_path):
        # Se for um arquivo...
        if os.path.isfile(os.path.join(root_path, file)):
            # Retorna o arquivo numa lista de retornos
            yield file


def get_all_folders(root_path: str) -> List[str]:
    """
    Retorna todos as pastas de um diretório de origem

    Essa função recebe um caminho para um diretório orignal e retorna as pastas encontrados nesse diretório

    :param root_path: Caminho do diretório de origem
    :type root_path: str
    :return: Uma lista com todas as pastas encontrados no diretório de origem
    :rtype: list of str
    """
    # Loop passando por todos os items da pasta no caminho de origem
    for folder in os.listdir(root_path):
        # Se for uma pasta...
        if os.path.isdir(os.path.join(root_path, folder)):
            # Retorna a pasta numa listas de retornos
            yield folder


def get_all_file_extensions(root_path: str) -> Set[str]:
    """
    Retorna uma lista com todas as extensões dos arquivos dentro de uma pasta

    Essa função recebe um caminho para um diretório de origem e retorna um conjunto com as extenssões dos arquivos

    :param root_path: Caminho do doretório de origem
    :type root_path: str
    :return: Conjunto com todas as extenssões de todos os arquivos dentro de uma pasta
    :rtype: set of str
    """
    # Criando um conjunto vazio que vai guardar as extensões
    file_extensions = set()

    # Loop os arquivos de uma pasta
    for file in get_all_files(root_path):
        # Separando nome da extensão do arquivo
        file_name, file_extension = os.path.splitext(file)

        # Adicionando apenas a extensão à coleção
        file_extensions.add(file_extension)

    return file_extensions


def get_file_folder(file_extension: str, extension_folder_structure: Dict[str, str]) -> str:
    """
    Retorna o nome da pasta que o arquivo vai ficar

    Essa função recebe a extensão do arquivo e a estrutura que define qual o nome da pasta para cada extensão de arquivo

    :param file_extension: Extensão do arquivo
    :type file_extension: str
    :param extension_folder_structure: Dicionário que define qual o nome da pasta para cada tipo de arquivo
    :type extension_folder_structure: dict
    :return: Nome da pasta correspondede à extensão do arquivo
    :rtype: str
    """
    # Retorna o nome da pasta com o método get(), se não houver, retornar "Outros"
    folder_name = extension_folder_structure.get(file_extension, "Outros")

    return folder_name


def get_file_extension(file_path: str) -> str:
    """
    Retorna apenas a extensão do arquivo

    Essa função recebe o caminho completo do arquivo e retorna apenas a extensão dele

    :param file_path: Caminho completo do arquivo
    :type file_path: str
    :return: Extensão do arquivo
    :rtype: str
    """
    # Separa nome do arquivo de sua extensão
    file_name, file_extension = os.path.splitext(file_path)

    return file_extension


def create_all_folders(root_path: str, extension_folder_structure: Dict[str, str]):
    """
    Cria todas as pastas de a cordo com a estrutura extensão_pasta

    Essa função recebe o caminho original e a estrutura que define o nome da pasta a depender da extensão

    :param root_path: Caminho do doretório de origem
    :type root_path: str
    :param extension_folder_structure: Dicionário contendo a estrutura que define qual pasta de cada extensão
    :type extension_folder_structure: dict
    :return: none
    """
    # Criar um conjunto vazio para armazenar os nomes das pastas criadas
    created_folders = set()

    # Loop que percorre o dicionário, pegando tanto chave quanto valor
    for file_extension, folder_name in extension_folder_structure.items():
        # Cria um novo caminho com o nome da pasta
        new_folder_path = os.path.join(root_path, folder_name)

        # Verificar se o nome da pasta está no conjunto
        if folder_name in created_folders:
            # Ignorar essa extensão e continuar o loop
            continue

        # Criar a pasta no caminho gerado
        os.makedirs(new_folder_path)

        # Adicionar o nome da pasta ao conjunto
        created_folders.add(folder_name)


def create_folder_from_file(root_path: str, folder_name: str):
    """
    Cria uma pasta nova com base no nome dela

    Essa função recebe um caminho original e o nomde que será usado para criar uma pasta

    :param root_path: Caminho do doretório de origem
    :type root_path: str
    :param folder_name: Nome da pasta que será criada
    :type folder_name: str
    :return: none
    """
    # Cria um caminho com o nome da pasta
    folder_path = os.path.join(root_path, folder_name)
    # Cria a pasta usando o caminho
    os.makedirs(folder_path)


def move_file(root_path: str, file_path: str):
    """
    Move um arquivo para algum caminho

    Essa função recebe um caminho original e o caminho do arquivo

    :param root_path: Caminho do doretório de origem
    :type root_path: str
    :param file_path: Caminho do arquivo
    :type file_path: str
    :return: none
    """
    # Cria uma caminho para a pasta do arquivo
    folder_file_path = os.path.join(root_path,
                                    get_file_folder(get_file_extension(file_path), file_extension_folder_name))
    # Move o arquivo para essa pasta
    shutil.move(file_path, folder_file_path)


def get_total_of_files(root_path: str) -> int:
    """
    Retorna a quantidade total de arquivos dentro de uma pasta

    Essa função recebe o diretório de origem e retorna os arquivos que possuir dentro de uma pasta apartir desse
    diretório de origem

    :param root_path: Caminho do diretório de origem
    :type root_path: str
    :return: Número de pastas dentro do diretório sendo organizado
    :rtype: int
    """
    total_of_files: int = 0

    for file in get_all_files(root_path):
        total_of_files += 1

    return total_of_files


def choose_root_path(root_path: str) -> str:
    """
    Retorna o novo caminho do diretório customizado

    Função que

    :param root_path:
    :return:
    """
    print("Escolha uma das opções abaixo:")

    for option, directory in white_listed_directories.items():
        print(f"[{option}] - {directory}")

    print("---------------------------")

    user_input = input()

    return user_input


def get_custom_dir_path(root_path: str, user_input: str) -> str:
    if white_listed_directories.get(int(user_input)) == "Custom":
        user_input = input(f"{root_path}\\")

        directory_path = os.path.join(root_path, user_input)

        return directory_path
    else:
        while not user_input.isdigit() or int(user_input) not in white_listed_directories.keys():
            print("Oops! Opção inválida, tente novamente:")

            for option, directory in white_listed_directories.items():
                print(f"[{option}] - {directory}")

            user_input = input()

        directory_path = os.path.join(root_path, white_listed_directories.get(int(user_input)))

        return directory_path


def show_end_message(total_of_files: int):
    if total_of_files <= 0:
        print("-----------------------------------------------------------------")
        print(f"❌ - Este diretório não possui arquivos desorganizados!")
        print("-----------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------")
        print(f"✅ - {total_of_files} arquivo(s) foram organizados com sucesso!!")
        print("-----------------------------------------------------------------")
