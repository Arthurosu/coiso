# Extruturas de repetição são formas de fazermos com que algo se repita
# uma quantidade de vezes que escolhermos ou até que algo mude.

# if é a extrutura de repetição mais básica, que funciona assim:
# if "se" algo for verdade, faça algo:
# ---------------------------------------
# numero = input("Escolha um número: ")
# if numero > 10:
#     print("Seu número é maior que 10.")
# ---------------------------------------
# else "senão" diz que se algo não for do jeito que o "if" pediu, faça algo:
numero = int(input("Escolha um número: "))
if numero > 10:
    print("Seu número é maior que 10.")
else:
    print("Seu número é menor que 10.")

# O "int()" é o que utilizamos para transformar uma variável de tipo String para uma de tipo int.