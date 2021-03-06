#!/bin/bash

#rm -r Results/network
mkdir Results/network

for packet in 1b 1kb 64kb
do
	for thread in 1 2
	do
		for (( i = 0; i < 3; i++ ))
		do
			echo "packet size:"$packet ", thread number: "$thread
			python mtcpServer.py $thread &
			python mtcpClient.py $packet $thread >> network"_"$packet"_"$thread.txt
			mv network"_"$packet"_"$thread.txt Results/network
		done
		
	done
done

