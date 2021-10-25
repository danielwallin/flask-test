## Dockerized flask todo api
```bash
# run in Docker
make dev

# enter flask container
make sh-backend

# enter db container
make sh-db

# enter psql container cli
make psql

# curl
# GET todos
curl http://localhost:8070/todos

# POST
curl -X POST http://localhost:8070/todos -H 'Content-Type: application/json' -d '{ "title": "Full Stack Test Project", "completed": false }'

```

## Stack 🥞
* Flask
* Postgres
* Docker
* Python