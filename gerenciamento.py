#codigo de inicialização do programa, onde o programa é executado

def main():
  biblioteca = Biblioteca()

  while True:
      print("\n1. Adicionar livro")
      print("2. Remover livro")
      print("3. Pesquisar por título")
      print("4. Pesquisar por autor")
      print("5. Exibir todos os livros")
      print("6. Sair")

      escolha = input("\nEscolha uma opção: ")

      if escolha == '1':
          titulo = input("Digite o título do livro: ")
          autor = input("Digite o nome do autor: ")
          ano = input("Digite o ano de publicação: ")
          livro = Livro(titulo, autor, ano)
          biblioteca.adicionar_livro(livro)
      elif escolha == '2':
          titulo = input("Digite o título do livro que deseja remover: ")
          biblioteca.remover_livro(titulo)
      elif escolha == '3':
          titulo = input("Digite o título do livro que deseja pesquisar: ")
          biblioteca.pesquisar_por_titulo(titulo)
      elif escolha == '4':
          autor = input("Digite o nome do autor que deseja pesquisar: ")
          biblioteca.pesquisar_por_autor(autor)
      elif escolha == '5':
          biblioteca.exibir_todos()
      elif escolha == '6':
          print("Saindo do programa...")
          break
      else:
          print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
  main()
class Livro:
    # informacoes sobre o livro
  def __init__(self, titulo, autor, ano):
      self.titulo = titulo
      self.autor = autor
      self.ano = ano
    # onde é salvo
class Biblioteca:
  def __init__(self):
      self.livros = []
    # o livro é adicionado na biblioteca
  def adicionar_livro(self, livro):
      self.livros.append(livro)
      print("Livro adicionado com sucesso!")
    # o livro é removido da biblioteca
  def remover_livro(self, titulo):
      for livro in self.livros:
          if livro.titulo == titulo:
              self.livros.remove(livro)
              print("Livro removido com sucesso!")
              return
      print("Livro não encontrado na biblioteca.")
      
    # pesquisa pelo titulo do livro
    
  def pesquisar_por_titulo(self, titulo):
      encontrados = [livro for livro in self.livros if livro.titulo.lower() == titulo.lower()]
      if encontrados:
          for livro in encontrados:
              print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
      else:
          print("Nenhum livro encontrado com este título.")
          
    # pesquisa pelo autor do livro
    
  def pesquisar_por_autor(self, autor):
      encontrados = [livro for livro in self.livros if livro.autor.lower() == autor.lower()]
      if encontrados:
          for livro in encontrados:
              print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
      else:
          print("Nenhum livro encontrado deste autor.")

    # mostra todos os livros registrados na biblioteca
    
  def exibir_todos(self):
      if self.livros:
          for livro in self.livros:
              print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
      else:
          print("A biblioteca está vazia.")




