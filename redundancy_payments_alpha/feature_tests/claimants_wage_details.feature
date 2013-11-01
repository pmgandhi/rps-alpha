Feature: claimants wage details

    Scenario: capturing claimants wage details so that ..
        Given the app is running
         When we visit /claim-redundancy-payment/wage-details/
         Then the page should have title "Claimant Wage Details"
           And the page should have an input field called "FrequencyOfPayment" labeled "How often do you get paid?"
           And the page should have an input field called "GrossRateOfPay" labeled "Gross rate of pay (before Tax and NI)"
                And the page should have an input field called "every" labeled "every"
                And the page should have an input field called "NumberHoursWorked" labeled "Number of hours you normally work"
                And the page should have an input field called "BonusOrCommission" labeled "Did your pay include any bonus or commission ?"
                And the page should have an input field called "Overtime" labeled "Did you work overtime as a part of your contract ?"
                And the page should have an input field called "NormalDaysofWork" labeled "How many days you normally work each week"
