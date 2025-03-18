#! /bin/bash

docker compose up --build --detach
docker compose exec -T backend python -m pytest
