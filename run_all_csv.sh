ls D*.csv | sort -n | xargs -t -n1 -i python3 ./filter_tick.py {} MTX
