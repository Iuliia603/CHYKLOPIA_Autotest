Feature: Book call functionality
  The user should be able to book a call in the calendar

  Background:
    Given user opens the Homepage
    And user clicks the Get a call button
    And the booking page is open


  Scenario: Selecting the date and time of the call in the calendar
    When user clicks the Get start button
    Then the calendar is open
    When user selects data
    And user select time
#    And user clicks the Next button
#    Then the information about the call is displayed
