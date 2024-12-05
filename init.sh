#!/bin/bash

DAY=$1
LANG=$2

if [ "$0" == "./init.sh" ]; then
    YEAR="24/"
    TO_ROOT="./"
else
    YEAR=""
    TO_ROOT="../"
fi

touch ${YEAR}in/${DAY}.in
cp  ${TO_ROOT}template.${LANG} ${YEAR}src/${DAY}.${LANG}
