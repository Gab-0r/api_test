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


  @patch
  @patchWrong
  Scenario Outline: Use PATCH method to wrong endpoint <endpoint>
    When user sends PATCH method to <endpoint> and patch a <element>
    Then user verifies patch status code 404
    And user verifies the PATCH response is empty

    Examples:
    | element | endpoint  |
    | post  | /post/20 |
    | comment | /cent/10 |
    | album | /alm/50 |
    | photo | /photo/68 |
    | todo  | /tod/15  |
    | user  | /use/7  |

  @patch
  @patchWrong
    Scenario Outline: Use PATCH method to the endpoint <endpoint> with wrong resource id
    When user sends PATCH method to <endpoint> and patch a <element>
    Then user verifies patch status code 500

      Examples:
      | element | endpoint  |
      | photo | /photos/6000  |
      | user  | /users/11 |
      | album | /albums/101 |
      | photo | /photos/5001  |
      | todo  | /todos/201    |
      | user  | /users/11     |
