#!/bin/bash

mysql -u root -p -e 'CREATE DATABASE aleatorio; USE aleatorio; CREATE TABLE numeros (num INT(11), x FLOAT, y FLOAT, z FLOAT) ENGINE MyISAM;'

exit 0
