Feature: employment details

#    Scenario: capturing employment details so that RPS can verify these details
#        Given the app is running
#         When we visit /claim-redundancy-payment/employment-details/
#         Then the page should have title "Employment Details"
#          And the page should have an input field called "job_title" labeled "Job Title"
#          And the page should have an input field called "category_of_worker" labeled "Category of Worker"
#          And the page should have an input field called "start_date" labeled "When did you start working for this employer?"
#          And the page should have an input field called "end_date" labeled "When did your employment end?"

    Scenario: filling in the contact details form
        Given a claimant with the employment details
            | DETAILS            | VALUE                 |
            | job_title          | Guardian of the North |
            | category_of_worker | Employed              |
            | start_date         | 01/04/1999            |
            | end_date           | 01/10/2013            |
          When the claimant goes to /claim-redundancy-payment/employment-details/
          And enters the employment details
         Then the claimant should be sent to /claim-redundancy-payment/done/

    Scenario: filling in the contact details form with a missing information
        Given a claimant with the employment details
            | DETAILS            | VALUE                 |
            | job_title          | Guardian of the North |
            | category_of_worker | Employed              |
         When the claimant goes to /claim-redundancy-payment/personal-details/
          And enters the employment details
         Then the claimant should stay on /employment-details/ with title "Employment Details"
