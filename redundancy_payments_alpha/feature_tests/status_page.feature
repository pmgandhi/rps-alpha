Feature: app status page

    Scenario: check that the app is running
        Given the app is running
         When we visit the /_status page
         Then the page should include "everything is ok"

