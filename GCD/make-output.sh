#!/bin/bash

g++ sol.cpp -o sol -O2

for x in *.in; do
	./sol < $x > ${x%in}out
done;

rm sol
