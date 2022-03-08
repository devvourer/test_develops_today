# Test assessment by DevelopsToday


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