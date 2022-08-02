# Project 2 / Final Module

Name:
UCID:

[![Production Workflow]() <-Put your own badge code here.

[Production Deployment]()

# Working with data records and Final Project 2

In this unit, you are required to complete the requirements specified below.  

## Unit Video

* [Unit Video - Here](https://youtu.be/Lyp917shPQQ)
## Test Data
* [Songs Data File](tests/test_data/my_music.csv)
## Project Requirements

**For your project, you need to implement the following four requirements and each one is worth 5 Points:**

1. Fix all the pylint errors (make sure the comments are accurate for the doc strings for tests and files) and add a
   context message to each assertion as described - [here](https://dmerej.info/blog/post/python-tests-tips/)
2. You need to add a new field to the song model for genre and update all the tests and application code to test that
   genre is added
3. You need to update the user dashboard to show a total count of songs and write a test to confirm this is visible
4. You need to update the user dashboard to show a list of genre and a count of songs in each genre and write a test for
   this that uses the test song data csv

Genre Tests go [Here](tests/genre_test.py)
Dashboard Tests go [Here](tests/dashboard_test.py)

**For your project you need to implement the following feature using a NEW flask blueprint for 5 Points each:**

1. A link in your main menu for a contact form with a test
2. A contact form page with a title, email, and message field with tests to verify each field
3. A contact route to display the page and process the post request with tests
4. A database model for the contact record with the fields id, title, email, and message. You need to write tests for
   adding and removing contact messages from the database.
5. A new page that displays a table like songs that is only visible to authenticated admin users that displays a list of
   contact records.
6. A thank-you page for a user submitting a contact request that displays a thank you and flashes a message that the
   requests was successfully submitted

Contact Tests go [Here](tests/contact_test.py)

**For these requirements you will need to select two and research, implement, and test the feature. Each one is worth 25
Points**

1. Create a public page to browse songs by genre
2. Fix the validation on the reg form class to properly display validation information for user account
   registration.
3. Add a function to send a confirmation email to the user that submits the contact request and sends an email to the
   site admin. You test this functionality with the service mailtrap and I've already setup how to make email work in
   this [project](https://github.com/kaw393939/flask_auth/tree/flask_email). You can't put
   the [mailtrap](https://mailtrap.io) api key in github and need to add it as a repository setting secret for tests to
   pass. You cannot expose API key to the web or it will be banned quickly.
4. Add the functionality with tests to edit songs based on how I handle managing user accounts. Look
   on [line 186](app/auth/__init__.py) for the function that sets up the routes to pass into the form.
5. Change out the current home page and add your own homepage design using Bootstrap to create a Z layout with
   a [carosel.](https://getbootstrap.com/docs/5.1/components/carousel/)
6. Fix the problem with duplicated songs by doing a query to see if the song is there before adding it.

Feature 1 Tests go [Here](tests/feature1_test.py)
Feature 2 Tests go [Here](tests/feature2_test.py)


#### Project Rubric

1. 10 x 5 Point Requirements = 50
2. 2 x 25 Point Requirements = 50

**Total: Points 100**

### Submission Instructions

1. Set up the application as you did before, you can copy your prod.yml file from the previous assignment. You will need
   to add the heroku API key, docker username, docker password secrets to this repository
2. Add your name to the top of the readme, add the link to your deployed app, and add the badge code as you did before.

### Docker Commands

1. docker ps <- lists running containers
2. docker kill <container id>  kills the container, you get the container ID from docker PS
    * Example: docker kill cf373e38ae66
3. docker compose up --build <- builds the app locally
4. docker exec -it <containerID> /bin/bash    <- Logs into the running container
    * Example: docker exec -it cf373e38ae66 /bin/bash

Note:  You really want to login to the container to run pytest but you can also run it locally as long as you create the
virtual environment and do the pip install requirements

# Project Setup

## Setting up CI/CD

The result of this will be that when you create a pull request to merge a branch to master, it will deploy to your
heroku development app/dyno and when you merge or push to master on github, it will deploy the app to the production
heroku app/dyno.

### Instructions

1. Create an account with Heroku, create an app for production and an app for development
2. Create a new repo in Docker hub

#### Setup Docker and Heroku Credentials In the Repository Settings under Action -> Secret

3. In your newly created Github repository, add new repository secrets for DOCKER_USERNAME, DOCKER_PASSWORD,
   HEROKU_API_KEY (Values are DOCKER_USERNAME: your docker hub username; DOCKER_PASSWORD: your docker hub password;
   HEROKU_API_KEY: API key from the heroku app)

### GitHub Notes:  Set the action secrets repository in: -> settings -> actions -> secrets

### Heroku Notes: Get the heroku API key from account in: -> applications -> create authorization button

#### Change GitHub Actions Workflows for Prod

4. Change line 42 to have your docker repo address in: .github/workflows/prod.yml
5. change lines 58 to have your heroku app name in: .github/workflows/prod.yml
6. change line 59 to have your heroku email in: .github/workflows/prod.yml
7. Push code to your local repo and check for any errors and fix any errors that appear when the workflow is running.
   You can check the workflow in the
   actions.

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest

### Future Notes and Resources

* https://flask-user.readthedocs.io/en/latest/basic_app.html
* https://hackersandslackers.com/flask-application-factory/
* https://suryasankar.medium.com/a-basic-app-factory-pattern-for-production-ready-websites-using-flask-and-sqlalchemy-dbb891cdf69f
* https://develie.hashnode.dev/exploring-flask-sqlalchemy-queries
* https://wtforms.readthedocs.io/en/3.0.x/
* https://bootstrap-flask.readthedocs.io/en/stable/
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/
