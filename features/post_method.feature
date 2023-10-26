Feature: API post method
  As a user
  I want to call post method to and endpoint
  In order to send data to the API


  @post
  Scenario Outline: Use POST method to send a <element> to API
    When user sends POST method to <endpoint>
    Then user sends GET method to <endpoint>
    And user verifies the get response has the correct info for <element>

    Examples:
    | element | endpoint  |
    | post    | /posts  |
    | comment | /comments |
    | album | /albums |
    | photo | /photos |
    | todo  | /todos  |
    | user  | /users  |