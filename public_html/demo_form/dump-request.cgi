#!/bin/sh

echo "Content-type: text/plain"
echo

echo "Stuff from the environment"
echo "--------------------------------"
echo

echo -n "PWD: "
pwd
echo

echo -n "Running as: "
whoami
echo

echo -n "Script name: "
echo $0
echo

echo -n "Script args: "
echo $*
echo

echo -n "Process info: "
ps -f $$
echo

echo -n "Env vars: "
env | sort
echo
echo

echo "Stuff from stdin"
echo "--------------------------------"
echo

cat
echo


