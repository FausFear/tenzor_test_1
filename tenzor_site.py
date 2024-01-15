from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

class SbisWebsite:
    def __init__(self, url):
        self.url = url
        self.browser = Chrome()

    # Открыть сайт
    def open(self):
        self.browser.get(self.url)
        time.sleep(4)

    # Нажать кнопку
    def click_button(self, selector):
        button = self.browser.find_element(By.CSS_SELECTOR, selector)
        button.click()
        time.sleep(4)

    # Активируем окно
    def switch_to_window(self, window_index):
        window_handles = self.browser.window_handles
        self.browser.switch_to.window(window_handles[window_index])
        time.sleep(2)

    # Поиск элемента по CSS селектору
    def find_element_by_css(self, css_selector):
        return self.browser.find_element(By.CSS_SELECTOR, css_selector)

    # Поиск элементов по CSS селектору
    def get_elements_by_css(self, css_selector):
        return self.browser.find_elements(By.CSS_SELECTOR, css_selector)

    # Получаем размеры изображений
    def get_element_size(self, element):
        return [element.size['width'], element.size['height']]

    # Закрываем браузер
    def close_browser(self):
        self.browser.quit()

def main():
    sbis = SbisWebsite("https://sbis.ru/")
    sbis.open()

    # Кнопка Контакты
    sbis.click_button("a[href='/contacts']")
    print("Нажали кнопку Контакты")

    # Кнопка Тензор
    sbis.click_button("img[src='/resources/SabyRuPages/_contacts/images/logo.svg?x_module=23.7141-56']")
    print("Нажали кнопку Тензор")

    # Переключение на второе окно
    sbis.switch_to_window(1)
    print("Переключились на второе окно")

    # Поиск блока "Сила в людях"
    block = sbis.find_element_by_css("div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
    print("Нашли блок Сила в людях")

    # Проверка текста в блоке "Сила в людях"
    if "Сила в людях" in block.text:
        print("Проверяем есть ли блок 'Сила в людях': ", True)

    # Переход на страницу "Подробнее"
    sbis.click_button("a[href='/about']")
    print("Нажали на кнопку Подробнее")

    # Печать текущего URL
    print("Текущий веб адрес: ", sbis.browser.current_url)

    # Поиск фотографий из блока "Работаем"
    block_works_photos = sbis.get_elements_by_css("div[class='tensor_ru-About__block3-image-filter']")

    # Создание списка размеров фотографий
    list_size_photo = [sbis.get_element_size(photo) for photo in block_works_photos]

    # Печать списка размеров фотографий
    print(list_size_photo)

    # Сравнение размеров фотографий
    true_photo_size_check = all(size == list_size_photo[0] for size in list_size_photo)
    if true_photo_size_check:
        print("Размеры фотографий одинаковые")
    else:
        print("Размеры фотографий разные")

    # Задержка перед закрытием браузера
    time.sleep(5)

    # Закрытие браузера
    sbis.close_browser()


if __name__ == "__main__":
    main()
