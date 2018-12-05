# booksearch

![Daisy Says Hello](booksearch/static/images/daisy.png)

Search for Books Using the Google Book API


This application should allow you to:

* Type in a query and display a list of books matching that query.
* Each item in the list should include the book's author, title, and publishing company, as well as a picture of the book.
* From each list item, you should also be able to navigate to more information about the book, but this information does not necessarily need to appear on a page within your application. In other words, this could link out to an external site with more information about that particular book.



### Running App Locally

1. Check out the repository. `git pull git@github.com:LorenDavie/booksearch.git`

2. Change to the project directory: `cd booksearch`

3. In the root directory of the project, make a virtual env, using python 3. `virtualenv --python=python3 --no-site-packages env`

4. Source the environment: `source env/bin/activate`

5. Make a file called `local.sh` and make it executable. The contents of the file should look like this:

```
#!/usr/bin/env bash

export BOOKSEARCH_DEBUG=true
export BOOKSEARCH_LOCALSTATIC=true
export GOOGLE_API_KEY=<your-api-key>

./manage.py $1 $2 $3 $4 $5 $6 $7

```

Use this file for Django commands.  So, for example, to run the server use `./local.sh runserver`.
