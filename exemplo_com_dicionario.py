perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b':'4',  'c': '5', 'd':'7',},
        'resposta_certa':'4'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 * 5?',
        'respostas': {'a': '5', 'b':'10',  'c': '25', 'd':'2',},
        'resposta_certa':'25'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 8 * 2 * 5 - 5?',
        'respostas': {'a': '75', 'b':'80',  'c': '0', 'd':'40',},
        'resposta_certa':'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 4 / 2 * 5?',
        'respostas': {'a': '6', 'b':'12',  'c': '10', 'd':'2',},
        'resposta_certa':'c'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 10 * 5 + 4?',
        'respostas': {'a': '5', 'b':'10',  'c': '50', 'd':'54',},
        'resposta_certa':'d'
    },

}
print()

resposta_certas=0
for pk , pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas : ')

    for rk , rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user=input('Sua resposta: ')

    if resposta_user == pv['resposta_certa']:
        print('Está correto')
        resposta_certas+=1
    else:
        print('ERROU')
    print()


qtd_perguntas=len(perguntas)
porcentagem_acertos=resposta_certas / qtd_perguntas * 100

print(f'Você acertou {resposta_certas} perguntas de {len(perguntas)}')
print(f'Você teve {porcentagem_acertos}% de acertos')