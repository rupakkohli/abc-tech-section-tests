from selenium.webdriver.common.by import By

FINAL_URL = "https://www.abc.net.au/news/topic/science-and-technology"

def test_page_title(driver):
    driver.get(FINAL_URL)
    assert "Science and Technology" in driver.title
