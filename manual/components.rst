Components
==========

ClaimForm
----------
Is a claim form.

Chomp
-----
1. Create a fake DMS ID.
 a. The DMS ID is a string. Can the first character be alpha, so that it doesn't conflict with wisdom.
2. Web Dav URL
3. Pass a fake link in the call to AcceptDoc. e.g. link to existing RPS guidance document? A blank page?
fake dms id - what numbers? it's a string. start with a string?

4. Call web services in the following order, and make sure that the same DMS_ID is passed to both.:
 a. AcceptDoc
 b. RP1
5. The Claim ID should be returned in the RP1 response.  Pass this back to the claimant, amd/or store it somewhere.



