import threading
from settings import *
import random
import time
import requests
from bs4 import BeautifulSoup
import json
from stem import Signal
from stem.control import Controller

import os
os.environ.get("SSLKEYLOGFILE")

session = requests.session()
def get_tor_session():
    session.proxies = {'http': 'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    return session




def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=password_hash_de)
        controller.signal(Signal.NEWNYM)


def find_captcha_base64_frpage(number_img, url):
    global html, session, soup
    html = session.get(url, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
    imgs_tag = soup.find_all("img")
    img_tag = imgs_tag[number_img]
    img_src = img_tag['src']
    return img_src


def find_captcha_base64_secpage(number_img):
    global html, session, soup
    soup = BeautifulSoup(html, "lxml")
    imgs_tag = soup.find_all("img")
    img_tag = imgs_tag[number_img]
    img_src = img_tag['src']
    return img_src


def find_captcha_data(num):
    global html, soup
    soup = BeautifulSoup(html, "lxml")
    inputs_tag = soup.find_all("input")
    input_tag = inputs_tag[num]
    data_captcha = input_tag['value']
    print(data_captcha)
    return data_captcha


def send_captcha_base64(base64_text):
    answer = requests.post(
        f"https://rucaptcha.com/in.php",
        json={"key": api_key_rucaptcha, "method": "base64", "body": base64_text, "json": "1"}
    )
    time.sleep(sleep_ready_captcha)
    captcha_list = json.loads(answer.text)
    captcha_id = captcha_list["request"]
    re_answer = requests.get(
        "https://rucaptcha.com/res.php?key=" + api_key_rucaptcha + "&action=get&id=" + captcha_id + "&json=1"
    )
    re_captcha_list = json.loads(re_answer.text)
    re_captcha = re_captcha_list["request"]
    return re_captcha


def send_captcha_to_formfp(ses, origin):
    global session, html
    data = {
        "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
        "captchaData": find_captcha_data(1),
        "ret": "/"
    }
    session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
    t = session1
    html = t.text
    soup = BeautifulSoup(html, "lxml")
    re_captchs = soup.find_all("input")
    captchs = re_captchs[0]
    check_capt = captchs['name']
    if check_capt != "_token":
        print("Ошибка. Первая капча была не правильной. Производим повторную отправку")
        data = {
            "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
            "captchaData": find_captcha_data(1),
            "ret": "/"
        }
        session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
        t = session1
        html = t.text
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "_token":
        print("Ошибка. Первая капча была не правильной. Производим повторную отправку")
        data = {
            "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
            "captchaData": find_captcha_data(1),
            "ret": "/"
        }
        session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
        t = session1
        html = t.text
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "_token":
        print("Ошибка. Первая капча была не правильной. Производим повторную отправку")
        data = {
            "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
            "captchaData": find_captcha_data(1),
            "ret": "/"
        }
        session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
        t = session1
        html = t.text
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "_token":
        print("Ошибка. Первая капча была не правильной. Производим повторную отправку")
        data = {
           "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
           "captchaData": find_captcha_data(1),
            "ret": "/"
        }
        session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
        t = session1
        html = t.text
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]

    if check_capt != "_token":
        print("Ошибка. Первая капча была не правильной. Производим повторную отправку")
        data = {
            "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
            "captchaData": find_captcha_data(1),
            "ret": "/"
        }
        session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
        t = session1
        html = t.text
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "_token":
        print("Ошибка. Первая капча была не правильной. Производим повторную отправку")
        data = {
            "captcha": send_captcha_base64(find_captcha_base64_frpage(0, origin)),
            "captchaData": find_captcha_data(1),
            "ret": "/"
        }
        session1 = ses.post(origin + origin_url_gate, data=data, headers=headers)
        t = session1
        html = t.text
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']




def send_form_to_secpage(sess, login, password, origin):
    global session, html

    data = {"_token": "",
            "login": login,
            "password": password,
            "captchaData": find_captcha_data(3),
            "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
            }
    session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
    r = session2
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    new_tag = soup.new_tag('input', id='file_history')
    soup.body.insert(1, new_tag)
    soup = BeautifulSoup(html, "lxml")
    re_captchs = soup.find_all("input")
    captchs = re_captchs[0]
    check_capt = captchs['name']
    if check_capt != "query":
        print("Ошибка. Вторая капча была не правильной. Производим повторную отправку")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        data = {"_token": "",
                "login": login,
                "password": password,
                "captchaData": find_captcha_data(3),
                "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
                }
        session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
        r = session2
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "query":
        print("Ошибка. Вторая капча была не правильной. Производим повторную отправку")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        data = {"_token": "",
                "login": login,
                "password": password,
                "captchaData": find_captcha_data(3),
                "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
                }
        session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
        r = session2
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "query":
        print("Ошибка. Вторая капча была не правильной. Производим повторную отправку")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        data = {"_token": "",
                "login": login,
                "password": password,
                "captchaData": find_captcha_data(3),
                "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
                }
        session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
        r = session2
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "query":
        print("Ошибка. Вторая капча была не правильной. Производим повторную отправку")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        data = {"_token": "",
                "login": login,
                "password": password,
                "captchaData": find_captcha_data(3),
                "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
                }
        session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
        r = session2
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "query":
        print("Ошибка. Вторая капча была не правильной. Производим повторную отправку")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        data = {"_token": "",
                "login": login,
                "password": password,
                "captchaData": find_captcha_data(3),
                "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
                }
        session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
        r = session2
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']

    if check_capt != "query":
        print("Ошибка. Вторая капча была не правильной. Производим повторную отправку")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        data = {"_token": "",
                "login": login,
                "password": password,
                "captchaData": find_captcha_data(3),
                "captcha": send_captcha_base64(find_captcha_base64_secpage(0))
                }
        session2 = sess.post(origin + origin_url_login, data=data, headers=headers)
        r = session2
        html = r.text
        soup = BeautifulSoup(html, "lxml")
        new_tag = soup.new_tag('input', id='file_history')
        soup.body.insert(1, new_tag)
        soup = BeautifulSoup(html, "lxml")
        re_captchs = soup.find_all("input")
        captchs = re_captchs[0]
        check_capt = captchs['name']




def sess_buy_page(link, sess, origin):
    global session, html
    session3 = sess.get(origin+link, headers=headers)
    r = session3
    html = r.text


def pars_momental_value():
    global html, soup, input_token, input_form_uuid, input_product_id, input_momental, input_type, input_roulette_id
    soup = BeautifulSoup(html, "lxml")
    print(html)
    new_tag = soup.new_tag('input', id='file_history')
    soup.body.insert(1, new_tag)
    inputs_tag = soup.find_all("input")
    pre_input_token = inputs_tag[2]
    pre_input_form_uuid = inputs_tag[3]
    pre_input_product_id = inputs_tag[4]
    pre_input_momental = inputs_tag[5]
    pre_input_type = inputs_tag[6]
    pre_input_roulette_id = inputs_tag[12]
    input_roulette_id = pre_input_roulette_id["value"]
    input_token = pre_input_token['value']
    input_form_uuid = pre_input_form_uuid['value']
    input_product_id = pre_input_product_id['value']
    input_momental = pre_input_momental['value']
    input_type = pre_input_type['value']


def buy(sess, origin):
    global session, html, input_token
    data = {"_token": input_token,
            "form-uuid": input_form_uuid,
            "product_id": input_product_id,
            "momental": input_momental,
            "type": input_type,
            "storage_type_id": 0,
            "coupon": "",
            "payment": "balance",
            "roulette_id": input_roulette_id
            }
    session4 = sess.post(origin + origin_url_momental_confirm, data=data, headers=headers)
    r = session4
    html = r.text


def feedback(sess, origin):
    global session, html
    soup = BeautifulSoup(html, "lxml")
    order_id_s = soup.find_all("a")
    order_id = order_id_s[53]
    or_id = order_id["data-order"]
    inputs_tag = soup.find_all("input")
    pre_input_token = inputs_tag[1]
    token_for_feedback = pre_input_token["value"]
    data = {"_token": token_for_feedback,
            "review": random.choice(open('otziv.txt', 'r').read().splitlines()),
            "tips": 0,
            "tips-custom": 50,
            "rate": 10
            }
    session5 = sess.post(origin + "/orders/" + or_id + "/review", data=data, headers=headers)
    r = session5
    html = r.text


def ip_adress(sess):
    global r_s_ip
    r = sess.get("http://httpbin.org/ip").text
    r_s = json.loads(r)
    r_s_ip = r_s["origin"]


def scripts(login, password, i, prodict_href_mom):
    global session, headers

    zerkalo = random.choice(open('zerkala.txt', 'r').read().splitlines())
    origin = zerkalo
    headers = random.choice(headers_list)

    renew_connection()
    session = get_tor_session()
    ip_adress(session)

    print("Успешно получен новый IP-адрес " + r_s_ip + " потоком - №" + i)
    time.sleep(sleep_ip)

    send_captcha_to_formfp(session, origin)
    print("Вход на первой странице выполнен успешно потоком - №" + i)
    time.sleep(sleep_first_auth)

    send_form_to_secpage(session, login, password, origin)
    print("Вход на второй странице выполнен успешно потоком - №" + i)
    time.sleep(sleep_second_auth)

    sess_buy_page(prodict_href_mom, session,origin)
    print("Сессия страницы моменталки получена успешно потоком - №" + i)
    time.sleep(sleep_session_buy_page)

    pars_momental_value()
    print("Страница мометалки была успешно пропарсена потоком - №" + i)
    time.sleep(sleep_parsing_momental_page)

    buy(session, origin)
    print("Товар был успешно куплен потоком - №" + i)
    time.sleep(sleep_after_buy)

    feedback(session, origin)
    print("Отзыв был успешно оставлен потоком - №" + i)
    print("До нового аккаунта ожидаем время")



for number in range(3):
    th1 = threading.Thread(target=scripts, args=("bacctest", "KK20814kk", "1", product_href1))
    th1.start()
    th1.join()
    time.sleep(sleep_before_new_iteration)
    th2 = threading.Thread(target=scripts, args=("bacctest2", "kk20814kk", "2", product_href1))
    th2.start()
    th2.join()
    time.sleep(sleep_before_new_iteration)
    th3 = threading.Thread(target=scripts, args=("bacctest3", "Kk20814Kk", "3", product_href1))
    th3.start()
    th3.join()
    time.sleep(sleep_before_new_iteration)




