import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Название для поиска
search_query = "Школа Новосибирск"

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу Google Maps
    driver.get("https://www.google.com/maps/")
    time.sleep(3)

    # Поиск поля ввода текста для поиска
    search_box = driver.find_element("id", "searchboxinput")

    # Ввод текста для поиска
    search_box.send_keys(search_query)

    # Немного подождать перед отправкой
    time.sleep(1)

    # Нажать клавишу Enter для запуска поиска
    search_box.send_keys(Keys.ENTER)

    # Немного подождать перед получением результатов
    time.sleep(2)

    # Прокрутка страницы вниз для загрузки дополнительных результатов
    action_chains = ActionChains(driver)
    for _ in range(2999):
        action_chains.send_keys(Keys.CONTROL).send_keys(Keys.DOWN).perform()
    time.sleep(1)

    # Список для хранения информации о сайтах
    sites = []

    # Функция для щелчка по результатам поиска
    def click_for(index):
        results = driver.find_elements("css selector", ".hfpxzc")
        results[index].click()
        print(len(results))
        return index + 1

    # Итерация по результатам поиска
    for i in range(len(results) - 1):
        print(a)
        a = click_for(a)
        time.sleep(2)
        info1 = driver.find_elements("css selector", ".CsEnBe")
        try:
            sites.append(info1[1].text)
            sites.append(info1[2].text)
            sites.append(info1[3].text)
        except:
            print("Error: no site")
        print(sites)
        time.sleep(1)
        # Нажатие кнопки "Назад" в браузере
        back_button = driver.find_element("xpath", "/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/button/span")
        back_button.click()
        time.sleep(1)

    print(sites)

    # Отбор сайтов из полученных данных
    sites_decr = [site for site in sites if "." in site]

    print(sites_decr)

finally:
    # Закрытие браузера
    driver.close()
