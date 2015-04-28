Feature: Work with tasks
  Allow adding, creating, updating and deleting tasks.

  Scenario: Add, edit and delete a task
    Given I just reset my account
    When I create a new todo Shoot the moon
    And I add the task
    And I ask for current tasks
    Then The new task should exist
    When I modify the task
    And I ask for the specific task
    Then The modified task should be different
    When I perform the task
    And I ask for the specific task
    Then The task should be completed
    When I delete that task
    And I ask for the specific task
    Then The deleted task should be gone