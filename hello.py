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

print('Você cadastrou', nomecadastro, 'com idade de', idadecadastro, 'anos')
