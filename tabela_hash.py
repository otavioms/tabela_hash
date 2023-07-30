#1. Implementação de uma classe chamada TabelaHash que será responsável por armazenar os nomes na tabela hash.
class TabelaHash:
  def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho


  def obter_indice(self, nome):
    """ O método obter_indice recebe um nome como parâmetro e permite ao usuário escolher uma função hash. """
    escolha_hash = input("Escolha a função hash: 1 - Divisão, 2 - Dobras, 3 - Multiplicação: ")
    if escolha_hash == "1":
        indice = self.hash_divisao(nome)
    elif escolha_hash == "2":
        indice = self.hash_dobra(nome)
    elif escolha_hash == "3":
        indice = self.hash_multiplicacao(nome)
    else:
        raise ValueError("Opção inválida.")
    return indice


#3. Função hash_divisao que recebe um nome como parâmetro e retorna o índice da tabela hash.
  """ A função 'hash_divisao' percorre cada caractere do nome, converte-o em seu valor numérico ASCII usando a função ord e soma esses valores.
      Em seguida, aplica o método da divisão utilizando o tamanho da tabela hash para calcular o índice. """
  def hash_divisao(self, nome):
        soma = sum(ord(c) for c in nome)
        indice = soma % self.tamanho
        print("Valor gerado:", soma)
        return indice


#4. Função hash_dobra que recebe um nome como parâmetro e retorna o índice da tabela hash.
  """ A função 'hash_dobra' também percorre cada caractere do nome, converte-o em seu valor numérico ASCII, soma esses valores e calcula dois índices parciais.
      O índice final é a soma dos dois índices parciais módulo o tamanho da tabela hash. """
  def hash_dobra(self, nome):
        soma = sum(ord(c) for c in nome)
        indice1 = soma % self.tamanho
        indice2 = soma // self.tamanho % self.tamanho
        indice = (indice1 + indice2) % self.tamanho
        print("Valor gerado:", soma)
        print("Valor índice:", indice)
        return indice


#5. Função hash_multiplicacao que recebe um nome como parâmetro e retorna o índice da tabela hash.
  """ A função 'hash_multiplicacao' usa uma constante (A) para melhorar a distribuição dos índices.
      Novamente, percorre cada caractere do nome, converte-o em seu valor numérico ASCII, soma esses valores e multiplica pela constante (A). """
  def hash_multiplicacao(self, nome):
        A = (5 ** 0.5 - 1) / 2  # Calcula a constante conhecida como proporção áurea, com o intuito de melhorar a distribuição dos valores de hash na tabela.
        soma = sum(ord(c) for c in nome)
        indice = int(self.tamanho * ((soma * A) % 1))
        print("Valor gerado:", soma)
        print("Valor índice:", indice)
        return indice


#2. Métodos necessários para adicionar, buscar e remover nomes na tabela:
  """ O método 'adicionar' calcula o índice usando a função de hash escolhida e adiciona o nome à lista correspondente na tabela hash. """
  def adicionar(self, nome):
        indice = self.obter_indice(nome)
        if self.tabela[indice] is None:
            self.tabela[indice] = nome
        else:
            print("Colisão ocorreu. Resolvendo colisão...")
            self.tratar_colisao(indice, nome)


##6. Tratamento de colisões.
  def tratar_colisao(self, indice, nome):
        escolha_colisao = input("Escolha o método de tratamento de colisão: 1 - Encadeamento Exterior, 2 - Encadeamento Interior, 3 - Endereçamento Aberto (Tentativa Sequencial): ")
        if escolha_colisao == "1":
            self.encadeamento_exterior(indice, nome)
        elif escolha_colisao == "2":
            self.encadeamento_interior(indice, nome)
        elif escolha_colisao == "3":
            self.enderecamento_aberto(indice, nome)
        else:
            raise ValueError("Opção inválida.")


  """ A função 'encadeamento_exterior' direciona elementos em uma zona de colisões, que é representada por uma lista na posição de colisão.
      Se a posição de colisão já contiver uma lista, o elemento é simplesmente adicionado a essa lista. Caso contrário, uma nova lista é criada contendo o elemento existente e o novo elemento. """
  def encadeamento_exterior(self, indice, nome):
      if isinstance(self.tabela[indice], list):
          self.tabela[indice].append(nome)
      else:
          self.tabela[indice] = [self.tabela[indice], nome]


  """ A A função 'encadeamento_interior' recebe um índice inicial e um elemento a ser inserido na tabela.
  A função realiza uma sondagem linear para encontrar uma posição vazia na tabela, percorrendo as posições sequencialmente a partir do índice inicial, até encontrar uma posição vazia para inserir o elemento.  """
  def encadeamento_interior(self, indice, nome):
      i = 1
      while True:
          indice_tentativo = (indice + i) % self.tamanho
          if self.tabela[indice_tentativo] is None:
              self.tabela[indice_tentativo] = nome
              break
          i += 1


  """ A função 'enderecamento_aberto' utiliza uma estratégia de sondagem linear para encontrar uma posição vazia na tabela.
      Ela começa a partir da posição de colisão inicial e, em cada iteração, calcula o próximo índice adicionando um deslocamento linearmente crescente ao índice original.  """
  def enderecamento_aberto(self, indice, nome):
      i = 1
      while True:
          indice_tentativo = (indice + i) % self.tamanho
          if self.tabela[indice_tentativo] is None:
              self.tabela[indice_tentativo] = nome
              break
          i += 1


  """ O método 'buscar' percorre a tabela hash e verifica se o nome está presente em alguma das listas. """
  def buscar(self, nome):
        indice = self.obter_indice(nome)
        if self.tabela[indice] == nome:
            return True
        elif isinstance(self.tabela[indice], list):
            if nome in self.tabela[indice]:
                return True
        return False


  """ O método 'remover' também calcula o índice e remove o nome da lista correspondente, se estiver presente. """
  def remover(self, nome):
      indice = self.obter_indice(nome)
      if self.tabela[indice] == nome:
          self.tabela[indice] = None
      elif isinstance(self.tabela[indice], list):
          if nome in self.tabela[indice]:
              self.tabela[indice].remove(nome)
      else:
          raise KeyError("Nome não encontrado.")


#9. Exição da tabela hash atualizada após cada operação.
""" A função 'exibir_tabela' é definida fora da classe e é usada para exibir o conteúdo da tabela hash. """
def exibir_tabela(tabela):
    print("Tabela Hash:")
    for indice, elemento in enumerate(tabela):
        print(f"Índice {indice}: {elemento}")


#7. Solicita ao usuário qual tipo de função hash deseja utilizar. #8. Além da criação do loop, que permite interagir até que ele decida sair do programa.
""" A função 'main' é responsável pela interação com o usuário.
Ela solicita o tamanho da tabela hash, cria uma instância da classe TabelaHash com o tamanho fornecido
e apresenta um menu de opções para adicionar, buscar ou remover nomes.  O loop continua até que o usuário escolha a opção para sair. """
def main():
    tamanho_tabela = int(input("Digite o tamanho da tabela hash: "))
    tabela_hash = TabelaHash(tamanho_tabela)

    while True:
        print("\n1 - Adicionar nome")
        print("2 - Buscar nome")
        print("3 - Remover nome")
        print("4 - Exibir tabela hash")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome a ser adicionado: ")
            tabela_hash.adicionar(nome)
        elif opcao == "2":
            nome = input("Digite o nome a ser buscado: ")
            if tabela_hash.buscar(nome):
                print("Nome encontrado.")
            else:
                print("Nome não encontrado.")
        elif opcao == "3":
            nome = input("Digite o nome a ser removido: ")
            try:
                tabela_hash.remover(nome)
                print("Nome removido com sucesso.")
            except KeyError as e:
                print(str(e))
        elif opcao == "4":
            exibir_tabela(tabela_hash.tabela)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Digite novamente.")


if __name__ == "__main__":
    main()

