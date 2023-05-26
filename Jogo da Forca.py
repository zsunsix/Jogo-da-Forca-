import random #importa uma biblioteca que trás funções aleatorias

palavras = ["Harry", "Hermione", "Voldemort", "Snape", "Coruja"]

palavra = random.choice(palavras)
tentativas = 0
cc = len(palavra)
chance = 5

letra_escolhida = []

palavra_atual = ["_"] * len(palavra)

print("Bem vindo ao Torneio")
print("Seu objetivo é acertar os personagem do maior filme de magia")
print("Você tera apenas 5 chances para acertar, caso erre será enfeitiçado")

while tentativas < chance:
    opcao = int(input("Escolha 1 para chutar e 2 para continuar "))

    if opcao == 1:
        chute = input("Digite o nome que voce acha que é")
        if chute == palavra:
            print("Você acertou")
            break
        else:
            print("Você errou")
            break
    else:
        letra = input("\nEscolha uma letra ! ").lower()

        while letra in letra_escolhida:
            print("Letra ja escolhida, tente novamente !")
            letra = input("\nEscolha uma letra !")
        letra_escolhida.append(letra)

        if letra in palavra.lower():
            print("A letra esta presente")
            for i in range(len(palavra)):
                if letra == palavra[i].lower():
                    palavra_atual[i] = letra
                    cc -= 1
        else:
            print("Você perdeu 1 tentativa")
            tentativas = tentativas + 1

        print("Restam ", chance - tentativas, "tentativas")
        print("Estado atual do nome")
        print(palavra_atual)

        if cc == 0:
            break

        print("\nAs letras que foram tentadas são:")
        print(", ".join(letra_escolhida))

if tentativas == chance:
    print("Você foi enfeitiçado")

else:
    print("Parabens você se tornou um aluno de Hogwarts!")


print("A palavra era", palavra)



