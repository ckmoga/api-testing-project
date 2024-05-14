Feature: User registration and login
  These scenarios validate the user registration and login features
  of the book store

  Scenario Outline: Invalid login
    When I login with email <email> and password <password>
    Then I should receive invalid request message
    # we are using 'none' for empty/None values so it can be parsed in step definition
    Examples:
      | email       | password        |
      | a@email.com | none            |
      | none        | goodPassword123 |

  Scenario: Successful login
    When I login with email a@email.com and password goodPassword123
    Then I should receive a token


  Scenario: Invalid credentials
    When I login with email a@email.com and password goodPassword1234
    Then I should receive invalid credentials error


  Scenario Outline: Unsuccessful registration
    When I register with <email>, <password>, <firstName> and <lastName>
    Then I should receive invalid request message

    Examples:
      | email       | password     | firstName | lastName |
      | a@email.com | goodPassword | John      | none     |
      | a@email.com | goodPassword | none      | Smith    |
      | none        | goodPassword | John      | Smith    |
      | a@email.com | none         | John      | Smith    |

  Scenario: Successful registration
    When I register with a@email.com, goodPassword, John and Smith
    Then I should receive a token

      # demonstrates the use of complex parameter structures such as list or json
  Scenario: Add books to the cart
    Given I have added these ["id1", "id2", "id3"] books to the cart
    When I view my cart contents
    Then there should be 5 books


  Scenario: Successful checkout
    Given I have added these ["id1", "id2", "id3"] books to the cart
    When I checkout
    Then I should receive order number


  Scenario: Invalid checkout
    When I checkout without items in the cart
    Then I should receive an error message