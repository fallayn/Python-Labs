from docx import Document

# Реализация алгоритма Бойера-Мура для поиска подстроки в тексте
def boyer_moore(text, pattern):
    # Конвертирование текста и паттерна в нижний регистр
    text = text.lower()
    pattern = pattern.lower()

    # Получение длин текста и паттерна
    n = len(text)
    m = len(pattern)

    # Подсчет таблицы смещений для алгоритма Бойера-Мура
    shifts = {}
    for i in range(m - 1):
        shifts[pattern[i]] = m - i - 1

    # Начало поиска с позиции паттерна
    i = m - 1
    while i < n:
        j = m - 1
        k = i

        # Проверка совпадения символов с конца паттерна
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1

        # Если все символы паттерна совпали, возвращаем индекс начала совпадения
        if j == -1:
            return i - m + 1

        # Смещение в соответствии с таблицей смещений
        if text[i] in shifts:
            i += shifts[text[i]]
        else:
            i += m

    return -1  # Паттерн не найден


# Функция для чтения текста из docx файла
def read_text_from_docx(file_name):
    doc = Document(file_name)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


# Функция для определения плагиата
def find_plagiarism(reference_text, wikipedia_text):
    reference_words = reference_text.split()  # Разделение реферата на слова

    # Инициализация переменной для подсчета количества совпадений
    plagiarism_count = 0

    # Поиск плагиата, считаем три подряд идущих слова как плагиат
    for i in range(len(reference_words) - 2):
        three_words = ' '.join(reference_words[i:i + 3])  # Получение трех слов
        index = boyer_moore(wikipedia_text, three_words)  # Поиск трех слов в тексте из Википедии
        if index != -1:
            plagiarism_count += 1

    # Вычисление процента плагиата
    total_words = len(reference_words)
    plagiarism_percentage = (plagiarism_count / (total_words - 2)) * 100

    return plagiarism_percentage


# Пример использования
# Считываем тексты из docx файлов
wikipedia_article = read_text_from_docx('/home/ru6ik/Desktop/Alina Study/Programming/lab6/exercise_three/fileForSearchAndOriginal//Жизнь_из_Википедии.docx')
reference_article = read_text_from_docx('/home/ru6ik/Desktop/Alina Study/Programming/lab6/exercise_three/fileForSearchAndOriginal//Жизнь.docx')

reference_article_duplicate = read_text_from_docx('/home/ru6ik/Desktop/Alina Study/Programming/lab6/exercise_three/fileForSearchAndOriginal//Жизнь_дубликат.docx')

plagiarism_percentage = find_plagiarism(reference_article, wikipedia_article)

plagiarism_percentage_duplicate = find_plagiarism(reference_article, reference_article_duplicate)
def print_answer(plgiat_percentage):
    print(f"Процент плагиата: {plgiat_percentage:.2f}%")
