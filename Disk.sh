#!/bin/bash

#rm -r Results/disk
mkdir Results/disk

for buffersize in 1b 1kb 1mb
do
	for access in seqn rnd
	do
		for opt in Write Read
		do
			for thread in 1 2
			do
				for (( i = 0; i < 3; i++ ))
				do
					echo "operation type: "$opt", access type: "$access	\
					", Buffer size:"$buffersize", thread number: "$thread
					python disk.py $opt $access $buffersize $thread >>	\
					disk"_"$opt"_"$access"_"$buffersize"_"$thread.txt
				done
				mv disk"_"$opt"_"$access"_"$buffersize"_"$thread.txt Results/disk
			done
		done
	done
done
