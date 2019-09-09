export HTTPLOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PYTHONPATH=$HTTPLOT/..:$PYTHONPATH
export JUPYTER_PATH=$HTTPLOT/..:$JUPYTER_PATH
export PATH=$HTTPLOT/bin/:$PATH
