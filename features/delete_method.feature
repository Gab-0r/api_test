Feature: API delete method
  As a user
  I want to call delete method
  In order to delete a resource

  @delete
  Scenario Outline: Use DELETE method to delete a <element> resource
    When user sends DELETE method to <endpoint> for delete a <element>
    Then user verifies delete status code 200
    And user verifies the delete response has the correct info for the resource deleted

    Examples:
    | element | endpoint  |
    | post  | /posts/10 |
    | comment | /comments/100 |
    | album | /albums/19       |
    | photo | /photos/650 |
    | todo  | /todos/23 |
    | user  | /users/2  |

