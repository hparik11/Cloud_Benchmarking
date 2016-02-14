#!/bin/bash


for Dtype in iops flops
do
	for (( i = 0; i < 600; i++ ))
	do
		echo "Samples are taken for "$Dtype $i
		python samples_cpu.py $Dtype >> samples"_"$Dtype.txt
		
	done
	mv samples"_"$Dtype.txt Results/cpu
done
