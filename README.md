# booksearch

![Daisy Says Hello](booksearch/static/images/daisy.png)

Search for Books Using the Google Book API

(Starring my basset hound, Daisy.)

This application should allow you to:

* Type in a query and display a list of books matching that query.
* Each item in the list should include the book's author, title, and publishing company, as well as a picture of the book.
* From each list item, you should also be able to navigate to more information about the book, but this information does not necessarily need to appear on a page within your application. In other words, this could link out to an external site with more information about that particular book.



### Running App Locally

1. Check out the repository. `git pull git@github.com:LorenDavie/booksearch.git`

2. Change to the project directory: `cd booksearch`

3. In the root directory of the project, make a virtual env, using python 3. `virtualenv --python=python3 --no-site-packages env`

4. Source the environment: `source env/bin/activate`

5. Install requirements: `pip install -r requirements.txt`

6. Make a file called `local.sh` and make it executable. The contents of the file should look like this:

```
#!/usr/bin/env bash

export BOOKSEARCH_DEBUG=true
export BOOKSEARCH_LOCALSTATIC=true
export GOOGLE_API_KEY=<your-api-key>

./manage.py $1 $2 $3 $4 $5 $6 $7

```

Use this file for Django commands.  So, for example, to run the server use `./local.sh runserver`.

## Design Approach

This is a pretty simple problem, so I tried to keep the solution simple as well. No class-based views, no custom taglibs, no multiple layers of abstraction.  Just some simple views, a form, and one extra business module to encapsulate client access to the Google Books API.

Also no tests, because there just isn't much to test.  I suppose I could write a test for connectivity to the Google API, but since every single use of the application will make a connection failure totally obvious, I chose not to do so.

The UI uses bootstrap to make it look acceptable. One small trick is that the **More Info** button is rendered in a different place on extra-small viewports (phones), because otherwise the float-right position of the normal button smashes into the text. This is accomplished with Bootstrap classes.

### Research and Tools

* [Example of Google Books API Usage in Python](https://developers.google.com/api-client-library/python/samples/simple_api_cmd_line_books.py)
* When hosting on Heroku I like to use [Django Storages](https://django-storages.readthedocs.io/en/latest/) and just push the static files to S3.
* Python code is formatted with [Black](https://black.readthedocs.io/en/stable/) because I'm tired of talking about code formatting. Everyone should just use code formatters now.

### Future Enhancements

Looks like the Google API returns 10 results by default.  Some sort of pagination to get to deeper results might be nice.  Also if I could find a way to automatically set up an Amazon affiliate link that would also be good.

### Easter Egg

Type a space into the search bar and hit enter.