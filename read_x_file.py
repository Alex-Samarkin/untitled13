import pandas as pd

def read_data_debug(filename):
    # читаем сырые данные
    f = open('..\\Data\\'+filename, 'r')
    lines = f.readlines()
    f.close()
    # пропускаем первые строки с комментариями, они начинаются с символа #
    # остальное помещаем в новый список
    lines1 = []
    for l in lines:
        if l[0] != '#':
            lines1.append(l)

    print(lines)
    print(lines1)

    # в следующей строке - количество колонок в формате число пробел слово columnus
    # за ней - количество строк (нам не нужно)
    # делим строку по пробелу, а результат превращаем в целое число)
    col_count = int(lines1[0].split(' ')[0])
    print(col_count)

    # выбираем строку с названием первой колонки
    # все строки содержат невидимый символ переноса строки
    # поэтому мы берем строу без последнего символа
    h_str = lines1[2][:-1].lstrip()
    # конструируем заголовок из названий колонок, разделенных запятыми
    for i in range(3, 2 + col_count):
        h_str += ',' + lines1[i][:-1]
    # h_str += '\n'
    print(h_str)

    lines2=[h_str]
    # формируем массив правильных строк
    # lines2 = []
    lines2.extend(lines1[2 + col_count:])
    print(lines2)

    # пишем данные во временный файл (это плохо, так делать не надо)
    tmp = 'tmp.csv'
    # формируем строки, где вместо пробелов запятые
    lines3=[]
    for l in lines2[1:]:
        l = ','.join(l.split())+'\n'
        lines3.append(l)

    # записываем файл
    f = open(tmp, 'w')
    f.writelines(lines3)
    f.close()

    # читаем файл и подставляем заголовки колонок
    df = pd.read_csv(tmp, header=None, names=h_str.split(','))
    print(df.columns)
    print(df)

    return df

def read_data(filename):
    # читаем сырые данные
    print('Start read file %s'%filename)
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    # пропускаем первые строки с комментариями, они начинаются с символа #
    # остальное помещаем в новый список
    lines1 = []
    for l in lines:
        if l[0] != '#':
            lines1.append(l)

    # print(lines)
    # print(lines1)

    # в следующей строке - количество колонок в формате число пробел слово columnus
    # за ней - количество строк (нам не нужно)
    # делим строку по пробелу, а результат превращаем в целое число)
    col_count = int(lines1[0].split(' ')[0])
    # print(col_count)

    # выбираем строку с названием первой колонки
    # все строки содержат невидимый символ переноса строки
    # поэтому мы берем строу без последнего символа
    h_str = lines1[2][:-1].lstrip()
    # конструируем заголовок из названий колонок, разделенных запятыми
    for i in range(3, 2 + col_count):
        h_str += ',' + lines1[i][:-1]
    # h_str += '\n'
    # print(h_str)

    lines2=[h_str]
    # формируем массив правильных строк
    # lines2 = []
    lines2.extend(lines1[2 + col_count:])
    # print(lines2)

    # пишем данные во временный файл (это плохо, так делать не надо)
    print('Write temporary file')
    tmp = 'tmp.csv'
    # формируем строки, где вместо пробелов запятые
    lines3=[]
    for l in lines2[1:]:
        l = ','.join(l.split())+'\n'
        lines3.append(l)

    # записываем файл
    f = open(tmp, 'w')
    f.writelines(lines3)
    f.close()

    print('Get formatted data. Use df.column for list columns')
    # читаем файл и подставляем заголовки колонок
    df = pd.read_csv(tmp, header=None, names=h_str.split(','))
    # print(df.columns)
    # print(df)

    return df