#!/bin/bash
X=1
while [ $X -lt 10 ]
do
        mv "./problem$X.py" "./problem00$X.py"
        mv "./problem$X.jl" "./problem00$X.jl"
        X=$(($X + 1))
done    

