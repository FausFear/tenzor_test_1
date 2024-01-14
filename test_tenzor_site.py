import pytest
from tenzor_site import SbisWebsite

@pytest.fixture
def sbis():
    sbis = SbisWebsite("https://sbis.ru/")
    yield sbis
    sbis.close_browser()


def test_contact_button(sbis):
    sbis.open()
    sbis.click_button("a[href='/contacts']")
    assert "Контакты" in sbis.browser.title


def test_power_block(sbis):
    sbis.open()
    sbis.click_button("a[href='/contacts']")
    sbis.click_button("img[src='/resources/SabyRuPages/_contacts/images/logo.svg?x_module=23.7141-56']")
    sbis.switch_to_window(1)
    block = sbis.find_element_by_css("div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
    assert "Сила в людях" in block.text


def test_works_photos_size(sbis):
    sbis.open()
    sbis.click_button("a[href='/contacts']")
    sbis.click_button("img[src='/resources/SabyRuPages/_contacts/images/logo.svg?x_module=23.7141-56']")
    sbis.switch_to_window(1)
    sbis.click_button("a[href='/about']")
    block_works_photos = sbis.get_elements_by_css("div[class='tensor_ru-About__block3-image-filter']")
    list_size_photo = [sbis.get_element_size(photo) for photo in block_works_photos]
    assert all(size == list_size_photo[0] for size in list_size_photo)
