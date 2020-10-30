
questions = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '4',
            'b': '3',
            'c': '8'
        },
        'resposta_certa': 'a',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 7 + 3?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '8'
        },
        'resposta_certa': 'b',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 3 * 3?',
        'respostas': {
            'a': '6',
            'b': '3',
            'c': '9'
        },
        'resposta_certa': 'c',
    },
}

answer_count = 0
for pk, pv in questions.items():
    print(f'{pk}: {pv["pergunta"]}')
    print("Answer the question:")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    answer_user = input('Your answer:')
    if answer_user == pv['resposta_certa']:
        print("Right choice!")
        answer_count += 1
    else:
        print("Wrong answer")
