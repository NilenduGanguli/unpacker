# Use the official MinIO image from the Docker Hub
FROM minio/minio

# Set environment variables for MinIO access and secret keys
ENV MINIO_ROOT_USER=minioadmin
ENV MINIO_ROOT_PASSWORD=minioadmin

# Expose the ports used by MinIO
EXPOSE 9000
EXPOSE 9001

# Set the entrypoint command to start the MinIO server
ENTRYPOINT ["minio", "server", "/data"]

# Use the default command for the MinIO image
CMD ["--console-address", ":9001"]
