#!/bin/bash


mkdir Results/disk
for opt in Write Read
do
	for access in seq 
	do
		for blocksize in 1b 1kb 1mb
		do
			for thread in 1 2
			do
				for (( i = 0; i < 1; i++ ))
				do
					echo "operation type: "$opt", access type: "$access	\
					", block size:"$blocksize", thread number: "$thread
					python disk.py $opt $access $blocksize $thread >>	\
					disk"_"$opt"_"$access"_"$blocksize"_"$thread.txt
				done
				mv disk"_"$opt"_"$access"_"$blocksize"_"$thread.txt Results/disk
			done
		done
	done
done
