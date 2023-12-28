from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


@given('Open Registration Page')
def OpenRegistrationPage(context):
    context.driver.get('https://phptravels.org/register.php')
    context.driver.maximize_window()


@given('Fill out All the personal Details')
def PersonalDetails(context):
    First_Name = context.driver.find_element(By.ID, 'inputFirstName')
    First_Name.send_keys('Rahul')
    time.sleep(2)

    Last_Name = context.driver.find_element(By.ID, 'inputLastName')
    Last_Name.send_keys('Shrestha')
    time.sleep(2)  # to make screen visible what is happening

    Email_Address = context.driver.find_element(By.ID, 'inputEmail')
    Email_Address.send_keys('rahulshrestha01@gmail.com')
    time.sleep(5)

    #  to open the country selection dropdown

    selected_dial_code = context.driver.find_element(By.CLASS_NAME, 'selected-dial-code')
    selected_dial_code.click()

    # select Nepal from the country list
    nepal_option = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Nepal (नेपाल)")]')))

    nepal_option.click()
    time.sleep(5)
    Input_MobileNo = context.driver.find_element(By.ID, 'inputPhone')
    Input_MobileNo.send_keys('9811121314')
    time.sleep(3)
    # To scroll Down

    context.driver.execute_script("window.scrollBy(0, 300);")


@given('Fill Billing Address')
def BillingAddress(context):
    Company_Name = context.driver.find_element(By.ID, 'inputCompanyName')
    Company_Name.send_keys('EB Pearls')
    Street = context.driver.find_element(By.ID, 'inputAddress1')
    Street.send_keys('Baneshwor')

    Address2 = context.driver.find_element(By.ID, 'inputAddress2')
    Address2.send_keys('Old-Baneshwor')

    City = context.driver.find_element(By.ID, 'inputCity')
    City.send_keys('Kathmandu')
    time.sleep(2)

    State = context.driver.find_element(By.ID, 'stateinput')
    State.send_keys('Bagmati')
    time.sleep(2)
    Postal_Code = context.driver.find_element(By.ID, 'inputPostcode')
    Postal_Code.send_keys('44600')

    select_country = Select(context.driver.find_element(By.ID, 'inputCountry'))

    # Select Nepal by its visible  text
    select_country.select_by_visible_text('Nepal')


@given('Additional Required Information')
def AdditionalInfo(context):
    Mobile_WhatsAPP = context.driver.find_element(By.ID, 'customfield2')
    Mobile_WhatsAPP.send_keys('9811121314')
    time.sleep(2)


@given('Account Security')
def AccountSecurity(context):
    Password = context.driver.find_element(By.ID, 'inputNewPassword1')
    Password.send_keys('Test@123#')
    Confirm_Password = context.driver.find_element(By.ID, 'inputNewPassword2')
    Confirm_Password.send_keys('Test@123#')
    context.driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(5)


@given('Handle Mailing List Option')
def HandleMalingList(context):
    #  element containing the "No" text
    checkbox =context.driver.find_element(By.XPATH, '//input[@type="checkbox"][@name="marketingoptin"]')

    # Check if the checkbox is checked
    assert checkbox.is_selected(),"Passed"
    time.sleep(2)
    context.driver.execute_script("window.scrollBy(0, 50);")
    time.sleep(20) # Captcha need to handle manually


@given('Click on Register')
def RegisterButton(context):
    Register_Button=context.driver.find_element(By.XPATH,'//*[@id="frmCheckout"]/p/input')
    Register_Button.click()


@then('User Must have Registered Successfully')
def RegistrationSuccessfully(context):
    Register_Message=context.driver.find_element(By.XPATH,'//*[@id="main-body"]/div/div[1]/div[1]/div[1]/div/div[1]/h3/text()').text
    assert Register_Message.is_displayed(),"Register Successfully"

#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