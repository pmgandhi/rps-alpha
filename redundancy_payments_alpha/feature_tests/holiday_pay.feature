Feature: claimants holiday pay

    Scenario: capturing claimants holiday pay details so that their claim can be processed by RPS
     Given the app is running
      When we visit /claim-redundancy-payment/holiday-pay/
       Then the page should have title "Holiday pay"
        And the page should have an input field called "holiday_owed" labeled "Are you owed any holiday pay?"
        And the page should have an input field called "holiday_start_date" labeled "What was the start date of your holiday year?"
        And the page should have an input field called "number_of_holiday_days_entitled" labeled "How many days holiday per year (including bank holidays) were you entitled to?"
        And the page should have an input field called "days_carried_over" labeled "If you were allowed to carry forward untaken holiday entitlement from your previous holiday year, how many days did you carry forward this year?"
        And the page should have an input field called "days_taken" labeled "How many days have you taken this year (including bank holidays)?"
        And the page should have an input field called "days_owed" labeled "How many days are you still owed (including bank holidays) up to your termination date?"
        And the page should have an input field called "holiday_taken_from" labeled "From"
        And the page should have an input field called "holiday_taken_to" labeled "To"
        And the page should have an input field called "number_of_days_pay_owed" labeled "Number of days for which pay is owed"