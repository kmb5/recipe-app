## Backup/restore docker compose Postgres DB

Backup:
```docker exec -t your-db-container pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql```

Restore:
```cat your_dump.sql | docker exec -i your-db-container psql -U postgres```