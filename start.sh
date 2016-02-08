#!/bin/bash

rm -r Results
mkdir Results

mkdir Results/cpu

for opt in flops iops
do
	for thread in 1 2 4
	do
		for (( i = 0; i < 5; i++ ))
		do
			echo "operation type: "$opt", thread number: "$thread
			python cpu_thread.py $opt $thread >>cpu"_"$opt"_"$thread.txt
		done
		mv cpu"_"$opt"_"$thread.txt Results/cpu
	done
done



