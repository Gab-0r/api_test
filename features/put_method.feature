Feature: API put method
  As a user
  I want to call put method to an endpoint
  I order to update a resource

  @put
  Scenario Outline: Use PUT method to update a <element> resource
    When user sends PUT method to <endpoint> for post a <element>
    Then user verifies put status code 200
    And user verifies the put response has the correct info for the <element> updated

    Examples:
    | element | endpoint  |
    | post  | /posts/90 |
    | comment | /comments/150 |
    | album | /albums/25  |
    | photo | /photos/950 |
    | todo  | /todos/125  |
    | user  | /users/2  |