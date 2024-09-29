import os
from time import sleep
import ast


id_global = None

#********************************** LOGIN ************************************************************
#função logar 
def login():
    login = input("Digite o seu login (CPF): ")
    
    valido_cpf = False
    senha_login = None
    id_login = None  
    
    sucesso = False
    
    with open("usuarios.txt", "r") as arquivo:
        lista_cadastros = arquivo.readlines()
        for cadastro in lista_cadastros:
            dados = cadastro.split(",")
            if(dados[5] == login):
                valido_cpf = True
                senha_login = dados[6][:-1]
                id_login = dados[0]
               
    
    if valido_cpf:
        senha = input("Digite sua senha: ")  
        if senha == senha_login:
            sleep(1)
            os.system('cls') or None
            print("Bem vindo ao Scout Futsal!")
            id_global = id_login
            sucesso = True
        else:
            print("Senha incorreta.")
            return sucesso,1

    else:
        print("CPF não cadastrado!")
        return sucesso,2
    
    return sucesso,0

#Função para redefinir a senha        
def redefinir_senha():
    nova_senha = input("Digite a nova senha: ")
    confirma_senha = input("Confirme a nova senha: ")
    with open("usuarios.txt", "a") as arquivo:
        print(arquivo.readlines())
    if nova_senha == confirma_senha:
        print("Senha redefinida com sucesso!")
    else:
        print("As senhas não coincidem. Tente novamente.")
    

#Função para cadastrar usuário
def cadastrar_usuario():
  nome = input("Digite seu nome para realizar o cadastro: ")
  idade = int(input("Digite sua idade: "))
  email = str(input("Digite seu e-mail: "))
  telefone = str(input("Digite seu número de telefone: "))
  cpf_treinador = str(input("Digite seu cpf: "))
  senha_treinador = str(input("Digite sua senha: "))
  id = None
  with open("usuarios.txt", "r") as temp:
      id = len(temp.readlines())
  with open("usuarios.txt", "a") as arquivo:
    arquivo.write(f"{id},{nome},{idade},{email},{telefone},{cpf_treinador},{senha_treinador}\n")

  print("Usuário cadastrado com sucesso!")

  



#*********************************** MENU DE OPÇÕES *********************************************
#Função para exibir o menu de opções
def exibir_menu():

    print("======= Menu =======")
    print("1. Registrar Atleta")
    print("2. Remover Atleta")
    print("3. Registrar Treino")
    print("4. Remover Treino")
    print("5. Registrar Partida")
    print("6. Remover Partida")
    print("7. Previsão por Atleta")
    print("8. Montagem de Equipe")
    print("9. Sair")
    print("====================")
    

#Função para registrar atletas
def registrar_atleta():
    # Solicita os dados do atleta
    camisa = input("Digite o numero de camisa do atleta: ")
    nome = input("Digite o nome do atleta: ")
    idade = input("Digite a idade do atleta: ")
    posicao = input("Digite a posição do atleta: ")
        
    # Abre o arquivo em modo de adição e escreve os dados
    with open("atleta.txt", "a") as arquivo:
        arquivo.write(f"{camisa},{nome},{idade},{posicao}\n")

    print("Atleta registrado com sucesso!")

#Função para imprimir atletas
def imprimir_atletas(arquivo):
    with open(arquivo, "r") as imprimir:
        lista_atletas = imprimir.readlines()
        for atleta in lista_atletas:
            dados = atleta.split(",")
        print(dados)


#Função para remover atleta
def remover_atleta(arquivo, n_c):
    
    # Lê todos os dados do arquivo
    with open(arquivo, "r") as f:
        lista_atletas = f.readlines()

    # Filtra os atletas que não serão removidos
    lista_atletas_filtrada = []
    for atleta in lista_atletas:
        dados = atleta.split(",")
        
        if dados[0].strip() != n_c:  
            lista_atletas_filtrada.append(atleta)

    # Escreve a lista filtrada de volta no arquivo
    with open(arquivo, "w") as f:
        f.writelines(lista_atletas_filtrada)

    print(f"Atleta com número {n_c} removido com sucesso, se ele existia.")

# Dicionário para armazenar os dados de treino dos atletas
dic_treino = {}

# Função para coletar e registrar dados do atleta
def registrar_dados_atleta():
    id = int(input("Digite o ID do atleta: "))
    nome = input("Digite o nome do atleta: ")
    data_treino = input("Digite a data do treino (DD/MM/AAAA): ")
    cobertura_ofensiva = float(input("Digite a cobertura ofensiva (de 0 a 10): "))
    cobertura_defensiva = float(input("Digite a cobertura defensiva (de 0 a 10): "))
    penetracao = float(input("Digite a penetração (de 0 a 10): "))
    impulsao = float(input("Digite a impulsão (de 0 a 10): "))
    mobilidade = float(input("Digite a mobilidade (de 0 a 10): "))
    qualidade_passe = float(input("Digite a qualidade do passe (de 0 a 10): "))
    qualidade_recepcao = float(input("Digite a qualidade da recepção (de 0 a 10): "))
    finalizacoes = int(input("Digite o número de finalizações: "))
    gols = int(input("Digite o número de gols: "))

    # Armazena os dados do atleta no dicionário
    dic_treino[id] = {
        'id': id,
        'nome': nome,
        'data_treino': data_treino,
        'cobertura_ofensiva': cobertura_ofensiva,
        'cobertura_defensiva': cobertura_defensiva,
        'penetracao': penetracao,
        'impulsao': impulsao,
        'mobilidade': mobilidade,
        'qualidade_passe': qualidade_passe,
        'qualidade_recepcao': qualidade_recepcao,
        'finalizacoes': finalizacoes,
        'gols': gols
    }

    print("Dados do atleta registrados com sucesso!")
    print(dic_treino)

    with open("treino.txt", 'a') as t:
        t.write(repr(dic_treino[id]) + '\n')
        #t.write(f"{dic_treino[id]}\n")


#Função para imprimir treinos
def imprimir_dados_treino():
    try:
        with open("treino.txt", 'r') as t:
            for linha in t:
                # Divide a linha pelos delimitadores (vírgulas)
                dados = linha.strip().split(',')
                print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

#Função para remover treino
def remover_treino(arquivo, id):
    # Lista para armazenar os dados que serão mantidos
    dados_mantidos = []
    encontrado = False
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                # Converte a string de volta para um dicionário
                dados = ast.literal_eval(linha.strip())
                
                # Verifica se o ID do atleta é diferente do ID a ser removido
                if dados.get('id') != id:
                    dados_mantidos.append(linha)
                else:
                    encontrado = True

        # Grava os dados mantidos de volta no arquivo
        with open(arquivo, 'w') as t:
            t.writelines(dados_mantidos)

        if encontrado:
            print(f"Atleta com ID {id} removido com sucesso.")
        else:
            print(f"Atleta com ID {id} não encontrado.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Erro ao processar o ID. Verifique se ele é um número inteiro.")
    except SyntaxError:
        print("Erro de sintaxe ao processar o arquivo. Verifique o formato dos dados.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para ler os dados do arquivo e transformar em uma lista de dicionários
def ler_dados_arquivo(caminho_arquivo):
    dados_atletas = []
    
    # Lê o arquivo linha por linha
    with open(caminho_arquivo, 'r') as file:
        for linha in file:
            linha_limpa = linha.strip()  # Remove espaços em branco e quebras de linha
            
            if not linha_limpa:
                continue  # Ignora linhas vazias
            
            try:
                # Converte a linha (string) em um dicionário
                atleta = ast.literal_eval(linha_limpa)
                dados_atletas.append(atleta)
            except (SyntaxError, ValueError) as e:
                print(f"Erro ao converter linha para dicionário: {e}")
    
    return dados_atletas



# Função que compara e sinaliza o melhor pivô
def melhor_pivo(caminho_arquivo):

    # Chama a função para ler os dados do arquivo
    dados_atletas_dois = ler_dados_arquivo(caminho_arquivo)

    # Verifica se dados_atletas não está vazio
    if not dados_atletas_dois:
        print("Nenhum atleta encontrado.")
        return None

    # Variáveis para armazenar o nome do atleta com a maior média e a própria média
    maior_media = 0
    melhor_atleta = None  

    # Itera sobre cada atleta e calcula a média
    for atleta in dados_atletas_dois:
        # Extrai os valores relevantes
        valores = [
            atleta.get('impulsao', 0),
            atleta.get('mobilidade', 0),
            atleta.get('cobertura_ofensiva', 0),
            atleta.get('finalizacoes', 0)
        ]
        
        # Calcula a média dos atributos
        media = sum(valores) / len(valores)
        
        # Compara a média e atualiza se for a maior
        if media > maior_media:
            maior_media = media
            melhor_atleta = atleta.get('nome', 'Atleta Desconhecido')  # Previne erro se 'nome' estiver ausente

    # Retorna o atleta com a maior média
    if melhor_atleta:
        print(f"O atleta considerado melhor pivô é {melhor_atleta} com uma média de {maior_media:.2f} dentre seus atributos!")
        return melhor_atleta, maior_media
    else:
        print("Nenhum atleta foi encontrado.")
        return None
    
    
    
# Função que compara e sinaliza o melhor fixo
def melhor_fixo(caminho_arquivo):

    # Chama a função para ler os dados do arquivo
    dados_atletas_dois = ler_dados_arquivo(caminho_arquivo)

    # Verifica se dados_atletas não está vazio
    if not dados_atletas_dois:
        print("Nenhum atleta encontrado.")
        return None

    # Variáveis para armazenar o nome do atleta com a maior média e a própria média
    maior_media = 0
    melhor_atleta = None  

    # Itera sobre cada atleta e calcula a média
    for atleta in dados_atletas_dois:
        # Extrai os valores relevantes
        valores = [
            atleta.get('qualidade_passe', 0),
            atleta.get('cobertura_defensiva', 0),
        ]
        
        # Calcula a média dos atributos
        media = sum(valores) / len(valores)
        
        # Compara a média e atualiza se for a maior
        if media > maior_media:
            maior_media = media
            melhor_atleta = atleta.get('nome', 'Atleta Desconhecido')  # Previne erro se 'nome' estiver ausente

    # Retorna o atleta com a maior média
    if melhor_atleta:
        print(f"O atleta considerado melhor Fixo é {melhor_atleta} com uma média de {maior_media:.2f} dentre seus atributos!")
        return melhor_atleta, maior_media
    else:
        print("Nenhum atleta foi encontrado.")
        return None
    
# Função que compara e sinaliza o melhor ala
def melhor_ala(caminho_arquivo):

    # Chama a função para ler os dados do arquivo
    dados_atletas_dois = ler_dados_arquivo(caminho_arquivo)

    # Verifica se dados_atletas não está vazio
    if not dados_atletas_dois:
        print("Nenhum atleta encontrado.")
        return None

    # Variáveis para armazenar o nome do atleta com a maior média e a própria média
    maior_mediaA = 0
    melhor_atletaA = None  

    # Itera sobre cada atleta e calcula a média
    for atleta in dados_atletas_dois:
        # Extrai os valores relevantes
        valores = [
            atleta.get('qualidade_recepcao', 0),
        ]
        
        # Calcula a média dos atributos
        media = sum(valores) / len(valores)
        
        # Compara a média e atualiza se for a maior
        if media > maior_mediaA:
            maior_mediaA = media
            melhor_atletaA = atleta.get('nome', 'Atleta Desconhecido')  # Previne erro se 'nome' estiver ausente

    # Retorna o atleta com a maior média
    if melhor_atletaA:
        print(f"O atleta considerado melhor Ala é {melhor_atletaA} com uma média de {maior_mediaA:.2f} dentre seus atributos!")
        return melhor_atletaA, maior_mediaA
        
    else:
        print("Nenhum atleta foi encontrado.")
        return None

#Função para montar equipe ofensiva
def equipe_ofensiva(caminho_arquivo):

    # Chama a função para ler os dados do arquivo
    dados_atletas_dois = ler_dados_arquivo(caminho_arquivo)

    # Verifica se dados_atletas_dois não está vazio
    if not dados_atletas_dois:
        print("Nenhum atleta encontrado.")
        return None

    # Lista para armazenar as médias de cada atleta
    medias_atletas = []

    # Itera sobre cada atleta e calcula a média
    for atleta in dados_atletas_dois:
        # Extrai os valores relevantes
        valores = [
            atleta.get('cobertura_ofensiva', 0),  
        ]
        
        # Calcula a média dos atributos
        media = sum(valores) / len(valores) if valores else 0  
        
        # Adiciona o atleta e sua média à lista
        medias_atletas.append((atleta.get('nome', 'Atleta Desconhecido'), media))

    # Ordena a lista de médias em ordem decrescente
    medias_atletas.sort(key=lambda x: x[1], reverse=True)

    # Imprime os 5 atletas com as maiores médias
    print("Os 5 melhores jogadores em cobertura ofensiva são:")
    for atleta, media in medias_atletas[:5]:  
        print(f"{atleta} com uma média de {media:.2f}.")

    return medias_atletas[:5]  


#Função para montar equipe defensiva
def equipe_defensiva(caminho_arquivo):

    # Chama a função para ler os dados do arquivo
    dados_atletas_dois = ler_dados_arquivo(caminho_arquivo)

    # Verifica se dados_atletas_dois não está vazio
    if not dados_atletas_dois:
        print("Nenhum atleta encontrado.")
        return None

    # Lista para armazenar as médias de cada atleta
    medias_atletas = []

    # Itera sobre cada atleta e calcula a média
    for atleta in dados_atletas_dois:
        # Extrai os valores relevantes
        valores = [
            atleta.get('cobertura_defensiva', 0),  
        ]
        
        # Calcula a média dos atributos
        media = sum(valores) / len(valores) if valores else 0  
        
        # Adiciona o atleta e sua média à lista
        medias_atletas.append((atleta.get('nome', 'Atleta Desconhecido'), media))

    # Ordena a lista de médias em ordem decrescente
    medias_atletas.sort(key=lambda x: x[1], reverse=True)

    # Imprime os 5 atletas com as maiores médias
    print("Os 5 melhores jogadores em cobertura defensiva são:")
    for atleta, media in medias_atletas[:5]:  
        print(f"{atleta} com uma média de {media:.2f}.")

    return medias_atletas[:5]


#Função principal onde se encontra o menu de opções
def main():
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
    
        match opcao: 
            case "1":
                sleep(1)
                os.system('cls') or None
                print("Você escolheu a opção: \n 1. Registrar Atleta")
                sleep(1)
                os.system('cls') or None
                registrar_atleta()
                imprimir_atletas("atleta.txt")

            case "2":
                sleep(1)
                os.system('cls') or None
                print("Você selecionou a opção: \n 2. Remover Atleta")
                sleep(1)
                os.system('cls') or None
                imprimir_atletas("atleta.txt")
                num_camisa = input("Digite o número do jogador que deseja remover: ")
                remover_atleta("atleta.txt",n_c = num_camisa)

            case "3":
                sleep(1)
                os.system('cls') or None
                print("Você escolheu a opção: \n 3. Registrar Treino")
                sleep(1)
                os.system('cls') or None
                registrar_dados_atleta()
                sleep(3)
                os.system('cls') or None

            case "4":
                sleep(1)
                os.system('cls') or None
                print("Você selecionou a opção: \n 4. Remover Treino") 
                imprimir_dados_treino()
                print("=============================================")
                id_remover = int(input("Digite o Id do treino que deseja remover: "))
                sleep(1)
                os.system('cls') or None
                remover_treino("treino.txt", id = id_remover)
                    
            case "5":
                sleep(1)
                os.system('cls') or None
                print("Você selecionou a opção: \n 5. Registrar Partida ") #Em construção

            case "6":
                sleep(1)
                os.system('cls') or None
                print("Você selecionou a opção: \n 6. Remover Partida ") #Em construção

            case "7":
                sleep(1)
                os.system('cls') or None
                print("Você selecionou a opção: \n 7. Previsão por Atleta ")
                melhor_pivo('treino.txt')
                melhor_fixo('treino.txt')
                melhor_ala('treino.txt')

            case "8":
                sleep(1)
                os.system('cls') or None
                print("Você escolheu a opção Montagem de Equipe ")
                sleep(1)
                os.system('cls') or None
                equipe_ofensiva('treino.txt')
                print("================================================")
                equipe_defensiva('treino.txt')
                

            case "9":
                sleep(1)
                os.system('cls') or None
                print("Saindo...")
                break

            case _:
                os.system('cls') or None
                print("Opção inválida!\n")
                sleep(0.5)
                os.system('cls') or None


if __name__ == "__main__":
    teste = login()
    if(teste[0]):
        sleep(1)
        os.system('cls') or None
        main()
    else:
        if(teste[1] == 2):
            print('Erro de cpf')
            while(not(teste[0])):
                
                usuario = (input("Deseja realizar cadastro? 0 == Não e 1 == Sim"))
                match usuario:
                    case '0':
                        break
                    case '1':
                        cadastrar_usuario()
                        teste = login()
                    case _:
                        print('inválido')
                
        elif(teste[1] == 1):
            print('Entre com uma senha válida ')



    














