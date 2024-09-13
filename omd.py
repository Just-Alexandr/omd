# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_no_umbrella():
    print('На улице резко пошёл дождь')
    print('Как же хорошо быть уткой 🦆')


def step2_umbrella():
    print('Зонтик оказался дырявым')
    step2_no_umbrella()


if __name__ == '__main__':
    step1()
