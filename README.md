# pxl_oboard

Pixel Online Board.
Super simple, super stupid.

Пиксельная онлайн доска.
Супер простая, супер тупая.

## --------------------------------
## >>>Рисование<<<:
## Уровень: ламер
1. Скачать im_creator.py
2. Запустить через `python3 im_creator.py`
3. Нарисовать что-то.
4. Нажать кнопку "Upload" для загрузки рисунка на сервер.
5. Ждать надписи в консоли "DONE"

## Уровень: овнокодер
Вы можете написать свой скрипт на основе post.py или...
1. Скачать bot.py
2. Запрогроммировать свои инструкции для бота:
#### draw([0,1], [0,2], "blue") - Функция для рисования, использует массив списков.
( Поставить точки в координатах [0,1] и [0,2] формата [x,y] )
#### linex(y, x1, x2) - Функция для создания массива линии по координате Х
( Y остаётся таким же, массив идёт из x1 в x2 )
#### liney(x, y1, y2) - Аналогично.
#### fill([x1,y1], [x2, y2]) - Генерация массива для заполнения, дальше передавать в draw()
## --------------------------------

## Установка своего сервера:
1. Скачать main.py
2. Запустить и наслаждаться, порт - 3333

