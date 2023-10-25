Feature: API get method
  As a user
  I want to call get method to an endpoint
  In order to obtain data from the API

  @get
  @getSingle
  Scenario Outline: Use GET method to obtain single <element>
    When user sends GET method to <endpoint>
    Then user verifies the response status code is 200
    And user verifies the get response has the correct info for <element>

    Examples:
    | element | endpoint  |
    | post    | /posts/50 |
    | comment | /comments/100 |
    | album   | /albums/33    |
    | photo   | /photos/13    |
    | todo    | /todos/21     |
    | user    | /users/5      |
