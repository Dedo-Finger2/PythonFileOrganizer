import os
import shutil

# Pegar qual pasta será organizada (downloads? documentos? custom?)
path = "C:\\Users\\anton\\Downloads"
directory = os.listdir(path)

# Listar os arquivos dentro daquela pasta e guardar dentro de uma variável
files = [f for f in directory if os.path.isfile(path + '/' + f)]

# Listar as pastas que existem no diretório que foi pego acima
folders = [f for f in directory if os.path.isdir(os.path.join(path, f))]

# Fazer um loop que passe por todos os arquivos no diretório
for file in files:
    # Guardar a extensão do arquivo numa variável
    file_name, extension = os.path.splitext(file)

    # Verificar se existe uma pasta com o nome da extensão do arquivo atualmente sendo analisado no Loop
    if extension[1:] in folders:
        # Caso True:
        # Mover o arquivo para essa pasta e continuar a interação
        shutil.move(path + "\\" + file_name + extension, path + "\\" + extension[1:])
    else:
        # Caso False:
        # Criar uma nova pasta no diretório com o nome sendo a extensão do arquivo
        os.makedirs(path + "\\" + extension[1:])
        # Mover o arquivo para essa pasta criada
        shutil.move(path + "\\" + file_name + extension, path + "\\" + extension[1:])
        # Adicionar o nome da extensão na lista de pastas
        folders.append(extension[1:])
# Mostrar uma mensagem dizendo que a organização acabou
print("Tudo ocorreu bem!")