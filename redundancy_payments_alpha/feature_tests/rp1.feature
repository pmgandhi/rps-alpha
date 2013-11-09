@jims
Feature: rp1 form

    Scenario: adding rp1 form details to data store
        When we add a dictionary containing sample rp1 details
        Then the data store should contain a claimant
        And the validator service should find a queued submission