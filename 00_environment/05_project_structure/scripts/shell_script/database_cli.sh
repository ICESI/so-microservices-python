#!/usr/bin/env bash

cat scripts/shell_script/schema_drop.sql | mysql -u root -poperativos
cat scripts/shell_script/schema_create.sql | mysql -u root -poperativos
echo "database created on `date`"
