Feature: Contact link feature

  Background:
    Given I am on contact page

  @ContactLink
  Scenario: Verify if when leaving only mandatory fields empty formular can't be submitted
    When I enter "645655" in order number field
    And I enter "descriere" in contact description field
    And I click on upload files button
    And I click on submit button
    Then I should see "Te rugam sa introduci o adresa de e-mail valida", "Te rugam sa selectezi o categorie" and "Te rugam sa selectezi motivul principal" error messages
