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

    @put
    @putWrongEndpoint
    Scenario Outline: Use PUT method to wrong endpoint <endpoint>
      When user sends PUT method to <endpoint> for post a <element>
      Then user verifies put status code 404
      And user verifies the PUT response is empty

      Examples:
      | endpoint  | element |
      | /pos/500  | post    |
      | /com?200  | comment |
      | /album/60 | album   |
      | /ph/1     | photo   |
      | /todo?/200  | todo  |

    Scenario Outline: Use PUT method to the endpoint <endpoint> with wrong resource id
      When user sends PUT method to <endpoint> for post a <element>
      Then user verifies put status code 500

      Examples:
      | endpoint  | element |
      | /photos/6000  | photo |
      | /users/11 | user  |
      | /albums/101 | album |
      | /photos/5001  | photo |
      | /todos/201    | todo  |
      | /users/11     | user  |
