Feature: claimants wage details

    Scenario: capturing claimants wage details so that ..
        Given the app is running
         When we visit /claim-redundancy-payment/wage-details/
         Then the page should have title "Claimant Wage Details"
           And the page should have an input field called "frequency_of_payment" labeled "How often do you get paid?"
           And the page should have an input field called "gross_rate_of_pay" labeled "Gross rate of pay (before Tax and NI)"
           And the page should have an input field called "every" labeled "every"
           And the page should have an input field called "number_of_hours_worked" labeled "Number of hours you normally work"
           And the page should have an input field called "bonus_or_commission" labeled "Did your pay include any bonus or commission ?"
           And the page should have an input field called "overtime" labeled "Did you work overtime as a part of your contract ?"
           And the page should have an input field called "normal_days_of_work" labeled "How many days you normally work each week"


    Scenario: Submit valid information
        Given that I am entering the wage information
        When I provide the following details and submit

        Given a claimant with the employment details
            | DETAILS               | VALUE        |
            | frequency_of_payment  | Month        |
            | gross_rate_of_pay     | 18000.00     |
            | every                 | Year         |
            | number_hours_worked   | 40           |
            | bonus_or_commission   | N            |
            | overtime              | N            |
            | normal_days_of_work   | 5            |


         When the claimant goes to /claim-redundancy-payment/wage-details/
         And enters the employment details
         Then the message "We will use your weekly wage of £345.21 to process your claims subject to confirmation from your HR records " should be displayed.
         Then the claimant should be sent to /claim-redundancy-payment/done/

