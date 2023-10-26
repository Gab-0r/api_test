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


  @get
  @getAll
  Scenario Outline: Use GET method to obtain the whole <name> resource
    When user sends GET method to <endpoint>
    Then user verifies the response status code is 200
    And user verifies the response for get all <name> resources

    Examples:
    | name  | endpoint  |
    | posts | /posts    |
    | comments  | /comments |
    | photos  | /photos     |
    | todos | /todos        |
    | users | /users  |


  @get
  @getWrongEndpoint
  Scenario Outline: Use GET method to the wrong endpoint <endpoint>
    When user sends GET method to <endpoint>
    Then user verifies the response status code is 404
    And user verifies the response is empty

    Examples:
    | endpoint  |
    | /posts/101 |
    | /pos/ |
    | /comment/500  |
    | /album/40 |
    | /phot0  |
    | /user/10  |