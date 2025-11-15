#!/bin/sh
set -euo pipefail
set -E

TODAY=$(date +"%d-%m-%Y")
echo "[$TODAY]: starting mongodb backup"

extractMongo() {
    # recupere les variables d'env du .env
    set -a
    . .env
    set +a

    mongosh "$ADM_MONGO_URI" --eval "const cars=db.cars.find().toArray(); const logs=db.logs.find().toArray(); print(JSON.stringify({cars, logs}, null, 2));" > "files/${TODAY}.json"
    echo "[$TODAY]: extraction successful"
}