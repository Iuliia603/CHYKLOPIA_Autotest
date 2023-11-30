Feature: Frequently Asked Questions functionality
  If the user selects a question, the color of the question should turn black and the answer should be displayed.
  If the question is not selected, the question text should be gray.


  Background:
    Given user opens UI/UX page
    Given user scrolls to Frequently Asked Questions


  Scenario:
    When user clicks on the question Why should I care about UX for my website?
    Then the first question color is gray
    When user clicks on the question Why should I care about UX for my website?
    Then answer about care is visible
    And the first question color is black


#  Scenario:
#    When user clicks on the question What should I prepare for my UX project?
#    Then answer about prepare is visible
#    And the second question color is black
#    When user clicks on the question What should I prepare for my UX project?
#    Then the second question color is gray
##
##
#  Scenario:
#    When user clicks on the question Do I need UX strategy?
#    Then answer about need UX strategy is visible
#    And the third question color is black
#    When user clicks on the question Do I need UX strategy?
#    Then the third question color is gray
#
#
#  Scenario:
#    When user clicks on the question What’s the investment price range?
#    Then answer about investment price range is visible
#    And the fourth question color is black
#    When user clicks on the question What’s the investment price range?
#    And the fourth question color is gray
#
#
#  Scenario:
#    When user clicks on the question How long will a UX project take?
#    Then answer about How long is visible
#    And the fifth question color is black
#    When user clicks on the question How long will a UX project take?
#    And the fifth question color is gray

