# criptografador de arquivos                                       |
# programa utilizado para criptografar e descriptografar arquivos  | \
# caso você tenha um arquivo sensível que queira encriptar             by: lucas-Dk | whatsapp: +5531986802198
# pode estar utilizando esse script!                               | /
# façam bom uso!                                                   |

import os
import sys
from pathlib import Path
from pyAesCrypt import encryptFile
from pyAesCrypt import decryptFile

os.system("clear")
chave = "encriptandoedescriptografandoosarquivos"

logar = sys.argv
if len(logar) == 2 or len(logar) == 4 or len(logar) == 6:
	if sys.argv[1] == "-e":
		if sys.argv[2] == "-t":
			print()
			localizacao = str(sys.argv[5])
			tipo_arquiv = str(sys.argv[3])
			local = Path.home() / "{}".format(localizacao)
			for tipo in os.listdir(str(local)):
				if tipo.endswith(str(tipo_arquiv)):
					arquivo = tipo
					novo_fl = "encriptado" + os.path.basename(arquivo) + ".aes"
					encryptFile(arquivo,novo_fl,chave)
					os.remove(arquivo)
					print("Arquivo criptografado!\n")

	if sys.argv[1] == "-d":
			caminho = str(sys.argv[3])
			local = Path.home() / "{}".format(caminho)
			for item2 in os.listdir(str(local)):
				if item2.endswith(".aes"):
					descript = item2
					volta_fl = descript.replace("encriptado","")
					volta2_f = volta_fl.replace(".aes","")
					decryptFile(descript,volta2_f,chave)
					os.remove(item2)
					print("Arquivo descriptografado!\n")
	if sys.argv[1] == "--h":
		os.system("clear")
		print("""
Comandos para utilizar o script:\n

-e [Criptografar]
-d [Descritografar]
-t [Tipo/Extensão do arquivo]
-l [Local onde o arquivo se encontra]

Exemplos de comandos prontos:

[Para Criptografar]

python3 cript.py -e -t .txt -l Desktop
python3 cript.py -e -t .txt -l Downloads\\Textos

[Para Descriptografar]

python3 cript.py -d -l Desktop
python3 cript.py -d -l Downloads\\Textos

[Para Ajuda]
python3 cript.py --h

""")

else:
	print("Digite: python3 cript.py --h")
# FIM
