#!/bin/sh

ENV=default
if [ -z ${1+x} ]; then 
	echo "ENV is set to default"; 
else 
	ENV=$1
	echo "var is set to '$1'"; 
fi

#SERVICE_HOME=
CONF_PATH=${SERVICE_HOME}/etc/${ENV}.cfg

cd ${SERVICE_HOME}
pwd

python ${SERVICE_HOME}/app/mongo_app.py ${CONF_PATH}