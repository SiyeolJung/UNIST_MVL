#!/bin/bash 

#PBS -l select=1:ncpus=4:ngpus=1
#PBS -N G1C4_siyeol_DifftalkInference
#PBS -q pleiades1
#PBS -r n 
#PBS -j oe 

source activate difftalk
cd $PBS_O_WORKDIR

sh /home2/intern4/project/Difftalk/inference.sh > output4.txt
