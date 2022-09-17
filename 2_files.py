"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding ='utf-8') as text:
        #for line in text
            string_file = text.read()
            print(string_file)
            print('длина строки - ',len(string_file))
            print('Кол-во слов в строке -', len(string_file.split()), '\n') 
            string_file = string_file.replace('.','!')
    with open('referat2.txt', 'w', encoding="utf-8") as result:
        result.write(string_file)

if __name__ == "__main__":
    main()

""" with open('referat2.txt', 'w', encoding="utf-8") as result:
    result.write() """
    