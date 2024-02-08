# perguntas = {
#     "Quantos anos edu tem?" : "A",
#     "Quantos irmaos edu tem?" : "B",
#     "Qual o nome de seu irmao:" : "C"
# }
#
# opçoes = {'A' : "A. 17 anos, B. 18 anos, C. 16 anos",
#           'B' : "A. 0 irmaos, B. 1 irmao, C. 2 irmaos",
#           'C' : "A. Matheus, B. Chaves, C. Rafael"
# }
#
# question_number = 1
# def play():
#     for key in perguntas:
#         print('\n', '_' * 50)
#         print('\n',key)
#         for key in opçoes:
#             print(opçoes.values(-1))
#     print('\n',"_" * 50)
#
#
# play()


def jogar():
    while True:
        print("Quantos anos edu tem?:")
        print("-" * 50)
        print(" A: 16 anos", "\n", "B: 17 anos", "\n", "C: 18 anos")
        print("-" * 50)
        escolha = input("escolha:").upper()
        if escolha not in ["B"]:
            print("-" * 50, "\n", "voce errou, tente denovo!", "\n", "-" * 50)
        else:
            print("Voce Acertou. Parabens!!!")
            break

    play_again = input("Voce quer jogar mais?: (yes/no):").lower()
    if play_again not in ["yes", "y", "s"]:
        print("Bye!")
    print("Bora mais uma entao!")

    while True:
        print("Quantos irmaos edu tem?:")
        print("-" * 50)
        print(" A: 1", "\n", "B: 0", "\n", "C: 2")
        print("-" * 50)
        escolha = input("escolha:").upper()
        if escolha not in ["A"]:
            print("-" * 50, "\n", "voce errou, tente denovo!", "\n", "-" * 50)
        else:
            print("Voce Acertou. Parabens!!!")
            break


jogar()

teste_git = True
