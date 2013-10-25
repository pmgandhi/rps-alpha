@use_http_client
Feature: end-to-end platform test

    Scenario: can request claim start page
         when I go to "/claim"
         then I should get back a status of "200"

    Scenario: frontpage redirects to claim page
         when I go to "/"
         then I should get back a status of "302"

