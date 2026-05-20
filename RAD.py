def cadastrar_aluno():
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = input("Digite a idade do aluno: ")
    aluno["curso"] = input("Digite o curso do aluno: ")

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {aluno['nome']}\n")
        arquivo.write(f"Idade: {aluno['idade']}\n")
        arquivo.write(f"Curso: {aluno['curso']}\n")
        arquivo.write("--------------------\n")

    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Nenhum aluno cadastrado ainda.")


while True:
    print("\n=== SISTEMA DE CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
