# User-agent для идентефикации запросов к гидре
# как от устройства. Тут собраны самые популярные
# user-agent на 30.12.2020.
import random


headers_list = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/50.0.2661.102 Safari/537.36'},\
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/83.0.4103.116 Safari/537.36 '},\
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/87.0.4280.88 Safari/537.36 '},\
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/81.0.4044.138 Safari/537.36 '}, \
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/69.0.3497.81 Safari/537.36 Maxthon/5.3.8.2000 '}, \
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/85.0.4183.121 Safari/537.36 '}, \
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/86.0.4240.198 Safari/537.36 '}, \
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/83.0.4103.61 Safari/537.36 '}, \
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/85.0.4183.102 Safari/537.36 '}, \
               \
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                              ' AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/86.0.4240.111 Safari/537.36 '}, \
               \
               {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}, \
                \
               {'User-Agent':'	Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36'}, \
                \
               {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}, \
                \
               {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}, \
                \
               {'User-Agent':'	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}, \
                \
               {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 Maxthon/5.3.8.2000'}, \
                \
               {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}, \
                \
               {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}, \
                \
               {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}, \

# Api ключ от аккаунта rucaptcha.
# Узнать можно по ссылке https://rucaptcha.com/setting
api_key_rucaptcha = "b39d08f4992d5c8e2ca82b1198e938a8"

# Ссылка на страницу оформление моменального клада.
# (Там где выбирается метод оплаты и купон)
# Т.к. URL меняется от аккаунта к аккаунту, нужно указывать всё что после домена.
# Если нужно покупать только 1 позицию на полке, то вставьте в product_href1 концовку ссылки
# и в software.py внизу, в потоках, поставьте product_href1 последним аргументом.
product_href1 = "/checkout/254208/2848006_65325543"
product_href2 = ""
product_href3 = ""
product_href4 = ""
product_href5 = ""
product_href6 = ""
product_href7 = ""
product_href8 = ""
product_href9 = ""
product_href10 = ""
product_href11 = ""
product_href12 = ""
product_href13 = ""
product_href14 = ""
product_href15 = ""
product_href16 = ""
product_href17 = ""
product_href18 = ""
product_href19 = ""
product_href20 = ""
product_href21 = ""
product_href22 = ""
product_href23 = ""
product_href24 = ""
product_href25 = ""
product_href26 = ""
product_href27 = ""
product_href28 = ""
product_href29 = ""
product_href30 = ""


# Пароль от хэша аккаунта Тора
password_hash_de = "KK20814kk"

# Ссылка на страницу запроса первой капчи
origin_url_gate = "/gate"

# Ссылка на страницу запроса второй капчи
origin_url_login = "/login"

# Ссылка на страницу запроса подтверждения покупки
origin_url_momental_confirm = "/checkout/momental/confirm"

# Время задержски на ожидание капчи от сервиса
sleep_ready_captcha = 20

# Время задержки на получение IP
sleep_ip = 3

# Время задержки после первого ввода капчи
sleep_first_auth = 3

# Время задержки после второго ввода капчи и авторизации
sleep_second_auth = 3

# Время задержки после получения сессии страницы покупки
sleep_session_buy_page = 3

# Время задержки после парсинга страницы покупки
sleep_parsing_momental_page = 2

# Время задержки после покупки
sleep_after_buy = 5

# Время задержки между отзывом и началом новой итерации в сек.
sleep_before_new_iteration = (random.randint(300, 1200))

# Количество покупок для одного аккаунта.
# Как только на всех аккаунтах выполнится заданное
# количество покупок, программа завершит работу.
kol_vo = 3


