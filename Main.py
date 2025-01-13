def read_sort_write(input_file, output_file):
    try:
        # Чтение содержимого файла
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Удаление лишних символов переноса строки и сортировка
        sorted_lines = sorted([line.strip() for line in lines])
        
        # Запись отсортированных строк в новый файл
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in sorted_lines:
                file.write(line + '\n')
        
        print(f"Сортировка завершена. Результат записан в файл '{output_file}'.")
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Укажите имена входного и выходного файлов
input_file = 'input.txt'  # Замените на имя вашего файла
output_file = 'output.txt'  # Замените на желаемое имя выходного файла

read_sort_write(input_file, output_file)
