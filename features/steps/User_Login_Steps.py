from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('Launch Chrome Browser')
def LaunchChromeBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'Open  PHPTravels Webpage Page')
def LoginPage(context):

    context.driver.get('https://phptravels.org/login')
    time.sleep(3)


@when('Input valid User Name "{userEmail}" and Password "{PWD}"')
def ValidCredentials(context, userEmail, PWD):
    Email_Address = context.driver.find_element(By.ID, 'inputEmail')
    Password = context.driver.find_element(By.ID, 'inputPassword')

    Email_Address.send_keys(userEmail)
    time.sleep(10)
    Password.send_keys(PWD)
    time.sleep(20) # There is captcha so it can't be handled by selenium we need to handle manually.


@when('Click on Login Button')
def ClickOnLoginButton(context):
    Login_Button = context.driver.find_element(By.ID, 'login')
    Login_Button.click()
    time.sleep(3)


@then('User Should successfully Login to PHPTravels')
def LoggedIn(context):
    try:
        LogOut_Element = context.driver.find_element(By.XPATH,
                                                     '//a[@href="/logout.php" and contains(text(), "Logout")]')
        assert LogOut_Element.is_displayed(), "User  log in successfully"
        print("User Logged In Successfully")
    except:
        print("User did not log in successfully")


@then('Close Browser')
def CloseBrowser(context):
    time.sleep(2)
    context.driver.close()
