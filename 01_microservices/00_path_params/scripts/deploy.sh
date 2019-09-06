#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`

LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8
VERBOSE=--verbose
API_PATH=gm_analytics/swagger/indexer.yaml
PORT=5000
ORIGIN=0.0.0.0

if [[ -z $PRODUCTION ]]
then
  export FLASK_ENV=development
  DEBUG=--debug
fi

connexion run $API_PATH -p $PORT -H $ORIGIN $VERBOSE $DEBUG 
