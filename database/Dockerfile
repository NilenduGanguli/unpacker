# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Environment variables to configure PostgreSQL
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Copy initialization scripts
COPY database/init-user-db.sh /docker-entrypoint-initdb.d/
COPY database/init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432
