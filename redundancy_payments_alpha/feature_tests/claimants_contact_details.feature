Feature: claimants contact details

    Scenario: capturing claimants contact details so that they can be contacted by RPS
        Given the app is running
         When we visit /claim-redundancy-payment/personal-details/
         Then the page should have title "Claimant Contact Details"
          And the page should have an input field called "forenames" labeled "Forename(s)"
          And the page should have an input field called "surname" labeled "Surname"
          And the page should have an input field called "title" labeled "Title"
          And the page should have an input field called "other" labeled "Other"
          And the page should have an input field called "building_number" labeled "Building Number"
          And the page should have an input field called "street" labeled "Street"
          And the page should have an input field called "district" labeled "District"
          And the page should have an input field called "town_or_city" labeled "Town or City"
          And the page should have an input field called "county" labeled "County"
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
            | building_number   | 1                 |
            | street            | street name       |
            | district          | some district     |
            | town_or_city      | Duckburg          |
            | county            | foobar            |
            | postcode          | a1 4lp            |
            | email             | duck@burg.com     |
            | telephone_number  | 00000 123456      |
            | nino              | AA112233B         |
            | date_of_birth     | 01/01/1900        |
         When the claimant goes to /claim-redundancy-payment/personal-details/
          And enters their details
         Then the claimant should be sent to /claim-redundancy-payment/employment-details/

    Scenario: filling in the contact details form with a missing information
        Given a claimant with the personal details
            | DETAILS           | VALUE             |
            | title             | Mr                |
            | surname           | Duck              |
            | building_number   | 1                 |
            | street            | street name       |
         When the claimant goes to /claim-redundancy-payment/personal-details/
          And enters their details
         Then the claimant should stay on /claimant-contact-details/
