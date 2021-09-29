# -*- coding: utf-8 -*-
"""
Основной код, основной файл интерфейса
"""

import pandas as pd
import numpy as np
from tkinter import messagebox as mb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.backends.backend_tkagg import (NavigationToolbar2Tk)
import tkinter as tk
from tkinter import ttk


PATH_MAX_NUMERIC_VALUES = '..//Data//max_numeric_values.csv'
PATH_STATISTICS = '..//Data//Statistics_YouTube.csv'
PATH_GRAPH = '..//Graphics//'
PATH_OUT = '..//Output//'


def delet_video_id():
    """
    Функция, удаляющая информацию о видео, по его id
    Принимает: нет
    Автор: Фетисов Данила
    Возвращает: нет
    """
    id_of_video = Delet_by_id.get()
    firstbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
    if id_of_video in set(firstbd.video_id):
        firstbd = firstbd.drop(index=firstbd.loc[firstbd.video_id == id_of_video].index)
        firstbd.to_csv(PATH_MAX_NUMERIC_VALUES, index=False)
        mb.showinfo("Инфо", "Данные успешно удaлены")
    else:
        mb.showerror('Ошибка!','Видео с таким id не существует')


def deleting(id_):
    global Delet_by_id

    delet_video_id()
    id_.delete(0, 'end')


def exchange_df():
    """
    Функция, меняющая определенные количественные характеристики видео
    Принимает: нет
    Автор: Фетисов Данила
    Возвращает: нет
    """
    firstbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)

    ex_video_id = Exchange_new_id.get()
    if ex_video_id == '':
        mb.showerror("Ошибка", "Введите id видео, данные которого хотите изменить")
    if ex_video_id in set(firstbd.video_id):
        ex_max_views = Exchange_new_number_of_views.get()
        if ex_max_views != '':
            firstbd.loc[firstbd.video_id == ex_video_id, 'max_views'] = ex_max_views

        ex_max_likes = Exchange_new_number_of_likes.get()
        if ex_max_likes != '':
            firstbd.loc[firstbd.video_id == ex_video_id, 'max_likes'] = ex_max_likes

        ex_max_dislikes = Exchange_new_number_of_dislikes.get()
        if ex_max_dislikes != '':
            firstbd.loc[firstbd.video_id == ex_video_id, 'max_dislikes'] = ex_max_dislikes

        ex_max_comment_count = Exchange_new_number_of_comments.get()
        if ex_max_comment_count != '':
            firstbd.loc[firstbd.video_id == ex_video_id, 'max_comment_count'] = ex_max_comment_count

        ex_category_video = Exchange_new_video_category.get()
        if ex_category_video != '':
            firstbd.loc[firstbd.video_id == ex_video_id, 'category_id'] = ex_category_video

        firstbd.to_csv(PATH_MAX_NUMERIC_VALUES, index=False)
        mb.showinfo("Инфо", "Данные успешно изменены")
    else:
        mb.showerror('Ошибка!', 'Видео с таким id не существует')

def change_data(id_, change_number_of_views, change_number_of_likes,
               change_number_of_dislikes, change_number_of_comments, change_video_category):

    global Exchange_new_id
    global Exchange_new_number_of_views
    global Exchange_new_number_of_likes
    global Exchange_new_number_of_dislikes
    global Exchange_new_number_of_comments
    global Exchange_new_video_category

    exchange_df()
    id_.delete(0, 'end')
    change_number_of_views.delete(0, 'end')
    change_number_of_likes.delete(0, 'end')
    change_number_of_dislikes.delete(0, 'end')
    change_number_of_comments.delete(0, 'end')
    change_video_category.delete(0, 'end')


def in_BD1_BD2():
    """
    Функция, которая осуществляет ввод данных из окна интерфейса в базы данных
    Автор: Фетисов Данила
    Входные параметры: нет
    Возвращает: нет
    """
    id_video = New_id.get()
    views = New_number_of_views.get()
    likes = New_number_of_likes.get()
    dislikes = New_number_of_dislikes.get()
    comments_count = New_number_of_comments.get()
    category = New_video_category.get()

    bd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
    bd_1 = pd.read_csv(PATH_STATISTICS)

    df_of_inputs = pd.DataFrame({
        'video_id': [id_video],
        'max_views': [views],
        'max_likes': [likes],
        'max_dislikes': [dislikes],
        'max_comment_count': [comments_count],
        'category_id': [category]
    })
    # проверка на содержание введенных данных в существующих таблицах
    if id_video == "":
        mb.showerror("Ошибка!", "Пожалуйста введите id видео")
    if id_video in set(bd.video_id):
        mb.showerror("Ошибка!", "Вы ввели существующие данные")
    else:
        data = pd.concat([bd, df_of_inputs], ignore_index=True, axis=0)
        data_1 = pd.concat([bd_1, df_of_inputs], ignore_index=True, axis=0)
        data.to_csv(PATH_MAX_NUMERIC_VALUES, index=False)
        data_1.to_csv(PATH_STATISTICS, index=False)
        mb.showinfo("Инфо", "Данные успешно введены")


def add_new_information(new_id, new_number_of_views,
               new_number_of_likes, new_number_of_dislikes,
               new_number_of_comments, new_video_category):
    global New_id
    global New_number_of_views
    global New_number_of_likes
    global New_number_of_dislikes
    global New_number_of_comments
    global New_video_category

    in_BD1_BD2()
    new_id.delete(0, 'end')
    new_number_of_views.delete(0, 'end')
    new_number_of_likes.delete(0, 'end')
    new_number_of_dislikes.delete(0, 'end')
    new_number_of_comments.delete(0, 'end')
    new_video_category.delete(0, 'end')


def all_children(frame2):
    """
    Функция, очищающая пространство окна
    Принимает: окно, которое нужно очитсить
    Автор: Фетисов Данила
    Возвращает: нет
    """
    _list = frame2.winfo_children()
    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list


def new():
    """
    Функция, создающая интерфейс для ввода данных в БД
    Принимает: нет
    Автор: Фетисов Данила
    Возвращает: нет
    """
    widget_list = all_children(frame2)
    for item in widget_list:
        item.destroy()

    tk.Button(frame2, text='Добавить новые данные',
              command=new,
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=60, y=20)
    tk.Button(frame2, text='Изменить существующие данные',
              command=change,
              highlightbackground="grey14",
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=360, y=20)
    tk.Button(frame2, text='Удалить данные',
              command=delete,
              highlightbackground="grey14",
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=660, y=20)

    tk.Label(frame2,
             text="ID Видео",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=100, y=125)

    new_id = tk.Entry(frame2,
                      highlightbackground="grey14",
                      width=65,
                      textvariable=New_id)
    new_id.place(x=350, y=125,
                 relheight=0.05)

    tk.Label(frame2,
             text="Колличество просмотров",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=100, y=200)

    new_number_of_views = tk.Entry(frame2,
                                   highlightbackground="grey14",
                                   width=65,
                                   textvariable=New_number_of_views)
    new_number_of_views.place(x=350, y=200,
                              relheight=0.05)

    tk.Label(frame2,
             text="Колличество лайков",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=100, y=275)

    new_number_of_likes = tk.Entry(frame2,
                                   highlightbackground="grey14",
                                   width=65,
                                   textvariable=New_number_of_likes)
    new_number_of_likes.place(x=350, y=275,
                              relheight=0.05)

    tk.Label(frame2,
             text="Колличество дизлайокв",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=100, y=350)

    new_number_of_dislikes = tk.Entry(frame2,
                                      highlightbackground="grey14",
                                      width=65,
                                      textvariable=New_number_of_dislikes)
    new_number_of_dislikes.place(x=350, y=350,
                                 relheight=0.05)

    tk.Label(frame2,
             text="Колличество коментариев",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=100, y=425)

    new_number_of_comments = tk.Entry(frame2,
                                      highlightbackground="grey14",
                                      width=65,
                                      textvariable=New_number_of_comments)
    new_number_of_comments.place(x=350, y=425,
                                 relheight=0.05)

    tk.Label(frame2,
             text="Категория видео",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=100, y=500)

    new_video_category = tk.Entry(frame2,
                                  highlightbackground="grey14",
                                  width=65,
                                  textvariable=New_video_category)
    new_video_category.place(x=350, y=500,
                             relheight=0.05)

    tk.Button(frame2, text="Cохранить новые данные",
              width=25,
              height=3,
              font=('Arial', '12', 'bold'),
              command=lambda: add_new_information(new_id, new_number_of_views,
                                         new_number_of_likes,
                                         new_number_of_dislikes,
                                         new_number_of_comments,
                                         new_video_category)).\
                                         place(x=750, y=500)


def change():
    """
    Функция, создающая интерфейс для изменения данных в БД
    Принимает: нет
    Автор: Фетисов Данила
    Возвращает: нет
    """
    widget_list = all_children(frame2)
    for item in widget_list:
        item.destroy()

    tk.Button(frame2, text='Добавить новые данные',
              command=new,
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=60, y=20)
    tk.Button(frame2, text='Изменить существующие данные',
              command=change,
              highlightbackground="grey14",
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=360, y=20)
    tk.Button(frame2, text='Удалить данные',
              command=delete,
              highlightbackground="grey14",
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=660, y=20)

    tk.Label(frame2,
             text="ID Видео, параметры которого изменятся",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=80, y=125)

    id_ = tk.Entry(frame2,
                   highlightbackground="grey14",
                   width=50,
                   textvariable=Exchange_new_id)
    id_.place(x=450, y=125, relheight=0.05)

    tk.Label(frame2,
             text="Новое колличество просмотров",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=80, y=200)

    change_number_of_views = tk.Entry(
                                    frame2,
                                    highlightbackground="grey14",
                                    width=50,
                                    textvariable=Exchange_new_number_of_views)
    change_number_of_views.place(x=450, y=200, relheight=0.05)

    tk.Label(frame2,
             text="Новок колличество лайков",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=80, y=275)

    change_number_of_likes = tk.Entry(
                                    frame2,
                                    highlightbackground="grey14",
                                    width=50,
                                    textvariable=Exchange_new_number_of_likes)
    change_number_of_likes.place(x=450, y=275, relheight=0.05)

    tk.Label(frame2,
             text="Новое колличество дизлайокв",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=80, y=350)

    change_number_of_dislikes = tk.Entry(
                                frame2,
                                highlightbackground="grey14",
                                width=50,
                                textvariable=Exchange_new_number_of_dislikes)
    change_number_of_dislikes.place(x=450, y=350, relheight=0.05)

    tk.Label(frame2,
             text="Новое колличество коментариев",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=80, y=425)

    change_number_of_comments = tk.Entry(
                            frame2,
                            highlightbackground="grey14",
                            width=50,
                            textvariable=Exchange_new_number_of_comments)
    change_number_of_comments.place(x=450, y=425, relheight=0.05)

    tk.Label(frame2,
             text="Новая категория видео",
             fg="black",
             font=('Arial', 12, 'bold')) \
        .place(x=80, y=500)

    change_video_category = tk.Entry(frame2,
                                     highlightbackground="grey14",
                                     width=50,
                                     textvariable=Exchange_new_video_category)
    change_video_category.place(x=450, y=500,
                                relheight=0.05)

    tk.Button(frame2, text="Cохранить изменённые данные",
              width=27,
              height=3,
              font=('Arial', '10', 'bold'),
              command=lambda: change_data(
                  id_, change_number_of_views,
                  change_number_of_likes, change_number_of_dislikes,
                  change_number_of_comments, change_video_category))\
        .place(x=760, y=500)


def delete():
    """
    Функция, создающая интерфейс для удаления данных из БД
    Принимает: нет
    Автор: Фетисов Данила
    Возвращает: нет
    """
    def delete_only_ID():
        flag = True
        Id = id_.get()
        if (flag is True):
            good_work = tk.Tk()
            good_work["bg"] = "green"
            good_work.title("Успешно")
            wide_good_work = w-125
            high_good_work = h-30
            good_work.geometry('250x60+{}+{}'.format(wide_good_work, high_good_work))
            tk.Label(good_work,
                     text="Данные успешно удалены",
                     fg="black",
                     bg="green",
                     font=('Arial', 12, 'bold')) \
                .place(x=0, y=0)
            tk.Button(good_work, text='ОК',
                      command=lambda: good_work.destroy(),
                      highlightbackground="grey14",
                      width=0,
                      height=0,
                      font=('Arial', '10', 'bold')) \
                .place(x=220, y=30)
            good_work.mainloop()

    widget_list = all_children(frame2)
    for item in widget_list:
        item.destroy()

    tk.Button(frame2, text='Добавить новые данные',
              command=new,
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=60, y=20)
    tk.Button(frame2, text='Изменить существующие данные',
              command=change,
              highlightbackground="grey14",
              width=28,
              height=3,
              font=('Arial', '12', 'bold'))\
        .place(x=360, y=20)
    tk.Button(frame2, text='Удалить данные',
              highlightbackground="grey14",
              width=28,
              height=3,
              font=('Arial', '12', 'bold')) \
        .place(x=660, y=20)

    tk.Label(frame2,
             text="В данной вкладке Вы можете удалить информацию только введя точное ID видео. ",
             fg="black",
             font=('Comic Sans MS', 15, 'bold')) \
        .place(x=80, y=100)
    tk.Label(frame2,
             text="Если Вы не обладаете точным значение ID видео, то вы сможете удалить информацию, ",
             fg="black",
             font=('Comic Sans MS', 15, 'bold')) \
        .place(x=50, y=150)
    tk.Label(frame2,
             text="преейдя на вкладку <Вывод данных по категориям>. ",
             fg="black",
             font=('Comic Sans MS', 15, 'bold')) \
        .place(x=220, y=200)

    tk.Label(frame2,
             text="Id видео",
             fg="black",
             font=('Arial', 13, 'bold')) \
        .place(x=325, y=300)
    id_ = tk.Entry(frame2,
                   highlightbackground="grey14",
                   width=50,
                   textvariable=Delet_by_id)
    id_.place(x=425, y=300,
              relheight=0.05)
    tk.Button(frame2, text="Удалить",
              width=27,
              height=3,
              font=('Arial', '10', 'bold'),
              command=lambda: deleting(id_))\
        .place(x=760, y=500)


def withdraw():
    """
    Функция, создающая список, со значениями, которые выбрал пользователь
    Принимает: нет
    Автор: Фетисов Данила
    Возвращает: нет
    """
    global dict_
    dict_ = []
    # получаем значения кнопок в булевском формате
    if chk1_state.get():
        dict_.append(1)
    if chk2_state.get():
        dict_.append(2)
    if chk3_state.get():
        dict_.append(3)
    if chk4_state.get():
        dict_.append(4)
    if chk5_state.get():
        dict_.append(5)
    if chk6_state.get():
        dict_.append(6)
    if chk7_state.get():
        dict_.append(7)
    if chk8_state.get():
        dict_.append(8)
    if chk9_state.get():
        dict_.append(9)
    if chk10_state.get():
        dict_.append(10)
    if chk11_state.get():
        dict_.append(11)
    if chk12_state.get():
        dict_.append(12)
    if chk13_state.get():
        dict_.append(13)
    if chk14_state.get():
        dict_.append(14)
    if chk15_state.get():
        dict_.append(15)
    if chk16_state.get():
        dict_.append(16)
    if len(dict_) > 3:
        mb.showerror('Ошибка!', 'Можно выбрать не больше 3 категорий!')
    elif len(dict_) == 0:
        mb.showerror('Ошибка!', 'Пожалуйста выберете категорию видео, но не больше 3-х!')


def from_BD1(count_of_views, count_of_likes, count_of_comments):
    """
    Функция, которая осуществляет вывод данных из первой БД
    Автор: Фетисов Данила
    Входные параметры: Кол-во просмотров, кол-во лайков, кол-во комментариев
    Возвращает: full_list - список строк таблицы 1, которые нужно вывести на экран
    """
    bd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
    category_1, category_2, category_3 = 0, 0, 0
    l = len(dict_)
    if l == 1:
        category_1 = int(dict_[0])
        category_2 = 0
        category_3 = 0
    elif l == 2:
        category_1 = int(dict_[0])
        category_2 = int(dict_[1])
        category_3 = 0
    elif l == 3:
        category_1 = int(dict_[0])
        category_2 = int(dict_[1])
        category_3 = int(dict_[2])    

    if count_of_views != 'Кол-во просмотров':
        view = count_of_views.split('-')
        lower_threshold_view = int(view[0])
        high_threshold_view = int(view[1])
    else:
        lower_threshold_view = bd.max_views.min()
        high_threshold_view = bd.max_views.max()

    if count_of_likes != 'Количество лайков':
        like = count_of_likes.split('-')
        lower_threshold_like = int(like[0])
        high_threshold_like = int(like[1])
    else:
        lower_threshold_like = 0
        high_threshold_like = bd.max_likes.max()

    if count_of_comments != 'Кол-во комментариев':
        comment = count_of_comments.split('-')
        lower_threshold_comment = int(comment[0])
        high_threshold_comment = int(comment[1])
    else:
        lower_threshold_comment = 0
        high_threshold_comment = bd.max_comment_count.max()
    sample = bd.query("(category_id == @category_1 or \
                        category_id == @category_2 or \
                        category_id == @category_3) and \
                       (max_views >= @lower_threshold_view and \
                        max_views <= @high_threshold_view) and \
                       (max_likes >= @lower_threshold_like and \
                        max_likes <= @high_threshold_like) and \
                       (max_comment_count >= @lower_threshold_comment \
                        and max_comment_count <= @high_threshold_comment)")

    full_list = sample.index
    return full_list


def sorting_data(combo_viewrs, combo_likes, combo_comments):
    """
    Функция, создающая интерфейс для сортировки БД
    Автор: Фетисов Данила
    Входные параметры: нет
    Возвращает: нет
    """
    withdraw()
    search_w = tk.Frame(frame3, bg='grey14')
    search_w.place(x=40, y=110, width=940, height=410)

    def warning_about_saving():
        answer = mb.askyesno(
            title="Важно!",
            message="Если вы только что удалили строку(-и), то нужно "
                    "нажать кнопку 'Вывести' еще раз, и после нажать "
                    "'Сохранить'. Хотите сохранить таблицу сейчас?")

        if answer:
            save_sorting_data()

    def save_sorting_data():
        """
        Функция, сохраняющая искомые строки(поиск по фильтрам) базы данных,
        которые видит пользователь при нажатии на кнопку "Вывести"
        Автор: Фетисов Данила
        Входные параметры: нет
        Возвращает: нет
        """
        # формируется название файлы, исходя из фильтров
        df = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        file_name = str(dict_[0]) + "_" + combo_viewrs.get() + "_" + combo_likes.get() + ".txt"

        df_search = df.iloc[list_]
        file = PATH_OUT + file_name
        df_search.to_csv(file, index=None, header=True,
                         encoding="utf-8", sep=',')
        mb.showinfo("Инфо!", "Таблица успешно сохранена в файл!")

    if len(dict_) != 0:
        list_ = from_BD1(combo_viewrs.get(),
                         combo_likes.get(), combo_comments.get())
        if len(list_) == 0:
            mb.showerror("Внимание!",
                         "Нет данных, подходящих под фильтры!")
        bd_1 = pd.read_csv(PATH_STATISTICS)
        bd_2 = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        table = ttk.Treeview(search_w, columns=(
            'Видео id', 'Заголовок видео', 'Название канала',
            'Кол-во просмотров', 'Кол-во лайков',
            'Кол-во дизлайков', 'Кол-во комментариев'),
            height=15, show='headings')
        table.column('Видео id', anchor=tk.CENTER)
        table.column('Заголовок видео', anchor=tk.CENTER)
        table.column('Название канала', anchor=tk.CENTER)
        table.column('Кол-во просмотров', anchor=tk.CENTER)
        table.column('Кол-во лайков', anchor=tk.CENTER)
        table.column('Кол-во дизлайков', anchor=tk.CENTER)
        table.column('Кол-во комментариев', anchor=tk.CENTER)
        table.heading('Видео id', text='Видео id')
        table.heading('Заголовок видео', text='Заголовок видео')
        table.heading('Название канала', text='Название канала')
        table.heading('Кол-во просмотров', text='Кол-во просмотров')
        table.heading('Кол-во лайков', text='Кол-во лайков')
        table.heading('Кол-во дизлайков', text='Кол-во дизлайков')
        table.heading('Кол-во комментариев', text='Кол-во комментариев')
        for row in list_:
            table.insert('', tk.END, values=(bd_2.iloc[row, 0],
                                             list(bd_1.loc[bd_1.video_id == bd_2.iloc[row, 0]].title)[0],
                                             list(bd_1.loc[bd_1.video_id == bd_2.iloc[row, 0]].channel_title)[0], 
                                             bd_2.iloc[row, 1],
                                             bd_2.iloc[row, 2],
                                             bd_2.iloc[row, 3],
                                             bd_2.iloc[row, 4]))
        scrolltable1 = tk.Scrollbar(search_w, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(search_w, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)

        def select_str_to_delete():
            """
            Функция, которая определяет индекс выбранной строки виджета TreeView
            Автор: Фетисов Данила
            Входные параметры: нет
            Возвращает: нет
            """
            item = table.selection()
            if item == ():  # если пользователь нажимает удалить, не выбрав строку
                mb.showerror("Ошибка!", "Сначала выберите строку!")
            else:
                item = table.selection()[0]
                deleting_select_str(item, table)
        button_delete = tk.Button(frame3, font=('Arial', '12', 'bold'),
                                  highlightbackground="grey14",
                                  text='Удалить',
                                  command=lambda: select_str_to_delete())
        button_delete.place(relx=0.755, rely=0.9375,
                            relheight=0.0495, relwidth=0.22)
        button_save = tk.Button(frame3, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14",
                                text='Сохранить',
                                command=lambda: warning_about_saving())
        button_save.place(relx=0.025, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
        or_lab = tk.Label(frame3, font=('Arial', '12', 'bold'),
                          highlightbackground="grey14", text='ИЛИ')
        or_lab.place(relx=0.4, rely=0.9375,
                     relheight=0.0495, relwidth=0.22)
        return table


def deleting_select_str(item, table):
    """
    Функция, осуществляющая удаление одной строки из базы данных
    Автор: Фетисов Данила
    Входные параметры: item - индекс выбранного элемента TreeView; table - виджет Treeview
    Возвращает: нет
    """
    # global PATH_STATISTICS, PATH_MAX_NUMERIC_VALUES
    curitem = table.item(item)
    id_of_video_to_delete = curitem['values'][0]

    df = pd.read_csv(PATH_STATISTICS)
    df = df.drop(index=df.loc[df.video_id == id_of_video_to_delete].index)
    df.to_csv(PATH_STATISTICS, index=False)
    df_1 = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
    df_1 = df_1.drop(index = df_1.loc[df_1.video_id == id_of_video_to_delete].index)
    df_1.to_csv(PATH_MAX_NUMERIC_VALUES, index=False)
    table.delete(item)  # удаление выбранного элемента из treeview

def some_graph():
    """
    Функция выводит графики по заданным критериям на экран
    Автор: Фетисов Данила
    Входные параметры: graph
    Возвращает: нет
    """
    graph = tk.Frame(frame4, bg="grey14")
    graph.place(x=55, y=135, width=920, height=420)
    if combo_label4.get() == 'Выберите фильтр:':
        mb.showerror("Ошибка!", "Сначала выберите фильтр!")
    if combo_label4.get() == 'Сводная таблица по каналам 2-й категории видео':
        mb.showerror("Ошибка!", "По этому фильтру можно "
                     "построить сводную таблицу. "
                     "Пожалуйста нажмите 'Посмотреть статистику'")
    if combo_label4.get() == 'Кат. видео - Среднее по кол-ву тегов под видео(сводн. табл.)':
        mb.showerror("Ошибка!", "По этому фильтру можно "
                     "построить сводную таблицу. "
                     "Пожалуйста нажмите 'Посмотреть статистику'")
    if combo_label4.get() == 'Кат. видео - Сумма по колич. хар-м(сводн. табл.)':
        mb.showerror("Ошибка!", "По этому фильтру можно "
                     "построить сводную таблицу. "
                     "Пожалуйста нажмите 'Посмотреть статистику'")
    if combo_label4.get() == 'Категория видео - Среднее кол-во просмотров':
        # выбор параметра и соответсвующий параметру график строится
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_views(fbd)
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('')
        bd.plot.scatter(ax=ax, y='max_views', x='category_id',
                        rot=45, fontsize=9, legend=False)
        title_boxplot = 'Среднее кол-во просмотров в каждой категории'
        plt.title(title_boxplot)
        plt.suptitle('')
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Категория видео - Среднее кол-во лайков':
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_likes(fbd)
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('')
        bd.plot.scatter(ax=ax, y='max_likes', x='category_id',
                        rot=45, fontsize=9, legend=False)
        title_boxplot = 'Среднее кол-во лайков под видео в каждой категории'
        plt.title(title_boxplot)
        plt.suptitle('')
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Категория видео - Среднее кол-во дизлайков':
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_dislikes(fbd)
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('')
        bd.plot.scatter(ax=ax, y='max_dislikes', x='category_id',
                        rot=45, fontsize=9, legend=False)
        title_boxplot = 'Среднее кол-во дизлайков под видео в каждой категории'
        plt.title(title_boxplot)
        plt.suptitle('')
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Категория видео - Среднее кол-во комментариев':
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_comment_count(fbd)
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('')
        bd.plot.scatter(ax=ax, y='max_comment_count',
                        x='category_id', rot=45, fontsize=9, legend=False)
        title_boxplot = 'Среднее кол-во комментариев под видео в каждой категории'
        plt.title(title_boxplot)
        plt.suptitle('')
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Количество просмотров - Дата в тренде':
        fbd = pd.read_csv(PATH_STATISTICS)
        sbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = views_on_data(fbd, sbd)
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('')
        bd.plot(ax=ax, y='max_views', x='trending_date', rot=45,
                fontsize=9, legend=False)
        title_boxplot = 'Среднее кол-во просмотров под видео в каждой категории в определенный день'
        plt.title(title_boxplot)
        plt.suptitle('')
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Анализ видео из 2-й категории':
        data_2 = pd.read_csv(PATH_STATISTICS).fillna(0)

        def de(a):
            return (a/1000000)

        def de1(a):
            return (a/10000)

        def de2(a):
            return (a/40000)

        df_1 = data_2.loc[data_2.category_id == 2]
        df_1 = df_1.iloc[:, [4, 7]]
        df_1 = df_1['views'].apply(de)
        df_1 = pd.DataFrame({'category_id': 2, 'views': df_1.values})
        df_1 = df_1.query("views < 3")
        df_1 = df_1.views
        df_2 = data_2.loc[data_2.category_id == 2]
        df_2 = df_2.iloc[:, [4, 10]]
        df_2 = df_2['comment_count'].apply(de1)
        df_2 = pd.DataFrame({'category_id': 2, 'comment_count': df_2.values})
        df_2 = df_2.comment_count
        df_3 = data_2.loc[data_2.category_id == 2]
        df_3 = df_3.iloc[:, [4, 8]]
        df_3 = df_3['likes'].apply(de2)
        df_3 = pd.DataFrame({'category_id': 2, 'likes': df_3.values})
        df_3 = df_3.likes

        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        fig.suptitle('')
        data = [df_1, df_2, df_3]
        bp = ax.boxplot(data)
        ax.set_ylabel('Кол-во просмотров в 10^6-10^4-10^4 соответ.')
        title_boxplot = 'Анализ кол-ва просмотров во 2-й категории видео'
        plt.title(title_boxplot)
        plt.xticks([1, 2, 3], ['Number of views', 'Number of comments',
                               'Number of likes'],
                   rotation=15)
        plt.suptitle('')
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Анализ популярности различных категорий видео':
        fbd = pd.read_csv(PATH_STATISTICS)

        def de(a):
            return (a/1000000)

        df_1 = fbd.loc[fbd.category_id == 2]
        df_1 = df_1.iloc[:, [4, 7]]
        df_1 = df_1['views'].apply(de)
        df_1 = pd.DataFrame({'category_id': 2, 'views': df_1.values})
        df_1 = df_1.query("views < 9")
        df_1 = df_1.views
        df_2 = fbd.loc[fbd.category_id == 4]
        df_2 = df_2.iloc[:, [4, 7]]
        df_2 = df_2['views'].apply(de)
        df_2 = pd.DataFrame({'category_id': 4, 'views': df_2.values})
        df_2 = df_2.query("views < 9")
        df_2 = df_2.views
        df_3 = fbd.loc[fbd.category_id == 13]
        df_3 = df_3.iloc[:, [4, 7]]
        df_3 = df_3['views'].apply(de)
        df_3 = pd.DataFrame({'category_id': 13, 'views': df_3.values})
        df_3 = df_3.query("views < 9")
        df_3 = df_3.views
        df_4 = fbd.loc[fbd.category_id == 14]
        df_4 = df_4.iloc[:, [4, 7]]
        df_4 = df_4['views'].apply(de)
        df_4 = pd.DataFrame({'category_id': 14, 'views': df_4.values})
        df_4 = df_4.query("views < 9")
        df_4 = df_4.views
        data = [df_1, df_2, df_3, df_4]
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        ax.set_ylabel('Кол-во прсоомтров в 10^6')
        plt.title('Сравнение нескольких популярности видео из различных категорий',
                  fontsize=20)
        bp = ax.boxplot(data)
        # plt.xticks(np.rad2deg(points), labels)
        plt.xticks([1, 2, 3, 4], ['All about films', 'Automobile topics',
                                  'Popular science literature',
                                  'Vlogs and travel'],
                   rotation=17)
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    if combo_label4.get() == 'Сравнение количесвтенных хар-к в популярных категориях видео':
        data_1 = pd.read_csv(PATH_MAX_NUMERIC_VALUES)

        index = np.arange(4)
        x1 = data_1.loc[data_1.category_id == 4].max_likes.sum()
        x2 = data_1.loc[data_1.category_id == 4].max_dislikes.sum()
        x3 = data_1.loc[data_1.category_id == 4].max_comment_count.sum()

        y1 = data_1.loc[data_1.category_id == 2].max_likes.sum()
        y2 = data_1.loc[data_1.category_id == 2].max_dislikes.sum()
        y3 = data_1.loc[data_1.category_id == 2].max_comment_count.sum()

        z1 = data_1.loc[data_1.category_id == 14].max_likes.sum()
        z2 = data_1.loc[data_1.category_id == 14].max_dislikes.sum()
        z3 = data_1.loc[data_1.category_id == 14].max_comment_count.sum()

        a1 = data_1.loc[data_1.category_id == 13].max_likes.sum()
        a2 = data_1.loc[data_1.category_id == 13].max_dislikes.sum()
        a3 = data_1.loc[data_1.category_id == 13].max_comment_count.sum()

        values1 = [x1, y1, z1, a1]
        values2 = [x2, y2, z2, a2]
        values3 = [x3, y3, z3, a3]

        bw = 0.3
        fig = plt.figure(figsize=(4, 5), dpi=70)
        ax = fig.add_subplot(1, 1, 1)
        plt.title('', fontsize=20)
        plt.bar(index, values1, bw, color='b', label='Likes')
        plt.bar(index+bw, values2, bw, color='g', label='Dislikes')
        plt.bar(index+2*bw, values3, bw, color='r', label='Comments')
        plt.xticks(index+bw, ['All about films', 'Automobile topics',
                              'Popular science literature', 'Vlogs and travel'],
                   rotation=16)
        plt.legend()
        show_graph = FigureCanvasTkAgg(fig, master=graph)
        show_graph.draw()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(show_graph, graph)
        toolbar.update()
        show_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def statistics_from_some_graph():
    """
    Функция, создающая интерфейс для вывода статистики по заданным критериям
    Автор: Фетисов Данила
    Входные параметры: нет
    Возвращает: нет
    """
    answerfr_1 = tk.Frame(frame4, bg="grey14")
    answerfr_1.place(x=55, y=135, width=920, height=420)
    if combo_label4.get() == 'Выберите фильтры':
        mb.showerror("Ошибка!", "Сначала выберите фильтр!")
    if combo_label4.get() == 'Анализ видео из 2-й категории':
        mb.showerror("Ошибка!", "По этому критерию строится boxplot-график. "
                     "Пожалуйста нажмите 'Построить'.")
    if combo_label4.get() == 'Сравнение количесвтенных хар-к в популярных категориях видео':
        mb.showerror("Ошибка!", "По этому критерию строится гистограмма. "
                     "Пожалуйста нажмите 'Построить'.")
    if combo_label4.get() == 'Анализ популярности различных категорий видео':
        mb.showerror("Ошибка!", "По этому критерию строится boxplot-график. "
                     "Пожалуйста нажмите 'Построить'.")
    if combo_label4.get() == 'Категория видео - Среднее кол-во просмотров':
        # выбор параметра и соответсвующая параметру таблица строится
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_views(fbd)
        list_ = list_from_bd(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Среднее кол-во просмотров'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Среднее кол-во просмотров', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Среднее кол-во просмотров',
                      text='Среднее кол-во просмотров')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                            relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Категория видео - Среднее кол-во лайков':
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_likes(fbd)
        list_ = list_from_bd(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Среднее кол-во лайков'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Среднее кол-во лайков', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Среднее кол-во лайков', text='Среднее кол-во лайков')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Категория видео - Среднее кол-во дизлайков':
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_dislikes(fbd)
        list_ = list_from_bd(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Среднее кол-во дизлайков'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Среднее кол-во дизлайков', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Среднее кол-во дизлайков',
                      text='Среднее кол-во дизлайков')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Категория видео - Среднее кол-во комментариев':
        fbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = mean_comment_count(fbd)
        list_ = list_from_bd(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Среднее кол-во комментариев'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Среднее кол-во комментариев', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Среднее кол-во комментариев',
                      text='Среднее кол-во комментариев')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Количество просмотров - Дата в тренде':
        fbd = pd.read_csv(PATH_STATISTICS)
        sbd = pd.read_csv(PATH_MAX_NUMERIC_VALUES)
        bd = views_on_data(fbd, sbd)
        list_ = list_from_bd_1(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Дата "в тренде"',
                                      'Количество просмотров в определенный день'),
                             height=15, show='headings')
        table.column('Дата "в тренде"', anchor=tk.CENTER)
        table.column('Количество просмотров в определенный день',
                     anchor=tk.CENTER)
        table.heading('Дата "в тренде"', text='Дата "в тренде"')
        table.heading('Количество просмотров в определенный день',
                      text='Количество просмотров в определенный день')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Кат. видео - Сумма по колич. хар-м(сводн. табл.)':
        fbd = pd.read_csv(PATH_STATISTICS)
        bd = pivot_table_1(fbd)
        bd = bd.reset_index()
        list_ = list_from_bd_1(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Возможность оставлять ком-ты',
                                      'Кол-во комментариев',
                                      'Кол-во лайков',
                                      'Кол-во дизлайков',
                                      'Кол-во просмотров'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Возможность оставлять ком-ты', anchor=tk.CENTER)
        table.column('Кол-во комментариев', anchor=tk.CENTER)
        table.column('Кол-во лайков', anchor=tk.CENTER)
        table.column('Кол-во дизлайков', anchor=tk.CENTER)
        table.column('Кол-во просмотров', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Возможность оставлять ком-ты',
                      text='Возможность оставлять ком-ты')
        table.heading('Кол-во комментариев', text='Кол-во комментариев')
        table.heading('Кол-во лайков', text='Кол-во лайков')
        table.heading('Кол-во дизлайков', text='Кол-во дизлайков')
        table.heading('Кол-во просмотров', text='Кол-во просмотров')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Кат. видео - Среднее по кол-ву тегов под видео(сводн. табл.)':
        fbd = pd.read_csv(PATH_STATISTICS)
        bd = pivot_table_2(fbd)
        bd = bd.reset_index()
        list_ = list_from_bd_1(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Возможность оставлять ком-ты',
                                      'Среднее кол-во комментариев',
                                      'Среднее кол-во тегов',
                                      'Среднее кол-во просмотров'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Возможность оставлять ком-ты', anchor=tk.CENTER)
        table.column('Среднее кол-во комментариев', anchor=tk.CENTER)
        table.column('Среднее кол-во тегов', anchor=tk.CENTER)
        table.column('Среднее кол-во просмотров', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Возможность оставлять ком-ты',
                      text='Возможность оставлять ком-ты')
        table.heading('Среднее кол-во комментариев',
                      text='Среднее кол-во комментариев')
        table.heading('Среднее кол-во тегов',
                      text='Среднее кол-во тегов')
        table.heading('Среднее кол-во просмотров',
                      text='Среднее кол-во просмотров')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14", text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)
    if combo_label4.get() == 'Сводная таблица по каналам 2-й категории видео':
        fbd = pd.read_csv(PATH_STATISTICS)
        bd = pivot_table_3(fbd)
        bd = bd.reset_index()
        list_ = list_from_bd_1(bd)
        table = ttk.Treeview(answerfr_1,
                             columns=('Категория видео',
                                      'Возможность оставлять ком-ты',
                                      'Название канала',
                                      'Среднее кол-во комментариев',
                                      'Среднее кол-во тегов',
                                      'Среднее кол-во лайков',
                                      'Среднее кол-во просмотров'),
                             height=15, show='headings')
        table.column('Категория видео', anchor=tk.CENTER)
        table.column('Возможность оставлять ком-ты', anchor=tk.CENTER)
        table.column('Название канала', anchor=tk.CENTER)
        table.column('Среднее кол-во комментариев', anchor=tk.CENTER)
        table.column('Среднее кол-во тегов', anchor=tk.CENTER)
        table.column('Среднее кол-во лайков', anchor=tk.CENTER)
        table.column('Среднее кол-во просмотров', anchor=tk.CENTER)
        table.heading('Категория видео', text='Категория видео')
        table.heading('Возможность оставлять ком-ты',
                      text='Возможность оставлять ком-ты')
        table.heading('Название канала',
                      text='Название канала')
        table.heading('Среднее кол-во комментариев',
                      text='Среднее кол-во комментариев')
        table.heading('Среднее кол-во тегов',
                      text='Среднее кол-во тегов')
        table.heading('Среднее кол-во лайков',
                      text='Среднее кол-во лайков')
        table.heading('Среднее кол-во просмотров',
                      text='Среднее кол-во просмотров')
        for row in list_:
            table.insert('', tk.END, values=row)
        scrolltable1 = tk.Scrollbar(answerfr_1, orient=tk.VERTICAL,
                                    command=table.yview)
        table.config(yscrollcommand=scrolltable1.set)
        scrolltable1.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltable = tk.Scrollbar(answerfr_1, orient=tk.HORIZONTAL,
                                   command=table.xview)
        table.config(xscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.BOTTOM, fill=tk.X)
        table.place(relwidth=1, relheight=1)
        button_save = tk.Button(answerfr_1, font=('Arial', '12', 'bold'),
                                highlightbackground="grey14",
                                text='Сохранить',
                                command=lambda: saving_sort_table(bd))
        button_save.place(relx=0.755, rely=0.9375,
                          relheight=0.0495, relwidth=0.22)


def pivot_table_3(firstbd):
    """
    Функция, создающая сводную таблицу по фильтрам
    Принимает: firstbd - база данных
    Автор: Фетисов Данлиа
    Возвращает: сводную таблицу
    """
    def spl(a):
        return len(str(a).split('|'))
    firstbd['count_of_tags'] = firstbd['tags'].apply(spl)
    data = firstbd.loc[firstbd.category_id == 2]
    fr = pd.pivot_table(data,
                        index=['category_id', 'comments_disabled', 'channel_title'],
                        values=['count_of_tags', 'views', 'comment_count', 'likes'],
                        aggfunc=np.mean)
    fr['count_of_tags'] = fr['count_of_tags'].apply(round)
    fr['comment_count'] = fr['comment_count'].apply(round)
    fr['views'] = fr['views'].apply(round)
    fr['likes'] = fr['likes'].apply(round)
    return fr


def pivot_table_1(firstbd):
    """
    Функция, создающая сводную таблицу по фильтрам
    Принимает: firstbd - база данных
    Автор: Фетисов Данлиа
    Возвращает: сводную таблицу
    """
    fr = pd.pivot_table(firstbd,
                        index=['category_id', 'comments_disabled'],
                        values=['views', 'likes', 'dislikes', 'comment_count'],
                        aggfunc=np.sum)
    return fr


def pivot_table_2(firstbd):
    """
    Функция, создающая сводную таблицу по фильтрам
    Принимает: firstbd - база данных
    Автор: Фетисов Данлиа
    Возвращает: сводную таблицу
    """
    def spl(a):
        return len(str(a).split('|'))
    firstbd['count_of_tags'] = firstbd['tags'].apply(spl)
    fr = pd.pivot_table(firstbd,
                        index=['category_id', 'comments_disabled'],
                        values=['count_of_tags', 'views', 'comment_count'],
                        aggfunc=np.mean)
    fr['count_of_tags'] = fr['count_of_tags'].apply(round)
    fr['comment_count'] = fr['comment_count'].apply(round)
    fr['views'] = fr['views'].apply(round)
    return fr


def list_from_bd(bd):
    """
    Функция, создающая список из базы данных (с округлением некоторых значений)
    Автор: Фетисов Данила
    Входные параметры: bd (type: DataFrame)
    Возвращает: список из элементов базы данных
    """
    shape = bd.shape
    number_row = shape[0]
    full_list = []
    for i in range(0, number_row):
        list_row = []
        for j in bd.iloc[i]:
            list_row.append(int(j))
        full_list.append(list_row)
    return full_list


def mean_views(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd - базу данных
    Автор: Фетисов Данлиа
    Возвращает: объект типа DataFrame с выборкой и высчитаными значениями
    """
    fr = firstbd.groupby('category_id', as_index=False).agg({'max_views': "mean"})
    return fr


def mean_likes(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd - базу данных
    Автор: Фетисов Данлиа
    Возвращает: объект типа DataFrame с выборкой и высчитаными значениями
    """
    fr = firstbd.groupby('category_id', as_index=False).agg({'max_likes': "mean"})
    return fr


def list_from_bd_1(bd):
    """
    Функция, создающая список из базы данных
    Автор: Фетисов Данила
    Входные параметры: bd (type: DataFrame)
    Возвращает: список из элементов базы данных
    """
    shape = bd.shape
    number_row = shape[0]
    full_list = []
    for i in range(0, number_row):
        list_row = []
        for j in bd.iloc[i]:
            list_row.append(j)
        full_list.append(list_row)
    return full_list


def mean_dislikes(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd - базу данных
    Автор: Фетисов Данила
    Возвращает: объект типа DataFrame с выборкой и высчитаными значениями
    """
    fr = firstbd.groupby('category_id', as_index=False).agg({'max_dislikes': "mean"})
    return fr


def mean_comment_count(firstbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: firstbd - базу данных
    Автор: Фетисов Данила
    Возвращает: объект типа DataFrame с выборкой и высчитаными значениями
    """
    fr = firstbd.groupby('category_id', as_index=False).agg({'max_comment_count': "mean"})
    return fr


def views_on_data(firstbd, secondbd):
    """
    Функция, создающая DataFrame по фильтрам
    Принимает: secondbd - базу данных
    Автор: Фетисов Данлиа
    Возвращает: объект типа DataFrame с выборкой и высчитаными значениями
    """
    firstbd = firstbd.drop_duplicates(subset=['trending_date'])
    firstbd = firstbd.reset_index(drop=True)
    firstbd = firstbd.drop(index = [n for n in range(firstbd.shape[0]) if (n % 2 == 1)])
    firstbd = firstbd.reset_index(drop=True)
    firstbd = firstbd.drop(index = [n for n in range(firstbd.shape[0]) if (n % 2 == 1)])
    firstbd = firstbd.reset_index()
    data_2 = firstbd[['video_id', 'trending_date']]
    data_max_1 = secondbd[['max_views', 'video_id']]
    data_2 = data_2.merge(data_max_1, how='inner',
                          left_on='video_id', right_on='video_id')
    data_2 = data_2.drop(['video_id'], axis=1)
    return data_2


def saving_sort_table(bd):
    """
    Функция для сохранения отсортированной таблицы
    Автор: Фетисов Данила
    Принимает: bd (type: DataFrame)
    Возвращает: нет
    """
    name = PATH_OUT + combo_label4.get() + '.txt'
    bd.to_csv(name, header=None, index=None, sep=' ', mode='a')
    mb.showinfo("Инфо", "Таблица успешно сохранена")


main_window = tk.Tk()
New_id = tk.StringVar()
New_number_of_views = tk.StringVar()
New_number_of_likes = tk.StringVar()
New_number_of_dislikes = tk.StringVar()
New_number_of_comments = tk.StringVar()
New_video_category = tk.StringVar()

Exchange_new_id = tk.StringVar()
Exchange_new_number_of_views = tk.StringVar()
Exchange_new_number_of_likes = tk.StringVar()
Exchange_new_number_of_dislikes = tk.StringVar()
Exchange_new_number_of_comments = tk.StringVar()
Exchange_new_video_category = tk.StringVar()

Delet_by_id = tk.StringVar()

main_window["bg"] = "grey14"
main_window.title("Главное окно")
w = main_window.winfo_screenwidth()
h = main_window.winfo_screenheight()
w = w//2
h = h//2
wide_main_window = w - 500
high_main_window = h - 300
main_window.geometry('1000x600+{}+{}'.format(wide_main_window, high_main_window))

notebook = ttk.Notebook(main_window)
notebook.pack(pady=0, expand=True)

frame1 = ttk.Frame(notebook, width=1000, height=600)
frame2 = ttk.Frame(notebook, width=1000, height=600)
frame3 = ttk.Frame(notebook, width=1000, height=600)
frame4 = ttk.Frame(notebook, width=1000, height=600)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

notebook.add(frame1, text='Общая информация')
notebook.add(frame2, text='Работа с данными')
notebook.add(frame3, text='Вывод данных по критериям')
notebook.add(frame4, text='Статистика')

tk.Label(frame1,
         text="Проект – анализ статистки популярных видео на YouTube.",
         fg="black",
         font=('Comic Sans MS', 17, 'bold')) \
        .place(x=155, y=5)

tk.Label(frame1,
         text="Что реализовано:",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=15, y=50)

tk.Label(frame1,
         text="1. Во вкладке «Работа с данными» Вы можете добавить новую строку в БД, изменить или",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=80, y=90)

tk.Label(frame1,
         text="удалить ее.",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=100, y=120)

tk.Label(frame1,
         text="2. Во вкладке «Вывод данных по критериям» Вы можете отсортировать БД по выбранным",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=80, y=165)

tk.Label(frame1,
         text="вами категориям и сохранить выборку в txt-файле.",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=100, y=195)

tk.Label(frame1,
         text="3. Во вкладке «Статистика» Вы можете построить различные графики, по выбранным вами",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=80, y=240)

tk.Label(frame1,
         text="количественным и качественным характеристикам, а также построить несколько сводных",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=100, y=270)

tk.Label(frame1,
         text="таблиц.",
         fg="black",
         font=('Comic Sans MS', 15)) \
        .place(x=100, y=300)

tk.Button(frame2, text='Добавить новые данные',
          command=new,
          width=28,
          height=3,
          font=('Arial', '12', 'bold'))\
          .place(x=60, y=20)
tk.Button(frame2, text='Изменить существующие данные',
          command=change,
          highlightbackground="grey14",
          width=28,
          height=3,
          font=('Arial', '12', 'bold'))\
         .place(x=360, y=20)
tk.Button(frame2, text='Удалить данные',
          command=delete,
          highlightbackground="grey14",
          width=28,
          height=3,
          font=('Arial', '12', 'bold'))\
          .place(x=660, y=20)

#  отсюда начинается третий лейбл
tk.Label(frame3,
         text="Выберите категор(-ию -ии) видео ",
         fg="black",
         font=('Arial', 12, 'bold')) \
        .place(x=200, y=5)
chk1_state = tk.BooleanVar()
chk2_state = tk.BooleanVar()
chk3_state = tk.BooleanVar()
chk4_state = tk.BooleanVar()
chk5_state = tk.BooleanVar()
chk6_state = tk.BooleanVar()
chk7_state = tk.BooleanVar()
chk8_state = tk.BooleanVar()
chk9_state = tk.BooleanVar()
chk10_state = tk.BooleanVar()
chk11_state = tk.BooleanVar()
chk12_state = tk.BooleanVar()
chk13_state = tk.BooleanVar()
chk14_state = tk.BooleanVar()
chk15_state = tk.BooleanVar()
chk16_state = tk.BooleanVar()


chk1 = tk.Checkbutton(frame3, text='1',
                      variable=chk1_state)
chk1.place(x=45, y=35)
chk2 = tk.Checkbutton(frame3, text='2',
                      variable=chk2_state)
chk2.place(x=85, y=35)
chk3 = tk.Checkbutton(frame3, text='3',
                      variable=chk3_state)
chk3.place(x=125, y=35)
chk4 = tk.Checkbutton(frame3, text='4',
                      variable=chk4_state)
chk4.place(x=165, y=35)
chk5 = tk.Checkbutton(frame3, text='5',
                      variable=chk5_state)
chk5.place(x=205, y=35)
chk6 = tk.Checkbutton(frame3, text='6',
                      variable=chk6_state)
chk6.place(x=245, y=35)
chk7 = tk.Checkbutton(frame3, text='7',
                      variable=chk7_state)
chk7.place(x=285, y=35)
chk8 = tk.Checkbutton(frame3, text='8',
                      variable=chk8_state)
chk8.place(x=325, y=35)
chk9 = tk.Checkbutton(frame3, text='9',
                      variable=chk9_state)
chk9.place(x=365, y=35)
chk10 = tk.Checkbutton(frame3, text='10',
                       variable=chk10_state)
chk10.place(x=405, y=35)
chk11 = tk.Checkbutton(frame3, text='11',
                       variable=chk11_state)
chk11.place(x=445, y=35)
chk12 = tk.Checkbutton(frame3, text='12',
                       variable=chk12_state)
chk12.place(x=485, y=35)
chk13 = tk.Checkbutton(frame3, text='13',
                       variable=chk13_state)
chk13.place(x=525, y=35)
chk14 = tk.Checkbutton(frame3, text='14',
                       variable=chk14_state)
chk14.place(x=565, y=35)
chk15 = tk.Checkbutton(frame3, text='15',
                       variable=chk15_state)
chk15.place(x=605, y=35)
chk16 = tk.Checkbutton(frame3, text='16',
                       variable=chk16_state)
chk16.place(x=645, y=35)

combo_viewrs = tk.StringVar(value='Кол-во просмотров')
combo_viewrs_m = tk.OptionMenu(frame3, combo_viewrs, *['Кол-во просмотров','0-10000','10000-100000','100000-1000000', \
                                                          '1000000-10000000', \
                                                          '10000000-50000000', '50000000-150000000', '150000000-300000000'])
combo_viewrs_m.place(x=50, y=75)


combo_likes = tk.StringVar(value='Количество лайков')
combo_likes_m = tk.OptionMenu(frame3, combo_likes, *['Количество лайков', '0-10000','10000-100000',\
                                                          '100000-500000','500000-1500000', '1500000-6000000'])
combo_likes_m.place(x=280, y=75)

combo_comments = tk.StringVar(value='Кол-во комментариев')
combo_comments_m = tk.OptionMenu(frame3, combo_comments, *['Кол-во комментариев', '0-10000', \
                                                          '10000-50000','50000-250000','250000-1500000'])
combo_comments_m.place(x=475, y=75)

tk.Button(frame3, text='Вывести данные',
          command=lambda: sorting_data(combo_viewrs, combo_likes, combo_comments),
          highlightbackground="grey14",
          width=23,
          height=3,
          font=('Arial', '12', 'bold'))\
          .place(x=750, y=20)

tk.Label(frame4,
         text="В этом окне Вы можете визуализировать базу данных ",
         fg="black",
         font=('Comic Sans MS', 15, 'bold')) \
         .place(x=220, y=5)

combo_label4 = tk.StringVar(value='Выберите фильтр:')
combo_label4_w = tk.OptionMenu(frame4, combo_label4,
                         *['Категория видео - Среднее кол-во просмотров',
                           'Категория видео - Среднее кол-во лайков',
                           'Категория видео - Среднее кол-во комментариев',
                           'Анализ видео из 2-й категории',
                           'Категория видео - Среднее кол-во дизлайков',
                           'Сравнение количесвтенных хар-к в популярных категориях видео',
                           'Количество просмотров - Дата в тренде',
                           'Анализ популярности различных категорий видео',
                           'Кат. видео - Среднее по кол-ву тегов под видео(сводн. табл.)',
                           'Кат. видео - Сумма по колич. хар-м(сводн. табл.)',
                           'Сводная таблица по каналам 2-й категории видео'])
# combo_label4.current(0)
combo_label4_w.place(x=50, y=75)

tk.Button(frame4, text='Построить график',
          highlightbackground="grey14",
          width=20,
          height=3,
          command=lambda: some_graph(),
          font=('Arial', '12', 'bold'))\
    .place(x=540, y=50)

tk.Button(frame4, text='Посмотреть статистику',
          highlightbackground="grey14",
          width=20,
          height=3,
          command=lambda: statistics_from_some_graph(),
          font=('Arial', '12', 'bold'))\
    .place(x=760, y=50)

main_window.mainloop()
