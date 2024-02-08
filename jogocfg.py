import os

import random

PEDRA = '1'
PAPEL = '2'
TESOURA = '3'

CHOICES = {
    PEDRA: "Pedra",
    PAPEL: "Papel",
    TESOURA: "Tesoura"
}


def show_choices():
    return (
        'Options: \n'
        f'--Pedra: {PEDRA} \n'
        f'--Papel: {PAPEL} \n'
        f'--Tesoura: {TESOURA} \n'
        f'Choose one pls: '
    )


def get_result(player, computador):
    if player == computador:
        resultado = 'empate'
    elif player == '1':
        if computador == '2':
            resultado = 'perdeu'
        elif computador == '3':
            resultado = 'ganhou'
    elif player == '2':
        if computador == '3':
            resultado = 'perdeu'
        elif computador == '1':
            resultado = 'ganhou'
    elif player == '3':
        if computador == '1':
            resultado = 'Perdeu'
        elif computador == '2':
            resultado = 'Ganhou'
    else:
        resultado = ''

    print('-' * 80)
    print(
        f'Escolha do computador: {CHOICES[computador]} \n'
        f'Escolha do jogador: {CHOICES[player]} \n'
        f'Resultado: {resultado} \n'
)
    print('-' * 80)
    return resultado


def play():
    while True:
        # escolhas = ['pedra', 'papel', 'tesoura']
        escolhas = [PEDRA, PAPEL, TESOURA]
        computador = random.choice(escolhas)
        player = input(show_choices()).lower()
        while player not in escolhas:
            player = input(f'Escolha invalida! \n\n {show_choices()}').lower()

        get_result(player, computador)
        play_again = input("Voce quer jogar dnv?: (yes/no):").lower()
        if play_again not in ["yes", "y", "s"]:
            print("Bye!")
            break
        print("Again? Ok, let's go!")
        print("_" * 80)


if __name__ == '__main__':
    play()


