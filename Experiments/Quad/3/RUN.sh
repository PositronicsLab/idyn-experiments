#!/bin/bash
~/Projects/Pacer/Examples/Quadruped/SCRIPTS/clean_data.sh .

moby-driver -y=osg -v=100 -mt=3 -s=0.0001 -p=libLinksPlugin.so ./MODELS/links1.xml > out.log 2> err.log
~/Projects/Pacer/Examples/Quadruped/SCRIPTS/parse_data.sh
