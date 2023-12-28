import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when(u'Open PHPTravels Webpage Page')
def LoginPage(context):
    context.driver.get('https://phptravels.org/login')
    context.driver.maximize_window()


@then('User should "successfully"')
def verify_successful_login(context):
    try:
        # Check for a logout link or any element visible after successful login
        logout_link = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="/logout.php" and contains(text(), "Logout")]'))
        )
        assert logout_link.is_displayed(), "User did not log in successfully"
        print("User logged in successfully")
    except Exception as e:
        print("User did not log in successfully:", str(e))


@then('User should "unsuccessfully"')
def verify_unsuccessful_login(context):
    try:
        # Check for an error message or any element visible after unsuccessful login
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="error-message"]'))
        )
        time.sleep(20)
        assert error_message.is_displayed(), "Login was expected to fail but did not"
        print("User failed to log in (as expected)")
    except Exception as e:
        print("User logged in unexpectedly:", str(e))
        time.sleep(20)
