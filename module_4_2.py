def test_function():
    print(f'Начало области видимости test_function() \n')


    def inner_function(a):
        print(f'Я функция "{a}" в обасти видимости test_function() \n')

    inner_function('inner')
    print(f'Конец области видимости test_function()')


test_function()
# inner_function("inner") #- Ошибка функция неопределена
