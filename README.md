Тестовое задание.
---
___

Ссылка на
тестовое - https://drive.google.com/file/d/1qaPZ0fxuuMgYcZ2ds_8oqYFYFqRdn3tf/view?usp=sharing

Запуск
---
___
#### 1)Зависимости в requirements

    pip install -r requirements.txt

#### 2)Запуск 

    python main.py

#### 3)Чтобы выйти - можно ctrl+C понажимать

Тесты
---
___

#### 1) Чтобы запустить в папке с проектом прописать

    pytest

### немного про тесты

Они чуток посредственные и стоило бы больше времени посидить попилить тесты

Просто мое мнение
---
___

### 1)Не совсем было понятно, как надо было выводить тотал в таблице - это тотал за текущий промежуток или за все время.
Если за текущий - то куррент баланс считается какой? Который на тот момент был или с нуля. Не совсем понял, поэтому сделал так.

### 2)Баланс может в минус уйти. Скажем так - не баг, а фича.
Логично было бы сделать, чтобы в минус не уходил, но эт не написано было, поэтому у нас добрый банк, который дает взаймы.

### 3)Про парсер комманд и кучу регулярок.
Он сделан так, чтобы нам было как можно проще в дальнейшем расширять параметры комманд. 
Для числовых и строковых аргументов разные регулярки - потому что, если делать по другому - будет многа багов. 
Если дадите классный варик - буду признателен.

#### 4) Ну и про "использование оптимальных алгоритмов"
Там так как нет бд и прочего и все храниться в дефолт python массиве =>, чтобы собрать все записи там приходится по всему проходится и делать линию.
Так к чему это, можно было конечно нижнею границу найти с помощью бин поиска, но эт было бы чет слишком сильно мне кажется.


Спасибо за внимание.
---
___