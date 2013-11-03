Feature: claimants contact details

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

    Scenario: filling in the contact details form with invalid information
        Given a claimant with the personal details
            | DETAILS           | VALUE             |
            | title             | Mr                |
            | surname           | Duck              |
            | building_number   | 1                 |
            | street            | street name       |
            | nino              | wibble            |
         When the claimant goes to /claim-redundancy-payment/personal-details/
          And enters their details
         Then the claimant should stay on /claimant-contact-details/ with title "Claimant Contact Details"
