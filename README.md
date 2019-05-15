# tmdb_api_scraper
This script scrapes data by requesting and parsing files from themoviedb.org using a personal api key obtained after 
submitting a request to tmdb for one, which was then approved. 

# sys

This scraper uses the sys module to pass an additional argument through my command line rather than in the code.
I achieved a personal api key after requesting one from tmdb and copied that api into my command line as a second
argument when running the python request file. For this code to work for other users, you will need to obtain a 
api key from tmdb and copy that into the command line after the script name. For example, if a user were to obtain
a personal api key "12345678" then in the command line they would enter "python tmdb_request.py 12345678" to run the
script and properly request the desired files.
