txt_index = '''Ваш индекс Руфье:'''
txt_workheart = '''Работоспособность сердца'''
txt_nodata = '''Нет данных для такого возраста'''
txt_res = []
txt_res.append('''Низкая.
Срочно обратитесь к врачу!''')
txt_res.append('''Удовлетворительный.
Обратитесь к врачу!''')
txt_res.append('''Средняя.
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''Выше среднего.
В ближайшее время обратитесь к врачу''')
txt_res.append('''Высокая.
Срочно обратитесь к врачу!''')


def ruffier_index(p1, p2, p3):
    '''Возвращает значение индекса по трем показателям пульса для сверки с таблицей'''
    return(4* (p1+p2+p3) - 200) / 10

def neud_level(age):
    '''Варианты с возрастом меньше 7 и взрослым надо обрабатывать отдельно,
    здесь подбираем уровень "неуд" только внутри таблицы:
    в возрасте 7 лет "неуд" - это индекс 216 дальше каждые 2 года он понижается.'''
    norm_age = (min(age, 15)-7) // 2
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    '''Функция получает индекс Руфье и интепретирует его,
    возвращает уровень готовности: число от '''
    if r_index >= level:
        return 0
    level = level -4
    if  r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4


def test(p1, p2, p3, age):
    '''Эту функцию можно использовать снаружи модуля для подсчетов индекса Руфье.
    Возвращает готовые тексты, которые остается нарисовать в нужном месте
    Использует для текстов константы, заданные в начале этого модуля.'''
    if age < 7:
        return (txt_index + '0', txt_nodata)
    else:
        ruff_index = ruffier_index(p1, p2, p3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + '\n' + str(ruff_index) + '\n' + txt_workheart + '\n' + result
        return res