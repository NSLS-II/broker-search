# Data Broker Search App

This is a proof-of-concept of the idea that metadatastore will empower
scientists to "Google their data." In this demo implementation, the results
come back as a truncated list of uids, each with a convenience "Copy to
clipboard" button. The HTML of each result is pluggable and can be
customized on a result-by-result basis.

The search requires the MongoDB to have a [wildcard text
index](https://docs.mongodb.org/manual/tutorial/create-text-index-on-multiple-fields/#index-all-fields). In early tests, it is fast enough to update the result list after each keystroke.

TODO:

* Add a calendar widget to restrict searches by date.
* Add an example that includes a plot in the results set. The plot should be
  drawn in asynchronously; it should not delay the apppearance of the text and
  other HTML content.
