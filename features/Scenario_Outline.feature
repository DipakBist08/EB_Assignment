Feature: Login to PHPTravels with Multiple Users

Scenario Outline: Verify login with different user credentials
  Given Launch Chrome Browser
  When Open PHPTravels Webpage Page
  And Input valid User Name "<userEmail>" and Password "<password>"
  And Click on Login Button
  Then User should "<loginStatus>"

Examples:
  | userEmail             | password         | loginStatus      |
  | testtest2022@gmail.com| Test@123#        | successfully     |
  | testtest2021@gmail.com| Test@123#        | unsuccessfully   |
  |testtest2022@gmail.com | Test123          | unsuccessfully   |
  |testtest2020@gmail.com | test111          | unsuccessfully   |
