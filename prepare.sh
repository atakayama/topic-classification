#!/bin/sh

while read line; do
	max=`echo $line | awk '{print $2}' | bc`
	phrase=`echo $line | awk '{print $1}'`
	i=0
	while [ $i -lt $max ]; do
		echo $phrase
		let i=$i+1
	done
done < data/prev.txt
