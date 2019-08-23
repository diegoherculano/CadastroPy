nome = input('Qual seu nome? ')
print('Seja bem vindo(a) %s' %(nome))

passar = input('Deseja cadastrar? ')

if passar == str("sim") or passar == str("s"):
	print('Seja bem vindo ao cadastro.')
else:
	print('Muito obrigado até mais.')
	exit()

print('A partir de agora você poderá cadastrar')
nomecadastro = input('Digite um nome: ')
idadecadastro = input('Digite uma idade: ')
recordname = []
recordidade = []

print('Você cadastrou', nomecadastro, 'com idade de', idadecadastro, 'anos')
recordname.append(nomecadastro)
recordidade.append(idadecadastro)
continuar = input('Deseja continuar? ')

while continuar == str("sim") or continuar == str("s"):
	nomecadastro = input('Digite um nome: ')
	idadecadastro = input('Digite uma idade: ')
	recordname.append(nomecadastro)
	recordidade.append(idadecadastro)
	print('Você cadastrou', nomecadastro, 'com idade de', idadecadastro, 'anos')
	fim = input('Deseja continuar? ')
	if fim == str("sim") or fim == str("s"):
		print('Tudo bem.')
	else:
		break
			
print('Listando....')
nomes = recordname
idades = recordidade
conta = len(nomes)
print('Você digitou um total de', conta, 'cadastros', nome, 'obrigado.')
for i in range(0, conta): 
	print('O nome:', nomes[i], 'com a idade de:', idades[i], 'anos.')
print('Fim... Até a próxima.')
		

