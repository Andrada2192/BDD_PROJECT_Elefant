Feature: Search bar feature

  Background:
    Given I am on the main page

  @first
  Scenario: Search given item and verify if the list displayed contains more than 10
    When I enter "iphone 14" in search field
    And I press the search button
    Then I should see a list of elements with less than 10 items


  @second
  Scenario: Search an item that doesn't exist
    When I enter "quicksand acrylic block" in search field
    And I press the search button
    Then I should see an error message