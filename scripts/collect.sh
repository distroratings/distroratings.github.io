#!/bin/sh

# currently we only collect number of IRC users per channel
./collect_irc.py | sed '1,/--BEGIN--/d' > ./irc_stats.csv
