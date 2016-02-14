# Cloud_Benchmarking - Illinois Institute of Technology


# Benchmarking software for CPU, GPU, Memory and Network evaluations

#################################################################################################################################

1. How to Start the CPU Process:- 

The “PROG1_Parikh_Harsh” directory contains the benchmarking programs. There are numerous files present in the directory.   

These files contain all the methods required to perform Benchmarking. 

Now, first to perform CPU Benchmark.  


1) Enter the “PROG1_Parikh_Harsh” directory.

cd  PROG1_Parikh_Harsh

2) Run the shell script “cpu.sh”.

Bash cpu.sh

After completion of this bash script, all the results are stored in Results/cpu. All the files contain in this folder is a separate result of every experiment. So total 6 files will be generated. 


Now for 600 samples of IOPS and FLOPS

1) Enter the “PROG1_Parikh_Harsh” directory.

cd  PROG1_Parikh_Harsh

2) Run the shell script “thread_samp.sh”.

Bash thread_samp.sh


After completion of this bash script, all the results are stored in Results/cpu. Two files will be generated contain the 600 samples each. 



#############################################################################################################################################################

2. How to Start the Disk Process:-


1) Enter the “PROG1_Parikh_Harsh” directory.

cd  PROG1_Parikh_Harsh

2) Run the shell script “Disk.sh”.

Bash Disk.sh


After completion of this bash script, all the results are stored in Results/disk. All the files contain in this folder is a separate result of every experiment. So total 24 files will be generated. In disk evaluation, I have used 30 MB files for doing operations. 



#################################################################################################################################################

3. How to Start the Network Process:-



1)TCP:- 

1) Enter the “PROG1_Parikh_Harsh” directory.

cd  PROG1_Parikh_Harsh

2) Run the shell script “network.sh”.

Bash network.sh


After completion of this bash script, all the results are stored in Results/network. All the files contain in this folder is a separate result of every experiment. So total 12 files will be generated for TCP.



2) UDP:-

1. Enter the “PROG1_Parikh_Harsh” directory.

cd  PROG1_Parikh_Harsh

2. Run the shell script “network1.sh”.

Bash network1.sh


After completion of this bash script, all the results are stored in Results/network. All the files contain in this folder is a separate result of every experiment. So total 12 files will be generated for UDP.

