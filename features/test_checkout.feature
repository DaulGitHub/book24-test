Feature: Checkout tests
  # Автотесты заказа товара

  Background:
    Given Logged as persona "Autotester"
    Given basket page

  @1
  Scenario: Checkout
    When I press "Оформить заказ" button
     And I press "Далее" button
     And I press "Курьер" button
     And I fill address fields
     And I press "Далее" button on courier block
     And I press "Далее" button on payment block
    Then I should see confirmation page
      | address                                            | coast delivery             | payment                            | payer type                        | name                            | mail           | phone            |
      | Москва г, Хорошёвское шоссе, д 88 стр 1, 4, 123308 | Стоимость доставки: 200 р. | При получении наличными или картой | Тип плательщика - Физическое лицо | AutotestSecondname AutotestName | daul_m@mail.ru | +7 953 771-36-87 |

