#network
docker network create -d bridge dev-net

# minios3
docker build -t minio-server-v1 -f ./minios3/Dockerfile .

docker run -d --name minio -p 9000:9000 -p 9001:9001 -v C:\Users\nilen\OneDrive\Desktop\unpacker\data\volumes\minios3:/data --network dev-net minio-server-v1

#database
docker build -t postgres-db-v1 -f ./database/Dockerfile .

docker run --name db -d -p 5432:5432 -v C:\Users\nilen\OneDrive\Desktop\unpacker\data\volumes\database:/var/lib/postgresql/data --network dev-net postgres-db-v1


#database
docker build -t dbops-v1 -f ./dbops/Dockerfile .

docker run --name dbops -d -p 8001:8001  --network dev-net dbops-v1

