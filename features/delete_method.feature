Feature: API delete method
  As a user
  I want to call delete method
  In order to delete a resource

  @delete
  Scenario Outline: Use DELETE method to delete a <element> resource
    When user sends DELETE method to <endpoint> for delete a <element>
    Then user verifies the status code is 200
    And user verifies the response is empty

    Examples:
    | element | endpoint  |
    | post  | /posts/10 |
    | comment | /comments/100 |
    | album | /albums/19       |
    | photo | /photos/650 |
    | todo  | /todos/23 |
    | user  | /users/2  |

  @delete
  @deleteWrong
  Scenario Outline: Use DELETE method to the wrong endpoint <endpoint>
    When user sends DELETE method to <endpoint> for delete a <element>
    Then user verifies the status code is 404
    And user verifies the response is empty

    Examples:
    | element | endpoint  |
    | post  | /post/20 |
    | comment | /cent/10 |
    | album | /alm/50 |
    | photo | /photo/68 |
    | todo  | /tod/15  |
    | user  | /use/7  |


  @delete
  @deleteWrong
  Scenario Outline: Use DELETE method to the enpoint <endpoint> with wrong resource id
    When user sends DELETE method to <endpoint> for delete a <element>
    Then user verifies the status code is 500

    Examples:
    | element | endpoint  |
    | photo | /photos/6000  |
    | user  | /users/11 |
    | album | /albums/101 |
    | photo | /photos/5001  |
    | todo  | /todos/201    |
    | user  | /users/11     |