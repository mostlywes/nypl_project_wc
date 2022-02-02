# a random-generating endpoint using the API of a digital collection

# Description

Random is how you retrieve a random capture based on a provided resource type from the 500 most recently listed captures.

# Endpoint

GET random/?type_of_resource={type_of_resource_value}

type_of_resource parameters are strings and possible values are: still image, text, cartographic, moving image, notated music, sound recording, three dimensional object, sound recording-musical, sound recording-nonmusical

Only one parameter may be provided.

# Example

'../random/?type_of_resource=still+image' will return a random capture from the 500 most recently added that is categorized as a still image.

# Response

A malformed request will return a 400 with an error message. A successful request will return a response in JSON form that follows the format:

{uuid: uuid, type_of_resource: type_of_resource, item_link: url}

An example of a possible concrete response is:

{"uuid": "510d47dc-caf8-a3d9-e040-e00a18064a99", "type_of_resource": "still image", "item_link": "http://digitalcollections.nypl.org/items/510d47dc-caf8-a3d9-e040-e00a18064a99"}

The uuid is useful for other endpoints of the NYPL Digital API, and the item link will take you directly to view the capture.

# Usage

Both the request and the response have a provided frontend that can be found at https://nypl-project-wc.herokuapp.com/

The request and response can be initiated and received via command line clients as well. For example, a curl request for a text resource type capture would look like:

curl nypl-project-wc.herokuapp.com/random/?type_of_resource=text

Normally API credentials would need to be provided via headers, but these are already configured and hidden as part of a Heroku app.
