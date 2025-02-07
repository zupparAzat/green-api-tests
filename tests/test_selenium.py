from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://console.green-api.com/auth/login")
    print("Текущий URL:", driver.current_url)
    driver.save_screenshot("page.png")

    try:
        # Ждём загрузки корневого элемента
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "root"))
        )

        # Проверяем текущий URL (возможно, произошёл редирект)
        print("Текущий URL после загрузки:", driver.current_url)

        # Ищем поле email (уточните селектор в DevTools)
        email_field = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        print("Элемент найден!")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()