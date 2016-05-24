# brewpub_project
This is the home for my brewpub project for the ChiPy Mentorship Program

## Documentation for brewpub API

###Register a user

#####POST: /user

#####BODY:
	{
		"username": "thirstyman33",
		"password": "Isureamthirsty99*",
		"email": "iamthirsty@email.com",
		"date_created": "2016-05-01T14:22:01.012000Z"
	}
	
#####NOTES:
	- username: the name the user selects (string)
	- password: password user selects
	- email: the user's email address (string)
	- date_created: date/time record
	
#####RESPONSE:
    {
      "id": "123232312329-AABC-9993",
      "username": "thirstyman33",
	    "password": "Isureamthirsty99*",
      "email": "iamthirsty@email.com",
	    "date_created": ""
    }

#####STATUS CODES:
	-201 if successfully created
	-400 if incorrect data provided
	-401 if permission denied
	-403 if user not authorized
	-409 if user already exists
	

###Update User Profile

#####PUT: /user

#####BODY:
	{
		"username": "thirstyman33",
		"password": "Isureamthirsty99*",
		"email": "iamthirsty@email.com"
	}
	
#####NOTES:
	- username: the name the user selects (string)
	- password: password user selects
	- email: the user's email address (string)
	
#####RESPONSE:
    {
      "id": "123232312329-AABC-9993",
      "username": "thirstyman33"
    }

#####STATUS CODES:
	-200 OK
	-400 if incorrect data provided (bad request)
	-401 if permission denied
	-404 if item not found

###Delete User Account

#####DELETE: /user/:id

#####RESPONSE: None

#####STATUS CODES:
	-204 if no content (deleted/success)
	-404 if item not found


###User Login

#####POST: /user/login

#####BODY:
	{
		"username": "thirstyman33",
		"password": "Isureamthirsty99*"
	}
	
#####NOTES:
	- username: the username user provides
	- password: the password user provides

#####RESPONSE:
    {
      "id": "123232312329-AABC-9993",
      "username": "thirstyman33",
      "password": "Iamthirsty99"
    }
  
#####STATUS CODES:
	-201 if successfully logged in
	-400 if incorrect data provided
	-401 if permission denied
	-403 if user not authorized
	-409 if user already logged in


###User Logout

#####PUT: /user/logout

#####BODY:
    {
	  	"username": "thirstyman33",
	  	"password": "Isureamthirsty99*"
    }

#####NOTES:
	- username: the username user provides
	- password: the password user provides

#####RESPONSE:
    {
      "id": "834892308484923048-1232",
      "username": "thirstyman33",
      "password": "Isureamthirsty99*"
	}

#####STATUS CODES:
	-200 OK
	-400 if incorrect data provided (bad request)
	-401 if permission denied
	-404 if item not found



##ADMIN

###Create a Brewpub 

#####POST: /brewpub

#####BODY:
    {
      "name": "House of Beer",
      "address" = "1200 N. State St., Chicago, IL, 60610",
      "telephone" = "3125551212",
      "website" = "www.beer.com",
      "hours" = ""
    }

#####NOTES:
    -name: the name of the brewpub
    -address: the address of the brewpub
    -telephone: the telephone number of the brewpub
    -website: the website address of the brewpub
    -hours: the days and hours the brewpub is open

#####RESPONSE:
    {
      "id": "89748392047389274-2u348938",
      "name": "House of Beer",
      "address" = "1200 N. State St., Chicago, IL, 60610",
      "telephone" = "3125551212",
      "website" = "www.beer.com",
      "hours" = ""
    }

#####STATUS CODES:
	-201 if successfully created
	-400 if incorrect data provided
	-401 if permission denied
	-403 if user not authorized
	-409 if brewpub already exists


###Update Brewpub Information

#####PUT/PATCH: /brewpub/:id

#####BODY:
    {
      "name": "House of Beer",
      "address" = "1200 N. State St., Chicago, IL, 60610",
      "telephone" = "3125551212",
      "website" = "www.beer.com",
      "hours" = ""
    }

#####NOTES:
    -name: the name of the brewpub
    -address: the address of the brewpub
    -telephone: the telephone number of the brewpub
    -website: the website address of the brewpub
    -hours: the days and hours the brewpub is open

#####RESPONSE:
    {
      "id": "0ffa96231",
      "name": "House of Beer",
      "address" = "1200 N. State St., Chicago, IL, 60610",
      "telephone" = "3125551212",
      "website" = "www.beer.com",
      "hours" = ""
    }

#####STATUS CODES:
	-200 OK
	-400 if incorrect data provided (bad request)
	-401 if permission denied
	-404 if item not found


###Delete Brewpub Information

#####DELETE: /brewpub/:id

#####RESPONSE: None

#####STATUS CODES:
	-204 if no content (deleted/success)
	-404 if item not found

###Get Brewpub Listing

#####GET: /brewpub

#####NOTES: 
    ?Should latitude/longitude be supplied as query params
    to narrow results by distance?

#####RESPONSE:
    "count": 10,
    "results": [
      {
        "id": "3428913728490729-3248",
        "name": "House of Beer",
        "address" = "1200 N. State St., Chicago, IL, 60610",
        "telephone" = "3125551212",
        "website" = "www.beer.com",
        "hours" = ""
      },
      ...
    ]

#####STATUS CODES:
    -200 OK/successful
    -400 if incorrect data provided (bad request)
    -401 if permission denied
    -403 if not authorized
    -404 if item not found


###Get Brewpub Detail Information

#####GET: /brewpub/:id 

#####RESPONSE:
    {
      "id": "7878974897-32748723",
      "name": "House of Beer",
      "address" = "1200 N. State St., Chicago, IL, 60610",
      "telephone" = "3125551212",
      "website" = "www.beer.com",
      "hours" = ""
    }

#####STATUS CODES:
    -200 OK/success
    -400 if incorrect data provided (bad request)
    -401 if permission denied
    -403 if not authorized
    -404 if item not found


###Create a Beer Item

#####POST: /beer

#####BODY:
    {
      "name": "Skunk Brew",
      "type": "Old Beer",
      "description": "This brew has the scent of Pepe Le Peu"
    }

#####NOTES:
    -name: the name of the beer
    -type: the type of the beer
    -description: the description listing for the beer

#####RESPONSE:
    {
      "id": "7813247364146-346274783268"
      "name": "Skunk Brew",
      "type": "Old Beer",
      "description": "This brew has the scent of Pepe Le Peu"
    }

#####STATUS CODES:
	  -201 if successfully created
	  -400 if incorrect data provided
	  -401 if permission denied
	  -403 if user not authorized
	  -409 if beer already exists


###Update Beer Item Information

#####PUT/PATCH: /beer/:id

#####BODY:
    {
      "name": "Skunk Brew",
      "type": "Old Beer",
      "description": "This brew has the scent of Pepe Le Peu"
    }

#####NOTES:
    -name: the name of the beer
    -type: the type of the beer
    -description: the description listing for the beer

#####RESPONSE:
    {
      "id": "7839742829374-BAAA-87897",
      "name": "Skunk Brew",
      "type": "Old Beer",
      "description": "This brew has the scent of Pepe Le Peu"
    }

#####STATUS CODES:
  	-200 OK/success
  	-400 if incorrect data provided (bad request)
	  -401 if permission denied
	  -404 if item not found

###Delete Beer Item

#####DELETE: /beer/:id

#####RESPONSE: None

#####STATUS CODES:
	  -204 if no content (deleted/success)
	  -404 if item not found


###Get Beer Listing

#####GET: /beer/

#####RESPONSE:
    "count": 10,
    "results": [
      {
        "id": "7813247364146-346274783268"
        "name": "Skunk Brew",
        "type": "Old Beer",
        "description": "This brew has the scent of Pepe Le Peu"
      },
      ...
    ]

#####STATUS CODES:
    -200 OK
    -400 if incorrect data provided (bad request)
    -401 if permission denied
    -403 if not authorized
    -404 if item not found


###Get Beer Detail Information

#####GET: /beer/:id

#####RESPONSE:
    {
      "id": "7813247364146-346274783268"
      "name": "Skunk Brew",
      "type": "Old Beer",
      "description": "This brew has the scent of Pepe Le Peu"
    }

#####STATUS CODES:
    -200 OK
    -400 if incorrect data provided (bad request)
    -401 if permission denied
    -403 if not authorized
    -404 if item not found


