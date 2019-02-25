To get this proof of concept up and running, install docker-compose (https://docs.docker.com/compose/install/) and from the root directory of the project run:
```
docker-compose up
```

Alternately, start arangodb on your computer (with root password `openSesame`), install pipenv globally (`pip install pipenv`) and from the root directory of the project run:
```
MULTINET_ROOT_PASSWORD=openSesame ARANGO_HOST=localhost ARANGO_PORT=8529 pipenv run python multinet-server/main.py
```

The following commands will help you walk through this example code.

Create the "skyways" database:

```
curl -X POST http://localhost:8080/db/skyways
```

Verify it exists on the system:
```
curl -X GET http://localhost:8080/
```

Create the "skyways" graph in the "skyways" database:
```
curl -X POST http://localhost:8080/graph/skyways/skyways
```

Verify it exists in the database:
```
curl -X GET http://localhost:8080/graph/skyways/skyways
```

Create the vertices by uploading the airports.csv file in the data directory. Replace the file path with the appropriate one for your system.
```
curl -X POST \
  http://localhost:8080/vertices/skyways/skyways/airports \
  -H 'content-type: multipart/form-data' \
  -F file=@/home/mildewey/multinet-server/data/airports.csv
```

Look at the first five vertices. For this proof of concept I cut it off automatically at 5 to avoid having to worry about paging. Note that the command to get the graph will also return more information now.
```
curl -X GET http://localhost:8080/vertices/skyways/skywayts/airports
```

Create the edges by uploading the flights.csv file in the data directory. Replace the file path with the appropriate one for your system. This command takes several minutes.

```
curl -X POST \
http://localhost:8080/edges/skyways/skyways/flights \
-H 'content-type: multipart/form-data' \
  -F from_collections=airports \
  -F to_collections=airports \
  -F file=@/home/mildewey/multinet-server/data/flights.csv
```

Look at the first five edges. For this proof of concept I cut it off automatically at 5 to avoid having to worry about paging. Note that the command to get the graph will also return more information now.
```
curl -X GET http://localhost:8080/edges/skyways/skyways/flights
```
