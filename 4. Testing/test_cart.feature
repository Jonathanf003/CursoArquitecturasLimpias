Feature: Cart functionality

  Scenario: Add product with price greater than $100 and apply 10% discount
    Given a cart with total price $200
    When I add a product with price $150
    Then the total price should be $135
