#!/bin/bash
~/Projects/Pacer/Examples/Quadruped/SCRIPTS/clean_data.sh .

moby-driver -y=osg -v=100 -mt=5 -s=0.0001 -p=libLinksPlugin.so ./MODELS/atlas.xml > out.log 2> err.log
~/Projects/Pacer/Examples/Quadruped/SCRIPTS/parse_data.sh
