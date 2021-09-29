# -*- coding: utf-8 -*-
"""
Модуль с функциями для изменения исходной БД
"""

import pandas as pd

def cange_gf():
    """
    Функция изменяет категории у видео и упорядочивает их
    Автор: Фетисов Данила
    Вход: отсутствует
    Выход: отсутствует
    """
    data = pd.read_csv(r"D:\work\USvideos.csv") #считывание бд1
    
    for i, row in data.iterrows():
        if row['category_id'] == 43:
            data.loc[i, 'category_id'] = 3
        if row['category_id'] == 29:
            data.loc[i, 'category_id'] = 4
        if row['category_id'] == 28:
            data.loc[i, 'category_id'] = 5
        if row['category_id'] == 27:
            data.loc[i, 'category_id'] = 6
        if row['category_id'] == 26:
            data.loc[i, 'category_id'] = 7
        if row['category_id'] == 25:
            data.loc[i, 'category_id'] = 8
        if row['category_id'] == 24:
            data.loc[i, 'category_id'] = 9
        if row['category_id'] == 23:
            data.loc[i, 'category_id'] = 11
        if row['category_id'] == 22:
            data.loc[i, 'category_id'] = 12
        if row['category_id'] == 20:
            data.loc[i, 'category_id'] = 13
        if row['category_id'] == 19:
            data.loc[i, 'category_id'] = 14
        if row['category_id'] == 17:
            data.loc[i, 'category_id'] = 16
            
    data.to_csv(r'D:\df\file3.csv', index=False)



