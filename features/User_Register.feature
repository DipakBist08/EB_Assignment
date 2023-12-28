Feature: User Registration
  Scenario: Verify that user can register with valid email
    Given Launch Chrome Browser
    And Open Registration Page
    And Fill out All the personal Details
    And Fill Billing Address
    And Additional Required Information
    And Account Security
    And Handle Mailing List Option
    And Click on Register
    Then User Must have Registered Successfully
    And Close Browser