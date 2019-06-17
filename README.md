# htt_plot

## Installation

* Go to lyovis10
* Clone this directory
* Put this package in your python path by doing: 

```
source ./init.sh
```

* Copy your small root files in this package, in a directory called `lucas_small` (see [datasets/lucas_small.py](datasets/lucas_small.py))

Also install [cpyroot](https://github.com/cbernet/cpyroot)

## Test

```
ipython -i macros/plot_inclusive_test.py 
```

## Test dask in a jupyter notebook on lyovis10 

On your computer, open a terminal and establish an ssh connection to lyovis10: 

```
ssh -L8889:lyovis10:8889 lyovis10
```

This forwards the local port 8889 to port 8889 on lyovis10. 

On lyovis10, activate the conda environment and start the jupyter notebook server: 

```
conda activate base
```

And start the jupyter notebook server from the htt_plot directory. 

```
jupyter notebook --no-browser --port=8889 --ip=0.0.0.0
```

Since the server listens to port 8889, you can connect to this port on your local computer, and the connection will be forwarded to port 8889 on lyovis10. So start a web browser and go to [http://localhost:8889/](http://localhost:8889/).

In the browser, open [macros/test_dask.ipynb](macros/test_dask.ipynb).


## Dataset report

See above how to use jupyter notebook remotely.

Then, in the jupyter notebook, open [harvest/dataset_report.ipynb](harvest/dataset_report.ipynb)

## TODO

**You should disable parallel mode in the main macro for development and debugging**

* add the proper cross-section and generated number of events for the MC datasets 
* implement the final signal selection cut
* start implementing the various background estimation methods
