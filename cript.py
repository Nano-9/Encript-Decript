# criptografador de arquivos                                       |
# programa utilizado para criptografar e descriptografar arquivos  | \
# caso você tenha um arquivo sensível que queira encriptar             by: lucas-Dk | whatsapp: +5531986802198
# pode estar utilizando esse script!                               | /
# façam bom uso!                                                   |

import os
import sys
import shutil
from pathlib import Path
from pyAesCrypt import encryptFile
from pyAesCrypt import decryptFile

os.system("clear")
chave = "encriptandoedescriptografandoosarquivos"

print("""
Menu:

[1] - Criptografar
[2] - Descriptografar
\n	""")
escolha = int(input("O que deseja: "))
if escolha == 1:
	print()
	localizacao = str(input("Informe onde o arquivo está: "))
	tipo_arquiv = str(input("Informe a extensão do arquivo: ")).strip().lower()
	local = Path.home() / "{}".format(localizacao)
	for tipo in os.listdir(str(local)):
		if tipo.endswith(str(tipo_arquiv)):
			arquivo = tipo
			novo_fl = "encriptado" + os.path.basename(arquivo) + ".aes"
			encryptFile(arquivo,novo_fl,chave)
			os.remove(arquivo)
elif escolha == 2:
	caminho = str(input("Caminho: "))
	local = Path.home() / "{}".format(caminho)
	for item2 in os.listdir(str(local)):
		if item2.endswith(".aes"):
			descript = item2
			volta_fl = descript.replace("encriptado","")
			volta2_f = volta_fl.replace(".aes","")
			decryptFile(descript,volta2_f,chave)
			os.remove(item2)
