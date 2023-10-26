Feature: API post method
  As a user
  I want to call post method to and endpoint
  In order to send data to the API


  @post
  Scenario Outline: Use POST method to send a <element> to API
    When user sends POST method to <endpoint> for post a <element>
    Then user verifies post status code 201
    And user verifies the post response has the correct info for posted <element>

    Examples:
    | element | endpoint  |
    | post    | /posts  |
    | comment | /comments |
    | album | /albums |
    | photo | /photos |
    | todo  | /todos  |
    | user  | /users  |