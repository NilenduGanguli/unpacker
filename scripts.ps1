# minios3
docker build -t minio-server-v1 -f ./minios3/Dockerfile .

docker run -d --name minio -p 9000:9000 -p 9001:9001 -v C:\Users\nilen\OneDrive\Desktop\unpacker\data\volumes\minios3:/data minio-server-v1

#database
docker build -t postgres-db-v1 -f ./database/Dockerfile .

docker run --name db -d -p 5432:5432 -v C:\Users\nilen\OneDrive\Desktop\unpacker\data\volumes\database:/var/lib/postgresql/data postgres-db-v1


