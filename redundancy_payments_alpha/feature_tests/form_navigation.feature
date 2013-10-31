Feature: form navigation

    Scenario: navigation between form pages and storing information
        Given the form pages
            | PAGE                                          |
            | /claim-redundancy-payment/personal-details    |
            | /claim-redundancy-payment/employment-details  |
            | /claim-redundancy-payment/done                |
         When we visit each form page
         Then we should see a navigation bar with these links
            | LINK                                          |
            | /claim-redundancy-payment/start               |
            | /claim-redundancy-payment/personal-details    |
            | /claim-redundancy-payment/employment-details  |

