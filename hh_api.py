import requests
import pprint
import hh_vacansy             # мои самописные функции



vacancy = 'python developer'

url = 'https://api.hh.ru/vacancies'

# vacancy = input('Введите название вакансии: ')

params = {
    'text': vacancy,
    'area': 1,        # Поиск ощуществляется по вакансиям города Москва
    'per_page': 100,  # Количество вакансий на странице (максимум)
}

# response = requests.get(url, params=params).json()

                # подсчет количества вакансий на сайте
total_vacancies = functions.count_total_vacancies(params, url)
print(f'Всего вакансий {vacancy} = {total_vacancies}')
                # подсчет средней заработной платы
average_salary = calculate_average_salary(params, url)
if average_salary is not None:
    print(f'Средняя заработная плата =  {average_salary} рублей')
else:
    print('Информация о зарплате не доступна в вакансиях')

