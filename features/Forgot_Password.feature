Feature: Forgot Password
  Scenario: Verify that user can recover password by clicking on forgot password button
    Given Launch Chrome Browser
    And Open PHPTravels webpage
    And Click on Account Dropdown
    And Click on Forgot Password
    And Provide Valid Email Address
    And Click on Submit Button
    Then Password will be sent in email "testtest2022@gmail.com"
