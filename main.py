def  nome_valido():
    
    while True:
        try:
            nome = input("Digite seu nome: ").strip()

            if not nome:
                raise ValueError("O nome não pode ser nulo.")

            if any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")

            return nome
        except ValueError as erro:
            print(f"ERRO: {erro}  tente novamente.")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado ao processar o nome: {erro}")

def  idade_valida():
    while True:
        try:
            idade_str = input("Digite sua idade: ").strip()
            idade = int(idade_str)

            if idade <= 0 or idade > 120:
                print("ERRO: A idade deve ser um valor positivo e razoável.tente novamente.")
                continue 

            return idade
        except ValueError:
           
            print("ERRO: A idade deve ser um número inteiro. não digite letras ou caracteres especiais.")
        except Exception as e:
           
            print(f"Ocorreu um erro inesperado ao processar a idade: {KeyError}")

def cadastro_principal():
    print("Iniciando seu cadastro:")

    nome_usuario = nome_valido()
    idade_usuario =idade_valida()

    print("\n--- Cadastro Finalizado ---")
    print(f"Nome: {nome_usuario}")
    print(f"Idade: {idade_usuario} anos")
cadastro_principal()