# CSCI5622-Final-Project
A machine learning model to predict the subreddit of users' comments.

**Team Members:** Cole Sturza, Alex Book, Will Mardick-Kanter 

## Resources

- [PSAW: Python Pushshift.io API Wrapper (for comment/submission search)](https://psaw.readthedocs.io/en/latest/)

## Running the Webscraper
The webscraper is run within a Docker container on a vagrant VM. You will need to isntall Vagrant, plus VirtualBox. The following commands will get it up and running. It is also possible to run the docker compose command without the Vagrant VM.

``$ vagrant up``

``$ vagrant ssh default``

``$ docker-compose up``
