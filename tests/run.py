from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get('http://localhost:8080')
    start_button = driver.find_element_by_class_name('start-button')
    start_button.click()

    search_box = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
    search_box.send_keys('1')

    li = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'li')))
    li.click()

    add_button = driver.find_element_by_class_name('add-button')
    add_button.click()
    search_box_value = search_box.get_attribute('value')

    driver.refresh()

    cells = driver.find_elements_by_class_name('cell')
    assert any(cell.text == search_box_value for cell in cells)

    trash_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'el-button--danger')))
    trash_button.click()

    driver.refresh()

    cells = driver.find_elements_by_class_name('cell')
    assert all(cell.text != search_box_value for cell in cells)

    driver.close()

    print('OK')


if __name__ == '__main__':
    main()

