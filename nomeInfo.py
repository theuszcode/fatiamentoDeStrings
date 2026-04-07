#Informações
nome = (input("Digite seu Nome: "))
idade = (input("Digite sua Idade: "))

#Variáveis
nomeInvertido = nome[::-1]
espaco = " " in nome
N = len(nome)
primeiraLetra = nome[0]
ultimaLetra = nome[-1]

#Condição
if nome and idade:
	print(f"Seu nome é {nome}.")
	print(f"Seu nome invertido é {nomeInvertido}.")
	print(f"Seu nome tem espaço? {espaco}.")
	print(f"Seu nome tem {N} letras.")
	print(f"A primeira letra do seu nome é {primeiraLetra}.")
	print(f"A ultima letra do seu nome é {ultimaLetra}.")
else:
	print("Desculpe, voce deixou campos vazios.")