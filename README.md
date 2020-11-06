# word generator | Python
Приложение для создания человеко-подобных слов, состоящая из списка открытых и закрытых звуков, идущих друг за другом

Для запсука приложения используйте комманду: "python3 wordsgen/app.py"

По умолчанию, флажок variant 1, служит для генерации слов начинающихся с согласных
variant 2, для генерации слов начинающихся с гласных

Формы variant 1 и variant 2, служат для изменения списка доступных букв/слогов
отделять каждую букву нужно пробелом(можно помещать слоги), например:

variant 1: 
b c d f g


variant 2: 
a e i u o

После ввода списка, следует обновить её, конпкой "Update"

Форма ввода "Enter last word", служит для подставления строки под конец слова


Алгоритм вывода слова, находися в модуле words_gen.py

Функция consonant(count, ending=""), служит для генерации слов начинающихся на согласную
Функция vowel(count, ending=""), служит для генерации слов начинающихся на гласную.

где count - длина слова в буквах/слогах
где ending - строка, подставляемая под конец слова.



EN


An application for creating human-like words, consisting of a list of open and closed sounds following each other

To start the application use the command: "python3 wordsgen / app.py"

By default, the variant 1 flag is used to generate words starting with consonants
variant 2, for generating words starting with vowels

Forms variant 1 and variant 2 are used to change the list of available letters / syllables
you need to separate each letter with a space (you can put syllables), for example:

variant 1:
b c d f g


variant 2:
a e i u o


After entering the list, you should update it using the "Upadate" button

Input form "Enter last word", serves to substitute a line at the end of a word


Word output algorithm, found in the words_gen.py module

The consonant (count, ending = "") function is used to generate words starting with a consonant
The vowel (count, ending = "") function is used to generate words beginning with a vowel.

where count is the length of the word in letters / syllables
where ending is a string substituted at the end of a word.
