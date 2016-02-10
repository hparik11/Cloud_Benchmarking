#!/bin/bash

rm -r Results/disk
mkdir Results/disk

for filesize in 1b 1kb 1mb
do
	for access in seqn rnd
	do
		for opt in Write Read
		do
			for thread in 1 2
			do
				for (( i = 0; i < 1; i++ ))
				do
					echo "operation type: "$opt", access type: "$access	\
					", File size:"$filesize", thread number: "$thread
					python disk.py $opt $access $filesize $thread >>	\
					disk"_"$opt"_"$access"_"$filesize"_"$thread.txt
				done
				mv disk"_"$opt"_"$access"_"$filesize"_"$thread.txt Results/disk
			done
		done
	done
done
