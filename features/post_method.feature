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

  @post
  @postWrongEndpoint
  Scenario Outline: use POST method to the wrong endpoint <endpoint>
    When user sends POST method to <endpoint> for post a <element>
    Then user verifies post status code 404
    And user verifies the post response is empty
    Examples:
    | element | endpoint  |
    | post    | /post  |
    | comment | /es |
    | album | /alms |
    | photo | /ph |
    | todo  | /ts  |
    | user  | /uss  |


  @post
  @postWrongData
    Scenario Outline: use POST method to <endpoint> with wrong data
      When user sends POST method to <endpoint> for post a <element>
      Then user verifies post status code 500
      Examples:
      | element | endpoint  |
      | wrong_post    | /posts    |
      | wrong_photo | /photos |
      | wrong_todo  | /todos  |
