# AgrippaBot

## About
>Twitter bot for Agrippa's Three Books of Occult Philosophy, translated by John French. This project was inspired by another similiar project by [Nneji123](https://github.com/Nneji123/RapLyricsBot/actions/workflows/test.yml), to whom I am grateful.

## Contents
  * About
  * Contents
  * Features
  * Repository file structure
  * Pre-requisites
  * How to run the Application
  * Tests
  * Deployment


## Features
The bot tweets a random line from previously sanitized text file containing all three volumes from John French's translation of Agrippa's Occult Philosophy. The text file can be found [here.](https://github.com/lombrosidade/agrippabot/data/agrippa.txt) The code is located in the [src](https://github.com/lombrosidade/agrippabot/src) folder.



## Repository File Structure
```bash
├───.github # Github Workflows
│   └───workflows
├── data
│   └── agrippa.txt # book file
├── docker-compose.yml # for containerization with docker
├── Dockerfile
├── LICENSE 
├── README.md
├── requirements.txt
├── src
│   ├── bot.py # bot file
|   ├── utils.py # Helper functions
│   ├── __init__.py
│   ├── server.py # flask server
├── tests # Tests folder
    ├── __init__.py
    └── conftest.py # pytest fixtures
    └── test_utils.py # Test for the helper functions and environment files
```

## Pre-requisites
In order to use the bot, you'll need to:
 
 1. Create a new Twitter account to act as the bot.
 2. Register for a [twitter developer account.](https://developer.twitter.com/en)  
 3. Create a [twitter app](https://developer.twitter.com/en/portal/projects-and-apps). Make sure to give it **Read and Write** permissions.
 4. Host it locally by running a Flask server or upload the Docker image to an environment of your choice.


## How to run the application
<details>
    <summary><b>How to run the application locally.<b></summary>

1. Clone this repository on your local machine
2. Create a virtual environment in your project's root directory: `python3 -m venv environment && source environment/bin/activate`
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `.env` in the root directory of your project. Put your twitter App keys there. You can also change the path to the text file. 
Once everything is tested, ready to deploy, you'll move these to environment variables. Make sure to add ".env" to the .gitignore!
```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<YOUR_ACCESS_TOKEN_SECRET_HERE>
CONSUMER_KEY=<YOUR_CONSUMER_KEY_HERE>
CONSUMER_SECRET=<YOUR_CONSUMER_SECRET_HERE>
TEXT_PATH=data/agrippa.txt
```
1. You can play around with the bot in `src/bot.py`
2. Test your changes locally by running `python src/bot.py` from the root directory of your project

</details>


<details> 
  <summary><b>Running on local machine with Docker Compose</b></summary>

**You can also run the application in a docker container using docker compose(if you have it installed)**

1. Clone the repository:
```bash
git clone https://github.com/lombrosidade/agrippa/
```

2. Change to the directory:
```
cd agrippa
```

3. Edit the `.envexample` file and store your keys there.

4. Run the docker compose command
```docker
docker compose up -d --build 
```
The text should be tweeted then.
</details>

# License
[MIT](https://github.com/lombrosidade/agrippa/LICENSE.md)

