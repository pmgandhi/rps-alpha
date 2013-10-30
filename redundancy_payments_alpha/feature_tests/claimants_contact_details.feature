Feature: claimants contact details

    Scenario: capturing claimants contact details so that they can be contacted by RPS
        Given the app is running
         When we visit the /claimant-contact-details page
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
