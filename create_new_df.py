# -*- coding: utf-8 -*-
"""
Модуль с функциями для создания новой БД
"""

import pandas as pd

def create_new_df():
    """
    Функция на основе данных из изначальной БД создает новую, оставляя только последние упоминания о видео
    Автор: Фетисов Данила
    Вход: отсутствует
    Выход: отсутствует
    """
    bd_1 = pd.read_csv(r'D:\df\file3.csv')
    
    dictionary = {}
    for x in set(bd_1.video_id):
        views = list(bd_1.loc[bd_1.video_id == x] \
                .loc[bd_1.trending_date == bd_1.loc[bd_1.video_id == x].trending_date.max()].views)[0]
        dictionary[x] = views
    
    data = pd.DataFrame(dictionary.items(), columns=['video_id', 'max_views'])
    
    dictionary = {}
    for x in set(bd_1.video_id):
        views = list(bd_1.loc[bd_1.video_id == x] \
                .loc[bd_1.trending_date == bd_1.loc[bd_1.video_id == x].trending_date.max()].likes)[0]
        dictionary[x] = views
        
    data_1 = pd.DataFrame(dictionary.items(), columns=['video_id', 'max_likes'])
    
    data = data.merge(data_1, left_on='video_id', right_on='video_id')
    
    dictionary = {}
    for x in set(bd_1.video_id):
        views = list(bd_1.loc[bd_1.video_id == x] \
                .loc[bd_1.trending_date == bd_1.loc[bd_1.video_id == x].trending_date.max()].dislikes)[0]
        dictionary[x] = views
    
    data_1 = pd.DataFrame(dictionary.items(), columns=['video_id', 'max_dislikes'])
    
    data = data.merge(data_1, left_on='video_id', right_on='video_id')
    
    dictionary = {}
    for x in set(bd_1.video_id):
        views = list(bd_1.loc[bd_1.video_id == x] \
                .loc[bd_1.trending_date == bd_1.loc[bd_1.video_id == x].trending_date.max()].comment_count)[0]
        dictionary[x] = views
    
    data_1 = pd.DataFrame(dictionary.items(), columns=['video_id', 'max_comment_count'])
    
    data = data.merge(data_1, left_on='video_id', right_on='video_id')
    



