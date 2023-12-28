Feature: Login to PHPTravels

  Scenario: verify that User Login to PHPTravels Webpage
    Given Launch Chrome Browser
    When Open  PHPTravels Webpage Page
    And Input valid User Name "testtest2022@gmail.com" and Password "Test@123#"
    And Click on Login Button
    Then User Should successfully Login to PHPTravels
    Then Close Browser



