# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# @pytest.fixture(scope="session")
# def browser():
#     options = Options()
#     options.add_extension("path/to/extension.crx")  # add extension path
#     options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()


# def test_block_zhihu(browser):
#     browser.get("https://www.zhihu.com/")
#     assert "This site can’t be reached" in browser.page_source
