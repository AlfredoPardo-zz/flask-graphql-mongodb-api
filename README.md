# Flask-Based GraphQL API using MongoDB for Persistence

## Getting Started

1. Build and Run the Docker Compose file

    > **your_host$** docker-compose build
    > **your_host$** docker-compose up

2. Jump to the API docker container
    > **your_host$** docker exec -it fgm_api ash

3. Run the script to load some data on the fgm_db_dev Database
    > **api#** python load_some_data.py

4. You can test the queries listed in the ***queries*** folder on http://127.0.0.1:5000/graphql

