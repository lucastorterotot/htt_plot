#!/bin/bash

for Nw in {1..20}
do
    mkdir -p with_dask_${Nw}_mt
    /usr/bin/time -v python $(which datacard_and_plot_maker) -s -c mt -o with_dask_$Nw -w $Nw > ./with_dask_${Nw}_mt/time_log.out
    tail -n 23 ./with_dask_${Nw}_mt/time_log.out > ./with_dask_${Nw}_mt/time_log_small.out
    mv ./with_dask_${Nw}_mt/time_log_small.out ./with_dask_${Nw}_mt/time_log.out
done

    
