Feature: API path method
  As a user
  I want to call patch method to an endpoint
  In order to patch a resource


  @patch
  Scenario Outline: Use PATCH method to path a <element> resource
    When user sends PATCH method to <endpoint> and patch a <element>
    Then user verifies patch status code 200
    And user verifies the patch response has the correct info for patched <element>
    Examples:
    | element | endpoint  |
    | post  | /posts/23 |
    | comment | /comments/10 |
    | album | /albums/50 |
    | photo | /photos/68 |
    | todo  | /todos/15  |
    | user  | /users/7  |


