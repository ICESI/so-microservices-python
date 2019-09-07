### How to execute

Development
```
00_path_params> ./scripts/deploy.sh
```

Production
```
export PRODUCTION=true
00_path_params> ./scripts/deploy.sh
```

Testing
```
tox -e pytest
```