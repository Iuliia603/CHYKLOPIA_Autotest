Feature: Header functionality
  In order to navigate through the website, the user should be able to access different directions from the header.

  Background:
    Given user opens the Homepage

# стр подтверждения
  Scenario: Open Capabilities page

    When user clicks the Capabilities button
    Then Capabilities page is open


# стр подтверждения
  Scenario: Open Brand Strategy & Development from the Capabilities dropdown

    When user clicks the Capabilities dropdown
    And user clicks Brand Strategy & Development
    Then Brand Strategy & Development page is open

@positive
  Scenario: Open Work page

    When user clicks the Work button
    Then Work page is open

# стр подтверждения
  Scenario: Button Get on a call functionality

    When user clicks the Get on a call button
    Then the page for booking a call is open


  Scenario: Logo functionality

    When user clicks the logo
    Then Home page is open



