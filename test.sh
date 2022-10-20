#!/bin/bash
cd testout

for X in 16 32 64 128 256 512
do
	repmax=1000
	Xsquare=$((X * X))
	quotient=1
	remainder=0
	if [ $Xsquare -ge $repmax ]
	then 
		quotient=$((Xsquare / repmax))
		remainder=$((Xsquare % repmax))
		counter=1
		while [ $counter -le $quotient ] 	
		do
			oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $repmax 1 $counter"
			oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $repmax 2 $counter"
			oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $repmax 3 $counter"
			oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $repmax 4 $counter"
			((counter++))
		done
		if [ $remainder -ne 0 ]
		then
			oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $remainder 1 1"
                        oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $remainder 2 1"
                        oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $remainder 3 1"
                        oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $remainder 4 1"
		fi
	else
		oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $Xsquare 1 1"
                oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $Xsquare 2 1"
                oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $Xsquare 3 1"
                oarsub -S -p "cputype='xeon'" -l /core=1,walltime=72 -t besteffort -t idempotent "/home/fdamore/julia /home/fdamore/exp_cluster.jl $X $Xsquare 4 1"
	fi
done
