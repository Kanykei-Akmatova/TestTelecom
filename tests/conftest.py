import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Edge()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def customer_data():
    first_name = "Tom"
    last_name = "Tomas"
    email = "tomas@abc.kg"
    address = "183 Kipp Street"
    telephone = "3435551234"
    return [first_name, last_name, email, address, telephone]


@pytest.fixture(scope="function")
def customer():
    return "393170"
