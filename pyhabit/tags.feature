Feature: Work with tags
  Allow adding, creating, updating and deleting tags.

  Scenario: Get current tags
    Given I just reset my account
    When I ask for current tags
    Then I should get the default tags

  Scenario: Add, edit and delete a tag
    Given I just reset my account
    When I create a new tag
    And I add it
    And I ask for current tags
    Then The new tag should exist
    When I modify the tag
    And I ask for current tags
    Then The modified tag should be different
    When I delete that tag
    And I ask for current tags
    Then The deleted tag should be gone