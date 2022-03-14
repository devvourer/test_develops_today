# Test assessment by DevelopsToday
## **Functional Requirements**

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
- There should be an endpoint to upvote the post
- We should have a recurring job running once a day to reset post upvotes count

## **Technical Requirements**

- Code should be written with Python 3
- REST API should be Django and Django REST Framework based
- API should be well documented with Postman collection. Make sure to use [Postman environments and variables](https://learning.postman.com/docs/postman/variables-and-environments/variables/#understanding-variables-and-environments), so you can switch between local API and deployed version. Add Postman collection link to the README
- API has to run as a Docker container. API + Postgres should be launched with docker-compose
- Code should be formatted with [Black](https://github.com/psf/black)
- Necessary to make sure that Flake8 linter passes. Would be great to have typing with [pyright](https://github.com/microsoft/pyright) as well
- The project should have clear README with steps to run it
- The code should be clean, passing linter checks and simple to understand. Code quality matters a lot
- Deploy API for testing to [Heroku](https://www.heroku.com/) or similar service. Add deployment link to the README

## 🐳 Requirements

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Deployment


 - First what we should to do its: 
```
git clone https://github.com/devvourer/test_develops_today.git
```
- Inside the project, we should create `.env` file, and write this config
```commandline
COMPOSE_PROFILES=nginx,celery
```

- Docker, in terminal we need to write this commands 
```
docker-compose build
docker-compose up
```

## Postman API Documentation

 - [Postman api documentation](https://www.postman.com/netex-kassa/workspace/test-developstoday/documentation/14689555-120ed368-739d-49b7-9b49-a7dfc3efff6e)

## Link to deployed project
 - [link](http://140.82.32.239:8000/api/article/)
