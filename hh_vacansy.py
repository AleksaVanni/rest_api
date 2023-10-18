import json
import re
import requests
import time
url = 'https://api.hh.ru/vacancies'

params = {
    'text': 'python developer',
    'area': 1,  # Поиск осуществляется по вакансиям города Москва
    'per_page': 100,  # Количество вакансий на странице (максимум)
}

total_salary = 0
total_vacancies = 0
page = 0
average_salary = []

while True:
    page += 1
    params['page'] = page

    print(f"Обрабатывается страница {page}")

    response = requests.get(url, params=params)

    # Проверьте, успешен ли запрос
    if response.status_code == 200:
        data = response.json()

        for vacancy in data['items']:
            salary_info = vacancy.get('salary')
            if salary_info:
                salary_string = str(salary_info.get('from'))
                matches = re.findall(r'\d+', salary_string)

                if matches:
                    salary_values = [int(match) for match in matches]
                    if len(salary_values) == 2:
                        min_salary, max_salary = salary_values
                        average_salary = (min_salary + max_salary) / 2
                        total_salary += average_salary
                    elif len(salary_values) == 1:
                        total_salary += salary_values[0]
                    total_vacancies += 1

        if len(data['items']) < params['per_page']:
            break
    else:
        print(f'Запрос страницы {page} завершился неудачно с кодом {response.status_code}')
        if response.status_code == 400:
            print('Превышен лимит запросов. Добавляем задержку...')
            time.sleep(60)  # Подождать 60 секунд (может потребоваться больше)
        else:
            print('что-то все не так')
            break

# Вычисление средней зарплаты
if len(average_salary) > 0:
    total_average_salary = sum(average_salary) / len(average_salary)
    print(f'Средняя зарплата: {total_average_salary} рублей')
else:
    print('Информация о зарплате не доступна в вакансиях')

results = {
    'vacancy': 'python developer',
    'area': 'Москва',
    'total_vacancies': total_vacancies,
    'average_salary': average_salary
}

# Сохранение результатов в JSON-файл
with open('results_python_developer.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print('Результаты сохранены в файл results_python_developer.json')
