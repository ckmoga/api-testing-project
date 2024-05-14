Feature: Search books, add books to cart and checkout
  This test suite verifies the feature for searching books,
  adding books to cart and checkout

  Scenario Outline: Search book by query
    When I search books for <keyword> keyword
    Then I should get <total> books

    Examples:
      | keyword | total |
      | john    | 5     |

  Scenario: Attempt to search with empty query
    When I search books without keyword
    Then I should get invalid request error

