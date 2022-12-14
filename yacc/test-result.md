Итак результаты тестирования на некоторых грамматиках: 
1. Арифметика
    * Было протестировано две разные грамматики для арифметики, первая самая простая с приоритетами и левой рекурсией, вторая без левой рекурсии, без приоритетов yacc, чистая грамматика, если можно так выразиться. Питоновские вычисления результатов опущены. На одинаковых наборах тестов первая грамматика показала существенно лучший результат, парсит высражение на порядка 25 процентов быстрее. Возможно из-за большего количества правил.
        * Результаты: 

            - no-paren(50000 символов)
                - arithmetic1 : 0.10344290733337402 seconds
                - arithmetic2 : 0.12003016471862793 seconds

            - ones(25000 символов)
                - arithmetic1 : 0.04082298278808594 seconds
                - arithmetic2 : 0.06065201759338379 seconds

            - paren(100000 символов)
                - arithmetic1 : 0.15662097930908203 seconds
                - arithmetic2 : 0.19559192657470703 seconds

            - no-parenLarge(1000000 символов)
                - arithmetic1 : 1.4125490188598633 seconds
                - arithmetic2 : 2.0343801975250244 seconds

            - onesLarge(1000000 символов)
                - arithmetic1 : 1.5152668952941895 seconds
                - arithmetic2 : 2.618345022201538 seconds

            - parenLarge(1000000 символов)
                - arithmetic1 : 1.5084118843078613 seconds
                - arithmetic2 : 2.045279026031494 seconds
        

2. Скобочные последовательности
    * Тоже 2 грамматики, немного на разные языки правда. Первая грамматика на все псп с двумя типами скобок. Вторая грамматика на язык Дика (с моего варианта теста), в нормальной форме Хомского. Ну и как не странно, на одинаковых тестах вторая грамматика показала результат хуже, чем первая. Тут уже целенаправленно была выбрана грамматика с большим кол-вом правил, из-за чего видимо и получается меньшая производительность.
        * Результаты: 
            - large-psp
                - psp : 0.40480518341064453 seconds
            - open-close
                - psp : 0.6884052753448486
                - psp-big-grammar : 1.144317865371704
            - open-then-close
                - psp : 0.5548670291900635
                - psp-big-grammar : 1.0440459251403809
