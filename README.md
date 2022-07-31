# GOOD TO KNOW

- Docker compose secrets can be in .env and referenced with ${VARIABLE_NAME}
- Alembic is used for DB migrations (when we want to change columns in DB)
    - Alembic driver is defined in alembic/env.py
    - Make migration: `docker compose run web alembic revision --autogenerate -m "{migration message}"`
    - Run migration: `docker compose run web alembic upgrade head`
- Python-dotenv can be used to get env variables from .env file
    - real env variables override .env file!
- How to figure out DB url: `DATABASE_URL = postgresql+psycopg2://{user}:{password}@{host}:{port}`
    - host will be name of the container and not localhost!

## Backup/restore docker compose Postgres DB

Backup:
```docker exec -t your-db-container pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql```

Restore:
```cat your_dump.sql | docker exec -i your-db-container psql -U postgres```