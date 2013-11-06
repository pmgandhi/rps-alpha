Feature: wages owed

    Scenario: capturing claimants unpaid wage details so that their claim can be processed by RPS
     Given the app is running
      When we visit /claim-redundancy-payment/wages-owed-details/
      Then the page should have title "Wages owed"
       And the page should have an input field called "owed" labeled "Are you owed any wages?"
       And the page should have an input field called "wage_owed_from" labeled "From"
       And the page should have an input field called "wage_owed_to" labeled "To"
       And the page should have an input field called "number_of_days_owed" labeled "Number of days for which pay is owed"
       And the page should have an input field called "gross_amount_owed" labeled "Gross amount of pay owed"
       And the page should have an input field called "failed_payment_from" labeled "From"
       And the page should have an input field called "failed_payment_to" labeled "To"
       And the page should have an input field called "net_amount" labeled "Net Amount of bounced cheque or failed payment"
       And the page should have subtitle "Failed Payment - If your employer attempted to pay your wages and that payment failed (e.g cheque bounced) please provide details below:"

    Scenario: submit valid information
        Given that I am entering the unpaid wage information
            | DETAILS             | VALUE      |
            | owed                | Y          |
            | wage_owed_from      | 01/04/2013 |
            | wage_owed_to        | 01/05/2013 |
            | number_of_days_owed |            |
            | gross_amount_owed   | 2000       |
            | failed_payment_from | 01/04/2013 |
            | failed_payment_to   | 07/04/2013 |
            | net_amount          | 1500       |
         When the claimant goes to /claim-redundancy-payment/wages-owed-details/
          And enters the unpaid wages details
         Then the claimant should be sent to /claim-redundancy-payment/summary/


    Scenario: mandatory fields check
        Given that I am entering the wage information
            | DETAILS             | VALUE      |
            | owed                | Y          |
            | wage_owed_from      |            |
            | wage_owed_to        |            |
            | number_of_days_owed |            |
            | gross_amount_owed   | 2000       |
            | failed_payment_from |            |
            | failed_payment_to   |            |
            | net_amount          |            |
         When the claimant goes to /claim-redundancy-payment/wages-owed-details/
          And enters the unpaid wages details
         Then the claimant should stay on /wages-owed-details/ with title "Wages owed"


