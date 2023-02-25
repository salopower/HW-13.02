from selenium.webdriver.common.by import By


def test_home_links(demo_page):
    home_links = demo_page.find_elements(By.PARTIAL_LINK_TEXT, "Home")
    assert len(home_links) == 2
