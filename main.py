import os
from typing import Dict
from pseudo_database import file_extension_folder_name
from functions import (get_file_folder, move_file, create_folder_from_file, get_file_extension,
                       get_all_folders, get_all_files, choose_root_path, get_total_of_files,
                       show_end_message, get_custom_dir_path)

root_path: str = "C:\\Users\\anton\\"


def main(path: str, extension_folder_structure: Dict[str, str]):
    """
    Função principal do sistema

    Essa função recebe um caminho original e a estrutura que define o nome da pasta para uma extensão de arquivo.
    A função vai verificar se a pasta já existe e mover o arquivo para lá, caso contrário, será criada a pasta para
    aquele tipo de arquivo e então o mesmo será movido para essa pasta recem criada.

    :param path: Caminho do doretório de origem
    :type path: str
    :param extension_folder_structure: Estrutura com o nome da pasta para cada extensão de arquivo
    :type extension_folder_structure: dict
    :return: none
    """
    # Pega o total de arquivos na pasta para mostrar depois
    total_of_files = get_total_of_files(path)

    # Para cada arquivo existente no diretório de origem...
    for file in get_all_files(path):
        # Cria um caminho para o arquivo
        file_path = os.path.join(path, file)

        # Se a pasta desse arquivo já existir...
        if get_file_folder(get_file_extension(file_path), extension_folder_structure) in get_all_folders(path):
            # Move o arquivo para a pasta
            move_file(path, file_path)
        else:
            # Cria uma pasta para esse tipode arquivo
            create_folder_from_file(path,
                                    get_file_folder(get_file_extension(file_path), extension_folder_structure))
            # Move o arquivo para a pasta
            move_file(path, file_path)

    # Exibe a mensagem de encerramneto do sistema
    show_end_message(total_of_files)


main(get_custom_dir_path(root_path, choose_root_path(root_path)), file_extension_folder_name)
