Feature: claimants contact details

    Scenario: capturing claimants contact details so that they can be contacted by RPS
        Given the app is running
         When we visit /claim-redundancy-payment/personal-details/
         Then the page should have title "Claimant Contact Details"
          And the page should have an input field called "forenames" labeled "First name(s)"
          And the page should have an input field called "surname" labeled "Last name"
          And the page should have an input field called "title" labeled "Title"
          And the page should have an input field called "other" labeled "Other"
          And the page should have an input field called "address_line_1" labeled "Line 1"
          And the page should have an input field called "address_line_2" labeled "Line 2"
          And the page should have an input field called "address_line_3" labeled "Line 3"
          And the page should have an input field called "town_or_city" labeled "Town or City"
          And the page should have an input field called "postcode" labeled "Post Code"
          And the page should have an input field called "email" labeled "Email Address"
          And the page should have an input field called "telephone_number" labeled "Telephone Number"
          And the page should have an input field called "nino" labeled "National Insurance Number"
          And the page should have an input field called "date_of_birth" labeled "Date Of Birth"

    Scenario: filling in the contact details form
        Given a claimant with the personal details
            | DETAILS           | VALUE             |
            | forenames         | Donald            |
            | surname           | Duck              |
            | title             | Mr                |
            | address_line_1    | Line 1            |
            | address_line_2    | Line 2            |
            | address_line_3    | Line 3            |
            | town_or_city      | Duckburg          |
            | postcode          | a1 4lp            |
            | email             | duck@burg.com     |
            | telephone_number  | 00000 123456      |
            | nino              | AA112233B         |
            | date_of_birth     | 01/01/1900        |
         When the claimant goes to /claim-redundancy-payment/personal-details/
          And enters their details
         Then the claimant should be redirected

    Scenario: filling in the contact details form with a missing information
        Given a claimant with the personal details
            | DETAILS           | VALUE             |
            | title             | Mr                |
            | surname           | Duck              |
            | building_number   | 1                 |
            | street            | street name       |
         When the claimant goes to /claim-redundancy-payment/personal-details/
          And enters their details
         Then the claimant should stay on /claimant-contact-details/ with title "Claimant Contact Details"
