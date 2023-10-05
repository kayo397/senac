import random

def jogar():
    random_word = random.choice(words_game)
    display_word = ['_' if letra != ' ' else ' ' for letra in random_word]
    
    print(f"\nA palavra a seguir possui {len(random_word)} letras")
    print(f"Dica: {tips.get(random_word, 'Desculpe, sem dica disponível para esta palavra.')}")
    print(' '.join(display_word))
    
    error_limit = int(input("\nInsira o limite de erros: "))
    
    used_letters = ["1"]
    
    while error_limit > 0:
        print("\nInsira 1 para ver letras já usadas")
        print("Insira 2 para ver a dica novamente")
        tentativa = input("\nInsira uma letra: ")
    
        if tentativa == "1":
            print(f"\nLetras usadas: {', '.join(used_letters[1:])}")
    
        elif tentativa == "2":
            print(f"\nDica: {tips.get(random_word, 'Desculpe, sem dica disponível para esta palavra.')}")
    
        elif tentativa in used_letters:
            print("\nVocê já tentou essa letra. Tente novamente.")
    
        elif tentativa in random_word:
            for i in range(len(random_word)):
                if random_word[i] == tentativa:
                    display_word[i] = tentativa
            used_letters.append(tentativa)
            print("\nVocê acertou a letra!")
            print(' '.join(display_word))
            
            # Verificar se todas as letras foram adivinhadas
            if all(letra != '_' for letra in display_word):
                print("\nParabéns! Você adivinhou a palavra!")
                break
    
        else:
            used_letters.append(tentativa)
            error_limit -= 1
            print("\nEssa letra não está na palavra.")
            print(f"Tentativas restantes: {error_limit}")
            print(' '.join(display_word))
    
    if error_limit == 0:
        print(f"\nLimite de tentativas alcançado. A palavra era: {random_word}")
    else:
        print("")

# Inicializando lista de palavras e dicas
words_game = ("python", "programação", "desenvolvimento", "tecnologia", "gerador")
tips = {
    "python": "Uma linguagem de programação popular.",
    "programação": "Processo de escrita, teste e manutenção de um programa de computador.",
    "desenvolvimento": "Conjunto de atividades necessárias para transformar uma ideia em um produto.",
    "tecnologia": "Conjunto de técnicas, habilidades, métodos e processos utilizados na produção de bens ou serviços.",
    "gerador": "Dispositivo que converte uma forma de energia em outra."
}

# Modo de dois jogadores
while True:
    print("Modo de Dois Jogadores:")
    print("Jogador 1, é sua vez!")
    input("Pressione Enter para continuar...")
    jogar()
    
    print("\n\nModo de Dois Jogadores:")
    print("Jogador 2, é sua vez!")
    input("Pressione Enter para continuar...")
    jogar()
    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != 's':
        break
