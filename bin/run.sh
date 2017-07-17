#!/bin/sh

ENV=default
if [ -z ${1+x} ]; then
	echo "ENV is set to default";
else
	ENV=$1
	echo "var is set to '$1'";
fi

#SERVICE_HOME=
export PYTHONPATH=${PYTHONPATH}:${SERVICE_HOME}/app

CONF_PATH=${SERVICE_HOME}/etc/${ENV}.cfg

cd ${SERVICE_HOME}
python ${SERVICE_HOME}/sbin/app.py ${CONF_PATH}
