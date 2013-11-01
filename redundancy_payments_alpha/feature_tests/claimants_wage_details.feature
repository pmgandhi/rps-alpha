Feature: claimants wage details

    Scenario: capturing claimants wage details so that ..
        Given the app is running
         When we visit /claim-redundancy-payment/wage-details/
         Then the page should have title "Claimant Wage Details"
           And the page should have an input field called "FrequencyOfPayment" labeled "How often do you get paid?"
           And the page should have an input field called "GrossRateOfPay" labeled "Gross rate of pay (before Tax and NI)"