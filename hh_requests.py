import requests
import pprint
import time



url = 'https://api.hh.ru/vacancies'

params = {
    'text': 'python developer',
    'area': 1,        # Поиск ощуществляется по вакансиям города Москва
    # 'per_page': 100,  # Количество вакансий на странице (максимум)
    'page': 1
}


# page = 0
skills = []
key_skills = {}

response = requests.get(url, params=params).json()
# pprint.pprint(response)


# список вакансий
items = response['items']

for item in items[:50]:
    url = item['url']
    response = requests.get(url).json()

    # if response.status_code == 200:
        # print(f'...обрабатывается страница {page}...')
    # pprint.pprint(response)
    # Ключевые навыки
    # print(response['key_skills'])
    #добавляем задержку между запросами
    time.sleep(1)

    for val in response['key_skills']:
        skills.append(val['name'])


    for item in skills:
        if item in response['key_skills']:
            key_skills[item] += 1

        else:
            key_skills[item] = 1

    result = sorted(key_skills.items(), key=lambda x: x[1], reverse=True)


    # else:
    # print(f'Запрос страницы {page} завершился неудачно с кодом {response.status_code}')
    # if response.status_code == 400:
    #     print('Превышен лимит запросов. Добавляем задержку...')
    #     time.sleep(60)  # Подождать 60 секунд (может потребоваться больше)
    # else:
    #     print('что-то все не так')
    #     break

# print(skills)


print(key_skills)
print('*' * 50)
pprint.pprint(result)






# Сохранение результатов в JSON-файл
# with open('results_python_developer.json', 'w', encoding='utf-8') as f:
#     json.dump(results, f, ensure_ascii=False, indent=4)
#
# print('Результаты сохранены в файл results_python_developer.json')