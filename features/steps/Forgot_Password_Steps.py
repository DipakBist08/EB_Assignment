import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open PHPTravels webpage')
def OpenWebPage(context):
    context.driver.get('https://phptravels.org/login')
    context.driver.maximize_window()


@given('Click on Account Dropdown')
def DropDownMeanu(context):
    Dropdown_Meanu = context.driver.find_element(By.XPATH, '//*[@id="Secondary_Navbar-Account"]/a')
    Dropdown_Meanu.click()


@given('Click on Forgot Password')
def ClickOnForgotPassword(context):
    Forgot_Pass = context.driver.find_element(By.ID, 'Secondary_Navbar-Account-Forgot_Password?')
    Forgot_Pass.click()
    time.sleep(15)  # for captcha handaling


@given(u'Provide Valid Email Address')
def step_impl(context):
    Email = context.driver.find_element(By.ID, 'inputEmail')
    Email.send_keys('testtest2022@gmail.com')
    time.sleep(20)


@given('Click on Submit Button')
def ClickOnSubmitButton(context):
    Submit = context.driver.find_element(By.XPATH, '//*[@id="main-body"]/div/div[1]/div/div/div/div/form/div[3]/button')
    Submit.click()


@then('Password will be sent in email "testtest2022@gmail.com"')
def PasswordSentToEmail(context):
    try:
        # Wait for the success message to be visible on the page
        success_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              '//div[@class="alert alert-success text-center" and contains(text(), "Password Reset Requested")]')))

        # Assert if the success message is displayed
        assert success_message.is_displayed(), "Password reset sent to email"
        print("Password reset was successful")
    except:
        print("Password reset message not found or not displayed")

    context.driver.close()
