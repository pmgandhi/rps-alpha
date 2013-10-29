Feature: claimants contact details

    @wip
    Scenario: capturing claimants contact details so that they can be contacted by RPS
        Given the app is running
         When we visit the /claimant-contact-details page
         Then the page should include "test string"
