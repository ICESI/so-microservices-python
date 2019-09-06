# integration
export PYTHONPATH=$PYTHONPATH:`pwd`
export FLASK_ENV=development
connexion run gm_analytics/swagger/indexer.yaml --debug -p 8088 -H 127.0.0.1

# production
export PYTHONPATH=$PYTHONPATH:`pwd`
connexion run gm_analytics/swagger/indexer.yaml --verbose -p 8088 -H 127.0.0.1
